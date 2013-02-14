import sys

def main(argv):
    for fname in argv:
        with open(fname) as f:
            #file processing stuffs

if __name__ == "__main__":
    main(sys.argv[1:])
