# -*- coding: utf-8 -*-
import random
import re

replacement_sequence = {
    "spurdo": "spurdo",
    "sparde": "spärde",
    "kek": "geg",
    "epic": "ebin",
    "right": "rite",
    "your": "ur",
    "god": "dog",
    "linux": "linugs",
    "fucking": "fuggin",
    "are": "r",
    "you": "u",
    "wh": "w",
    "th": "d",
    "af": "ab",
    "ap": "ab",
    "ca": "ga",
    "ck": "gg",
    "co": "go",
    "ev": "eb",
    "ex": "egz",
    "et": "ed",
    "iv": "ib",
    "it": "id",
    "ke": "ge",
    "nt": "nd",
    "op": "ob",
    "ot": "od",
    "po": "bo",
    "pe": "be",
    "pi": "bi",
    "up": "ub",
    "va": "ba",
    "ck": "gg",
    "cr": "gr",
    "kn": "gn",
    "lt": "ld",
    "mm": "m",
    "nt": "dn",
    "pr": "br",
    "ts": "dz",
    "tr": "dr",
    "bs": "bz",
    "ds": "dz",
    "es": "es",
    "fs": "fz",
    "gs": "gz",
    "is": "iz",
    "as": "az",
    "ls": "lz",
    "ms": "mz",
    "ns": "nz",
    "rs": "rz",
    "ss": "sz",
    "ts": "tz",
    "us": "uz",
    "ws": "wz",
    "ys": "yz",
    "alk": "olk",
    "ing": "ign",
    "ic": "ig",
    "ng": "nk",
    "p": "b"
}
sillyOs = ["ö", "ø", "0"]


def multiple_replace(sequence, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, sequence.keys())))
    return regex.sub(lambda mo: sequence[mo.string[mo.start():mo.end()]], text)


def callback(matchobj):
    length = random.randint(0, 4) + 1
    return " " + random.choice([':' + 'D' * length, 'x' + 'D' * length])


def spurdify(text: str) -> str:
    result = text.lower()

    result = multiple_replace(replacement_sequence, result)
    result = re.sub(r'o', lambda m: random.choice(sillyOs), result)
    result = re.sub(r'[.,;]', callback, result)

    return result
