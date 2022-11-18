import sys

opt = sys.argv[1]

if opt == '-a':
    with open('memo.txt', 'a') as f:
        f.write(f'{sys.argv[2]}\n')

elif opt == '-v':
    with open('memo.txt') as f:
        print(f.read())