def singleton(klass):
  class Singleton(klass):
    _instance = None
    _sealed = False
    
    def __new__(klass, *args, **kwargs):
      if Singleton._instance is None:
        Singleton._instance = super(Singleton, klass).__new__(klass)
        Singleton._instance._sealed = False
      return Singleton._instance
    
    def __init__(self, *args, **kwargs):
      if self._sealed: return
      super(Singleton, self).__init__(*args, **kwargs)
      self._sealed = True
  
  Singleton.__name__ = klass.__name__
  return Singleton