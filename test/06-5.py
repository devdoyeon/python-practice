import sys

src = sys.argv[1]
dst = sys.argv[2]

with open(src) as f:
    tab_content = f.read()
with open(dst, 'w') as f:
    f.write(tab_content.replace('\t', ' ' * 4))