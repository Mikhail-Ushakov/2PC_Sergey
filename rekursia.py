class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def sleep(self):
        print(f'{self.name} is sleepping')

fluffy = Cat('Snowball', 'white')
print(fluffy.name)
print(fluffy.colour)

fluffy.rer = 'good'
print(fluffy.rer)
print(dir(fluffy))

Cat.sleep(fluffy)
fluffy.sleep(12)