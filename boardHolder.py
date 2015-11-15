from FreeCAD import *

# 10mm bolt shaft
# 3mm nut
# PCB is 1.6mm thick.
# = 5.4mm long screwhole

# plate = Part.makePlane(50, 50).extrude(Vector(0,0,1.5))
# Part.show(plate)

support = Part.makeCylinder(3, 5.4)
screwholeCutout = Part.makeCylinder(1.7, 5.4)

screwhole = support.cut(screwholeCutout)
Part.show(screwhole)

# screwhole.translate(Vector(3, 3, 0))
# Part.show(screwhole)
# screwhole.translate(Vector(44, 0, 0))
# Part.show(screwhole)
# screwhole.translate(Vector(0, 44, 0))
# Part.show(screwhole)
# screwhole.translate(Vector(-44, 0, 0))
# Part.show(screwhole)


