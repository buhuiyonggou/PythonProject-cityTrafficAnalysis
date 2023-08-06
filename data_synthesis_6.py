DECIMAL_ROUND = 2
DIVIDE_ZERO_TEST = 0
import pandas as pd


def get_count_dictionary(given_lists):
    """
    Function -- get_count_dictionary
        Counting numbers by adding values to a dictionary
    Parameters:
        -- give_lists type: list
    ErrorRaised:
        -- ValueError: notify if given_lists are empty
    Return a dictionary counting numbers of keys
    """
    if given_lists is None:
        raise ValueError(
            "Error happens in get_count_dictionary(), passed list is empty."
        )
    counting_dictionanry = dict()

    for j in given_lists:
        counting_dictionanry[j] = 0

    for item in given_lists:
        counting_dictionanry[item] += 1

    return counting_dictionanry


def get_xticklabels(given_dict):
    """
    Function -- get_count_dictionary
        Get xticklabels from a given list, eliminate duplicated elements in the list
    Parameters:
        -- given_list type: list
    ErrorRaised: None
    Return a list with each geo_area, which will be used to make graph
    """
    xticklabels = []

    for key in given_dict.keys():
        xticklabels.append(key)

    for i in range(1, len(xticklabels)):
        if type(xticklabels[i - 1]) != type(xticklabels[i]):
            raise ValueError(
                "Error happens in get_xticklabels(), variables of x_label is not in identical type."
            )

    # if elements in the list are in the same type
    return xticklabels


def data_combine(given_dict1, given_dict2):
    """
    Function -- data_combine
        Create a column ratio which is divided by numbers of signals and intersections, and return columns for a required dictionary
    Parameters:
        -- given_dict1 type: dict
        -- given_dict2 type: dict
    ErrorRaised:
        -- TypeError: notify any of two given objects is not in dictionary
        -- ValueError: notify elements in amount lists should be int
        -- ValueError: notify two lists containing geo_area are not identical or have the same order
    Return a tuple of several lists
    """
    area1 = []
    area2 = []
    intersections_amount = []
    signals_amount = []
    ratio = []

    if type(given_dict1) != dict or type(given_dict2) != dict:
        raise TypeError(
            "Error happens in create_columns(). Passed data are not dictionaries"
        )

    for key, val in given_dict1.items():
        area1.append(key)
        intersections_amount.append(val)

    for key, val in given_dict2.items():
        area2.append(key)
        signals_amount.append(val)

    # if they are not identical, further comparision based on the list could be mismatched
    if area1 != area2:
        raise ValueError(
            "Error happens in create_columns(). The columns connecting different files are different"
        )

    for i in range(len(area1)):
        if intersections_amount[i] == DIVIDE_ZERO_TEST:
            raise ZeroDivisionError(
                "Error happens in create_columns(). Divisor could not be zero "
            )
        ratio.append(round(signals_amount[i] / intersections_amount[i], DECIMAL_ROUND))

    return area1, signals_amount, intersections_amount, ratio


def create_data_frame(give_headers, give_lists):
    """
    Function -- create_data_frame
        Generate a data frame according to given headers and data list
    Parameters:
        -- give_lists type: list
    ErrorRaised:
        -- ValueError: notify if given headers and lists are not in the same length, they couldn't be zipped
        -- ValueError: notify if dictionary that passed in is empty
    Return a data frame
    """
    if len(give_headers) != len(give_lists):
        raise ValueError(
            "Error happens in data_synthesize(). There is empty header/key in dictionary."
        )
    get_dict_panel = dict(zip(give_headers, give_lists))
    get_dataframe = pd.DataFrame(get_dict_panel)

    return get_dataframe
