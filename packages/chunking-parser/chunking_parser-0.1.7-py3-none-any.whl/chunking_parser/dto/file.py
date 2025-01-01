import typing as tp
from pydantic import BaseModel, Field

class AnnotationsDataModelDTO(BaseModel):
    bbox: tp.Union[tp.List, str]
    page_no: int
    content: str


class AnnotationsMetaDTO(BaseModel):
    file_name: str = Field(..., description="file name")
    user_id: str = Field(..., description="user id")
    type: tp.Literal["RECT_ANNOT"] = Field(..., description="type of annotation")
    data: tp.List[AnnotationsDataModelDTO] = Field(..., description="data points")

