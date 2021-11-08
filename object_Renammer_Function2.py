# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:51:55 2021

@author: james
"""




from maya import cmds

#Using a dictionary here for key value pairs. It also makes the code easier and more manageable to use than the previous portion of the code.
# In this case you have the key as the objectType and the value as a suffix.
# For the camera we will set None as we want to use it to indicate Camera's should have no suffix
# Having a dictionary in this chunk of code is also more efficient than using a bunch of if, else if, and else statements because I can add more values and their keys which will make this code more efficient and faster.

SUFFIXES = {
    "mesh": "geo",
    "joint": "jnt",
    "camera": None,
}



DEFAULT = "grp"


# This variable down below will use the ls function in maya to list out what objects are currently and fully in the scene.
# We'll also need to make an if statement in case there isn't any objects in the scene as well.
# We should also get the full path to the object instead of just the name of the object.
# Long is a function in the Maya cmds library that will return the full path for the names of the objects.
# The other point of using Long is to also tell whether or not objects have a parent child relationship.

# Selection here is our varagin, I'm setting this equal to false currently to let the function know whether or not I would like to use this as an input.

def rename(selection=False):
    """
    Renames objects by adding suffixes based on the object type
    Args:
        selection (bool): Whether we should use the selection or not. Defaults to False
    Raises:
        RuntimeError: If nothing is selected
    Returns:
        list: A list of all the objects renamed
    """



    # The ls function also takes an input called selection, and we can just pass that through.
    objects = cmds.ls(selection=selection, dag=True)

    # Now if we are trying to use the selection and nothing is selected, lets give an error.
    if selection and not objects:
        raise RuntimeError("You don't have anything selected")

    # Now we need to sort our items from longest to shortest again so that we don't rename parents before children
    objects.sort(key=len, reverse=True)

    # Now we loop through all the objects we have
    for obj in objects:

        # We get the shortname again by splitting at the last |
        shortName = obj.split('|')[-1]

        # Now we see if there are children and if there are we get their type.
        # This is in case we receive a transform and not its shape
        children = cmds.listRelatives(obj, children=True) or []
        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)

        # Now we look at the dictionary and ask to get the value associated with the key
        # In this case, if objType is mesh, we will get geo
        # If the dictionary doesn't hold the item, it will return the default value instead that we ask it for
        suffix = SUFFIXES.get(objType, DEFAULT)

        if not suffix:
            continue

        # To prevent adding the suffix twice, we'll check if it already has the suffix and skip it if it does
        if shortName.endswith('_'+suffix):
            continue

        # Now we'll make the new name using string formatting
        # Instead of using the + symbol, we can use the %s symbol to insert strings
        newName = '%s_%s' % (shortName, suffix)
        cmds.rename(shortName, newName)

        # Now we find where in the list of objects our current object is
        index = objects.index(obj)

        # Then we replace it in the list with the name of the new object
        objects[index] = obj.replace(shortName, newName)

    # Finally we return the list back to the user of our function
    # Returning is how a function can let things outside it know what the result of it is
    return objects