def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:%s" % res)


g = foo()
print(next(g))
print("---------")
print(g.send(7))
