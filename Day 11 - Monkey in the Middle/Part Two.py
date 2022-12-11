from math import lcm
from inputs.input import get_input

inp = get_input(11).read().split("\n\n")

lcm_test = 0

class Monkey:
    def __init__(self, id, items, operation, test, throw_true, throw_false):
        self.id = id
        self.items = items
        self.operation = operation.split(" ")[1]
        self.operation_value = int(operation.split(" ")[2]) if operation.split(" ")[2] != "old" else None
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspections = 0

    def inspect(self):
        new = []
        for item in self.items:
            self.inspections += 1
            r = item
            if self.operation == "+":
                r += self.operation_value or r
            elif self.operation == "*":
                r *= self.operation_value or r
            if r > lcm_test:
                r %= lcm_test
            new.append(r)
        self.items = new

    def test_items(self):
        for item in self.items:
            if (item % self.test == 0):
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
    items = [int(i) for i in monkey[1][18:].split(", ")]
    operation = monkey[2][19:]
    test = int(monkey[3][21:])
    throw_true = int(monkey[4][29:])
    throw_false = int(monkey[5][29:])
    monkeys.append(Monkey(id, items, operation, test, throw_true, throw_false))

lcm_test = lcm(*[i.test for i in monkeys])

for monkey in monkeys:
    monkey.throw_true = monkeys[monkey.throw_true]
    monkey.throw_false = monkeys[monkey.throw_false]

for i in range(10000):
    for monkey in monkeys:
        monkey.turn()

top_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)[:2]

print(top_monkeys[0].inspections * top_monkeys[1].inspections)
