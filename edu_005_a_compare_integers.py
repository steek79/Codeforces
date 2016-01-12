# http://codeforces.com/contest/616/problem/A
# Time Limit Exceeded

a = raw_input() # contains no more than 10^6 digits
b = raw_input()


def remove_leading_zero(n):
    while len(n) > 1:
        if n[0] == '0':
            n = n[1:]
        else:
            break
    return n


a = remove_leading_zero(a)
b = remove_leading_zero(b)

a = int(a)
b = int(b)

if a < b:
    ans = '<'
elif a > b:
    ans = '>'
else:
    ans = '='

print ans
