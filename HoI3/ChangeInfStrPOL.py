infile = open('c:/tmp/ARv10.hoi3', 'r')
outfile = open('c:/tmp/ARv11.hoi3', 'w')
x = 0
while True:
    x = x + 1
    line = infile.readline()
    if not line:
        break
    if line == '	owner="POL"\n':
        print "line %d: %s" % (x, line)
        x = x + 1
        line2 = infile.readline()
        vchange = False
        if (line2 == '	controller="POL"\n'):
            print "line %d: %s" % (x, line2)
            vchange = True
        outfile.write(line)
        outfile.write(line2)
        if vchange:
             while True:
                x = x + 1
                line3 = infile.readline()
                if line3 == '	infra=\n':
                    # zapis infra
                    outfile.write(line3)
                    # zapis {
                    x = x + 1
                    line3 = infile.readline()
                    outfile.write(line3)
                    # zapis  10.000 10.000 	}
                    x = x + 1
                    line3 = infile.readline()
                    outfile.write(' 10.000 10.000 	}\n')
                    break
                else:
                    outfile.write(line3)
    else:
        outfile.write(line)
infile.close()
outfile.close()
