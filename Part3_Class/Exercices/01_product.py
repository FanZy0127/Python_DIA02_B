"""
Ci dessous on a un exemple de getter/setter définit avec des décorateurs

"""


class Product:

    def __init__(self, name: str, price: float, tva: float = .2):
        self._price = price
        self._tva = tva
        self._name = name

    @property
    def price(self) -> float:
        return (self.tva + 1) * self._price

    @price.setter
    def set_price(self, price: float):
        self._price = price

    @property
    def tva(self) -> float:
        return self._tva

    @tva.setter
    def set_tva(self, tva: float):
        self._tva = tva

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def set_name(self, name: str):
        self._name = name


apple = Product("pomme",  1.2)
orange = Product("orange", 1.1)
print(f'Une {apple.name} coûte {apple.price}€.')
print(f'Une {orange.name} coûte {orange.price}€.')

products_sum = apple.price + orange.price
print(f'Le coût total pour une {apple.name} et une {orange.name} est de {products_sum}€.')