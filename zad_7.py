import requests

basic_url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"


class Brewery:
    def __init__(
            self,
            id: str,
            name: str,
            brewery_type: str,
            address_1: str | None,
            address_2: str | None,
            address_3: str | None,
            city: str,
            state_province: str,
            postal_code: str,
            country: str,
            longitude: float | None,
            latitude: float | None,
            phone: str | None,
            website_url: str | None,
            state: str,
            street: str | None,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (f"Nazwa piwska: {self.name}\n"
                f"Typ piwska: {self.brewery_type}\n"
                f"ID: {self.id}\n"
                f"Adres 1: {self.address_1}\n"
                f"Adres 2: {self.address_2}\n"
                f"Adres 3: {self.address_3}\n"
                f"Ulica: {self.street}\n"
                f"Miasto: {self.city}\n"
                f"Kod pocztowy: {self.postal_code}\n"
                f"Region: {self.state_province}\n"
                f"Stan: {self.state}\n"
                f"Kraj: {self.country}\n"
                f"Długość geograficzna: {self.longitude}\n"
                f"Szerokość geograficzna: {self.latitude}\n"
                f"Telefon: {self.phone}\n"
                f"Strona WWW: {self.website_url}")


szesciopak_na_promocji: list[Brewery] = []
browarnia_response = requests.get(basic_url)
browarnia_data = browarnia_response.json()

for p in browarnia_data:
    piwko = Brewery(**p)
    szesciopak_na_promocji.append(piwko)

for piwsko in szesciopak_na_promocji:
    print(piwsko)
    print("-" * 40, "\n" * 2)
