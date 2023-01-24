import sys

a = []
f = open(sys.argv[1], "r")
for x in f.readlines():
    a.append(x.strip("\n"))
White = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'ki', 'qu', 'r1', 'r2', 'b1', 'b2', 'n1', 'n2']
wpawns = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']
wknights = ['n1', 'n2']
wrooks = ['r1', 'r2']
wbishops = ['b1', 'b2']
Black = []
for i in White:
    Black.append(i.upper())
bpawns = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
bknights = ["N1", "N2"]
bbishops = ["B1", "B2"]
brooks = ["R1", "R2"]
tablo = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", ],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", ],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", ],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", ],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", ],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", ],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", ],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", ]
]
board = [
    ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", ],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", ],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2", ]
]
initial_board = [
    ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", ],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", ],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2", ]
]


def get_destination_index(dest):
    row = -1
    column = -1
    for k in tablo:
        row = row + 1
        for j in k:
            column = column + 1
            if (j.__eq__(dest)):
                return (str(row) + "," + str(column - (row * (len(tablo[0])))))


def get_index(piece):
    row = -1
    column = -1
    for k in board:
        row = row + 1
        for j in k:
            column = column + 1
            if (j.__eq__(piece)):
                return (str(row) + "," + str(column - (row * (len(board[0])))))


def notation(divv):
    for i in tablo:
        for j in i:
            return tablo[divv[0]][divv[1]]


def wis_valid(x):
    if x == '  ' or x in Black and x != 'KI':
        return True


def bis_valid(x):
    if x == '  ' or x in White and x != 'ki':
        return True


def wpawns_moves(piece):
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if board[r - 1][c] != ('KI'):
        if (board[r - 1][c].__eq__('  ') or board[r - 1][c] in Black):
            x = [r - 1, c]

            return (notation(x))
        else:
            return ('FAILED')

    else:
        return ("FAILED")


def bpawns_moves(piece):
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if board[r + 1][c] != ('ki'):

        if (board[r + 1][c].__eq__('  ') or board[r + 1][c] in White):
            x = [r + 1, c]
            print(notation(x))
        else:
            print('FAILED')
    else:
        print("FAILED")


def wknight_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])

    if r >= len(board) - 2 or c == len(board[0]) - 1:
        pass
    else:
        if wis_valid(board[r + 2][c + 1]):
            x = [r + 2, c + 1]
            valid_moves.append(notation(x))
    if r >= len(board) - 2 or c == 0:
        pass
    else:
        if wis_valid(board[r + 2][c - 1]):
            x = [r + 2, c - 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == len(board[0]) - 1:
        pass
    else:
        if wis_valid(board[r - 2][c + 1]):
            x = [r - 2, c + 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == 0:
        pass
    else:
        if wis_valid(board[r - 2][c - 1]):
            x = [r - 2, c - 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c >= len(board[0]) - 2:
        pass
    else:
        if wis_valid(board[r + 1][c + 2]):
            x = [r + 1, c + 2]
            valid_moves.append(notation(x))
    if r == 0 or c >= len(board[0]) - 2:
        pass
    else:
        if wis_valid(board[r - 1][c + 2]):
            x = [r - 1, c + 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c <= 2:
        pass
    else:
        if wis_valid(board[r + 1][c - 2]):
            x = [r + 1, c - 2]
            valid_moves.append(notation(x))
    if r == 0 or c <= 2:
        pass
    else:
        if wis_valid(board[r - 1][c - 2]):
            x = [r - 1, c - 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r + 1][c + 1]) == '  ':
            x = [r + 1, c + 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == 0:
        pass
    else:
        if (board[r + 1][c - 1]) == '  ':
            x = [r + 1, c - 1]
            valid_moves.append(notation(x))
    if r == 0 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r - 1][c + 1]) == '  ':
            x = [r - 1, c + 1]
            valid_moves.append(notation(x))
    if r == 0 or c == 0:
        pass
    else:
        if (board[r - 1][c - 1]) == '  ':
            x = [r - 1, c - 1]
            valid_moves.append(notation(x))
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def bknight_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])

    if r >= len(board) - 2 or c == len(board[0]) - 1:
        pass
    else:
        if bis_valid(board[r + 2][c + 1]):
            x = [r + 2, c + 1]
            valid_moves.append(notation(x))
    if r >= len(board) - 2 or c == 0:
        pass
    else:
        if bis_valid(board[r + 2][c - 1]):
            x = [r + 2, c - 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == len(board[0]) - 1:
        pass
    else:
        if bis_valid(board[r - 2][c + 1]):
            x = [r - 2, c + 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == 0:
        pass
    else:
        if bis_valid(board[r - 2][c - 1]):
            x = [r - 2, c - 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c >= len(board[0]) - 2:
        pass
    else:
        if bis_valid(board[r + 1][c + 2]):
            x = [r + 1, c + 2]
            valid_moves.append(notation(x))
    if r == 0 or c >= len(board[0]) - 2:
        pass
    else:
        if bis_valid(board[r - 1][c + 2]):
            x = [r - 1, c + 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c <= 2:
        pass
    else:
        if bis_valid(board[r + 1][c - 2]):
            x = [r + 1, c - 2]
            valid_moves.append(notation(x))
    if r == 0 or c <= 2:
        pass
    else:
        if bis_valid(board[r - 1][c - 2]):
            x = [r - 1, c - 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r + 1][c + 1]) == '  ':
            x = [r + 1, c + 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == 0:
        pass
    else:
        if (board[r + 1][c - 1]) == '  ':
            x = [r + 1, c - 1]
            valid_moves.append(notation(x))
    if r == 0 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r - 1][c + 1]) == '  ':
            x = [r - 1, c + 1]
            valid_moves.append(notation(x))
    if r == 0 or c == 0:
        pass
    else:
        if (board[r - 1][c - 1]) == '  ':
            x = [r - 1, c - 1]
            valid_moves.append(notation(x))
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def wbishop_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in Black:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in Black:
            break
        r = r - 1
        c = c - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def bbishop_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in White:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in White:
            break
        r = r + 1
        c = c - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def wrook_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in Black:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in Black:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in Black:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in Black:
            break
        r = r - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def brook_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in White:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in White:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in White:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in White:
            break
        r = r - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def wqueen_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in Black:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in Black:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in Black:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in Black:
            break
        r = r - 1
    r = int(divv[0])
    c = int(divv[1])

    while r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in Black:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != len(board[0]) - 1 and wis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in Black:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and wis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in Black:
            break
        r = r + 1
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in Black:
            break
        r = r - 1
        c = c - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def bqueen_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    while c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in White:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in White:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in White:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in White:
            break
        r = r - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != len(board[0]) - 1 and bis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in White:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in White:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in White:
            break
        r = r + 1
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and bis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in White:
            break
        r = r - 1
        c = c - 1
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def wking_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != len(board[0]) - 1 and wis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != 0 and wis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))

    if r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
    if c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
    if c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
    if r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()


def bking_moves(piece):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if r != 0 and c != len(board[0]) - 1 and bis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
    if r != 0 and c != 0 and bis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
    if c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
    if c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
    if r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
    if not valid_moves:
        print("FAILED")
    else:
        for c in sorted(valid_moves):
            print(c, end=' ')
        print()
    # ----------------------- SHOWMOVES ENDED NOW CODES FOR MOVING THE PIECES ARE BELOW----------------------------------------------


def wpawn_goes(piece, destination):
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if board[r - 1][c] != ('KI'):
        if (board[r - 1][c].__eq__('  ') or board[r - 1][c] in Black):
            x = [r - 1, c]
            y = notation(x)
    if destination == y:
        print("OK")
        board[r][c], board[r - 1][c] = '  ', board[r][c]
    else:
        print("FAILED")


def bpawn_goes(piece, destination):
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    if board[r - 1][c] != ('ki'):
        if (board[r + 1][c].__eq__('  ') or board[r + 1][c] in White):
            x = [r + 1, c]
            y = notation(x)
    if destination == y:
        print("OK")
        board[r][c], board[r + 1][c] = '  ', board[r][c]
    else:
        print("FAILED")


def wknight_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    if r >= len(board) - 2 or c == len(board[0]) - 1:
        pass
    else:
        if wis_valid(board[r + 2][c + 1]):
            x = [r + 2, c + 1]
            valid_moves.append(notation(x))
    if r >= len(board) - 2 or c == 0:
        pass
    else:
        if wis_valid(board[r + 2][c - 1]):
            x = [r + 2, c - 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == len(board[0]) - 1:
        pass
    else:
        if wis_valid(board[r - 2][c + 1]):
            x = [r - 2, c + 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == 0:
        pass
    else:
        if wis_valid(board[r - 2][c - 1]):
            x = [r - 2, c - 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c >= len(board[0]) - 2:
        pass
    else:
        if wis_valid(board[r + 1][c + 2]):
            x = [r + 1, c + 2]
            valid_moves.append(notation(x))
    if r == 0 or c >= len(board[0]) - 2:
        pass
    else:
        if wis_valid(board[r - 1][c + 2]):
            x = [r - 1, c + 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c <= 2:
        pass
    else:
        if wis_valid(board[r + 1][c - 2]):
            x = [r + 1, c - 2]
            valid_moves.append(notation(x))
    if r == 0 or c <= 2:
        pass
    else:
        if wis_valid(board[r - 1][c - 2]):
            x = [r - 1, c - 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r + 1][c + 1]) == '  ':
            x = [r + 1, c + 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == 0:
        pass
    else:
        if (board[r + 1][c - 1]) == '  ':
            x = [r + 1, c - 1]
            valid_moves.append(notation(x))
    if r == 0 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r - 1][c + 1]) == '  ':
            x = [r - 1, c + 1]
            valid_moves.append(notation(x))
    if r == 0 or c == 0:
        pass
    else:
        if (board[r - 1][c - 1]) == '  ':
            x = [r - 1, c - 1]
            valid_moves.append(notation(x))
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def bknight_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    if r >= len(board) - 2 or c == len(board[0]) - 1:
        pass
    else:
        if bis_valid(board[r + 2][c + 1]):
            x = [r + 2, c + 1]
            valid_moves.append(notation(x))
    if r >= len(board) - 2 or c == 0:
        pass
    else:
        if bis_valid(board[r + 2][c - 1]):
            x = [r + 2, c - 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == len(board[0]) - 1:
        pass
    else:
        if bis_valid(board[r - 2][c + 1]):
            x = [r - 2, c + 1]
            valid_moves.append(notation(x))
    if r <= 1 or c == 0:
        pass
    else:
        if bis_valid(board[r - 2][c - 1]):
            x = [r - 2, c - 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c >= len(board[0]) - 2:
        pass
    else:
        if bis_valid(board[r + 1][c + 2]):
            x = [r + 1, c + 2]
            valid_moves.append(notation(x))
    if r == 0 or c >= len(board[0]) - 2:
        pass
    else:
        if bis_valid(board[r - 1][c + 2]):
            x = [r - 1, c + 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c <= 2:
        pass
    else:
        if bis_valid(board[r + 1][c - 2]):
            x = [r + 1, c - 2]
            valid_moves.append(notation(x))
    if r == 0 or c <= 2:
        pass
    else:
        if bis_valid(board[r - 1][c - 2]):
            x = [r - 1, c - 2]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r + 1][c + 1]) == '  ':
            x = [r + 1, c + 1]
            valid_moves.append(notation(x))
    if r == len(board) - 1 or c == 0:
        pass
    else:
        if (board[r + 1][c - 1]) == '  ':
            x = [r + 1, c - 1]
            valid_moves.append(notation(x))
    if r == 0 or c == len(board[0]) - 1:
        pass
    else:
        if (board[r - 1][c + 1]) == '  ':
            x = [r - 1, c + 1]
            valid_moves.append(notation(x))
    if r == 0 or c == 0:
        pass
    else:
        if (board[r - 1][c - 1]) == '  ':
            x = [r - 1, c - 1]
            valid_moves.append(notation(x))
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def wbishop_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in Black:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in Black:
            break
        r = r - 1
        c = c - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def bbishop_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in White:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in White:
            break
        r = r + 1
        c = c - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def wrook_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in Black:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in Black:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in Black:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in Black:
            break
        r = r - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def brook_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in White:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in White:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in White:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in White:
            break
        r = r - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def wqueen_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in Black:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in Black:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in Black:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in Black:
            break
        r = r - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in Black:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != len(board[0]) - 1 and wis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in Black:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and wis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in Black:
            break
        r = r + 1
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in Black:
            break
        r = r - 1
        c = c - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def bqueen_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    while c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
        if board[r][c + 1] in White:
            break
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
        if board[r + 1][c] in White:
            break
        r = r + 1
    r = int(divv[0])
    c = int(divv[1])
    while c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
        if board[r][c - 1] in White:
            break
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
        if board[r - 1][c] in White:
            break
        r = r - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != len(board[0]) - 1 and bis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
        if board[r - 1][c + 1] in White:
            break
        r = r - 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
        if board[r + 1][c + 1] in White:
            break
        r = r + 1
        c = c + 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))
        if board[r + 1][c - 1] in White:
            break
        r = r + 1
        c = c - 1
    r = int(divv[0])
    c = int(divv[1])
    while r != 0 and c != 0 and bis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
        if board[r - 1][c - 1] in White:
            break
        r = r - 1
        c = c - 1
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def wking_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    if r != 0 and c != len(board[0]) - 1 and wis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != len(board[0]) - 1 and wis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != 0 and wis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))

    if r != 0 and c != 0 and wis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
    if c != len(board[0]) - 1 and wis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and wis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
    if c != 0 and wis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
    if r != 0 and wis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


def bking_goes(piece, destination):
    valid_moves = []
    divv = get_index(piece).split(",")
    r = int(divv[0])
    c = int(divv[1])
    divv_des = get_destination_index(destination).split(",")
    z = int(divv_des[0])
    t = int(divv_des[1])
    if r != 0 and c != len(board[0]) - 1 and bis_valid(board[r - 1][c + 1]):
        x = [r - 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != len(board[0]) - 1 and bis_valid(board[r + 1][c + 1]):
        x = [r + 1, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and c != 0 and bis_valid(board[r + 1][c - 1]):
        x = [r + 1, c - 1]
        valid_moves.append(notation(x))

    if r != 0 and c != 0 and bis_valid(board[r - 1][c - 1]):
        x = [r - 1, c - 1]
        valid_moves.append(notation(x))
    if c != len(board[0]) - 1 and bis_valid(board[r][c + 1]):
        x = [r, c + 1]
        valid_moves.append(notation(x))
    if r != 7 and bis_valid(board[r + 1][c]):
        x = [r + 1, c]
        valid_moves.append(notation(x))
    if c != 0 and bis_valid(board[r][c - 1]):
        x = [r, c - 1]
        valid_moves.append(notation(x))
    if r != 0 and bis_valid(board[r - 1][c]):
        x = [r - 1, c]
        valid_moves.append(notation(x))
    if destination in valid_moves:
        print("OK")
        board[r][c], board[z][t] = '  ', board[r][c]
    else:
        print("FAILED")


for i in a:
    if 'showmoves' in i:
        print('> ' + i)
        liste = i.split(' ')
        if liste[1] in White:

            if liste[1] in wpawns:
                piece = liste[1]
                print(piece)
                wpawns_moves(piece)
            if liste[1] in wknights:
                wknight_moves(liste[1])

            if liste[1] in wbishops:
                wbishop_moves(liste[1])
            if liste[1] in wrooks:
                wrook_moves(liste[1])
            if liste[1] == "qu":
                wqueen_moves(liste[1])
            if liste[1] == "ki":
                wking_moves(liste[1])

        if liste[1] in Black:
            if liste[1] in bpawns:
                bpawns_moves(liste[1])
            if liste[1] in bknights:
                bknight_moves(liste[1])

            if liste[1] in bbishops:
                bbishop_moves(liste[1])
            if liste[1] in brooks:
                brook_moves(liste[1])
            if liste[1] == "QU":
                bqueen_moves(liste[1])
            if liste[1] == "KI":
                bking_moves(liste[1])

    if 'move ' in i:
        print('> ' + i)
        liste = i.split(' ')
        if liste[1] in White:
            if liste[1] in wpawns:
                wpawn_goes(liste[1], liste[2])
            if liste[1] in wknights:
                wknight_goes(liste[1], liste[2])
            if liste[1] in wbishops:
                wbishop_goes(liste[1], liste[2])
            if liste[1] in wrooks:
                wrook_goes(liste[1], liste[2])
            if liste[1] == 'qu':
                wqueen_goes(liste[1], liste[2])
            if liste[1] == 'ki':
                wking_goes(liste[1], liste[2])
        if liste[1] in Black:
            if liste[1] in bpawns:
                bpawn_goes(liste[1], liste[2])
            if liste[1] in bknights:
                bknight_goes(liste[1], liste[2])
            if liste[1] in bbishops:
                bbishop_goes(liste[1], liste[2])
            if liste[1] in brooks:
                brook_goes(liste[1], liste[2])
            if liste[1] == 'QU':
                bqueen_goes(liste[1], liste[2])
            if liste[1] == 'KI':
                bking_goes(liste[1], liste[2])
    if 'print' in i:
        print('> ' + i)
        print("--------------------------")
        for r in board:
            for c in r:
                print(c, end=" ")
            print()
        print("--------------------------")
    if 'exit' in i:
        print('> ' + i)
        break
    if 'initialize' in i:
        print('> ' + i)
        print("OK")
        board = initial_board
        print("--------------------------")
        for r in board:
            for c in r:
                print(c, end=" ")
            print()
        print("--------------------------")
f.close()
