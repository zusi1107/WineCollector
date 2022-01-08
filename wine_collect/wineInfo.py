class WineInfo:

	def __init__(self, n):
		print("Initializing WineInfo: " + str(n))
		self.name = n
	
	def method1():
		print("method1 called for name: " + str(self.name))

	def __str__(self):
		return 'WineInfo[name=%s]' % (self.name)