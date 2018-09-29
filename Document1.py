class Matrix:
	counter = 0

	#def __init__(self):



	def __init__(self, list1):
		self.list1 = list1
		Matrix.counter += 1
		self.id = Matrix.counter





	def rows(self):
		return len(self.list1)

	def columns(self):
		return len(self.list1[0])

	def dimentions(self):
		return "{0}X{1}".format(len(self.list1) , len(self.list1[0]))

	def description(self):

		for x in self.list1:
			print(x)

	def get_id(self):
		return id






list1=Matrix([[8,9],[1,2],[5,6]])
list2=Matrix([[1],[2],[3]])
list3=Matrix([])
#list2=Matrix()
print(list1.rows())
print(list1.columns())
print(list1.dimentions())
print(list1.description())
print('===========')

print(list3.rows())
print('===========')

print(list2.rows())
print(list2.columns())
print(list2.dimentions())
print(list2.description())
print(Matrix.counter)
print(list1.id)
print(list2.id)
print(list3.get_id())
