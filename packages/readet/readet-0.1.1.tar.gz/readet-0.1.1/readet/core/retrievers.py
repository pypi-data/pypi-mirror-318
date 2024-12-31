# ################################# #
# Retrievers						#
# collection of retrievers with one #
# level more abstraction than		#
#  LangChain various retrievers		#
# ################################# #
import warnings 
from typing import List, Union, Literal, Dict, Any, TypeVar, Optional  
from os import path, makedirs, listdir 
from abc import ABCMeta, abstractmethod 
from langchain_core.documents import Document
from langchain_core.stores import BaseStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TokenTextSplitter
from langchain.storage import InMemoryStore 
from langchain_chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever, ParentDocumentRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI
from .. utils import models, docs, save_load

# ######################################### #
# helper functions						    #
# ######################################### #

def format_documents(documents: List[Document]) -> str:
	return f"\n {'-' * 100} \n".join([f"Document {i + 1}: \n\n" + 
								   	d.page_content for i, d in enumerate(documents)])

def load_store_from_disk(store_path: Optional[str] = None,
						  version_number: Optional[Literal['last'] | int] = None, 
						  pkl_object: Optional[str| Dict] = None) -> Dict[str, Any]:
	
	store = InMemoryStore()
	if store_path is not None and version_number is not None and pkl_object is None:
		versions = sorted([file_name for file_name in listdir(store_path) if file_name.startswith("persisted_retriever_")])
		if len(versions) == 0:
			raise ValueError(f"Nothing is stored in {store_path}")
		if version_number == 'last':
			store_version = versions[-1]
		elif isinstance(version_number, int) and (0 <= version_number < len(versions)):
			store_version = versions[version_number]
		else:
			raise ValueError(f"Invalid version number: {version_number}; choose a number between 0 and {len(versions) - 1}")
		
		store_dict = save_load.load_from_pickle(path.join(store_path, store_version))
		
	elif pkl_object is not None:
		if isinstance(pkl_object, str) and pkl_object.endswith(".pkl"):
			store_dict = save_load.load_from_pickle(pkl_object)
		elif isinstance(pkl_object, Dict):
			store_dict = pkl_object
		else:
			raise ValueError(f"Invalid pkl object: {pkl_object}")
	else:
		raise ValueError(f"Invalid store path: {store_path}, version number: {version_number}, or pkl object: {pkl_object}")
	
	store.mset(store_dict.items())
	return store
	

# ######################################### #
# Retrievers base class						#
# ######################################### #	
class Retriever(metaclass = ABCMeta):
	def __init__(self):
		self.runnable = None 
		self.built = False 
	
	@abstractmethod
	def build(self):
		...
	
	@abstractmethod
	def num_docs(self) -> int:
		...

	@abstractmethod
	def add_pdf(self, pdf_files: List[str] | str, 
			 	document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
				splitter: Literal['recursive', 'token'] = 'recursive',
				splitter_kwargs: Dict[str, Any] = {}) -> None:
		...
	
	def run(self, query: str) -> str:
		if self.built is False:
			self.build()
		docs = self.runnable.invoke(query)
		return format_documents(docs)
	
	def __call__(self, query: str) -> str:
		return self.run(query)
	
# ######################################### #
# PlainRetriever							#
# ######################################### #
PR = TypeVar('PR', bound = 'PlainRetriever')
class PlainRetriever(Retriever):
	"""
	Plain retriver class
	Class that abstracts the retrieval of documents from a vector store
	Accepts a list of Document objects and an embedding model name
	"""
	def __init__(self, documents: List[Document], 
				embeddings: str = 'openai-text-embedding-3-large'):
		super().__init__()
		self.vector_store = Chroma.from_documents(documents,
				embedding = models.configure_embedding_model(embeddings))
		self.runnable = None 
	
	def build(self, search_type: Literal["mmr", "similarity"] = "similarity", 
				k: int = 5, lambda_mult: float = 0.5, fetch_k: int = 20) -> None:
		self.runnable = self.vector_store.as_retriever(search_type = search_type, k = k, 
												  lambda_mult = lambda_mult, fetch_k = fetch_k)
		self.built = True 
	
	def add_pdf(self, pdf_files: List[str] | str, 
			 	document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
				splitter: Literal['recursive', 'token'] = 'recursive',
				splitter_kwargs: Dict[str, Any] = {}) -> None:
		documents = docs.doc_from_pdf_files(pdf_files, document_loader, splitter, splitter_kwargs)
		self.vector_store.add_documents(documents) 
		self.build()
	
	def num_docs(self) -> int:
		pass 
	
	@classmethod
	def from_pdf(cls, pdf_files: Union[str, List[str]], 
				embeddings: str = 'openai-text-embedding-3-large',
				document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
				splitter: Literal['recursive', 'token'] = 'recursive',
				chunk_size: int = 2000, chunk_overlap: int = 200) -> PR:
		documents = docs.doc_from_pdf_files(pdf_files, document_loader, splitter, 
									  	chunk_size=chunk_size, chunk_overlap=chunk_overlap)
		return cls(documents, embeddings)

# ######################################### #
# ContextualCompressionRetriever			#
# ######################################### #
CC = TypeVar('CC', bound = 'ContextualCompression')
class ContextualCompression(Retriever):
	"""
	Class that abstracts the ContextualCompressionPipeLine
	This class builds a ContextualCompressionRetriever and accepts a list of documents
	"""
	def __init__(self, documents: List[Document],  
				embeddings: str = 'openai-text-embedding-3-large', 
					store: Optional[BaseStore] = None, store_path: Optional[str] = None,
					parent_splitter: Literal['recursive', 'token'] = 'token', 
					child_splitter: Literal['recursive', 'token'] = 'recursive', 
					parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200,
					child_chunk_size: int = 2000, child_chunk_overlap: int = 100):
		super().__init__()
		self.llm = OpenAI(temperature = 0)
		self.base_retriever = ParentDocument(documents = documents, embeddings = embeddings, 
				store = store, store_path = store_path, parent_splitter = parent_splitter, 
					child_splitter = child_splitter, parent_chunk_size = parent_chunk_size, 
						parent_chunk_overlap = parent_chunk_overlap, child_chunk_size = child_chunk_size, 
							child_chunk_overlap = child_chunk_overlap)
		self.base_retriever.build()
		self.runnable = None 
	
	def build(self):
		"""
		returns the runnable for use in a chain
		"""
		compressor = LLMChainExtractor.from_llm(self.llm)
		self.runnable = ContextualCompressionRetriever(base_compressor = compressor, 
												 base_retriever = self.base_retriever.runnable) 
		self.built = True

	@property
	def num_docs(self) -> int:
		return len(self.base_retriever.documents) 
	
	@property
	def documents(self) -> List[Document]:
		return self.base_retriever.documents
	
	def add_pdf(self, pdf_files: List[str] | str, 
			 	document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
				splitter: Literal['recursive', 'token'] = 'recursive',
				chunk_size: int = 2000, chunk_overlap: int = 200) -> None:
		self.built = False 
		self.base_retriever.add_pdf(pdf_files, document_loader, splitter, chunk_size = chunk_size, chunk_overlap = chunk_overlap)
		self.build()
	
	@classmethod
	def from_pdf(cls, pdf_files: Union[str, List[str]],
			  store: Optional[BaseStore] = None, store_path: Optional[str] = None,
			   splitter: Literal['recursive', 'token'] = 'recursive', 
			   	document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf' ,
				embeddings: str = 'openai-text-embedding-3-large',
				parent_splitter: Literal['recursive', 'token'] = 'token', 
				child_splitter: Literal['recursive', 'token'] = 'recursive',
				parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200,
				child_chunk_size: int = 2000, child_chunk_overlap: int = 100,
			   	chunk_size: int = 2000, chunk_overlap: int = 200) -> CC:
		
		documents = docs.doc_from_pdf_files(pdf_files, document_loader, splitter, chunk_size = chunk_size, chunk_overlap = chunk_overlap)
		return cls(documents, embeddings = embeddings, store = store, store_path = store_path, 
					parent_splitter = parent_splitter, child_splitter = child_splitter, 
						parent_chunk_size = parent_chunk_size, parent_chunk_overlap = parent_chunk_overlap, 
							child_chunk_size = child_chunk_size, child_chunk_overlap = child_chunk_overlap)
	
	@classmethod
	def load_from_disk(cls, store_path: str, documents: Optional[Union[str, List[str], List[Document]]] = None,
					 version_number: Literal['last'] | int = 'last', pkl_object: Optional[str| Dict] = None,
						embeddings: str = 'openai-text-embedding-3-large', documnet_loader: Literal['pypdf', 'pymupdf'] = 'pypdf', 
							parent_splitter: Literal['recursive', 'token'] = 'recursive', child_splitter: Literal['recursive', 'token'] = 'recursive',
								parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200, child_chunk_size: int = 2000, child_chunk_overlap: int = 100) -> CC:
		
		store = load_store_from_disk(store_path, version_number, pkl_object)
		document_objects = None
		if documents is not None:
			if isinstance(documents, str) or all(isinstance(doc, str) for doc in documents):
				document_objects = docs.doc_from_pdf_files(documents, documnet_loader, splitter = None)
			elif all(isinstance(doc, Document) for doc in documents):
				document_objects = documents
			else:
				raise ValueError(f"Invalid document type: {type(documents)}")
		
		return cls(document_objects, embeddings = embeddings, store = store, store_path = store_path,
			  parent_splitter = parent_splitter, child_splitter = child_splitter, 
					parent_chunk_size = parent_chunk_size, parent_chunk_overlap = parent_chunk_overlap, 
						child_chunk_size = child_chunk_size, child_chunk_overlap = child_chunk_overlap)

# ######################################### #
# 	Parent Document Retriever				#
# ######################################### #
PD = TypeVar('PD', bound = 'ParentDocument')
class ParentDocument(Retriever):
	"""
	Class that abstracts the Parent Document Retriever
	store: an instance of BaseStore; if None, an in-memory store will be used
	store_path: path to the directory where the vector store will be saved
	"""
	def __init__(self, documents: Optional[List[Document]] = None, 
				embeddings: str = 'openai-text-embedding-3-large',
				store: Optional[BaseStore] = None, store_path: Optional[str] = None,
				parent_splitter: Literal['recursive', 'token'] = 'token', 
			  	child_splitter: Literal['recursive', 'token'] = 'recursive', 
					parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200,
						child_chunk_size: int = 2000, child_chunk_overlap: int = 100):
		
		super().__init__()
		self.parent_splitter = None 
		self.child_splitter = None 

		if parent_splitter == 'recursive':
			self.parent_splitter = RecursiveCharacterTextSplitter(separators = None, 
				chunk_size = parent_chunk_size, chunk_overlap = parent_chunk_overlap, add_start_index = True)
		elif parent_splitter == 'token':
			self.parent_splitter = TokenTextSplitter()
		
		if child_splitter == 'recursive':
			self.child_splitter = RecursiveCharacterTextSplitter(separators = None, 
				chunk_size = child_chunk_size, 
				chunk_overlap = child_chunk_overlap, add_start_index = True)
		elif child_splitter == 'token':
			self.child_splitter = TokenTextSplitter()
		
		# documents and vector store #
		if store is None:
			self.store = InMemoryStore()
		else:
			self.store = store

		self.store_path = None 
		self.add_documents_count = 0
		if store_path is not None:
			if not path.exists(store_path):
				makedirs(store_path)
			self.store_path = store_path
			num_files = len([file_name for file_name in listdir(store_path) if file_name.endswith(".pkl")])
			self.add_documents_count = num_files 

		self.documents = []
		if documents is not None:
			self.documents.extend(documents)
		self.vector_store = Chroma(collection_name = "persisted_retriever", 
								embedding_function = models.configure_embedding_model(embeddings), 
									persist_directory = store_path)
		
	def build(self) -> None:
		self.runnable = ParentDocumentRetriever(vectorstore = self.vector_store, 
												docstore = self.store, 
												parent_splitter = self.parent_splitter, 
												child_splitter = self.child_splitter, id_key = "doc_id")
		if len(self.documents) > 0:
			self.runnable.add_documents(self.documents)
			self.add_documents_count += 1
			if self.store_path is not None:
				save_file = path.join(self.store_path, f"persisted_retriever_{self.add_documents_count}.pkl")
				save_load.save_to_pickle(self.runnable.docstore.store, save_file)
		
		self.built = True 
	
	@property 
	def num_docs(self) -> int:
		return len(self.runnable.docstore.store.values())
		
	def add_pdf(self, pdf_files: List[str] | str, 
			 	document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
				splitter: Literal['recursive', 'token'] = 'recursive',
				chunk_size: int = 2000, chunk_overlap: int = 200) -> None:
		self.built = False 
		documents = docs.doc_from_pdf_files(pdf_files, document_loader, splitter, chunk_size = chunk_size, chunk_overlap = chunk_overlap)
		self.documents.extend(documents) 
		self.build()
		self.built = True  
	
	@classmethod
	def from_pdf(cls, pdf_files: Union[str, List[str]],
		embeddings: str = 'openai-text-embedding-3-large',
					store_path: str = None,
				document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf',
					parent_splitter: Literal['recursive', 'token'] = 'recursive', 
						child_splitter: Literal['recursive', 'token'] = 'recursive',
							parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200,
								child_chunk_size: int = 2000, child_chunk_overlap: int = 100) -> PD:
		
		documents = docs.doc_from_pdf_files(pdf_files,
			document_loader = document_loader, splitter = None)
		
		return cls(documents, embeddings = embeddings, store_path = store_path, 
					parent_splitter = parent_splitter, child_splitter = child_splitter, 
						parent_chunk_size = parent_chunk_size, parent_chunk_overlap = parent_chunk_overlap, 
							child_chunk_size = child_chunk_size, child_chunk_overlap = child_chunk_overlap)
	@classmethod
	def load_from_disk(cls, store_path: str, documents: Optional[Union[str, List[str], List[Document]]] = None,
					 version_number: Literal['last'] | int = 'last', pkl_object: Optional[str| Dict] = None,
						embeddings: str = 'openai-text-embedding-3-large', document_loader: Literal['pypdf', 'pymupdf'] = 'pypdf', 
								parent_splitter: Literal['recursive', 'token'] = 'recursive', 
									child_splitter: Literal['recursive', 'token'] = 'recursive',
										parent_chunk_size: int = 2000, parent_chunk_overlap: int = 200,
											child_chunk_size: int = 2000, child_chunk_overlap: int = 100) -> PD:
		
		store = load_store_from_disk(store_path, version_number, pkl_object)
		document_objects = None 

		if documents is not None:
			if isinstance(documents, str) or all(isinstance(doc, str) for doc in documents):
				document_objects = docs.doc_from_pdf_files(documents, document_loader, splitter = None)
			elif all(isinstance(doc, Document) for doc in documents):
				document_objects = documents
			else:
				raise ValueError(f"Invalid document type: {type(documents)}")
		
		return cls(document_objects, embeddings = embeddings, store = store, store_path = store_path, 
					parent_splitter = parent_splitter, child_splitter = child_splitter, 
						parent_chunk_size = parent_chunk_size, parent_chunk_overlap = parent_chunk_overlap, 
							child_chunk_size = child_chunk_size, child_chunk_overlap = child_chunk_overlap)

		
# ######################################### #
# 	Retriever Factory						#
# ######################################### #
def get_retriever(documents: List[Document] | List[str] | str | None,
			retriever_type: Literal['plain', 'contextual-compression', 'parent-document'] ='parent-document', **kwargs) -> Retriever:
	
	load_version_number = kwargs.get('load_version_number', None)
	pkl_object = kwargs.get('pkl_object', None)
	if load_version_number is not None or pkl_object is not None:
		if retriever_type == 'parent-document':
			retriever = ParentDocument.load_from_disk(kwargs.get('store_path'), documents = documents,
				version_number = load_version_number, pkl_object = pkl_object, embeddings = kwargs.get('embeddings', 'openai-text-embedding-3-large'),
					document_loader = kwargs.get('document_loader', 'pypdf'), parent_splitter = kwargs.get('parent_splitter', 'token'),
						child_splitter = kwargs.get('child_splitter', 'recursive'), parent_chunk_size = kwargs.get('parent_chunk_size', 2000), 
							child_chunk_size = kwargs.get('child_chunk_size', 2000), parent_chunk_overlap = kwargs.get('parent_chunk_overlap', 200),
								child_chunk_overlap = kwargs.get('child_chunk_overlap', 100))
		else:
			raise ValueError(f"Invalid retriever type: {retriever_type}; choose 'patent-document'")
	
	elif load_version_number is None and pkl_object is None and (isinstance(documents, str) or all(isinstance(doc, str) for doc in documents)):
		if retriever_type == 'parent-document':
			retriever = ParentDocument.from_pdf(documents, store_path = kwargs.get('store_path'),
				embeddings = kwargs.get('embeddings', 'openai-text-embedding-3-large'),
					document_loader = kwargs.get('document_loader', 'pypdf'), parent_splitter = kwargs.get('parent_splitter', 'token'),
						child_splitter = kwargs.get('child_splitter', 'recursive'), parent_chunk_size = kwargs.get('parent_chunk_size', 2000), 
							child_chunk_size = kwargs.get('child_chunk_size', 2000), parent_chunk_overlap = kwargs.get('parent_chunk_overlap', 200),
								child_chunk_overlap = kwargs.get('child_chunk_overlap', 100))
		elif retriever_type == 'plain':
			retriever = PlainRetriever.from_pdf(documents, embeddings = kwargs.get('embeddings', 'openai-text-embedding-3-large'),
				document_loader = kwargs.get('document_loader', 'pypdf'), splitter = kwargs.get('splitter', 'recursive'))
		else:
			raise ValueError(f"Invalid retriever type: {retriever_type}; choose 'patent-document' or 'plain'")

	
	elif load_version_number is None and pkl_object is None and (all(isinstance(doc, Document) for doc in documents) or documents is None):
		if retriever_type == 'plain':
			retriever = PlainRetriever(documents, embeddings = kwargs.get('embeddings', 'openai-text-embedding-3-large'))
		
		elif retriever_type == 'parent-document':
			retriever = ParentDocument(documents, embeddings = kwargs.get('embeddings', 'openai-text-embedding-3-large'),
				store = kwargs.get('store', None), store_path = kwargs.get('store_path', None), 
					parent_splitter = kwargs.get('parent_splitter', 'token'), child_splitter = kwargs.get('child_splitter', 'recursive'),
						parent_chunk_size = kwargs.get('parent_chunk_size', 2000), parent_chunk_overlap = kwargs.get('parent_chunk_overlap', 200),
							child_chunk_size = kwargs.get('child_chunk_size', 2000), child_chunk_overlap = kwargs.get('child_chunk_overlap', 100))
		
		elif retriever_type == 'contextual-compression':
			raise NotImplementedError("Contextual Compression Retriever is not yet implemented")
	else:
		raise ValueError(f"Invalid document type, version number, or pkl file name")

	retriever.build()
	return retriever 