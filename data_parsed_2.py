SIGNS_REPLACE = "\r\n"
CHAR_DIVISION = ";"
SPACE_CLEAN = ""
DEFAULT_TYPE = "UnknownType"
DEFAULT_GEO = "UnknownGeo"
REMOVE_HEADERS = 0


def data_parse(given_resp):
    """
    Function -- data_parse
        Clean the data to a list
    Parameters: given_resp, type: str
    ErrorRaised:
        -- AttributeError: notify if passed content is empty or not belongs to certain type
    Return a list with splited strings
    """
    if given_resp.text is False:
        raise AttributeError(
            "Error happens in data_parse(), given_resp has no required attribute"
        )

    url_content = given_resp.text

    if url_content == None:
        raise AttributeError("Error happens in data_parse(), nothing could be parsed.")

    new_lines = url_content.replace(SIGNS_REPLACE, CHAR_DIVISION)
    get_list = new_lines.strip().split(CHAR_DIVISION)

    return get_list


def get_attri_lists(given_list, total_column, get_column1, get_column2):
    """
    Function -- get_data_lists
        Create analytical data lists, in which specific columns are picked and stored for passing to instantiate objects
    Parameters:
        -- give_lists, type: list
        -- total_column, type: int
        -- get_column1, type: int
        -- get_column2, type: int
    ErrorRaised:
        -- IndexError: notify total lenth of given data is too short to use
        -- ValueError: notify if two parsed lists are not equal in length
    Return a nested list ziped by two lists
    """
    # remove the last extra column caused by split ";"
    given_list = given_list[REMOVE_HEADERS : REMOVE_HEADERS - 1]
    applicable_data1 = []
    applicable_data2 = []
    attributes_list = []

    if len(given_list) < total_column:
        raise IndexError(
            "Error happens in get_data_lists(), data from web is too short."
        )
    # remove the first line of web data
    given_list = given_list[total_column:]

    for i in range(len(given_list)):
        if i % total_column == get_column1:
            applicable_data1.append(given_list[i])
        elif i % total_column == get_column2:
            applicable_data2.append(given_list[i])

    if len(applicable_data1) != len(applicable_data2):
        raise ValueError(
            "Error happens in get_data_lists(), target lists have different length"
        )
    # clean null element in the list
    for i in range(len(applicable_data1)):
        if applicable_data1[i] == SPACE_CLEAN:
            applicable_data1[i] = DEFAULT_TYPE

    for j in range(len(applicable_data2)):
        if applicable_data2[j] == SPACE_CLEAN:
            applicable_data2[j] = DEFAULT_GEO

    attributes_list = list(zip(applicable_data1, applicable_data2))

    return attributes_list
