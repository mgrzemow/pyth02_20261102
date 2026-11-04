# python guarantees __exit__
# use instead of destructor
class MyContextManager:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('exit', exc_type, exc_value, traceback)
        # if __exit__returns True, it will block the exception
        # return True
if __name__ == '__main__':
    x = MyContextManager()
    with x as alias:
        print(x, alias)
        9/0



    print('after exit')
