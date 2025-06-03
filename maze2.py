

def __break_walls_r(self,i,j):
    self.__cell[i][j].visited = True
    while True:
        next_index_list = [] 