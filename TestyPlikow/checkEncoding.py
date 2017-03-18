import codecs

encodings = ['windows-1250', 'utf-8', 'windows-1252', 'utf-8-sig']

for e in encodings:
    try:
        # fh = codecs.open('c:/tmp/ASCII.txt', 'r', encoding=e)
        # fh = codecs.open('c:/tmp/UTF8.txt', 'r', encoding=e)
        fh = codecs.open('c:/tmp/csv1.txt', 'r', encoding=e)
        fh.readlines()
        fh.seek(0)
    except UnicodeDecodeError:
        print('got unicode error with %s , trying different encoding' % e)
    else:
        print('opening the file with encoding:  %s ' % e)
        break
fh.close()
