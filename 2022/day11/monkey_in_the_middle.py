class Monkey:
    def __init__(self, troop, starting_items, operation, test_divisor, recipients):
        self.troop = troop
        self.items = starting_items
        self._operation = lambda old: eval(operation)
        self.test_divisor = test_divisor
        self.recipients = recipients
        self.items_inspected = 0

    def turn(self):
        self.items = [int(self._operation(item) / 3) for item in self.items]
        self.items_inspected += (num_items := len(self.items))
        for _ in range(num_items):
            item = self.items.pop(0)
            recipient = self.recipients[item % self.test_divisor == 0]
            self.troop[recipient].items.append(item)
        return self


with open("input.txt", "r") as notes:
    notes = notes.read().split("\n\n")
troop = []
for note in (n.split("\n") for n in notes):
    troop.append(
        Monkey(
            troop=troop,
            starting_items=list(map(int, note[1].split(":")[-1].split(","))),
            operation=note[2].split("=")[-1],
            test_divisor=int(note[3].split(" ")[-1]),
            recipients=(int(note[5].split(" ")[-1]), int(note[4].split(" ")[-1])),
        )
    )
for round_ in range(20):
    for monkey in troop:
        monkey.turn()
item_inspections = sorted([monkey.items_inspected for monkey in troop])
print(item_inspections[-1] * item_inspections[-2])
