# def count():
#     with open("a.txt") as f:
#         for line in f.readlines():
#             print(line)
class A():
    def foo1(self):
        print("A")


class B(A):
    def foo2(self):
        pass


class C(A):
    def foo1(self):
        print("C")


class D(B, C):
    pass


d = D()
d.foo1()
