from sys import argv import string
class Adjacency_Matrix:
    def __init__(self, vfile):
        self.moves = {(0,1):'-',(1,1):'\\',(1,0):'|',(1,-1):'/',(0,-1):'-',(-1,-1):'\\',(-1,0):'|',(-1,1):'/'}
        self.matrix = []
        self.graph = [list(line) for line in open(vfile).read().splitlines()]
        self.width = 0
        self.height = int(self.graph[0][0])
        del self.graph[0]
        for line in self.graph:
           if len(line) > self.width:
               self.width = len(line)

        for line in range(self.height):
            self.graph[line] += [' '] * (self.width-len(self.graph[line]))

        self.create_matrix()
        self.print_matrix()

        for y in range(self.height):
            for x in range(self.width):
                if self.graph[y][x] in string.ascii_lowercase:
                    print "Searching for connections to " + self.graph[y][x]
                    for check in self.moves.keys():
                        check_y = y + check[0]
                        check_x = x + check[1]
                        if check_y in range(self.height) and check_x in range(self.width) and self.graph[check_y][check_x] == self.moves[check]:
                            self.search_for_vertex(y,x,check, self.graph[y][x])

        for line in self.graph:
            print ''.join(line)

        self.print_matrix()

    def search_for_vertex(self,y,x,check, char):
        search_y = y + check[0]*2
        search_x = x + check[1]*2
        searching = True
        while searching:
            if search_y not in range(self.height) or search_x not in range(self.width) or self.graph[search_y][search_x] == ' ':
                return None

            elif self.graph[search_y][search_x] in string.ascii_lowercase:
                print "Found connected vertex " + self.graph[search_y][search_x]
                self.matrix[string.ascii_lowercase.index(char)][string.ascii_lowercase.index(self.graph[search_y][search_x])] = '1'
                self.matrix[string.ascii_lowercase.index(self.graph[search_y][search_x])][string.ascii_lowercase.index(char)] = '1'
                return None

            elif self.graph[search_y][search_x] == '#':
                print "Found vertex bridge!"
                for new_check in self.moves.keys():
                    new_check_y = search_y + new_check[0]
                    new_check_x = search_x + new_check[1]
                    if new_check != (-check[0],-check[1]) and new_check_y in range(self.height) and new_check_x in range(self.width) and self.graph[new_check_y][new_check_x] == self.moves[new_check]:
                        self.search_for_vertex(search_y,search_x,new_check,char)
                        return None
            search_y += check[0]
            search_x += check[1]

    def create_matrix(self):
        num_chars = 0
        for line in self.graph:
            for space in line:
                if space in string.ascii_lowercase:
                    num_chars += 1

        self.matrix = [['0' for _ in range(num_chars)] for _ in range(num_chars)]

    def print_matrix(self):
        for line in self.matrix:
            print ''.join(line)

vfile = argv[1]
adjacency_matrix = Adjacency_Matrix(vfile)
