import re
f = open('6-13.csv', 'r')
lines = []
for line in f.readlines():
    line = re.sub(r',(\d\d\d[,.])', r'\1', line)
    cols = line.split(',')
    _cols = []
    for col in cols:
        #col = col.decode('gbk')
        col = re.sub(r'\s\s+', r'', col)
        #col = col.encode('utf-8')
        _cols.append(col)
    lines.append('\t'.join(_cols))
f.close()

f = open('new.csv', 'w')
f.write('\n'.join(lines))
f.close()
