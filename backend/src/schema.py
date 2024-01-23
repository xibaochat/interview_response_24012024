from pydantic import BaseModel
from typing import Optional
from typing import List, Union

class Record(BaseModel):
    instruction: List[Union[int, str]]
    result: Optional[int] = None
