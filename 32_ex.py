from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod

    def print(self):

        pass

    def prepare_for_printing(self):

        self.print()

class PDFDocument(Document):

    def print(self):

        print("Printing PDF document...")

class WordDocument(Document):

    def print(self):

        print("Printing Word document...")

class ExcelDocument(Document):

    def print(self):

        print("Printing Excel document...")





class DocumentFactory:

    def create_document(self, doc_type):

        if doc_type == 'pdf':

            return PDFDocument()

        elif doc_type == 'word':

            return WordDocument()

        elif doc_type == 'excel':

            return ExcelDocument()

        else:

            raise ValueError(f"Unsupported document type: {doc_type}")

if __name__ == "__main__":

    factory = DocumentFactory()

    pdf_doc = factory.create_document('pdf')

    pdf_doc.prepare_for_printing()

    word_doc = factory.create_document('word')

    word_doc.prepare_for_printing()
