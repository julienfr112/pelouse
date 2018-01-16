'''
remarque: dans le texte, il semble que les coordonnée commence à zero, la troisième machine est donc en dehos d'un carré de coté 5
j'ai aggrandi le carré pour que ça rentre.
'''


data = '''6 6
1 2 N
LFLFLFLFF
3 3 E
FRFFRFRRF
5 2 S
FLFLFFRFLF'''.split('\n')

size = [int(d) for d in data[0].split()]
field = [[None for x in range(size[0])] for y in range(size[1])]
# print(field)

machines = [
    (data[i * 2 + 1], data[i * 2 + 2])
    for i in range(0, len(data) // 2)
]
# print(machines)

pos = [None for _ in machines]
for i, (ini, _) in enumerate(machines):
    x, y, p = ini.split()
    x, y = int(x), int(y)
    pos[i] = [x, y, p]
    assert field[x][y] is None
    field[x][y] = i

turnright = {'N': 'O', 'O': 'S', 'S': 'E', 'E': 'N'}
turnleft = {v: k for k, v in turnright.items()}
nicedirection = {'N': '^', 'O': '<', 'S': 'v', 'E': '>'}

progs = [prog for pos, prog in machines]
while any(progs):
    for l in reversed(list(zip(*field))):  # on réorganise les lignes pour que zero soit en bas à droite
        print(' '.join('#' if i is None else nicedirection[pos[i][2]] for i in l))
    print()
    for i, p in enumerate(list(progs)):
        if p:
            action = p[0]
            print(action, pos[i])
            if action == 'F':
                oldpos = pos[i].copy()
                if pos[i][2] == 'N':
                    pos[i][1] += 1
                elif pos[i][2] == 'E':
                    pos[i][0] += 1
                elif pos[i][2] == 'S':
                    pos[i][1] -= 1
                elif pos[i][2] == 'W':
                    pos[i][0] -= 1
                if -1 < pos[i][0] < size[0] and -1 < pos[i][1] < size[1] and field[pos[i][0]][pos[i][1]] is None:
                    field[oldpos[0]][oldpos[1]] = None
                    field[pos[i][0]][pos[i][1]] = i
                else:
                    pos[i] = oldpos

            elif action == 'R':
                pos[i][2] = turnright[pos[i][2]]
            elif action == 'L':
                pos[i][2] = turnleft[pos[i][2]]
        progs[i] = p[1:]
