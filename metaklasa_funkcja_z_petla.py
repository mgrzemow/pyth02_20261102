# napisać funkcję, która ma takie parametry jak type i
# ktora wola type

def pierwsza_metaklasa(cls_name, clas_inh, cls_dict):
    new_dict = {}
    for atr_name, atr_value in cls_dict.items():
        if atr_name.startswith(f'_{cls_name}__'):
            new_dict[atr_name[3:]] = atr_value
        else:
            new_dict[atr_name] = atr_value
    return type(cls_name, clas_inh, new_dict)

class A(metaclass=pierwsza_metaklasa):
    __atr = 12
    def m1(self, x):
        print('A.m1', x)

a = A()
a.m1(12)
print(a._atr)

