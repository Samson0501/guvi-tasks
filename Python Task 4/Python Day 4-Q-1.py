class Circle:
    def __init__(self, radii_list): #this method initializes a new instance of the class and providing a parameter
        self.radii = radii_list #storing the list of radii

# Example usage:
radii_list = [10, 501, 22, 37, 100, 999, 87, 351] # provided the list

circle = Circle(radii_list)
#created a new object with the list of radii

print(circle.radii)