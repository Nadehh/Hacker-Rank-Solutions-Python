#problem desc @ https://www.hackerrank.com/contests/programming-interview-questions/challenges/balanced-delimiters/submissions/code/1310195885

pairs_opening = {"(":")","[":"]","{":"}"}
opening = "({["

def balancedDelimiters(delimitirString):
    """
    Checks for balanced delimiters by using a stack.
    """
    #if delimiterString isn't even, it cannot be balanced.
    if len(delimitirString) % 2 != 0:
        return False
    stack = []
    for delimiter in delimitirString:

        if delimiter in opening:
            stack.append(delimiter)
        else:
            opening_delimiter = stack.pop()
            if delimiter != pairs_opening[opening_delimiter]:
                return False
    return True


print(balancedDelimiters(input()))
