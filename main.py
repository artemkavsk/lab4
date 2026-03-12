from itertools import combinations

items = [
    ('r','rifle',    3, 25),
    ('p','pistol',   2, 15),
    ('a','ammo',     2, 15),
    ('m','medkit',   2, 20),
    ('i','inhaler',  1, 5),
    ('k','knife',    1, 15),
    ('x','axe',      3, 20),
    ('t','talisman', 1, 25),
    ('f','flask',    1, 15),
    ('d','antidot',  1, 10),
    ('s','supplies', 2, 20),
    ('c','crossbow', 2, 20)
]

# variant 1
CAP = 8       # 2x4
BASE = 15
need = None   # болезни нет, обязательных предметов нет

print(2 ** len(items))

total_all = sum(it[3] for it in items)

best = ([], float('-inf'))
n = len(items)

for r in range(n + 1):
    for combo in combinations(range(n), r):
        size = sum(items[i][2] for i in combo)
        if size > CAP:
            continue

        # обязательный предмет не нужен для варианта 1
        if need is not None:
            marks = [items[i][0] for i in combo]
            if need not in marks:
                continue

        sum_taken = sum(items[i][3] for i in combo)
        not_taken = total_all - sum_taken
        final = BASE + sum_taken - not_taken

        if final > best[1]:
            best = (list(combo), final)

chosen, final = best

cells = []
for i in chosen:
    cells += [items[i][0]] * items[i][2]

cells += ['.'] * (CAP - len(cells))

rows = [cells[:4], cells[4:8]]

print("chosen items:")
for i in chosen:
    print(items[i])

print()
for row in rows:
    print(' '.join(f'[{x}]' for x in row))

print(f"\nfinal = {final}")