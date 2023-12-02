from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

class WordDocument(Document):
    def get_type(self):
        return "Word Document"

    def get_content(self):
        return "Content of a Word document"

class PdfDocument(Document):
    def get_type(self):
        return "PDF Document"

    def get_content(self):
        return "Content of a PDF document"

class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

    def print_document(self):
        document = self.create_document()
        print(f"Printing {document.get_type()}: {document.get_content()}")


class WordDocumentCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()

class PdfDocumentCreator(DocumentCreator):
    def create_document(self):
        return PdfDocument()

word_creator = WordDocumentCreator()
word_creator.print_document()

pdf_creator = PdfDocumentCreator()
pdf_creator.print_document()
