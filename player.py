
class Player(object):

	def __init__(self, jersey_number, name):
		self.jersey_number = jersey_number
		self.name = name

	def name(self):
		return self.name

	def jersey_number(self):
		return self.jersey_number

	def create_stat_list(self):
		