def is_inside(point=[], rec=[]):
    x1 = point[0]
    x2 = rec[0]
    y1 = point[1]
    y2 = rec[1]
    width = rec[2]
    height = rec[3]
    if x1 in range(x2, x2 + width):
        if y1 in range(y2, y2 + height):
            return True
        else:
            return False
    else:
        return False

# point = is_inside([180, 120],[140, 60, 200, 100])
point = is_inside([100, 120], [140, 60, 200, 100])
if point == True:
    print("Inside")
else:
    print("Outside")