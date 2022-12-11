from math import floor

from inputs.input import get_input

inp = get_input(11).read().split("\n\n")

class Monkey:
    def __init__(self, id, items, operation, test, throw_true, throw_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspections = 0

    def inspect(self):
        new = []
        for item in self.items:
            self.inspections += 1
            new.append(str(
                floor(eval(
                    self.operation.replace("old", item)
                    )/3)
                ))
        self.items = new

    def test_items(self):
        for item in self.items:
            if (int(item) % self.test == 0):
                # True
                self.throw_true.items.append(item)
            else:
                # False
                self.throw_false.items.append(item)
        self.items = []

    def turn(self):
        self.inspect()
        self.test_items()


monkeys = []

for monkey in inp:
    monkey = monkey.split("\n")
    id = monkey[0][:-1].split(" ")[1]
    items = monkey[1][18:].split(", ")
    operation = monkey[2][19:]
    test = int(monkey[3][21:])
    throw_true = int(monkey[4][29:])
    throw_false = int(monkey[5][29:])
    monkeys.append(Monkey(id, items, operation, test, throw_true, throw_false))

for monkey in monkeys:
    monkey.throw_true = monkeys[monkey.throw_true]
    monkey.throw_false = monkeys[monkey.throw_false]

for _ in range(20):
    for monkey in monkeys:
        monkey.turn()

top_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)[:2]

print(top_monkeys[0].inspections * top_monkeys[1].inspections)
