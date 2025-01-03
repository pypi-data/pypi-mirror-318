from enum import Enum
from datetime import datetime
from sslib.helper.string import StringHelper


class DictEx:
  def to_dict(self, include_none:bool = False):
    output = {}
    for k, v in self.__dict__.items():
      if include_none == False and v is None: continue
      output[k] = self._convert(v)
    return output
    
  def _convert(self, source:any) -> any:
    if isinstance(source, datetime):
      return StringHelper.datetime(source)
    elif isinstance(source, Enum):
      return source.value
    else:
      return source