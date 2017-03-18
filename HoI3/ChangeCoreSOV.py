infile = open('c:/tmp/ARv12.hoi3', 'r')
outfile = open('c:/tmp/ARv13.hoi3', 'w')
x=0
while 1:
    x=x+1
    line = infile.readline()
    if not line:
        break
    if line=='	owner="POL"\n':
        x=x+2
        line2 = infile.readline()
        line3 = infile.readline()
        if (line2=='	controller="POL"\n') and (line3=='	core="SOV"\n'):
            outfile.write('	owner="POL"\n')
            outfile.write('	controller="POL"\n')
            outfile.write('	core="POL"\n')
        else:
            outfile.write(line)
            outfile.write(line2)
            outfile.write(line3)
    else:
        outfile.write(line)
infile.close()
outfile.close()