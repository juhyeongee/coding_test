import sys

N = int(sys.stdin.readline())

for i in range(N):
    sentence = sys.stdin.readline().split()
    new_sentence = []
    for j in sentence:
        j = j[::-1]
        new_sentence.append(j)
    print(' '.join(new_sentence))
        