import sys

datafile = sys.argv[1]

with open(datafile) as f:
    for line in f:
        line = line.strip();
        if line.startswith('iter'):
            print line.split('=')[1], " ",
        elif line.startswith('loss'):
            for content in line.split(','):
                print content.split('=')[1], " ",
            print
