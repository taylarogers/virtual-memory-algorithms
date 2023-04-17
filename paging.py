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
    frames = []
    pageFaults = 0
    usedTime = []

    for page in pages:
        if frames.count(page) == 0:
            pageFaults += 1

            for i in range(len(frames)):
                usedTime[i] += 1

            if len(frames) < size:
                frames.append(page)
                usedTime.append(0)
            else:
                frames.pop(usedTime.index(max(usedTime)))
                usedTime.pop(usedTime.index(max(usedTime)))                
                
                frames.append(page)
                usedTime.append(0)
        else:
            for i in range(len(frames)):
                usedTime[i] += 1

            usedTime[frames.index(page)] = 0
        
    return(pageFaults)

def OPT(size, pages):
    frames = []
    pageFaults = 0

    for page in pages[:]:
        if frames.count(page) == 0:
            pageFaults += 1
            pages.pop(0)

            if len(frames) < size:
                frames.append(page)
            else:
                nextOccurances = []

                for i in range(size):
                    if pages.count(frames[i]) != 0:
                        nextOccurances.append(pages.index(frames[i]))
                    else:
                        nextOccurances.append(10000000000)
                
                frames.pop(nextOccurances.index(max(nextOccurances)))
                frames.append(page)
        else:
            pages.pop(0)
            continue
    
    return(pageFaults)

def main():
    numPages = 20
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