def area_of_square(side):
    area = side ** 2
    return area
def area_of_rectangle(length,width):
    area = length * width
    return area
def area_of_circle(radius):
    return 3.14 *radius ** 2
def area_of_traingle(base,height):
    return 0.5 * base * height

print("-----------------------------------------------")
print("----------------Area Calculator----------------")
print("-----------------------------------------------")

print("Chose a shape to calculate the area: ")
print("1. Square")
print("2.Rectangle")
print("3.Circle")
print("4.Traingle")

choice = int(input("Enter your choice: "))

if choice == 1:
    side = float(input("Enter the side length of the squares: "))
    area = area_of_square(side)
    print(f"The area of the square is: {area}")
elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_of_rectangle(length,width)
    print(f"The area of rectangle is {area:.2f}")
elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    area = area_of_circle(radius)
    print(f"The area of circle is {area:.2f}")
elif choice == 4:
    base = float(input("Enter the base of traingle: "))
    height = float(input("Enter the height of the traingle: "))
    area = area_of_traingle(base, height)
    print(f"The area of traingle is {area:.2f}")
else:
    print("Invalid Choice. Please try again.")