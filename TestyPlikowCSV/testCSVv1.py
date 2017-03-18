import csv, io

c_plik = 'c:/tmp/csv1.txt'
c_delimiter = ';'
c_quoting = csv.QUOTE_NONNUMERIC
c_encoding = 'windows-1250'

fi = open(c_plik, 'r')
reader = csv.reader(fi, delimiter=c_delimiter, quoting=c_quoting)

for row in reader:
    print row
    print str(row[1]) + '; ' + row[2].decode(c_encoding)

