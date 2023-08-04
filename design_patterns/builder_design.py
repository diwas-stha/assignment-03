from abc import ABC, abstractmethod

#PRODUCT
class Document:
    def __init__(self):
        self.content = []
    
    def add_content(self, content):
        self.content.append(content)

    def __str__(self):
        return "\n".join(self.content)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(str(self))


#Interface Builder
class IDocumentBuilder(ABC):
    @abstractmethod
    def add_header(self, text):
        pass

    @abstractmethod
    def add_paragraph(self, text):
        pass

    @abstractmethod
    def get_document(self) -> Document:
        pass

#Concrete Builder
class PDFBuilder(IDocumentBuilder):
    def __init__(self):
        self.document = Document()

    def add_header(self, text):
        self.document.add_content(f"PDF Header: {text}")

    def add_paragraph(self, text):
        self.document.add_content(f"PDF Paragraph: {text}")

    def get_document(self) -> Document:
        return self.document


class HTMLBuilder(IDocumentBuilder):
    def __init__(self):
        self.document = Document()

    def add_header(self, text):
        self.document.add_content(f"<h1>{text}</h1>")

    def add_paragraph(self, text):
        self.document.add_content(f"<p>{text}</p>")

    def get_document(self) -> Document:
        return self.document


class PlainTextBuilder(IDocumentBuilder):
    def __init__(self):
        self.document = Document()

    def add_header(self, text):
        self.document.add_content(f"PLAIN TEXT HEADER: {text}")

    def add_paragraph(self, text):
        self.document.add_content(f"PLAIN TEXT PARAGRAPH: {text}")

    def get_document(self) -> Document:
        return self.document

#Director
class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_document(self):
        self.builder.add_header("Sample Document")
        self.builder.add_paragraph("This is a sample document.")


if __name__ == "__main__":
    save_document_directory = r"D:\Fusemachines\Assignments\assignment-03\design_patterns\sample_documents"
    # Generate and save PDF document
    pdf_builder = PDFBuilder()
    director = DocumentDirector(pdf_builder)
    director.construct_document()
    pdf_document = pdf_builder.get_document()
    # pdf_document.save_to_file("sample.pdf")

    # Generate and save HTML document
    html_builder = HTMLBuilder()
    director = DocumentDirector(html_builder)
    director.construct_document()
    html_document = html_builder.get_document()
    html_document.save_to_file(save_document_directory + "\sample.html")

    # Generate and save Plain Text document
    plain_text_builder = PlainTextBuilder()
    director = DocumentDirector(plain_text_builder)
    director.construct_document()
    plain_text_document = plain_text_builder.get_document()
    plain_text_document.save_to_file(save_document_directory + "\sample.txt")
