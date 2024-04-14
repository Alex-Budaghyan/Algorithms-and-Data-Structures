class Location:
    def __init__(self, loc: dict):
        self.loc = loc

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Length of locations must be equal.")

        loc = {}
        for i in self.loc.keys():
            loc[i] = other.loc[self.loc[i]]

        return Location(loc)

    def reverse(self):
        res = {}
        for i in self.loc.keys():
            res[self.loc[i]] = i
        return Location(res)

    def __len__(self):
        return len(self.loc)

    def __str__(self):
        return f'{[i for i in self.loc.values()]}'


class Group:
    def __init__(self, *args) -> None:
        self.group = list(args)

    def __str__(self):
        s = ''
        for i in self.group:
            s += str(i) + '\n'
        return s


class Table:
    def __init__(self, base):
        self.table = [[None for _ in range(base)] for __ in range(base)]

        e_tmp = {}
        for i in range(1, base + 1):
            e_tmp[i] = i
        e = Location(e_tmp)

        for i in range(base):
            for j in range(i):
                self.table[i][j] = None
            self.table[i][i] = e


def cascade(table: Table, cascades_to_do: list, index: int):
    location = cascades_to_do[index]
    for i in range(1, len(location) + 1):
        if location.loc[i] != i:
            if table.table[i - 1][location.loc[i] - 1] is None:
                table.table[i - 1][location.loc[i] - 1] = location
                cascades_to_do.append(location * location.reverse())
                for loc in cascades_to_do[:]:
                    cascades_to_do.append(loc * location)
                    cascades_to_do.append(location * loc)
                return table
            else:
                location = location * location.reverse()
    return table


def sims_algorithm(group: Group, table: Table):
    cascades_to_do = group.group[:]
    k = 0
    while k < len(cascades_to_do):
        table = cascade(table, cascades_to_do, k)
        k += 1
    for i in range(len(table.table)):
        for j in range(len(table.table[0])):
            if table.table[i][j] is not None:
                print(table.table[i][j], end='\t')
            else:
                print('\tDatark\t', end='\t')
        print()


lc1 = Location({1: 2, 2: 3, 3: 1, 4: 4})
lc2 = Location({1: 2, 2: 4, 3: 3, 4: 1})

group = Group(lc1, lc2)
table = Table(len(lc1))

sims_algorithm(group, table)
print()

lc1 = Location({1: 3, 2: 4, 3: 2, 4: 1})
lc2 = Location({1: 2, 2: 4, 3: 3, 4: 1})

group = Group(lc1, lc2)
table = Table(len(lc1))

sims_algorithm(group, table)
