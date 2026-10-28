class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Informacje o domu:\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia: {self.area} m²\n"
                f"Liczba pokoi: {self.rooms}\n"
                f"Rozmiar działki: {self.plot} m²\n"
                f"Cena: {self.price} zł")


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, floor: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Informacje o mieszkaniu:\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia: {self.area} m²\n"
                f"Liczba pokoi: {self.rooms}\n"
                f"Piętro: {self.floor}\n"
                f"Cena: {self.price} zł")

h1 = House(250, 5, 25000000, "Katowice, ul. Orzechowa 67", 250)
f1 = Flat(80, 4, 750000, "Czeladź, ul. Miła 8", "parter")

print(h1)
print(f1)