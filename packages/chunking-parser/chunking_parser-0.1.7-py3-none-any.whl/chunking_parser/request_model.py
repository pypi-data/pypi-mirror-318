import typing as tp
from pydantic import BaseModel, Field

class AnnotationsDataModel(BaseModel):
    bbox: tp.Union[tp.List, str]
    page_no: int
    content: str


class AnnotationsMetaRequest(BaseModel):
    file_name: str = Field(..., description="file name")
    user_id: str = Field(..., description="user id")
    type: tp.Literal["RECT_ANNOT"] = Field(..., description="type of annotation")
    data: tp.List[AnnotationsDataModel] = Field(..., description="data points")
