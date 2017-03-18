# f=open('ARv6.hoi3', 'w')
#f = open('C:/Documents and Settings/Arek/PycharmProjects/HoI3/chg1.txt', 'r+')
f = open('c:/tmp/chg1.txt', 'r+')
for x in range(1, 7):
    l=f.readline()
    print "line %d: %s" % (x, l)
#    f.write('0123456789abcdef\r\n')
f.close()