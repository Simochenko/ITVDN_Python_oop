class Point:
    """Класс для представления координат точек на плоскости"""
    x = 1
    y = 1


print(Point.__doc__)
print(Point.__name__)
print(dir(Point))


pt = Point()
print(pt.__dict__)
pt.x = 5
pt.y = 10
print(pt.__dict__)
print(getattr(pt, "x"))
print(getattr(pt, "z", False))
print(hasattr(pt, "z"))
print(hasattr(pt, "y"))
setattr(pt, "z", 7)
print(pt.__dict__)
delattr(pt, "z")
print(pt.__dict__)

Point.z = 100
pt.msg = "hello"
res = getattr(pt, "sss", False)
print(pt.__dict__)
class Point3D:
    pass
pt = Point()
print(isinstance(pt, Point3D))