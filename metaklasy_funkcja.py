# napisać funkcję, która ma takie parametry jak type i
# ktora wola type

def pierwsza_metaklasa(cls_name, clas_inh, cls_dict):
    print('pierwsza metaklasa', cls_name, clas_inh, cls_dict)
    cls_dict['version'] = '1.2.3'
    return type(cls_name, clas_inh, cls_dict)

class A(metaclass=pierwsza_metaklasa):
    atr = 12
    def m1(self, x):
        print('A.m1', x)

a = A()
a.m1(12)
print(a.version)

