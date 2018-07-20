class CallableObject(object):
	def __init__(self, name):
		self.name = name

	def __call__(self, *args, **kwargs):
		print(self.name, 'received call', args, kwargs)


callable_object = CallableObject('awesome_method')
callable_object('hello')
# Output > awesome_method received call ('hello',) {}

callable_object('hello', to='world')
# Output > awesome_method received call ('hello',) {'to': 'world'}
