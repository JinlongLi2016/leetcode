n, m = [int(i) for i in input().strip().split(' ')]
i = 0 
p = []
while i < n:
    line = input().strip().split(' ')
    p.append([int(people) for people in line])
    i += 1

start_row, end_row = 0, n
start_col, end_col = 0, m
while start_row < end_row and start_col < end_col:
    # down
    if start_col < end_col:
        for i in range(start_row, end_row):
            print(p[i][start_col], end = ' ')
        start_col +=1
    #  ->
    if start_row < end_row and start_col < end_col:
        for i in range(start_col, end_col):
            print(p[end_row-1][i], end = ' ')
        end_row -= 1
    # up
    if start_row < end_row and start_col < end_col:
        for i in range(end_row-1, start_row-1, -1):
            print(p[i][end_col-1], end = ' ')
        end_col -= 1
    # right
    if start_row < end_row and start_col < end_col:
        for i in range(end_col-1, start_col-1, -1):
            print(p[start_row][i], end = ' ')
        start_row += 1
