# brent-search

Brent's method for univariate function optimization.

## Example

```python
from brent_search import brent

def func(x, s):
  return (x - s)**2 - 0.8

r = brent(lambda x: func(x, 0), -10, 10)
print(r)
```

The output should be

```python
(0.0, -0.8, 6)
```

## Install

From command line, enter

```bash
pip install brent-search
```

## Authors

* [Danilo Horta](https://github.com/horta)

## Acknowledgements

- http://people.sc.fsu.edu/~jburkardt/c_src/brent/brent.c
- Numerical Recipes 3rd Edition: The Art of Scientific Computing
- https://en.wikipedia.org/wiki/Brent%27s_method


## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/limix/brent-search/master/LICENSE.md).
