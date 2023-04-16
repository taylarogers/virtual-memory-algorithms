import sys
from random import seed
from random import randint

def FIFO(size, pages):
    return("FIFO")

def LRU(size, pages):
    return("LRU")

def OPT(size, pages):
    return("OPT")

def main():
    numPages = 50
    pages = []

    for i in range(numPages):
        pages.append(randint(0,9))

    size = int(sys.argv[1])

    print('FIFO:', FIFO(size, pages), 'page faults.')
    print('LRU:', LRU(size, pages), 'page faults.')
    print('OPT:', OPT(size, pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()