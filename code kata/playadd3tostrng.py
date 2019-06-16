S = input()
for B in S:
    if ord(B) > 64  and ord(B) < 88 or ord(B) > 96 and ord(B) < 120:
        print(chr(ord(B)+3),end='')
    else:
        print(chr(ord(B)+3-26),end='')
        
