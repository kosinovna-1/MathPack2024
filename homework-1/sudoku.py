import pathlib
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    Sud = [values[n*i:n*(i+1)] for i in range(n)]
    return Sud


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""

    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""

    return [grid[i][pos[1]] for i in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    
    m,n = pos
    s = []
    kv = [[m//3*3,m//3*3+3],[n//3*3,n//3*3+3]]
    for i in range(kv[0][0],kv[0][1]):
        s += grid[i][kv[1][0]:kv[1][1]]
    return s


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""

    n = len(grid)
    for k in range(n):
        for t in range(n):
            if grid[k][t] == '.':
                return (k,t)
    return (-1,-1)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции"""

    n = len(grid)
    digits = set([str(i+1) for i in range(n)])
    a = get_row(grid,pos)
    b = get_col(grid,pos)
    c = get_block(grid,pos)
    unpos = set(a+b+c)
    return digits-unpos


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """

    pos = find_empty_positions(grid)
    if pos == (-1,-1):
        return grid
    possible = find_possible_values(grid,pos)
    if len(possible) == 0:
        return False
    for c in possible:
        st = grid[pos[0]][:pos[1]]+[c]+grid[pos[0]][pos[1]+1:]
        g = grid[:pos[0]]+ [st] +grid[pos[0]+1:]
        ans = solve(g)
        if ans:
            return ans
    return False


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """

    if not solution: return False
    n = len(solution)
    b = []
    for i in range(3):
        for j in range(3):
            b.append((3*i,3*j))
    for i in range(n):
        if len(set(get_row(solution,(i,0)))-{'.'}) != n: return False
        if len(set(get_col(solution,(0,i)))-{'.'}) != n: return False
        if len(set(get_block(solution,b[i]))-{'.'}) != n: return False
    return True
            


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""

    from random import randint as rand
    n = 9
    if N > n**2: N = n**2
    N = n**2-N
    koordinates = []
    for i in range(n):
        for j in range(n):
            koordinates.append((i,j))
    grid = new_sudoku()
    while N > 0:
        t = rand(0,len(koordinates)-1)
        i,j = koordinates[t]
        grid[i][j] = '.'
        koordinates.pop(t)
        N -= 1
    return grid

def new_sudoku():
    """Генерация заполненного поля судоку"""

    n = 9
    koordinates = [[(i,j) for j in range(3)] for i in range(3)]
    Sud = [["." for j in range(n)] for i in range(n)]
    for k in range(3):
        d = random_perest()
        for i in range(3):
            for j in range(3):
                Sud[i+3*k][j+3*k] = d[3*i+j]
    Sud = solve(Sud)
    if check_solution(Sud): return Sud
    new_sudoku()

def random_perest():
    """Функция перестановки 9-ти цифр в случайном порядке"""

    from random import randint as rand
    n = 9
    digits = [c for c in "123456789"]
    d = []
    for i in range(n):
        t = rand(0,len(digits)-1)
        d.append(digits[t])
        digits.pop(t)
    return d
    

if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
