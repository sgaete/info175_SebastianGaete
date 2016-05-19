# -*- coding: utf-8 -*-

import string


def encryptCP(text):
    text = string.lower(text)
    cenit = "cenit"
    polar = "polar"
    nword = ""

    for i in range(len(text)):
        if text[i] in cenit:
            nword = nword + polar[cenit.find(text[i])]
        elif text[i] in polar:
            nword = nword + cenit[polar.find(text[i])]
        else:
            nword = nword + text[i]
    return nword

if __name__ == "__main__":
    print encryptPolar("el weon")


