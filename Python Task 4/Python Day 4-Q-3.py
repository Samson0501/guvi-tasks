def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

dimensions = [10, 501, 22, 37, 100, 999, 87, 351]

for i in range(0, len(dimensions), 2):
    length = dimensions[i]
    width = dimensions[i + 1]
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"Rectangle with length {length} and width {width}:")
    print(f"Area: {area}, Perimeter: {perimeter}")
    print()
