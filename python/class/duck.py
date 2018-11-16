# あるインスタンスのsoundとwalkメソッドを実行
def test_duck(it):
	it.sound()
	it.walk()

# クラスを定義
class Duck:
	def sound(self):
		print("ガァガァ")
	def walk(self):
		print("アヒルが歩く")
	
class Dog:
	def sound(self):
		print("ワンワン")
	def walk(self):
		print("犬がが歩く")
	
class Cat:
	def sound(self):
		print("ニャーニャー")
	def walk(self):
		print("猫が歩く")
	
# ダック・タイピング
ahiru = Duck()
test_duck(ahiru)

inu = Dog()
test_duck(inu)

neko = Cat()
test_duck(neko)