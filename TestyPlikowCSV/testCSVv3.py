import csv, io

c_plik = 'c:/tmp/csv2v2.csv'
c_delimiter = ';'
c_quoting = csv.QUOTE_NONE
c_encoding = 'windows-1250'

fi = open(c_plik, 'r')
reader = csv.reader(fi, delimiter=c_delimiter, quoting=c_quoting)

for row in reader:
    print row, str(row[1]), row[2].decode(c_encoding)