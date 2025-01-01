import httpx


class Slack:
  def __init__(self, webHook:str):
    self.__webHook = webHook
    
  def send_message(self, message:str) -> bool:
    res = httpx.post(self.__webHook, json={'text':message})
    return True if res.status_code == httpx.codes.OK else False