# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index= []
    length = 0
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            index.append(i)
            length+=1

        if next in ")]}":
            if(length==0):
                return i+1
            length -= 1
            if are_matching(opening_brackets_stack.pop(),next):
                index.pop()
            else:
                return i+1
    if(length != 0):
        return index[0]+1
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
