# Comparison

Byzantium and Constantinople are different Ethereum versions. Constantinople will be activated on the mainnet on January 16th, 2019.

**Recipients** column shows the maximum number of recipients for a transaction using the block gas limit.
 **Gas usage** is shown per transfer.
**Fee** is additional service fee.

## Byzantium

### Ether

| Contract | Recipients | Gas usage | Additional fee |
|---|---|---|---|
| disperse | 230-830 | 9629-34701 | none |
| bulksender | 230-255 | 9873-34772 | 0.01 eth |
| multisender | 200-200 | 10057-35057 | 0.05 eth |

### Tokens

| Contract | Recipients | Gas usage | Additional fee |
|---|---|---|---|
| disperse | 242-449 | 17813-32928 | none |
| bulksender | 207-255 | 23577-38508 | 0.01 eth |
| multisender | 200-200 | 23921-38921 | 0.05 eth |

## Constantinople

### Ether

| Contract | Recipients | Gas usage | Additional fee |
|---|---|---|---|
| disperse | 230-830 | 9629-34701 | none |
| bulksender | 230-255 | 9873-34772 | 0.01 eth |
| multisender | 200-200 | 10057-35057 | 0.05 eth |

### Tokens

| Contract | Recipients | Gas usage | Additional fee |
|---|---|---|---|
| disperse | 284-616| 12977-28091 | none |
| bulksender | 255-255 | 14052-28993 | 0.01 eth |
| multisender | 200-200 | 14369-29369 | 0.05 eth |


## Installation

Requires Python 3.7, install using:
```
pipenv install
```

To run this benchmark:
```
pipenv run benchmark
```
