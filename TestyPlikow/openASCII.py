import io

cfi = 'c:/tmp/ASCII.txt'
cfo = 'c:/tmp/ASCIIv2.txt'
c_encoding = 'windows-1250'

fi = io.open(cfi, 'r', encoding=c_encoding)
fo = io.open(cfo, 'w', encoding=c_encoding)
i=0
while 1:
    i = i + 1
    line = fi.readline()
    if not line:
        break
    nline = str(i) +' ; ' + str(len(line[1 : -1])) + ' : ' + line[1 : -1]
    print nline
    fo.write(nline + '\n')
fi.close()
fo.close()