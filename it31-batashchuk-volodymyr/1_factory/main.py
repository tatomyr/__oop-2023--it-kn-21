from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError("You should implement this method")

# Subclasses
class WordDocument(Document):
    def create(self):
        return "Word document created"

class PDFDocument(Document):
    def create(self):
        return "PDF document created"

class SpreadsheetDocument(Document):
    def create(self):
        return "Spreadsheet document created"

# Factory class
class DocumentFactory:
    def get_document(self, doc_type):
        if doc_type == "word":
            return WordDocument()
        elif doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "spreadsheet":
            return SpreadsheetDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")

# Client code
factory = DocumentFactory()
document = factory.get_document("pdf")
print(document.create())  # Output: PDF document created
