from itertools import combinations

items = [
    ('r','rifle', 3, 25),
    ('p','pistol',2,15),
    ('a','ammo',  2,15),
    ('m','medkit',2,20),
    ('i','inhaler',1,5),
    ('k','knife',1,15),
    ('x','axe',3,20),
    ('t','talisman',1,25),
    ('f','flask',1,15),
    ('d','antidot',1,10),
    ('s','supplies',2,20),
    ('c','crossbow',2,20)
]

CAP = 8
BASE = 15

total_all = sum(it[3] for it in items)

best = ([], float('inf'))
n = len(items)

for r in range(n + 1):
    for combo in combinations(range(n), r):

        size = sum(items[i][2] for i in combo)
        if size > CAP:
            continue

        sum_taken = sum(items[i][3] for i in combo)
        not_taken = total_all - sum_taken

        diff = abs(sum_taken - not_taken)

        if diff < best[1]:
            best = (list(combo), diff)

chosen, _ = best

sum_taken = sum(items[i][3] for i in chosen)
not_taken = total_all - sum_taken

final = BASE

cells = []
for i in chosen:
    cells += [items[i][0]] * items[i][2]

cells += ['.'] * (CAP - len(cells))

rows = [cells[:4], cells[4:8]]

for r in rows:
    print(' '.join(f'[{x}]' for x in r))

print(f"Итоговые очки выживания:{final}")