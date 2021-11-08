# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:24:11 2021

@author: james mckenna
"""






from maya import cmds

# This variable down below will use the ls function in maya to list out what objects are currently and fully in the scene.
# We'll also need to make an if statement in case there isn't any objects in the scene as well.
# We should also get the full path to the object instead of just the name of the object.
# Long is a function in the Maya cmds library that will return the full path for the names of the objects.
# The other point of using Long is to also tell whether or not objects have a parent child relationship.

def rename():
    
    selection = cmds.ls(selection=True,long=True)

    #printing out the selection to see what is currently stored in the scene in Maya.
    print(selection)


    # Starting the if statement to look at the length of the selection variable, to see if any objects are currently in the scene.
    # If there isn't any objects in the scene, it jumps down into the next command which will make a selection variable with long and dag functions.
    # dag is a function in cmds that will represent all of the objects that are in the outliner which shows all the objects in the scene inside of Maya. Hence why were are setting it to true in this case.
    
    if len(selection) == 0:
        selection = cmds.ls(dag=True, long=True)
        
        
        
    # We can run into an issue where we'll rename a parent before a child, causing the path to the child to change.
    # To work around that we'll sort the list by length
    
    # We'll use the sort function in python that takes the len of the object to sort it from biggest to smallest, then we'll reverse it so that the longest objects are given first.
        
    selection.sort(key=len, reverse=True)
    
    
    # Now we need to loop through the all the objects in the scene and rename them.
    # A for loop can be used and provided to do this.
    # We step through all the items one by one in the selection object, assign it to a variable (obj) and run the logic below it.
    
    for obj in selection:
        # In Maya, all the objects will be shown in a pattern like this [ |'grandparent'|'parent'|'child' ] so in order to break this up, we'll to have use a delimiter value to break the names apart.
        # We just want the child part of the name, so we split using the | character which gives us a list of ['grandparent', 'parent', 'child']
        # We need to get the last item in the list, so we use [-1]. This means we backwards through the list and pick the next item, which would therefore be the last item.
        shortName = obj.split('|')[-1]
    
        print("Before rename: ", shortName)
    
        # Next we need to check for transforms, Maya identifies objects via a transform and shape. So we have to check for the transform first, then get the child for that object type.
        # We can use the command, listRelatives, that will allow us to narrow down the search via parameters, in order for us to be able to find the child object and the full path to that child object.
        # However, when using the list command in Maya, if Maya has nothing to give back it will return with None; if Maya can't find a list. So in order to get around this, we have to implement a conditional statment via the or command.
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []
        
        # The [] will take care of the None value if it can't find a list or returns None, it will then instead just return an empty list. That way no matter what happens, the object children will always return back as a list.
        
        # Below is an if-else statment that will check to see that there is only one child object, it will also do an object type check on that specific object.
        
        if len(children) == 1:
            # Take the first child
            child = children[0]
            objType = cmds.objectType(child)
        else:
            # Get the object type of the current object
            objType = cmds.objectType(obj)
        
            
        # Now we want to check the object types and what we want to rename them to.
        # We use a bunch of if statements to find the suffix we want to add
        # Squares and circles can be handled by the mesh objType, so they will have the suffix geo now.
     
        if objType == "mesh":
            suffix = "geo"
        elif objType == "joint":
            suffix = "jnt"
        elif objType == "camera":
            # In the case of the camera, we will say to continue.
            # Continue means that we will continue on to the next item in the list and skip the rest of the logic for this one
            print("Skipping camera:")
            continue
        else:
            suffix = "grp"
    
        # Now we need to construct the new name, concanating strings together for the new names of the child objects.
        newName = shortName + "_" + suffix
    
        # Now tell it to rename the obj to the new name with the suffix
        cmds.rename(obj, newName)
    
        print("After rename: ", newName)
        
    

















































