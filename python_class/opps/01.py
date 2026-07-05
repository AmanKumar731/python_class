class myclass:
    classname = "my class"

    def say_hello(self, name):
        print(f"Hello, {name}!, i am {self.classname}.")

obj= myclass()
print(obj.say_hello())

class calculater:
    def add(self,x,y):
        return x+y


    def subtesct(self,x,y):
        return x-y
    

    def multiply(self,x,y):
        return x*y
    

    def devide(self,x,y):
        return x/y
    
