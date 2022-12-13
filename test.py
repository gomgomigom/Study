class A:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def say_name(self):
        print(self._name)

    def say_age(self):
        print(self._age)


class B(A):
    def __init__(self, name, age, test):
        super().__init__(name, age)
        self._test = test

    def say_test(self):
        print(self._test)


class C:
    def __init__(self, name, age):
        self.A = A(name, age)

    def cal_add(self):
        return self.A._age


test1 = A("test1", 2)
test1.say_name()

test2 = B("2", 3, "TTTTTTEST")
test2.say_name()
test2.say_test()

test3 = C("na", 213)
print(test3.cal_add())
