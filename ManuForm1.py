from FreeCAD import *

KEYDIST = 19.05
KEYWELL_CURVE = 15 # degrees

def key(ySize=1, extraDepth=0, ytop = 0, ybot = 0):
    mmx = KEYDIST
    mmy = KEYDIST * ySize
    cutoutSize = 13.9 # 14mm for cherry MX switch
    extracutoutX = 15.6
    extracutoutY = mmy - 3

    disassemblygapwidth = 3.1
    centerflapwidth = 5.8

    tinycornersize = (cutoutSize - (disassemblygapwidth * 2) - centerflapwidth) / 2

    plate = Part.makePlane(mmx, mmy + ytop + ybot).extrude(Vector(0,0,1.5))
    plate.translate(Vector(0, -ybot, 0))
    cutout = Part.makeBox(cutoutSize,cutoutSize,3)
    cutoutPost = Part.makePlane(extracutoutX, disassemblygapwidth).extrude(Vector(0,0,3))
    cutoutPost2 = Part.makePlane(extracutoutX, disassemblygapwidth).extrude(Vector(0,0,3))
    cutoutPost.translate(Vector(-(extracutoutX - cutoutSize) / 2, tinycornersize, 0))
    cutoutPost2.translate(Vector(-(extracutoutX - cutoutSize) / 2, (cutoutSize - tinycornersize - disassemblygapwidth), 0))
    cutout = cutout.fuse(cutoutPost)
    cutout = cutout.fuse(cutoutPost2)
    cutout.translate(Vector((mmx - cutoutSize) / 2, (mmy - cutoutSize) / 2, -1))
    #cutout.translate(Vector(0,0-ytop+ybot))

    result = plate.cut(cutout)

    #result.translate(Vector(0,0-ytop-ybot,0))

    if extraDepth > 0:
        extrasquare = Part.makePlane(mmx, mmy).extrude(Vector(0,0,-extraDepth))
        extracutout = Part.makeBox(extracutoutX,extracutoutY,extraDepth*2)
        extracutout.translate(Vector((mmx - extracutoutX) / 2, (mmy - extracutoutY) / 2, -(extraDepth)))
        extraResult = extrasquare.cut(extracutout)
        result = result.fuse(extraResult)
    return result


keyMiddle = key(ySize = 1.3, extraDepth = 2)
keyMiddle.translate(Vector(0,(-KEYDIST*0.3)/2,0))

keyUp = key(ySize = 1, extraDepth = 10, ybot = 1)
#keyUp.translate(Vector(0,(-KEYDIST*0.1)/2,0))

keyUp.rotate(Vector(0,0,7.5), Vector(1,0,0), KEYWELL_CURVE)
keyUp.translate(Vector(0,KEYDIST,0))

keyDown = key(ySize = 1, extraDepth = 10, ytop = 1)
#keyDown.translate(Vector(0,(-KEYDIST*0.1)/2,0))

keyDown.rotate(Vector(0,KEYDIST,7.5), Vector(1,0,0), -KEYWELL_CURVE)
keyDown.translate(Vector(0,-KEYDIST,0))


columnBaseTrim = Part.makeBox(500, 500, 10)
columnBaseTrim.translate(Vector(-250,-250,-12))





column = keyMiddle.fuse(keyUp).fuse(keyDown)
column = column.cut(columnBaseTrim)
column.rotate(Vector(0,0,0), Vector(1,0,0), KEYWELL_CURVE/2)

column2 = column.copy()
column2.translate(Vector(KEYDIST, 0, 0))

column3 = column.copy()
column3.translate(Vector(KEYDIST * 2, KEYDIST * 0.5, 0))

column4 = column.copy()
column4.translate(Vector(KEYDIST * 3, 0, 0))

column5 = column.copy()
column5.translate(Vector(KEYDIST * 4, -KEYDIST * 1.25, 0))

column6 = column.copy()
column6.translate(Vector(KEYDIST * 5, -KEYDIST * 1.25, 0))

columns = column.fuse(column2).fuse(column3).fuse(column4).fuse(column5).fuse(column6)


columns = columns.cut(columnBaseTrim)




longThumb1 = key(ySize = 1.5, extraDepth = 1)
longThumb1.rotate(Vector(0,KEYDIST * 1.5,0), Vector(1,0,0), 10)
longThumb1.rotate(Vector(0,KEYDIST * 1.5,0), Vector(0,1,0), -40)
longThumb1.translate(Vector(2, -(KEYDIST * 2.5) - 0.5, -12))

longThumb2 = key(ySize = 1.5, extraDepth = 1)
longThumb2.rotate(Vector(0,KEYDIST * 1.5,0), Vector(1,0,0), 10)
longThumb2.rotate(Vector(0,KEYDIST * 1.5,0), Vector(0,1,0), -40)
longThumb2.translate(Vector(3 + KEYDIST, -(KEYDIST * 2.5) - 2.5, -6))


shortThumb = key(ySize = 1, extraDepth = 1)
shortThumb.rotate(Vector(0,KEYDIST * 1.5,0), Vector(1,0,0), 10)
shortThumb.rotate(Vector(0,KEYDIST * 1.5,0), Vector(0,1,0), -40)
shortThumb.translate(Vector(2, -(KEYDIST * 4) - 0.5, -12))


#final = columns.fuse(longThumb1).fuse(longThumb2)

columns.rotate(Vector(0,0,0), Vector(0,1,0), 20)
longThumb1.rotate(Vector(0,0,0), Vector(0,1,0), 20)
longThumb2.rotate(Vector(0,0,0), Vector(0,1,0), 20)
shortThumb.rotate(Vector(0,0,0), Vector(0,1,0), 20)

Part.show(columns)
Part.show(longThumb1)
Part.show(longThumb2)
Part.show(shortThumb)

