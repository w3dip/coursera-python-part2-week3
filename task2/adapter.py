class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        lights = []
        obstacles = []
        rows = len(grid)
        columns = len(grid[0])
        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == 1:
                    lights.append((y, x))
                elif grid[x][y] == -1:
                    obstacles.append((y, x))
        self.adaptee.set_dim((columns, rows))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()