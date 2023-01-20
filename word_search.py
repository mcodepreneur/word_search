def load_lists():
    '''Instate global variables and read 
    wordlist and letter grid into them'''
    global word_list
    global grid
    global found_words
    found_words = set()
    word_list = []
    for x in open(input(), 'r').readlines():
        word_list.append(x.strip().lower())
    grid = []
    for x in open(input(), 'r').readlines():
        grid.append(x.split())

def scan_grid():
    '''Passes rows columns and diagonals as 
    strings into string parsers'''
    for x in grid:
        double_str_parse(''.join(x))
    for i in range(len(grid)):
        column = []
        for x in grid:
            column.append(x[i])
        double_str_parse(''.join(column))
    for i in range(-(len(grid)-3), len(grid)-2):
        line = []
        x = int(i < 0) * -i
        y = int(i > 0) * i
        k = len(grid) - abs(i)
        for j in range(k):
            line.append(grid[x][y])
            x += 1; y += 1
        str_parse(''.join(line))

def str_parse(string):
    '''Parses string into all possible substrings
    length >= 3 and checks against word_list, 
    adding matches to list found_words'''
    for i in range(len(string)-2):
        cut = string[i:]
        for j in range(len(cut), 2, -1):
            spec = cut[:j]
            if spec in word_list:
                found_words.add(spec)
    
def double_str_parse(string):
    '''Passes both the parameter string and the
    reversed string to str_parse'''
    str_parse(string)
    str_parse(string[::-1])

def occurs_in(substr, word_list):
    '''Not useful as forcing lowercase was
    intergrated into word_list loading step'''
    pass

def main():
    load_lists()
    scan_grid()
    print('\n'.join(sorted(found_words)))

main()
