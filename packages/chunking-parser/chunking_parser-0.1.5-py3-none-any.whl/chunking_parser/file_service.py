import typing as tp

from application.file import Files
from application.page import PDFPageClauseProperties
from application.user import User
from .parser_service import get_parsing_instance

class FileService:
    def __init__(self, file: Files, user: User):
        self.user = user
        self.file = file
    
    async def get_file_clauses_properties(
        self, strategy
    ) -> tp.List[PDFPageClauseProperties]:
        try: 
            parsing_instance = get_parsing_instance()
            pdf_page_metadata = await parsing_instance.get_feature_of_pdf_file(
                self.file
            )
            processed_chunks = strategy.process_chunks(pdf_page_metadata)
            return processed_chunks
        except Exception as e:
            raise e
    
    async def process_annotations_details_of_clauses_from_file(
        self, version: str = "V1"
    ):
        from .strategy.strategy_factory import ChunkingStrategyFactory
        strategy = ChunkingStrategyFactory().get_strategy(version)
        processed_chunks = await self.get_file_clauses_properties(strategy)
        return processed_chunks
    