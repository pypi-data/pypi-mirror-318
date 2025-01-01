import re
import json
from datetime import datetime


class StringHelper:
  @staticmethod
  def find_number(source:str, suffix:str) -> float:
    return re.match(r'\d+(?=㎡)')
  
  @staticmethod
  def to_json(source:any) -> str:
    return json.dumps(source, ensure_ascii=False)
  
  @staticmethod
  def entity_to_json(source:any) -> str:
    from base.entity import Entity
    if isinstance(source, list):
      elements = []
      for element in source:
        if isinstance(element, Entity):
          elements.append(element.to_dict())
      return json.dumps(elements, ensure_ascii=False)
    elif isinstance(source, Entity):
      return json.dumps(source.to_dict(), ensure_ascii=False)
    return None
  
  @staticmethod
  def from_json(source:str) -> any:
    return json.loads(source)
  
  @staticmethod
  def datetime(source:datetime) -> str | None:
    return source.strftime('%Y-%m-%d') if source is not None else None