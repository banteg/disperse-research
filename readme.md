# Disperse Reseach

The benchmark setup is built from low-level primitives offered by `py-evm`.
- Relies solely on the virtual machine and in-memory state database. Mining and blockchain are removed.
- It provides the tools to make tests against different forks trivial.
- Utils to generate deterministic keypairs, manipulate storage keys and effective gas estimation using binary search.

## Installation

Requires Python 3.7, install using `pipenv`.

To run the full suite:
```
pipenv run benchmark
```
