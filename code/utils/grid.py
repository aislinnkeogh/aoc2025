class Grid:

    def __init__(self, filepath, cell_type="str"):
        self.parse(filepath, cell_type)
        self.shape = (len(self.grid), len(self.grid[0])) # rows x columns

    def parse(self, filepath, cell_type):
        with open(filepath) as f:
            match cell_type:
                case "str":
                    self.grid = [[x for x in line.strip()] for line in f]
                case "int":
                    self.grid = [[int(x) for x in line.strip()] for line in f]
                case "float":
                    self.grid = [[float(x) for x in line.strip()] for line in f]

    def get(self, x, y):
        "Maps (x, y) Cartesian coordinates to [row][col] indices"
        return self.grid[y][x]
    
    def get_adjacent_positions(self, x, y, diagonal=True):
        positions = [
            (x, y-1), # up
            (x-1, y), # left
            (x+1, y), # right
            (x, y+1) # down
        ]
        if diagonal:
            positions.extend([
                (x-1, y-1), # top left
                (x+1, y-1), # top right
                (x-1, y+1), # bottom left
                (x+1, y+1) # bottom right
            ])

        contents = []
        for i, j in positions:
            if any(cond for cond in [i<0, j<0, i>=self.shape[1], j>=self.shape[0]]): # position doesn't exist: out of bounds
                pass
            else:
                contents.append(self.get(i, j))

        return contents

    def update(self, x, y):
        self.grid[y][x] = 'x'

    def __str__(self):
        "Method to show something human-readable when print() is called on a grid object"
        return "\n".join("".join(str(cell) for cell in row) for row in self.grid)