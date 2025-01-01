import json
import typing as tp
from .strategy_abs import ChunkingStrategy
from application import PDFPageClauseProperties, PDFPageTextInfo
from application.rule_engine import ClauseBreakPointRules


class AdvancedChunkingStrategy(ChunkingStrategy):
    def check_for_starting_and_eol_char(
        self,
        current_metadata: PDFPageTextInfo,
        next_metadata : PDFPageTextInfo
    ):
        next_text = next_metadata.text
        current_text = current_metadata.text

        #Using the logic from BasicChunkingStrategy
        block_char_value, block_char_regex = (
            ClauseBreakPointRules.check_decimal_numbers_with_period_as_starting_char(
                next_metadata.text
            )
        )
        next_metadata.block_start = True if block_char_value else False

        start_char_value, start_char_regex = ClauseBreakPointRules.check_starting_char(
            next_text
        )
        eol_exist = ClauseBreakPointRules.check_condition_for_eol(
            line=current_text.strip()
        )
        if (
            next_metadata.is_bold()
            and not current_metadata.is_bold()
            and ClauseBreakPointRules.check_period(line=current_text.strip())
        ):
            eol_exist = True

        if next_metadata.is_ocr():
            eol_exist = True

        if(
            next_metadata.startswith(['SCHEDULE', 'APPENDIX', 'EXHIBIT'])
            and next_metadata.is_next_page(current_metadata)
          ):
            next_metadata.block_start = True
            eol_exist = True
        return start_char_value, start_char_regex, eol_exist

class BasicChunkingStrategy(ChunkingStrategy):

    def check_for_starting_and_eol_char(
        self,
        current_metadata: PDFPageTextInfo,
        next_metadata : PDFPageTextInfo
    ):

        start_char_value, start_char_regex = (
            ClauseBreakPointRules.check_decimal_numbers_with_period_as_starting_char(
                next_metadata.text
            )
        )
        next_metadata.block_start = True if start_char_value else False
        if next_metadata.is_ocr():
            eol_exist = True
        else:
            eol_exist = ClauseBreakPointRules.check_colon(current_metadata.text.strip())

        return start_char_value, start_char_regex, eol_exist
