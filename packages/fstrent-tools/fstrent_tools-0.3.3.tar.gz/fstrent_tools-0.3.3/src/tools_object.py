import sys

__all__ = [
    'compare_objects',
    'get_object_attributes',
    'get_object_methods',
    'get_object_size',
    'get_object_type',
    'is_object_empty',
    'print_obj'
]

def compare_objects(obj1, obj2):
    """
    Compares two objects for equality.

    Args:
        obj1 (any): The first object.
        obj2 (any): The second object.

    Returns:
        bool: True if the objects are equal, False otherwise.
    """
    return obj1 == obj2

def get_object_attributes(obj):
    """
    Returns a dictionary of an object's attributes.

    Args:
        obj (any): The object to get the attributes of.

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return vars(obj)

def get_object_methods(obj):
    """
    Returns a list of an object's methods.

    Args:
        obj (any): The object to get the methods of.

    Returns:
        list: A list of the object's methods.
    """
    return [method for method in dir(obj) if callable(getattr(obj, method))]

def get_object_size(obj):
    """
    Returns the size of an object in bytes.

    Args:
        obj (any): The object to get the size of.

    Returns:
        int: The size of the object in bytes.
    """
    return sys.getsizeof(obj)

def get_object_type(obj):
    """
    Returns the type of an object.

    Args:
        obj (any): The object to get the type of.

    Returns:
        str: The type of the object.
    """
    return type(obj).__name__

def is_object_empty(obj):
    """
    Checks if an object is empty.

    Args:
        obj (any): The object to check.

    Returns:
        bool: True if the object is empty, False otherwise.
    """
    if isinstance(obj, (list, tuple, dict, set, str)):
        return len(obj) == 0
    elif obj is None:
        return True
    else:
        return False

def print_obj(obj):
    obj_list = {}
    for attr, value in obj.__dict__.items():
        obj_list[attr] = value
    print(obj_list)
