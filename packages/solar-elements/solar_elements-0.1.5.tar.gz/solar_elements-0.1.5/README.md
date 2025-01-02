# Elements

Elements is a Python library for interacting with Solar, a framework for building
cross-compatible social media platforms.

Visit [https://credenso.cafe/info/](https://credenso.cafe/info/) to learn more
about the SOLAR system.

*Elements is in active development.*

## Installation
Elements can be installed from PyPI under the name solar-elements:
`pip install solar-elements`
Alternatively, it can be cloned to the system and installed locally:
`pip install -e path/to/cloned_repo`

## Usage
Installing this library provides access to the 'elements' of online presence.

Here is some of what's possible:

### Storage
By default, Solar stores all data in plaintext JSON format. It is stored in 
a folder indicated by the Solar config file (...) or 'data/' by default.

```
from elements.core import Element
e = Element(content="Hello!")
path = e.save()
print(path)
> 'data/elements/01432c93.json'
e2 = Element.load('elements/01432c93')
assert e.id == e2.id
```

### Encryption
Solar implements Nostr-standard encryption (according to [NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md))

```
from elements.core.encryption import encrypt, decrypt, nonce
key = nonce()
safu = encrypt('hello', key)
greeting = decrypt(safu, key)
print(greeting)
> 'hello'
```

### Accounts
One of the most important features of Solar is its account system. Each Solar
account is identified by a 32-byte private key. This key can be used as a [BIP32](https://en.bitcoin.it/wiki/BIP_0032) master key in order to derive an arbitrary
number of other keys, each of which can be used to integrate with other protocols.

To put it simply, a Solar account can be used to derive Bitcoin wallets, SSH keys,
Nostr identities and much more.

```
from elements.accounts import Member
from elements.sessions import Session
account = Member.register('npc', password='1234')
account.save()
s = Session(account, '1234') 
nostr = s.integration('nostr')
print(nostr.nsec)
> nsec1abc123...
print(nostr.npub)
> npub1abc123...
```

Check the src/elements/accounts/integrations/ folder to learn more about
the integrations available.


## Development

This package is maintained using poetry.
