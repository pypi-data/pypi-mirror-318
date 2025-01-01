[![Testcases](https://github.com/iromli/sprig-aes/actions/workflows/testcases.yml/badge.svg)](https://github.com/iromli/sprig-aes/actions/workflows/testcases.yml)

# sprig-aes

Library and CLI to encrypt and decrypt text using AES CBC mode.

Note that the implementation is ported from:

1. http://masterminds.github.io/sprig/crypto.html#encryptaes
2. http://masterminds.github.io/sprig/crypto.html#decryptaes


## Installation

Typical installation using `pip`:

```sh
pip install sprig-aes
```

This will install the `sprig_aes` library and `sprig-aes` CLI.

Note that as per version `0.6.0`, users may install self-contained Python zipapps (CLI-only) using the following command:

```sh
pip install shiv
make zipapp
mv sprig-aes.pyz ~/.local/bin/sprig-aes
```

## Using The Library

```py3
from sprig_aes import sprig_encrypt_aes
from sprig_aes import sprig_decrypt_aes

key = "6Jsv61H7fbkeIkRvUpnZ98fu"
enc_text = sprig_encrypt_aes("a secret message", key)
dec_text = sprig_decrypt_aes(enc_text, key)
```

## Using The CLI

Encrypt/decrypt simple string:

```sh
enc_text=$(sprig-aes encrypt 'a secret message' --key 6Jsv61H7fbkeIkRvUpnZ98fu)
sprig-aes decrypt "$enc_text" --key 6Jsv61H7fbkeIkRvUpnZ98fu
```

Encrypt/decrypt contents of a file:

```sh
sprig-aes encrypt-file /path/to/file --key 6Jsv61H7fbkeIkRvUpnZ98fu > /path/to/encrypted-file
sprig-aes decrypt-file /path/to/encrypted-file --key 6Jsv61H7fbkeIkRvUpnZ98fu
```
