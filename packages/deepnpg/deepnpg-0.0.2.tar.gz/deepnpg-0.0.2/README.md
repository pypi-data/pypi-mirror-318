# DeepNPG: Deep Neural Preconditioner with Graph Neural Networks

[![!pypi](https://img.shields.io/pypi/v/deepnpg?color=purple)](https://pypi.org/project/deepnpg/)
[![Download Status](https://img.shields.io/pypi/dm/deepnpg.svg?label=PyPI%20downloads)](https://pypi.org/project/deepnpg/)

``DeepNPG`` is a Python library for building preconditiioner with Graph Neural Networks. It provides straightforward interfaces to convert matrix into graph and perform efficient neural network training.

All data (e.g., ``numpy.ndarray``, ``spicpy.sparse.csc/csr/bsr``) will be automatically converted into sparse COOrdinate format (COO format), and then to gemetric data format.


## Install

``DeepNPG`` can be installed easily with pip bash command:

```Python
pip install deepnpg
```