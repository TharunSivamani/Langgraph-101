# Langgraph-101

## Typed Annotations

### Dictionary

```python
movie = {"name": "Avengers Endgame", "year": 2019}
```

### Typed Dictionary

```python
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int

movie = Movie(name="Avenger Endgame", year=2019)
```

### Union

```python
from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x

x = 5
x = 1.234
x = "I am a string" # Error
```

### Optional

```python
from typing import Optional

def greet(msg: Optional[str]):
    return f"Msg: {msg}"
```

### Any

```python
from typing import Any

def pprintt(x: Any):
    print(x)
```

### Lambda

```python
square = lambda x: x * x

nums = [1, 2, 3, 4, 5]
sq = list(map(lambda x: x * x, nums))
```