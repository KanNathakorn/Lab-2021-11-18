filename = input()
try:
    openfile = open(filename, 'r')
    for read in openfile:
        print(read, end='')
except:
    print('ERROR: File not found')
