class TwoSum:
	def __init__(self):
		data_structure = []
				
	# function that adds the number "input" to an internal data structure
	def add(self, input):
		self.data_structure.append(input)
						
	# function to find if there exists any pair of numbers which sum is equal to "value"
    	def find(self, value):
		pairs = {}

		vals = self.data_structure

		for i in range(len(vals)):
			if vals[i] not in pairs:
				pairs[vals[i]] = [i, 1]
			else:
				pairs[vals[i]][-1] += 1 

			comp = value - vals[i]
			info = pairs.get(comp)

			if info and info[0] != i and info[1] > 1:
				return [i, info[0]]									
