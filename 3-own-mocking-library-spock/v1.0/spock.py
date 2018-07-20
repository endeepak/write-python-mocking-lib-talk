class Call(object):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


class SpyMethod(object):
    def __init__(self, name):
        self.name = name
        self.calls = []

    def __call__(self, *args, **kwargs):
        self.calls.append(Call(args, kwargs))


class Spock(object):
    def __getattr__(self, attr_name):
        spy_method = SpyMethod(attr_name)
        setattr(self, attr_name, spy_method)
        return spy_method
