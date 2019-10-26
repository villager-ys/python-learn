class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, *kwargs)
        return cls._instance


class B(Singleton):
    pass


def singleton2(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return get_instance


@singleton2
class C:
    pass


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton).__call__(*args, *kwargs)
        return cls._instance


class D(metaclass=Singleton):
    pass
