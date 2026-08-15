'''Area and Perimeter of a Circle

Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.
Another method for computing perimeter.

'''

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return self.radius*2*3.14

getRadius = float(input("Enter radius of a circle: "))
aCircle = Circle(getRadius)
print (f"Area of the circle is: {round(aCircle.area(), 2)}")
print (f"Perimeter of the circle is: {round(aCircle.perimeter(), 2)}")

# Output:
# Enter radius of a circle: 10.0
# Area of the circle is: 314.0
# Perimeter of the circle is: 62.8