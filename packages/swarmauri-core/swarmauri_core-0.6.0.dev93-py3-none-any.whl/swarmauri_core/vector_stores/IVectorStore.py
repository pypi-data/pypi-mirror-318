from abc import ABC, abstractmethod
from typing import List, Dict, Union
from swarmauri_core.vectors.IVector import IVector
from swarmauri_core.documents.IDocument import IDocument

class IVectorStore(ABC):
    """
    Interface for a vector store responsible for storing, indexing, and retrieving documents.
    """

    @abstractmethod
    def add_document(self, document: IDocument) -> None:
        """
        Stores a single document in the vector store.

        Parameters:
        - document (IDocument): The document to store.
        """
        pass

    @abstractmethod
    def add_documents(self, documents: List[IDocument]) -> None:
        """
        Stores multiple documents in the vector store.

        Parameters:
        - documents (List[IDocument]): The list of documents to store.
        """
        pass

    @abstractmethod
    def get_document(self, doc_id: str) -> Union[IDocument, None]:
        """
        Retrieves a document by its ID.

        Parameters:
        - doc_id (str): The unique identifier for the document.

        Returns:
        - Union[IDocument, None]: The requested document, or None if not found.
        """
        pass

    @abstractmethod
    def get_all_documents(self) -> List[IDocument]:
        """
        Retrieves all documents stored in the vector store.

        Returns:
        - List[IDocument]: A list of all documents.
        """
        pass

    @abstractmethod
    def delete_document(self, doc_id: str) -> None:
        """
        Deletes a document from the vector store by its ID.

        Parameters:
        - doc_id (str): The unique identifier of the document to delete.
        """
        pass

    @abstractmethod
    def clear_documents(self) -> None:
        """
        Deletes all documents from the vector store

        """
        pass


    @abstractmethod
    def update_document(self, doc_id: str, updated_document: IDocument) -> None:
        """
        Updates a document in the vector store.

        Parameters:
        - doc_id (str): The unique identifier for the document to update.
        - updated_document (IDocument): The updated document object.

        Note: It's assumed that the updated_document will retain the same doc_id but may have different content or metadata.
        """
        pass

    @abstractmethod
    def document_count(self) -> int:
        pass 