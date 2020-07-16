import json

from . import grammartools


def usage():
    print('''
grammar-compact.py <grammar>
    Given an inferred grammar, remove redundant rules and definitions
            ''')


def main(args) -> int:
    if not args or args[0] == '-h':
        usage()
        return 1
    gfname = args[0]
    with open(gfname) as f:
        gf = json.load(fp=f)
    grammar = gf['[grammar]']
    start = gf['[start]']
    command = gf['[command]']

    # now, what we want to do is first regularize the grammar by splitting each
    # multi-character tokens into single characters.
    g = grammartools.compact_grammar(grammar, start)
    print(json.dumps({'[start]': start, '[grammar]':g, '[command]': command}, indent=4))
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv[1:]))
