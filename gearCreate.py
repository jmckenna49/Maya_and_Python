# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:27:12 2021

@author: james mckenna

"""


from maya import cmds


# This python project required me to make 3 separate gears in Autodesk Maya.
# First I made the object to see how to do it first using object creation by making a pipe; or circle with a hole in it.
# Then I picked every other face on the outside portion of the pipe; then extruded that to a certain length in order to make it a gear.
# After I understood how to make a gear in Maya, then I proceeded to try and understand how to write the code in Python in order to automate this process.

# In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
# This function will take in teeth and length into 
def gearCreate(teeth, length):
    print("Creating Gear:",teeth,length)

    # In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
    spans = teeth*2
    
    # The cmds function polyPipe returns a constructor and a transform hence why we're equating the two together here.
    #The transform is the name of the node, the constructor is the node that creates the pipe and controls its parameters.
    transform, constructor = cmds.polyPipe(subdivisionsAxis=spans)
    
    # This is saying that the teeth should have a minimum range starting at teeth *2, since thats where our side faces are going to start, and ending at teeth*3 because that's where we want it to end, but going in step sizes of 2.
    sideFaces = range(spans*2, spans*3, 2)


    # This is a statement that will clear any selection we already have inside of Maya. That way when we add a face it wont be over adding or overwriting. 
    cmds.selet(clear=True)

    # Now we start looping over all our side faces in our list.
    
    for faces in sideFaces:
        # This is telling Maya to select that specific face and then add it to the selection.
        # pPipe1.f["# you're giving to the pipe face"]
        # the f[#] tells the pipe which face of the object you wnat it to select.
        
        cmds.select('%s.f[%s]' %(transform,faces), add=True)
        
        # This command will allows us to extrude the faces that we select off our pipe in order to make it a gear.
        # We have to tell it which direction we wish it for it to extrude, so we're giving it the z direction to make it look like a gear.
        # We are also setting our list to grab the first object, because this will only return a list of size 1 in the first place.
        
    extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]

    # This line will give back a tuple inside of maya that will be the name of the node, the shape and the face that's extruded.
    # The constructor is the node that creates the original pipe, and the extrude is the node that extrudes faces on the pipe that we have made.
    return transform, constructor, extrude











