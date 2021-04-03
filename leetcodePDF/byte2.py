# decode the string. print all decoding ways.

# string = input().strip()
S = '12'
d = {k:v for k, v in zip( list(range(1, 27)), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def forward(path, i):
    if i >= len(S):
        print(''.join(path))
        return 

    if 1<= int(S[i]) <=9:
        path.append(d[ int(S[i]) ])
        forward(path, i+1)
        path.pop()
    if i < len(S)-1 and (10 <= int(S[i:i+2]) <= 26):
        path.append( d[ int(S[i:i+2])  ])
        forward(path, i+2)
        path.pop()

forward([], 0)