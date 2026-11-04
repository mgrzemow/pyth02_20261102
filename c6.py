# napisać menedżera kontekstu mirzącego czas wykonania kodu pod with
import time
import collections

time.perf_counter()


class Stoper:
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        self.t1 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.t2 = time.perf_counter()
        # print('exit', exc_type, exc_value, traceback)

    def __repr__(self):
        return f'{self.msg}: {self.t2 - self.t1:0.2f} s.'


if __name__ == '__main__':
    with Stoper('50 000 insertow') as s:
        x = []
        for i in range(50_000):
            x.insert(0, i)
    print(s)  # 100 000 insertow zajęło x s.

    with Stoper('100 000 insertow') as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)
    print(s)  # 100 000 insertow zajęło x s.

    with Stoper('200 000 insertow') as s:
        x = []
        for i in range(200_000):
            x.insert(0, i)
    print(s)  # 100 000 insertow zajęło x s.

    with Stoper('400 000 insertow') as s:
        x = []
        for i in range(400_000):
            x.insert(0, i)
    print(s)  # 100 000 insertow zajęło x s.

    with Stoper('400 000 insertow') as s:
        x = collections.deque()
        for i in range(400_000):
            x.insert(0, i)

    print(s)  # 100 000 insertow zajęło x s.
