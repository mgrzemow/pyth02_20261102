"""Ćwiczenie: walidacja adresu IP przez property oraz działanie __slots__."""


class Serwer:
    """Serwer z adresem IP walidowanym przez property."""

    __slots__ = [
        # 'ip',
        "_ip"
    ]

    def _set_ip(self, ip):
        """Sprawdza adres i zapisuje go jako krotkę liczb."""
        x = ip.split(".")
        self._ip = tuple(map(int, x))
        if len(self._ip) != 4:
            raise ValueError("bad ip format - 4 sections seprated by dots")
        if not all(0 <= i <= 255 for i in self._ip):
            raise ValueError("bad ip format - each section is between 0 and 255")

    def _get_ip(self):
        """Zwraca adres jako napis."""
        return ".".join(map(str, self._ip))

    ip = property(fget=_get_ip, fset=_set_ip)

    def __init__(self, ip: str):
        """Ustawia adres przez property, więc też z walidacją."""
        self.ip = ip


if __name__ == "__main__":
    s = Serwer("127.0.0.1")
    print(s.ip)
    s.ip = "192.168.1.1"
    print(s.ip)
    # __slots__ blokuje atrybuty spoza listy
    try:
        print(s.atr)
    except AttributeError as e:
        print("AttributeError:", e)

    # te mają nie przejść
    for bledny_ip in ["192.168.0.1.5", "666.1.2.3", "192.168.0.ala"]:
        try:
            s.ip = bledny_ip
        except ValueError as e:
            print(bledny_ip, "->", e)

    # dodatkowa funkcjonalność:
    # internal format: (191,168,0,1)
    # validation:
    # - 4 sections seprated by dots
    # - each section is between 0 and 255
    # addidional read-only property:
    # - ip_tuple: (192.168.0.1)
    # proponuję ValueError
