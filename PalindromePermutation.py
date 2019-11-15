def check_palindrome_permutation(string):
    chars = dict()
    even = len(string) % 2 == 0
    
    for s in string:
        try:
            chars[s]+=1
        except KeyError:
            chars[s] = 1

    uneven_count = 0

    for c in chars:
        if chars[c] % 2 != 0:
            uneven_count+=1

    if uneven_count > 0 and even:
            return False
    elif uneven_count > 1:
            return False
    return True


print(check_palindrome_permutation("ablewwsieaeisaaelbr"))
