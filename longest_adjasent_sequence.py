def longestAdjacentSequence(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False] * rows for i in range(cols)]
    stack = []
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    maxSequenceLen = 0

    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                continue
            sequencelen = 0
            stack.append([row, col])
            while stack:
                currentCell = stack.pop()
                currentRow = currentCell[0]
                currentCol = currentCell[1]

                if (visited[currentRow][currentCol]):
                    continue
                current = matrix[currentRow][currentCol]
                visited[currentRow][currentCol] = True
                sequencelen += 1

                for direction in directions:
                    adjacentRow = currentRow + direction[0];
                    adjacentCol = currentCol + direction[1];

                    if adjacentCol < 0 or adjacentCol >= cols or adjacentRow < 0 or adjacentRow >= rows or \
                            visited[adjacentRow][adjacentCol]:
                        continue

                    adjacent = matrix[adjacentRow][adjacentCol]
                    if current == adjacent:
                        stack.append([adjacentRow, adjacentCol])

            maxSequenceLen = max(sequencelen, maxSequenceLen)
        return maxSequenceLen


test1 = [
    [
        'R', 'R', 'B',
    ],
    [
        'G', 'G', 'R',
    ],
    [
        'R', 'B', 'G',
    ]]

test2 = [
    [
        'R', 'R', 'R', 'G',
    ],
    [
        'G', 'B', 'R', 'G',
    ],
    [
        'R', 'G', 'G', 'G',

    ],
    [
        'G', 'G', 'B', 'B'
    ]]

test3 = [
    [
        'R', 'R', 'B', 'B', 'B', 'B',
    ],
    [
        'R', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'B', 'R', 'B', 'G', 'B',
    ],
    [
        'R', 'B', 'R', 'B', 'R', 'B',
    ],
    [
        'R', 'B', 'B', 'B', 'G', 'B',
    ]]
rows = 1000
cols = 1000
test4 = [[0] * cols] * rows

for row in range(rows):
    for col in range(cols):
        test4[row][col] = 'R'

print(longestAdjacentSequence(test1))
print(longestAdjacentSequence(test2))
print(longestAdjacentSequence(test3))
print(longestAdjacentSequence(test4))