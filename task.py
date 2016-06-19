import sys

class parser:

    def __init__(self, inTxt, pantTxt):
        self.input = open(inTxt)
        self.pant = open(pantTxt)
        print("Initializer has started")


def main(argv):
    if len(argv) < 3:
        sys.stderr.write("Not enough arguments! usage: python task.py in.txt pant.txt")
        sys.exit(1)

    pars = parser(argv[1], argv[2])

if __name__ == "__main__":
    sys.exit(main(sys.argv))