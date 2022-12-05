class Smartphone:
    def __init__(self, brand, details):
        self._brand = brand
        self._infomations = details

    def __str__(self):
        return f"str : {self._brand} - {self._infomations}"

    def __repr__(self):
        return f"repr : {self._brand} - {self._infomations}"

    def get_infomation(self):
        print(f"Current Id : {id(self)}")
        print(
            f'Smartphone Detail Info : {self._brand} {self._infomations.get("price")}'
        )

        Smartphone1 = Smartphone("Iphone", {"color": "White", "price": 10000})
        Smartphone2 = Smartphone("Galaxy", {"color": "Black", "price": 8000})

        Smartphone1.detail_info()

        print(Smartphone1.__class__, Smartphone2.__class__)
        # 부모는 같음
        print(id(Smartphone1.__class__) == id(Smartphone2.__class__))


Smartphone1 = Smartphone("Iphone", {"color": "White", "infomations": 121})
print(Smartphone1)
print(Smartphone1.__dict__)
