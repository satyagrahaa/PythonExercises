#  palindrome

x = 'i am not a palindrome!'
y = 'liarsrail'
#  print ''.join(reversed(y)) == y

"""
def pal(st):
	if st[i] == st[-i-1]:
		return pal(st.strip(st[i])
	else:
		return

a = pal(y)
print a

"""


def palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False


xx = palindrome(x)
print xx
