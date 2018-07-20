class DynamicGreeter(object):
    def __getattr__(self, attr_name):
        if attr_name.startswith('greet_'):
            def greeter():
                print('Hello ' + attr_name.replace('greet_', ''))
            return greeter
        else:
            raise Exception('Could not understand method ' + attr_name)


greeter = DynamicGreeter()
greeter.greet_python()
greeter.greet_everyone()
greeter.something_else()
