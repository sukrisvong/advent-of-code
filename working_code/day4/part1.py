
def check_up(r,c):
    if(r < 3):
        return False
    try:
        return m[r-1][c] == 'M' and m[r-2][c] == 'A' and m[r-3][c] == 'S'
    except IndexError:
        return False

def check_down(r,c):
    try:
        return m[r+1][c] == 'M' and m[r+2][c] == 'A' and m[r+3][c] == 'S'
    except IndexError:
        return False

def check_left(r,c):
    if(c < 3):
        return False
    try:
        return m[r][c-1] == 'M' and m[r][c-2] == 'A' and m[r][c-3] == 'S'
    except IndexError:
        return False

def check_right(r,c):
    try:
        return m[r][c+1] == 'M' and m[r][c+2] == 'A' and m[r][c+3] == 'S'
    except IndexError:
        return False

def check_up_left(r,c):
    if(r < 3 or c < 3):
        return False
    try:
        return m[r-1][c-1] == 'M' and m[r-2][c-2] == 'A' and m[r-3][c-3] == 'S'
    except IndexError:
        return False

def check_down_right(r,c):
    try:
        return m[r+1][c+1] == 'M' and m[r+2][c+2] == 'A' and m[r+3][c+3] == 'S'
    except IndexError:
        return False

def check_up_right(r,c):
    if(r < 3):
        return False
    try:
        return m[r-1][c+1] == 'M' and m[r-2][c+2] == 'A' and m[r-3][c+3] == 'S'
    except IndexError:
        return False

def check_down_left(r,c):
    if(c < 3):
        return False
    try:
        return m[r+1][c-1] == 'M' and m[r+2][c-2] == 'A' and m[r+3][c-3] == 'S'
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
        if m[r][c] != 'X':
            continue
        if check_up(r,c):
            print(f'Up found: {r},{c}')
            total_count += 1
        if check_down(r,c):
            print(f'Down found: {r},{c}')
            total_count += 1
        if check_left(r,c):
            print(f'Left found: {r},{c}')
            total_count += 1
        if check_right(r,c):
            print(f'Right found: {r},{c}')
            total_count += 1
        if check_up_left(r,c):
            total_count += 1
            print(f'UpLeft found: {r},{c}')
        if check_down_right(r,c):
            total_count += 1
            print(f'DownRight found: {r},{c}')
        if check_up_right(r,c):
            total_count += 1
            print(f'UpRight found: {r},{c}')
        if check_down_left(r,c):
            print(f'DownLeft found: {r},{c}')
            total_count += 1

for line in m:
    print(line)
print(total_count)
