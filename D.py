filename = input('Enter a filename: ')
opendict = open('dict.txt', 'r')
dictfile = opendict.read()
try:
    openfile = open(filename, 'r')
    num = 0
    for read in openfile:
        num += 1
        x = read.lower().replace(',', '').replace('.', '').strip().split()
        y = read.replace(',', '').replace('.', '').strip().split()
        i = 0
        while i < len(x):
            if x[i] not in dictfile.lower().split():
                print(f'Line {num}:', y[i])
            i += 1
except FileNotFoundError:
    print('Error: Cannot open the file')
