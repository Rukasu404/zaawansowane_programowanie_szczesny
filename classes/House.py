import classes.Property


class House(classes.Property.Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Informacje o domu:\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia: {self.area} m²\n"
                f"Liczba pokoi: {self.rooms}\n"
                f"Rozmiar działki: {self.plot} m²\n"
                f"Cena: {self.price} zł")
