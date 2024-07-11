class Circle:
    __pi = 3.141  # Private class variable for pi

    def __init__(self, radii_list): #method initializes a new instance of the Circle class with the list of radii.
        self.radii = radii_list

    def get_areas(self):
        """Calculate and return a list of areas for the circles with the given radii."""
        return [Circle.__pi * r**2 for r in self.radii]

    def get_circumferences(self):
        """Calculate and return a list of circumferences for the circles with the given radii."""
        return [2 * Circle.__pi * r for r in self.radii]

# Example usage:
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)

print("Radii:", circle.radii)
print("Areas:", circle.get_areas())
print("Circumferences:", circle.get_circumferences())
