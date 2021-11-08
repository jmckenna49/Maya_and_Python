from maya import cmds


#below is a piece of code I made inside of Maya's General Script Editor.
#I'm commenting this piece of code just so that's easier to follow along without having to have maya up and running.
#this piece of code does need to be run inside of maya in order for it to be read and executed appropriately.
#I know Python can access both the cmds and OpenMaya API, however currently, I've only begun using Python inside of Maya's General Editor.
#I'll hopefully be accessing and using the API as a become more aware and focused on the code itself.





#making a cube inside of Maya's General Script editor, to see cubes that can be made.
cube = cmds.polyCube()
cubeShape = cube[0]


#making a circle now instead of a cube to see what is madein the general script editor of maya
circle = cmds.circle()

#having to call out first indexes of the circle and cube being made, due to circle and cube holding two values.
#the values inside of circle are the name of the circle, and the second index is holding the maya node for that circle.
#nodes in maya are the objects name, input, output, and the attributes that are used within that node.
#the same thing happens with cube up above in the code, hence why the first index is being called.

circleShape = circle[0]


#the function parent will say that the object cupeShape will be a child to circleShape
#this is also apparent in the Maya program where  if you move the parent object it will move the child object
#however the child object can still move without the parent object, so we need to lock them in order to prevent this
cmds.parent(cubeShape,circleShape)


#in Maya, on the channels window with the child object selected, this will allow the user to see the x, y, and z axis' for this object
#there, right click on the x axis and this will lock the x attribute into place. It will also dispaly into the script editor what attribute is being selected; which is very helpful for the python command window.
#the window outputs "setAttr -lock true "pCube2.tx" this tells us the command we have to use setAttr from cmds, and what object and what attribute we need to automate in our code down below.
#This allows us to use python and the cmds module to change the attributes of the object with python now.

#below allows us to automate the child object so that its always having fixed x, y, and z axises, cannot be rotated by itself, and cannot be scaled by itself.
#this however does allow the user to rotate, scale, and translate the object based off the parent object
cmds.setAttr(cubeShape+".translate",lock = True)
cmds.setAttr(cubeShape+".rotate",lock = True)
cmds.setAttr(cubeShape+".scale",lock = True)


# this last line allows python to tell Maya that once this script is executed, select the parent object once this script has been run.

cmds.select(circleShape)













