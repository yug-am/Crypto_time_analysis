from crypto_timer.grapher import grapher
from hash_timer.compare_sha import compare_sha_grapher
from key_exchange_timer.dh_key_exchange_grapher import *
from crypto_timer.rsa_deep_dive import *


def time_cypto():
    #   launches cypto timer
    hash_compare = False
    dhke = False
    rsa_dd = False
    if hash_compare:
        compare_sha_grapher()
    elif rsa_dd:
        rsa_deep_dive()
    elif dhke:
        dh_key_exchange_grapher()
    else:
        grapher()


if __name__ == '__main__':
    time_cypto()
