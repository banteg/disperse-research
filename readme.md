# Disperse Reseach

The benchmark setup is built from low-level primitives offered by `py-evm`.
- Relies solely on the virtual machine and an in-memory state database. Mining and blockchain components have been removed.
- It provides the tools to make tests against different forks trivial.
- Utils to generate deterministic keypairs, manipulate storage and more.
- Effective gas estimation using binary search.

Read the [research paper](https://github.com/banteg/disperse-reseach/blob/master/paper/disperse.pdf).

## Installation

Requires Python 3.7, install using:
```
pipenv install
```

To run the full suite:
```
pipenv run benchmark
```

To install the tools needed to compile the contracts, run:
```
yarn
```

To compile the contracts:
```
npx buidler compile
```
