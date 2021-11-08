# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:58:34 2021

@author: james mckenna
"""

from maya import cmds

"""
 This python project required me to make 3 separate gears in Autodesk Maya.
 First I made the object to see how to do it first using object creation by making a pipe; or circle with a hole in it.
 Then I picked every other face on the outside portion of the pipe; then extruded that to a certain length in order to make it a gear.
 After I understood how to make a gear in Maya, then I proceeded to try and understand how to write the code in Python in order to automate this process.

 In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
 This function will take in teeth and length in as two parameters for this function. Teeth must be passed in as int and length must be an int or float.

 Making the gearCreate module that I created earlier, into a class. That way it can be imported just like a module but objects can be created easier with methods and object down below.
 This also allows for let redundant code and easier to read accessibility.

"""

# Class was made in order to make use of this module for way easier use for other Python programs maybe needed in the future.
# Object is the base for everything in python, and by basing off of the python 'object' we get all of its attributes for free.

class Gear(object):
    """

    # This creates an instance of the class.
    # Classes descrive an object, instances are the objects that they describe
    # For example an Animal class describes an animal, but a dog on the street would be an instance of an Animal
    gearA = Gear()
    gearA.create(teeth=20, length=0.2)
    gearA.changeTeeth(teeth=10, length=0.5)
    
    """
    
    
    
    
    # Creating a constructor to initialize transform, extrude, and constructor down below. 
    def __init__(self):
        # We will just use this __init__ to create placeholder variables on the class
        # Variables that start with self are set on the instance and can be accessed outside this function.
        # The __init__ method is a constructor that helps with object creation as well as letting us set values for future use down in the code.
        
        self.transform = None
        self.extrude = None
        self.constructor = None
        
    #Creating instance methods for easier use.
    def gearCreate(self, teeth, length):
       
        
        """
        This function will create a gear with teeth and length as parameters.
        Args:
            teeth: The number of teeth to create in integers
            length: The length of the teeth as a float or int.
        Returns:
            A tuple of the transform, constructor and extrude node
        """


        # In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
        spans = teeth *2
    
        # The cmds function polyPipe returns a constructor and a transform hence why we're equating the two together here.
        #The transform is the name of the node, the constructor is the node that creates the pipe and controls its parameters.
        self.transform, self.constructor = cmds.polyPipe(subdivisionsAxis=spans)
        
         # This is saying that the teeth should have a minimum range starting at teeth *2, since thats where our side faces are going to start, and ending at teeth*3 because that's where we want it to end, but going in step sizes of 2.
        sideFaces = range(spans*2,spans*3,2)
        
        # This is a statement that will clear any selection we already have inside of Maya. That way when we add a face it wont be over adding or overwriting. 
        cmds.selet(clear=True)
        
        # Now we start looping over all our side faces in our list.
        for faces in sideFaces:
            
        # This is telling Maya to select that specific face and then add it to the selection.
        # pPipe1.f["# you're giving to the pipe face"]
        # the f[#] tells the pipe which face of the object you wnat it to select.    
            
            cmds.select('%s.f[%s]' %(self.transform,faces), add=True)
            
        # This command will allows us to extrude the faces that we select off our pipe in order to make it a gear.
        # We have to tell it which direction we wish it for it to extrude, so we're giving it the z direction to make it look like a gear.
        # We are also setting our list to grab the first object, because this will only return a list of size 1 in the first place.
            
        self.extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]
        


    
    # Wanting a function that will modify the constructor and extrude the node to change how many teeth we can get and modify the length.
    #Creating instance methods for easier use.
    def teethChange(self, extrude, teeth, length):
        """
        Change the number of teeth on a gear with a given number of teeth and a given length for the teeth.
        This will create a new extrude node.
        Args:
            constructor (str): the constructor node
            extrude (str): the extrude node
            teeth (int): the number of teeth to create
            length (float): the length of the teeth to create
        """
        
            
        # In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
        spans = teeth*2
        
        # The immportant part of this function is the edit parameter being set to true.
        # This will allow us to edit the original pipe, or pipe we created previously so that we can edit and modify the teeth on it instead of creating a new object.
        cmds.polyPipe(self.constructor, edit =True, subdivisionsAxis=spans)
        
        # In order to make the teeth on the pipe or outer face, the teeth have to alternate every other edge. 
        spans = teeth*2
    
        #Creating a list for the faces that need to be extruded for teeth
        sideFaces = range(spans*2, spans*3, 2)
    
        
        # Creating an empty list to get the face names that we want to extrude off of.
        faceNames = []
    
        #Using this to loop over our side faces in our list.
        for faces in sideFaces:
            
            faceName ="f[%s]" % (faces)
            
            #This will tell us what face we are looking at by number, and will append it to our empty list we initialized before.
            faceNames.append(faceName)
    
        # The extrude node has an attribute called inputComponents.
        # We can call an attribute called setAttr to help us set our attributes we want for that specific face.
    
        # cmds.setAttr('extrudeNode.inputComponents', numberOfItems, item1, item2, item3, type='componentList')
        # This command will allow us to extrude the node based off of 
        # Using *faceNames allows this function to expand the list of faceNames we already have. So that it can be automated easier. We also need to tell it the type of attribute we want.
        cmds.setAttr("%s.inputComponents" % (self.extrude), len(faceNames), *faceNames, type="componentList")
    
        
        # Now we want to edit the extruded faces based off of lenght. So we have to grab another cmds function in order to do that.
        # Edit will also allow us to edit exisiting faces and not have to make new ones.
        # ltz is short form that Maya can use for localTranslateZ, just found this out so I thought I would test it in this little bit of code.
        cmds.polyExtrudeFacet(self.extrude, edit=True, ltz=length)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        