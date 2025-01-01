from abc import abstractmethod
import json
import typing as tp
from application import PDFPageClauseProperties, Files, PDFPageTextInfo, User
from chunking_parser.request_model import AnnotationsMetaRequest, AnnotationsDataModel
from application.rule_engine import ClauseBreakPointRules


class ChunkingStrategy:

    @abstractmethod
    def check_for_starting_and_eol_char(
        self,
        current_metadata: PDFPageTextInfo,
        next_metadata : PDFPageTextInfo):
        pass

    def process_chunks(
        self, content_meta: tp.List[PDFPageTextInfo]
    ) -> tp.List[PDFPageClauseProperties]:
        if not content_meta:
            return None

        #Clearing any empty chunks
        content_meta = [chunk for chunk in content_meta if chunk.is_valid()]
        #for chunk in content_meta:
            #print(chunk)
            #print('**')

        idx = 0
        prev_char_regex = None
        prev_char_value = None
        prev_page_no = 1
        chunk_cnt = 0
        start_char_x_coord = 0.0
        text_paragraph = ""
        max_x2, max_y2, min_x1, min_y1 = 0, 0, float("inf"), float("inf")
        total_meta_len = len(content_meta)
        result = []
        combined_bbox = []
        para = ""
        block_start = True
        while idx < total_meta_len:
            (
                eol_exist,
                start_char_regex,
                start_char_value,
            ) = (True, None, None)

            current_metadata = content_meta[idx]
            succeeding_metadata = content_meta[idx+1] if idx < (total_meta_len-1) else None

            page_no = current_metadata.page_no
            x1, y1, x2, y2 = current_metadata.bbox

            if succeeding_metadata:
                _, succ_y1, _, _ = succeeding_metadata.bbox
                if y1 != succ_y1 or page_no != prev_page_no:
                    start_char_value, start_char_regex, eol_exist = (
                        self.check_for_starting_and_eol_char(
                            current_metadata, succeeding_metadata
                        )
                    )

            if not text_paragraph:
                start_char_x_coord = x1
            text_paragraph += current_metadata.text + " "

            if prev_page_no < page_no:
                if text_paragraph:
                    bbox = [min_x1, min_y1, max_x2, max_y2]
                    combined_bbox.append(bbox)
                prev_page_no = page_no
                max_x2, max_y2, min_x1, min_y1 = 0, 0, float("inf"), float("inf")
            max_x2 = max(max_x2, x2)
            max_y2 = max(max_y2, y2)
            min_x1 = min(min_x1, x1)
            min_y1 = min(min_y1, y1)

            if start_char_regex or eol_exist:
                para = text_paragraph.strip()
                bbox = [min_x1, min_y1, max_x2, max_y2]
                combined_bbox.append(bbox)
                if result and not result[-1].identifier_regex:
                    if (
                        prev_char_value
                        and ClauseBreakPointRules.remove_extra_puncuations(
                            prev_char_value
                        ).upper()
                        in list(ClauseBreakPointRules.roman_values.keys())
                    ):
                        prev_char_regex = (
                            ClauseBreakPointRules.roman_numbers_in_braces_regex
                        )

                properties_object = PDFPageClauseProperties(
                    chunk_cnt,
                    identifier_regex=(
                        str(prev_char_regex) if prev_char_regex else prev_char_regex
                    ),
                    identifier_value=(
                        str(prev_char_value) if prev_char_value else prev_char_value
                    ),
                    content=para,
                    block_start=block_start,
                    bbox=json.dumps(bbox),
                    page_no=page_no,
                    colon=ClauseBreakPointRules.check_colon(line=para),
                    start_char_x_coord=start_char_x_coord,
                )
                result.append(properties_object)
                text_paragraph = ""
                block_start = succeeding_metadata.block_start if succeeding_metadata else True
                chunk_cnt += 1
                prev_char_regex = start_char_regex
                prev_char_value = start_char_value
                max_x2, max_y2, min_x1, min_y1 = 0, 0, float("inf"), float("inf")
                combined_bbox = []
            idx += 1

        if text_paragraph:
            bbox = [min_x1, min_y1, max_x2, max_y2]
            result.append(
                PDFPageClauseProperties(
                    chunk_cnt,
                    identifier_regex=(
                        str(prev_char_regex) if prev_char_regex else prev_char_regex
                    ),
                    identifier_value=(
                        str(prev_char_value) if prev_char_value else prev_char_value
                    ),
                    content=text_paragraph,
                    block_start=block_start,
                    bbox=json.dumps(bbox),
                    page_no=page_no,
                    colon=ClauseBreakPointRules.check_colon(line=para),
                    start_char_x_coord=start_char_x_coord,
                )
            )
        return result



    def extract_bbox_details(
        self, user: User, file: Files, objects: tp.List[PDFPageClauseProperties]
    ) -> AnnotationsMetaRequest:
        data = [
            AnnotationsDataModel(
                bbox=obj.bbox, page_no=obj.page_no, content=obj.content
            )
            for obj in objects
        ]
        return AnnotationsMetaRequest(
            file_name=file.file_name,
            data=data,
            user_id=user.get_userid(),
            type="RECT_ANNOT",
        )

    def get_page_no_to_bbox_mapping(
        self, objects: tp.List[PDFPageClauseProperties]
    ) -> tp.Dict[int, any]:
        page_no_to_bbox_mapping = {}
        for obj in objects:
            if obj.page_no not in page_no_to_bbox_mapping:
                page_no_to_bbox_mapping[obj.page_no] = [json.loads(obj.bbox)]
            else:
                page_no_to_bbox_mapping[obj.page_no].append(json.loads(obj.bbox))

        return page_no_to_bbox_mapping
