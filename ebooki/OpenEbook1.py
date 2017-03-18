import io

c_fi = 'C:/Documents and Settings/All Users.WINDOWS/Dokumenty/eBooks/Calibre/Borun Krzysztof/Male zielone ludziki - T1 (66)/Male zielone ludziki - T1 - Borun Krzysztof.txt'
c_fo = 'c:/tmp/ebook1.txt'
c_encoding = 'windows-1250'

fi = io.open(c_fi, 'r', encoding=c_encoding)
fo = io.open(c_fo, 'w', encoding=c_encoding)
i=0
j=4
while 1:
    i = i + 1
    line = fi.readline()
    if not line:
        break
    if line == (str(j) + ' \n'):
        j = j + 1
        line = fi.readline()
        line = fi.readline()
        line = fi.readline()
    nline = str(i) +' ; ' + str(len(line)) + ' : ' + line
    print nline
    fo.write(line)
fi.close()
fo.close()