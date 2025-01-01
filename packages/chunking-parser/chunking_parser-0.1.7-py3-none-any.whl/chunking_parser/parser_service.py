from abc import abstractmethod
import asyncio
import typing as tp
import io
import fitz

from application.user import User

from application import PDFPageTextInfo, Files, PDFProcessor
from .dto.file import AnnotationsDataModelDTO

from enum import Enum


class BaseEnum(Enum):
    pass


class Parser(BaseEnum):
    NORMALPARSER = "Normal_parser"
    PDFPARSER = "PDFParser"
    WORDPARSER = "WordParser"


def get_parsing_instance(ptype: str = Parser.PDFPARSER.value):
    # apply conditions for parsing
    builder_ = None
    director = ParsingDirector()
    if ptype == Parser.PDFPARSER.value:
        builder_ = PyMuPDFParserBuilder()
    director.builder = builder_
    return director


class ParsingBuilder:
    @abstractmethod
    async def operations(self, file: Files):
        pass

    @abstractmethod
    async def add_annotations(self, file: Files, annotations):
        pass

    @abstractmethod
    async def get_textbox(self, doc: any, annot_details: AnnotationsDataModelDTO):
        pass


class ParsingDirector:
    _parsing_builder = None

    @property
    def builder(self):
        return self._parsing_builder

    @builder.setter
    def builder(self, parsing_builder: ParsingBuilder):
        self._parsing_builder = parsing_builder

    async def get_feature_of_pdf_file(self, file: Files):
        return await self._parsing_builder.operations(file)

    async def add_specific_feature_of_pdf(self, file: Files, annotations: any):
        await self._parsing_builder.add_annotations(file, annotations)

    async def get_textbox(
        self, doc: any, annot_details: AnnotationsDataModelDTO
    ) -> PDFPageTextInfo:
        return await self._parsing_builder.get_textbox(doc, annot_details)


class PyMuPDFParserBuilder(ParsingBuilder):
    async def operations(self, file: Files) -> tp.List[tp.Dict[str, any]]:
        #print(file, "file")
        return await PyMuPDFParser.parse(file)

    async def add_annotations(self, file: Files, annotations: any):
        return await PyMuPDFParser.add_annotation(file, annotations)

    async def get_textbox(
        self, doc: any, annot_details: AnnotationsDataModelDTO
    ) -> PDFPageTextInfo:
        return await PyMuPDFParser.get_textbbox(doc, annot_details)


class PyMuPDFParser:
    async def get_textbbox(
        doc: any, annot_details: AnnotationsDataModelDTO
    ) -> PDFPageTextInfo:
        page = doc.load_page(annot_details.page_no)
        text_in_bbox = page.get_textbox(annot_details.bbox)
        return PDFPageTextInfo(
            page_no=annot_details.page_no, text=text_in_bbox, bbox=annot_details.bbox
        )

    @staticmethod
    def _get_text_metadata(
        page: fitz.Page, ptype: str, page_no: int
    ) -> tp.List[PDFPageTextInfo]:
        formatted_data = []
        text = page.get_text(ptype, sort=True)
        blocks = text.get("blocks", [])
        cnt = 0
        for block in blocks:
            cnt += 1
            if block.get("image"):
                #Using the OCR code
                import pytesseract
                from PIL import Image
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                text = pytesseract.image_to_string(img)
                bbox = list(block.get("bbox", ()))
                formatted_data.append(
                        PDFPageTextInfo(
                            page_no=page_no, text=text, ocr_text=True, font="", size=0, bbox=bbox
                        )
                    )

                continue
            lines = block["lines"]
            for line in lines:
                spans = line["spans"]
                for span in spans:
                    origin = span.get("origin", [])
                    text = span.get("text", "")
                    font = span.get("font", "")
                    size = span.get("size", 0)
                    bbox = list(span.get("bbox", ()))
                    formatted_data.append(
                        PDFPageTextInfo(
                            page_no=page_no, text=text, font=font, size=size, bbox=bbox
                        )
                    )

        return formatted_data

    def _add_outline_to_paragraph_in_a_page(
        chunks: tp.List[tp.Union[tp.Dict[str, any], tp.List]], page: fitz.Page
    ) -> None:
        highlight_color = (0.78, 0.89, 0.96)  # RGB values
        for chunk in chunks:
            if isinstance(chunk, list):
                highlight = page.add_rect_annot(chunk)
            else:
                highlight = page.add_rect_annot(chunk["bbox"])
            highlight.set_colors(stroke=highlight_color)
            highlight.update()

    async def add_annotation(file: Files, annotations):
        async for page, page_no in PDFProcessor.get_page(file):
            if page_no not in annotations:
                continue
            bbox_list = annotations[page_no]
            PyMuPDFParser._add_outline_to_paragraph_in_a_page(bbox_list, page)

    @staticmethod
    async def parse(file: Files, ptype="dict") -> tp.List[tp.Dict[str, any]]:
        try:
            overall_data_in_file = []
            #print(file)
            async for page, page_no in PDFProcessor().get_page(file):
                formatted_metadata = PyMuPDFParser._get_text_metadata(
                    page, ptype, page_no
                )
                #print(formatted_metadata)
                overall_data_in_file.extend(formatted_metadata)
            return overall_data_in_file
        except Exception as e:
            print(e)
            ...
            # print(traceback.format_exc())

def read_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            return raw_data    

    except FileNotFoundError:
        return "File not found. Please check the file path."



# if __name__ == "__main__":
#     user = User("me")
#     file_path = "/Users/aashishsharma/Downloads/Aashish_Resume.pdf"
#     file_ = read_file(file_path)
#     print(file_)
#     file = Files(file_name=file_path.split("/")[-1])
#     file = file.set_file(file_)
#     asyncio.run(PyMuPDFParser.parse(file))
