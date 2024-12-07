def check_ms_up(r,c):
    if(r < 1 or c < 1):
        return False
    try:
        return m[r-1][c-1] == 'M' and m[r-1][c+1] == 'M' and m[r+1][c+1] == 'S' and m[r+1][c-1] == 'S'
    except IndexError:
        return False

def check_ms_right(r,c):
    if(r < 1 or c < 1):
        return False
    try:
        return m[r-1][c-1] == 'S' and m[r-1][c+1] == 'M' and m[r+1][c+1] == 'M' and m[r+1][c-1] == 'S'
    except IndexError:
        return False

def check_ms_down(r,c):
    if(r < 1 or c < 1):
        return False
    try:
        return m[r-1][c-1] == 'S' and m[r-1][c+1] == 'S' and m[r+1][c+1] == 'M' and m[r+1][c-1] == 'M'
    except IndexError:
        return False

def check_ms_left(r,c):
    if(r < 1 or c < 1):
        return False
    try:
        return m[r-1][c-1] == 'M' and m[r-1][c+1] == 'S' and m[r+1][c+1] == 'S' and m[r+1][c-1] == 'M'
    except IndexError:
        return False

# Open File
with open('input.txt', 'r') as input_file:
    # Get Input by line
    m = []
    for line in input_file.readlines():
        m.append(line)

R = len(m)
C = len(m[0])


total_count = 0
for r in range(R):
    for c in range(C-1):
        if m[r][c] != 'A':
            continue
        if check_ms_up(r,c):
            print(f'Up found: {r},{c}')
            total_count += 1
        if check_ms_down(r,c):
            print(f'Down found: {r},{c}')
            total_count += 1
        if check_ms_left(r,c):
            print(f'Left found: {r},{c}')
            total_count += 1
        if check_ms_right(r,c):
            print(f'Right found: {r},{c}')
            total_count += 1

print(total_count)
