class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running!...')


class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print('Dog is running!...')
	def call(self):
		print('汪汪汪！！！')

class Cat(Animal):
	"""docstring for Cat"""
	def run(self):
		print('Cat is running!...')
	def call(self):
		print('喵喵喵！！！')



dog = Dog()
dog.run()
dog.call()
cat = Cat()
cat.run()
cat.call()

# 获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(Animal))