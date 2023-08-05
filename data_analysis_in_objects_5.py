ATTRIBUTE_COLUMN1 = 0
ATTRIBUTE_COLUMN2 = 1


def get_objects(given_lists, given_class):
    """
    Function -- create_objects
        create objects and store them into a list
    Parameters:
        -- given_lists type: list
        -- given_class type: class
    ErrorRaised:
        -- TypeError: notify if given parameter can generate objects
    Return a list that stored objects
    """
    objects_list = []
    # for objects from Intersections, DATA_COLUMN1 is stree_name, for those from TrafficSignals, DATA_COLUMN1 is signal_type, and DATA_COLUMN2 is geo_area for both
    for i in range(len(given_lists)):
        make_objects = given_class(
            given_lists[i][ATTRIBUTE_COLUMN1], given_lists[i][ATTRIBUTE_COLUMN2]
        )
        if not isinstance(make_objects, given_class):
            raise TypeError(
                "Error happens in create_objects(), given_class cannot create applicable objects"
            )
        objects_list.append(make_objects)

    return objects_list


def get_locations_from_objects(given_objects_list):
    """
    Function -- get_locations_from_objects
        Get attribute locations from objects
    Parameters:
        -- given_objects_list, type: list
    ErrorRaised:
        -- AttributeError: notify if the attribute of instances is None
    Return a sorted list with objects' location
    """
    attribute_list = []
    for each in given_objects_list:
        if not hasattr(each, "geo"):
            raise AttributeError(
                "Error happens in get_locations_from_objects(), objects doens't have required attributes"
            )
        attribute_list.append(each.geo)
    return sorted(attribute_list)


def get_types_from_objects(given_objects_list):
    """
    Function -- get_types_from_objects
        Get attribute types from objects
    Parameters:
        -- given_objects_list, type: list
    ErrorRaised:
        -- AttributeError: notify if the attribute of instances is None
    Return a sorted list with objects' type
    """
    attribute_list = []
    for each in given_objects_list:
        if not hasattr(each, "signal_type"):
            raise AttributeError(
                "Error happens in get_types_from_objects(), objects doens't have required attributes"
            )
        attribute_list.append(each.signal_type)
    return sorted(attribute_list)
