from cryptos import *
import binascii, base58

priv_keys_wif = [
    b'92CQgHdhV4txXhuL3ZwLaa7mpCzRu8mHppZANVqnonLKv96gPHs',
    b'91yoRoGbSBcRJVCYxWEwLtDuMj3SzvMg4cm9q7KqgzuhGiwSS6G',
    b'92QmukWsv3TCNDgRccQ88vqfyEFN5zQMSYRnwC2rDxUn8eet4ay',
    b'91eo9h9J5h2mgHpW4PjH4cE5UATTRkcWaynw2CvQp7q8F6shnE7']
priv_keys = [binascii.hexlify(base58.b58decode(priv_key_wif))[::-1][8:][::-1][2:] for priv_key_wif in priv_keys_wif]
addresses = [pubkey_to_hash(privtopub(priv_key)).hex() for priv_key in priv_keys]

print(addresses)
