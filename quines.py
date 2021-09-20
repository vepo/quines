import sys

def main():
    with open(sys.argv[0]) as prog:
        print(prog.read())

if __name__ == "__main__":
    main()