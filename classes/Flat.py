from classes.Property import Property


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, floor: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Informacje o mieszkaniu:\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia: {self.area} m²\n"
                f"Liczba pokoi: {self.rooms}\n"
                f"Piętro: {self.floor}\n"
                f"Cena: {self.price} zł")
