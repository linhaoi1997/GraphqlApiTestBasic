class A:
    a = 1
    b = 2


class B(A):
    pass


def test():
    print(B.a)
