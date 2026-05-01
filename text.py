"""
Adapted from from the Helmut project.
https://github.com/okfn/helmut/blob/master/helmut/text.py
"""

from unicodedata import normalize as ucnorm, category


def normalize(text):
    """Simplify a piece of text to generate a more canonical
    representation. This involves lowercasing, stripping trailing
    spaces, removing symbols, diacritical marks (umlauts) and
    converting all newlines etc. to single spaces.
    """
    text = text.lower().replace("the university of", "university of").strip()
    decomposed = ucnorm("NFKD", text)
    filtered = []
    for char in decomposed:
        cat = category(char)
        if cat.startswith("C"):
            filtered.append(" ")
        elif cat.startswith("M"):
            # marks, such as umlauts
            continue
        elif cat.startswith("Z"):
            # newlines, non-breaking etc.
            filtered.append(" ")
        elif cat.startswith("S"):
            # symbols, such as currency
            continue
        else:
            filtered.append(char)
    text = "".join(filtered)
    while "  " in text:
        text = text.replace("  ", " ")
    # Remove unwanted characters
    # Undocumented bugs in the SearchFAST/AssignFAST API cause it to
    # choke on parantheses and colons, returning a 400: Bad Request error
    # if they're part of the query. Replacing hyphens with a space because
    # the original Helmut code did and it doesn't seem like it could do
    # any harm.
    tt = str.maketrans({"(": "", ")": "", ":": "", "-": " "})
    text = text.translate(tt)

    return ucnorm("NFKC", text)


def url_slug(text):
    text = normalize(text)
    text = text.replace(" ", "-")
    text = text.replace(".", "_")
    return text


def tokenize(text, splits="COPZ"):
    token = []
    for c in str(text, "utf-8"):
        if category(c)[0] in splits:
            if len(token):
                yield "".join(token)
            token = []
        else:
            token.append(c)

    if len(token):
        yield "".join(token)
