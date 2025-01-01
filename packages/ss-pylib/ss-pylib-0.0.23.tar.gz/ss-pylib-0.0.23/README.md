# SWEET-SOOP Python Library

## Decorator
### Singleton
**How to use**
```python
from sslib.decorator.singleton import singleton

@singleton
class MyClass:
  pass
```

## Helper
### Config
**.env**
```c
[common] //group
NAME = sweetsoop  //key = value
```
**How to use**
```python
from sslib.helper.config import Config

config = Config(os.path.dirname(__file__) + '/.env')
print(config.get('common.NAME'))
```