from pydantic import BaseModel

class FileMeta(BaseModel):
    filename: str
    url: str
