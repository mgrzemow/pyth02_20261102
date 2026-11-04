# napisać menedżera kontekstu mirzącego czas wykonania kodu pod with
import time
time.perf_counter()

class Stoper:
    def __init__(self, msg):
        ...
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('exit', exc_type, exc_value, traceback)
    def __repr__(self):
        return f''
if __name__ == '__main__':
    with Stoper('100 000 insertow') as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)
    print(s) # 100 000 insertow zajęło x s.
