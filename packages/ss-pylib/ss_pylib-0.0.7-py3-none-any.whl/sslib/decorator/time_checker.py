from datetime import timedelta
import time


def time_checker(title:str):
  def decorator(func):
    def wrapper(*args, **kwargs):
      print(f'{title} 시작')
      start = time.time()
      result = func(*args, **kwargs)
      end = timedelta(seconds=(time.time() - start))
      print(f'{title} 종료({end})')
      return result
    return wrapper
  return decorator