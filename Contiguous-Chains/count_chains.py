from sys import argv
import Queue

class Chain_Detector:
    def __init__(self,chain_file):
        chain_data = open(chain_file).read().splitlines()
        height,width = chain_data[0].split(' ')
        self.height,self.width = int(height),int(width)
        del chain_data[0]
        self.chain_data = []
        for row in chain_data:
            row += ' '*(self.width-len(row)+1)
            self.chain_data.append(list(row))

        chain_queue = Queue.Queue()
        self.chain_count = 0

        while self.find_link() != None:
            chain_queue.put(self.find_link())
            self.chain_count += 1

            while not chain_queue.empty():
                y,x = chain_queue.get()
                print y,x
                self.print_data()
                self.chain_data[y][x] = ' '
                if x != 0 and self.chain_data[y][x-1] == 'x':
                    chain_queue.put((y,x-1))
                if x+1 != self.width and self.chain_data[y][x+1] == 'x':
                    chain_queue.put((y,x+1))
                if y != 0 and self.chain_data[y-1][x] == 'x':
                    chain_queue.put((y-1,x))
                if y+1 != self.height and self.chain_data[y+1][x] == 'x':
                    chain_queue.put((y+1,x))

        print "Found %d chains!" % self.chain_count

    def find_link(self):
        for row in range(self.height):
            for column in range(self.width):
                if self.chain_data[row][column] == 'x':
                    return (row,column)

        return None

    def print_data(self):
        for row in self.chain_data:
            print ''.join(row)

chain_file = argv[1]
chain_detector = Chain_Detector(chain_file)
