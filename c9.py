class Serwer:
    __slots__ = [
        # 'ip',
        '_ip'
    ]

    def _set_ip(self, ip):
        x = ip.split('.')
        self._ip = tuple(map(int, x))
        if len(self._ip) != 4:
            raise ValueError('bad ip format - 4 sections seprated by dots')
        if not all(0 <= i <= 255 for i in self._ip):
            raise ValueError('bad ip format - each section is between 0 and 255')

    def _get_ip(self):
        return '.'.join(map(str, self._ip))

    ip = property(fget=_get_ip, fset=_set_ip)

    def __init__(self, ip: str):
        self.ip = ip


if __name__ == '__main__':
    s = Serwer('127.0.0.1')
    print(s.ip)
    s.ip = '192.168.1.1'
    print(s.ip)
    print(s.atr)

    # te mają nie przejść
    # s = Serwer('192.168.0.1.5')
    # s.ip = '666.1.2.3'
    # s.ip = '192.168.0.ala'
    # dodatkowa funkcjonalność:
    # internal format: (191,168,0,1)
    # validation:
    # - 4 sections seprated by dots
    # - each section is between 0 and 255
    # addidional read-only property:
    # - ip_tuple: (192.168.0.1)
    # proponuję ValueError
