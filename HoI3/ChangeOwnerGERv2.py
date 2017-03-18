infile = open('c:/tmp/ARv8.hoi3', 'r')
outfile = open('c:/tmp/ARv9.hoi3', 'w')
x=0
while 1:
    x=x+1
    line = infile.readline()
    if not line:
        break
    if line=='	owner="GER"\n':
        print "line %d: %s" % (x, line)
        x=x+3
        line2 = infile.readline()
        line3 = infile.readline()
        line4 = infile.readline()
        if (line2=='	controller="GER"\n') and (line4=='	core="SOV"\n'):
            print "line %d: %s" % (x-1, line2)
            print "line %d: %s" % (x, line3)
            outfile.write('	owner="POL"\n')
            outfile.write('	controller="POL"\n')
        else:
            outfile.write(line)
            outfile.write(line2)
        outfile.write(line3)
        outfile.write(line4)
    else:
        outfile.write(line)
infile.close()
outfile.close()