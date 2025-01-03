# Introduction

Search of both English-Korean and Korean-English dictionaries of endic.naver.com

Based on the [NDic](https://github.com/jupiny/ndic) repository by [SeunghwanJoo](https://github.com/jupiny). However, this library was outdated, so this is a "updated" version of it.

# Installation

Install via pip:

```cmd
pip install naverdict
```

# How to use

Using this as a Python package you can use:

```python
>>> from naverdict.search import search

>>> search("하다")
```
```
["do", "have", "give", "make", "play"]
```

Using this as a CMD/CLI you can use:

```bash
$ naverdict 하다
```
```
do
have
give
make
play
```