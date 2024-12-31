class SingletonInstance:
  __instance = None
  
  @classmethod
  def __get_instance(cls):
    return cls.__instance
  
  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__instance
    return cls.__instance