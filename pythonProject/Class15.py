import random
import string
def random_string(length):
    characters = string.ascii_letters
    random_str = ''.join(random.choices(characters, k=3))
    return random_str

print("Coding...")
s = input("Enter your string : ")
ans = ''

if not len(s) > 3:
    ans = s[::-1]
    print("Encoded string :", ans)
else:
    ch = s[:1]
    s_removed = s[1:]
    s_new = s_removed + ch
    rand1 = random_string(3)
    rand2 = random_string(3)
    ans = rand1 + s_new + rand2
    print("Encoded string :", ans)

print("Decoding...")
if not len(ans) > 3:
    rev = ans[::-1]
    print("Decoded string : ", rev)
else:
    s_parsed = ans[3:-3]
    ch_last = s_parsed[-1:]
    s_removed = s_parsed[:-1]
    rev = ch_last + s_removed
    print("Decoded string :", rev)