class Call(object):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def received(self, *args, **kwargs):
        return (self.args, self.kwargs) == (args, kwargs)


class SpyMethod(object):
    def __init__(self, name):
        self.name = name
        self.calls = []

    def __call__(self, *args, **kwargs):
        self.calls.append(Call(args, kwargs))

    def was_called_with(self, *args, **kwargs):
        for call in self.calls:
            if(call.received(*args, **kwargs)):
                return True
        return False


class Spock(object):
    def __getattr__(self, attr_name):
        spy_method = SpyMethod(attr_name)
        setattr(self, attr_name, spy_method)
        return spy_method
