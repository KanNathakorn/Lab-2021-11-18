infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
for read in infile:
    capital = read[0].upper()
    outfile.write(capital + read[1:])
infile.close()
outfile.close()
