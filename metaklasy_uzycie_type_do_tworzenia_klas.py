class A:
    atr = 12
    def m1(self, x):
        print('A.m1', x)

# type(cls_name, clas_inh, cls_dict)
def m1(self, x):
    print('A.m1', x)

d = {
    'atr': 12,
    'm1': m1,
}

NewA = type('NewA', (), d)
a = NewA()
a.m1(1)
print(a.atr)