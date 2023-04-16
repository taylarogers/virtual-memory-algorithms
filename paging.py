import sys
from random import seed
from random import randint

def FIFO(size, pages):
    frames = []
    pageFaults = 0
    
    for page in pages:
        if frames.count(page) == 0:
            pageFaults += 1

            if len(frames) < size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            continue

    return(pageFaults)

def LRU(size, pages):
    return("LRU")

def OPT(size, pages):
    return("OPT")

def main():
    numPages = 7
    pages = []

    for i in range(numPages):
        pages.append(randint(0,9))

    size = int(sys.argv[1])

    print(pages)
    print('FIFO:', FIFO(size, pages), 'page faults.')
    print('LRU:', LRU(size, pages), 'page faults.')
    print('OPT:', OPT(size, pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()