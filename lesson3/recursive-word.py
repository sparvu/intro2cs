import sys

def read_word():
    c = sys.stdin.read(1)
    print(c)
    if c != " ":
        read_word()
    print(c)

char = read_word()

