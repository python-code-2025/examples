#import my_package.module1
#import my_package.module2
import my_package

my_package.module1.hello()
my_package.module2.sum(5,6)

def hello():
    print("This is a local function hello")

hello()