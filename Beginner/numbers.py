# 2(a) Format function
def format_value(a, b):
    return format(a, b)
print("Formatted value:", format_value(145, 'o'))

# 2(b) Area of circular pond and water calculation
radius = 84
pi = 3.14
area = pi * radius * radius
water = int(area * 1.4)
print("Area of Pond:", area)
print("Total Water:", water)

# 2(c) Speed calculation
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = int(distance / time_seconds)
print("Speed (m/s):", speed)
