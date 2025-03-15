from child13 import Child

objectChild=Child('Pencil','Blue')
objectChild.getChildData()

objectChild.getInfo()

#Note, you can call below method, even it is marked protected
print("Calling protected method:")
objectChild._getParentData()
