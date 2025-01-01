from configparser import ConfigParser


class Config:
  def __init__(self, path:str):
    self.config_parser = ConfigParser()
    self.config_parser.read(path)
    
  def get(self, group:str|None, key:str) -> str:
    group = group if group is not None else 'common'
    return self.config_parser[group][key]