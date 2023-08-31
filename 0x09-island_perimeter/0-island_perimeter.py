#!/usr/bin/python3
""" Island Perimeter. """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid. """
    # Handle empty grid.
    if not grid:
        return 0

    # Initialize perimeter.
    perimeter = 0
    # Get grid dimensions.
    rows = len(grid)
    cols = len(grid[0])
    # Iterate over grid.
    for row in range(rows):
        for col in range(cols):
            # Check if cell is land.
            if grid[row][col] == 1:
                # Check the cell before.
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check the cell after.
                if col + 1 >= cols or grid[row][col + 1] == 0:
                    perimeter += 1
                # Check the cell above.
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check the cell below.
                if row + 1 >= rows or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter