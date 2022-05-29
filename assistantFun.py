

def get_Zero_pos(puzzele):
    pos = puzzele.index(0)
    return pos


def horizontal_available_moves(pos):
    if (pos%3 ==0):
        return ['>']
    elif (pos%3 ==2):
        return ['<']
    else:
        return ['<', '>']

def vertical_available_moves(pos):
    if pos <3:
        return ['v']
    elif pos <6:
        return ['v', '^']
    else:
        return ['^']

def possible_moves(puzzele):
    pos = get_Zero_pos(puzzele)
    vertical = vertical_available_moves(pos)
    horizontal = horizontal_available_moves(pos)
    return vertical + horizontal

    

def aplly_move(puzzele, move):
    pos = get_Zero_pos(puzzele)
    if move == '^':
        puzzele[pos-3], puzzele[pos] = puzzele[pos], puzzele[pos-3]
    elif move == 'v':
        puzzele[pos+3], puzzele[pos] = puzzele[pos], puzzele[pos+3]
    elif move == '>':
        puzzele[pos+1], puzzele[pos] = puzzele[pos], puzzele[pos+1]
    elif move == '<':
        puzzele[pos-1], puzzele[pos] = puzzele[pos], puzzele[pos-1]
    return puzzele


def check_for_winning(puzzele):
    return puzzele == [0, 1, 2, 3, 4, 5, 6, 7, 8]
