import sys
from random import seed
from random import randint

# The oldest page in memory is removed, and new page can be inserted
def FIFO(size, pages):
    frames = []
    pageFaults = 0
    
    for page in pages:
        # Check if page is in memory
        if frames.count(page) == 0:
            pageFaults += 1

            # Check if all frames in memory are in use
            if len(frames) < size:
                frames.append(page)
            else:
                # Remove first frame (oldest)
                frames.pop(0)
                frames.append(page)
        else:
            # Page can just be accessed an nothing further to be done
            continue

    return(pageFaults)

# The page that was least recently used in memory is removed, and a new page can be inserted
def LRU(size, pages):
    frames = []
    pageFaults = 0

    for page in pages:
        # Check if frame is in memory
        if frames.count(page) == 0:
            pageFaults += 1

            # Check if frame 
            if len(frames) < size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            index = frames.index(page)
            frames.append(frames[index])
            frames.pop(index)
        
    return(pageFaults)
# The page the will be used the latest in the future is removed, and new page added
def OPT(size, pages):
    frames = []
    pageFaults = 0

    # Run through copy of array - allow you to pop values off the array of future values and just search through those
    for page in pages[:]:
        # Check if frame is in memory
        if frames.count(page) == 0:
            pageFaults += 1
            # Remove page to keep track of future values
            pages.pop(0)

            # Check if there is space in memory or not
            if len(frames) < size:
                frames.append(page)
            else:
                # Keep range of the indexes of the next occurring values to be able to find the largest
                nextOccurances = []

                # Find the indexes of the next occurances for each value in memory
                for i in range(size):
                    if pages.count(frames[i]) != 0:
                        nextOccurances.append(pages.index(frames[i]))
                    else:
                        # Use this value when the page is going to be used later
                        nextOccurances.append(-1)
                
                # Remove the value in frames that has the largest index valueor isn't going to be mentioned later
                if nextOccurances.count(-1) == 0:
                    frames.pop(nextOccurances.index(max(nextOccurances)))
                else:
                    frames.pop(nextOccurances.index(-1))

                frames.append(page)
        else:
            # Remove page to keep track of future values
            pages.pop(0)
            continue
    
    return(pageFaults)

def main():
    # Hardcoded value of many pages should be used to test the algorithms
    numPages = 7
    pages = []

    # Create random values between 0 and 9 that will be used
    for i in range(numPages):
        pages.append(randint(0,9))

    pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]

    # Retrieve terminal command from user stating number of frames in memory
    size = int(sys.argv[1])

    # Determine page faults for each algorithmn and print to screen
    print(pages)
    print('FIFO:', FIFO(size, pages), 'page faults.')
    print('LRU:', LRU(size, pages), 'page faults.')
    print('OPT:', OPT(size, pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()