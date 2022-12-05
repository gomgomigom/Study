class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hello(self):
        print(self.name, "hello")

    @classmethod
    def confirm(haha):
        print(haha.population)


he = Robot("he")

he.say_hello()


print(Robot.population)

he.confirm()
