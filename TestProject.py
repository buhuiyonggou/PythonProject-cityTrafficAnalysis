DATA_INTERSECTION = "https://opendata.vancouver.ca/explore/dataset/street-intersections/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
DATA_SIGNALS = "https://opendata.vancouver.ca/explore/dataset/traffic-signals/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
TEST_GIVEN_LIST1 = [
    ("ST. GEORGE ST AND E 64TH AV", "Downtown"),
    ("PRINCE EDWARD ST AND E 65TH AV", "Killarney"),
    ("ST. GEORGE ST AND E 62ND AV", "Killarney"),
    ("FREMLIN ST AND W 71ST AV", "Renfrew-Collingwood"),
    ("W 71ST AV AND SHAUGHNESSY ST", "Marpole"),
]
TEST_GIVEN_LIST2 = [
    ("UnknownType", "Downtown"),
    ("Pedestrian Actuated Signal", "Renfrew-Collingwood"),
    ("Semi Actuated", "Killarney"),
    ("Pedestrian Actuated Signal", "Renfrew-Collingwood"),
    ("Pedestrian Actuated Signal", "Marpole"),
]
HEADERS = ["Area", "Number_signals", "Number_Intersections", "Ratio"]

import unittest
from requests.exceptions import HTTPError
import pandas as pd
import tkinter as tk
from url_request_1 import get_url_from_web
from data_parsed_2 import data_parse, get_attri_lists
from class_intersections_3 import Intersections
from class_traffic_signals_4 import TrafficSignals
from data_analysis_in_objects_5 import (
    get_objects,
    get_locations_from_objects,
    get_types_from_objects,
)
from data_synthesis_6 import (
    get_xticklabels,
    get_count_dictionary,
    data_combine,
    create_data_frame,
)
from GUI_controller_8 import TKinteraction


class ProjectTest(unittest.TestCase):
    """
    A testSimpleFraction is used to test the whole project.
    The class includes 34 test functions, every function is tested by its functionality and errors(if raised). Tested functions range from those get data from website and parsed to those synthesize analytical data structures.
    Descriptions of each function is written above functions.
    Besides, we test the TKinteraction class. We test whether it has required attributes and __str__, __eq__ methods.
    This testcase doesn't include:
    1. matplotlib_method_7
    2. functions in class TKinteraction
    3. Interactions in the dashboard
    """

    # make prepared data and two instance for testing
    def setUp(self):
        self.interstions = Intersections("UnknownStreetName", "DownTown")
        self.signals = TrafficSignals("UnknownType", "Marpole")
        self.test_objects1 = get_objects(TEST_GIVEN_LIST1, Intersections)
        self.test_objects2 = get_objects(TEST_GIVEN_LIST2, TrafficSignals)
        self.test_geo1 = get_locations_from_objects(self.test_objects1)
        self.test_geo2 = get_locations_from_objects(self.test_objects2)
        self.test_type = get_types_from_objects(self.test_objects2)
        self.count_geo1 = get_count_dictionary(self.test_geo1)
        self.count_geo2 = get_count_dictionary(self.test_geo2)
        self.count_type = get_count_dictionary(self.test_type)
        self.root = tk.Tk()
        # hide the window
        self.root.withdraw()
        self.test_visualization = TKinteraction(self.root)

    # test if the function successfuly request data from target website; If the website doesn't exist, report False.
    def test_url(self):
        self.assertTrue(get_url_from_web(DATA_INTERSECTION))
        self.assertTrue(get_url_from_web(DATA_SIGNALS))

    # test if HTTPError happens, ConnectionError are handled in the function, not for test so far
    def test_url_http_error(self):
        with self.assertRaises(HTTPError):
            get_url_from_web(DATA_SIGNALS + "/test_for_project")

    # test if parsed data are stored as lists
    def test_data_parse(self):
        self.assertIsInstance(data_parse(get_url_from_web(DATA_INTERSECTION)), list)
        self.assertIsInstance(data_parse(get_url_from_web(DATA_SIGNALS)), list)

    # test AttributeError in data_parse function
    def test_data_parse_type_error(self):
        with self.assertRaises(AttributeError):
            test_url_signals = []
            data_parse(test_url_signals)
        with self.assertRaises(AttributeError):
            test_url_signals = "format.txt"
            data_parse(test_url_signals)

    # test None content in data_parse function
    def test_data_parse_attri_error(self):
        with self.assertRaises(AttributeError):
            data_parse(None)

    # test if returned data is list(the lists created are not identical to what we used for the project), and each consists of strings.
    def test_get_attri_lists(self):
        attributes_list_intersections = TEST_GIVEN_LIST1
        self.assertIsInstance(attributes_list_intersections, list)
        for i in attributes_list_intersections:
            for j in i:
                self.assertIsInstance(j, str)

        attributes_list_signals = TEST_GIVEN_LIST2
        self.assertIsInstance(attributes_list_signals, list)
        for i in attributes_list_signals:
            for j in i:
                self.assertIsInstance(j, str)

    # test if IndexError in the function raises
    def test_get_attri_index_error(self):
        with self.assertRaises(IndexError):
            get_attri_lists([], 2, 1, 0)

    # test if columns from dataset don't have the same length
    def test_get_attri_value_error(self):
        with self.assertRaises(ValueError):
            get_attri_lists(
                data_parse(get_url_from_web(DATA_INTERSECTION))[0:5], 2, 0, -1
            )
        with self.assertRaises(ValueError):
            get_attri_lists(data_parse(get_url_from_web(DATA_SIGNALS))[0:-1], 3, 2, 0)

    # test if instance of class Intersections has correct attributes
    def test_intersections_init(self):
        self.assertEqual(self.interstions.name, "Intersections")
        self.assertEqual(self.interstions.street_name, "UnknownStreetName")
        self.assertEqual(self.interstions.geo, "DownTown")
        self.assertNotEqual(self.interstions.geo, "West End")

    # test if attributes of the class are strings
    def test_intersections_init_error(self):
        with self.assertRaises(ValueError):
            Intersections(123, [])
        with self.assertRaises(ValueError):
            Intersections({}, 123.00)

    # test if instance of class Intersections output correctly
    def test_class_intersections_print(self):
        self.assertEqual(
            str(self.interstions),
            "The class Intersections has three attributes, Intersections, UnknownStreetName and DownTown.",
        )
        self.assertNotEqual(str(self.interstions), "")

    # test if instances of class Intersections are equal in attributes/methods
    def test_intersections_equal(self):
        self.assertEqual(
            self.interstions == Intersections("UnknownCross", "DownTown"), False
        )
        self.assertEqual(
            self.interstions == Intersections("UnknownStreetName", "DownTown"), True
        )
        self.assertEqual(
            self.interstions == Intersections("UnknownStreetName", "Marpole"), False
        )

    # test if instance of class TrafficSignals has correct attributes
    def test_signals_init(self):
        self.assertEqual(self.signals.name, "Traffic_Signals")
        self.assertEqual(self.signals.signal_type, "UnknownType")
        self.assertEqual(self.signals.geo, "Marpole")
        self.assertNotEqual(self.interstions.geo, "West End")

    # test if attributes of the class are strings
    def test_signals_init_error(self):
        with self.assertRaises(ValueError):
            TrafficSignals(123, [])
        with self.assertRaises(ValueError):
            TrafficSignals("str", 0.00)

    # test if instance of class TrafficSignals output correctly
    def test_class_signals_print(self):
        self.assertEqual(
            str(self.signals),
            "The class TrafficSignals has three attributes, Traffic_Signals, UnknownType and Marpole.",
        )
        self.assertNotEqual(str(self.signals), "")

    # test if instances of class TrafficSignals are equal in attributes/methods
    def test_signals_equal(self):
        self.assertEqual(
            self.signals == TrafficSignals("UnknownType", "DownTown"), False
        )
        self.assertEqual(self.signals == TrafficSignals("UnknownType", "Marpole"), True)
        self.assertEqual(
            self.signals == TrafficSignals("UnknownStreetName", "Marpole"), False
        )

    # test if objects are instantiated successfully
    def test_get_objects(self):
        for each in get_objects(TEST_GIVEN_LIST1, Intersections):
            self.assertIsInstance(each, Intersections)
        for each in get_objects(TEST_GIVEN_LIST2, TrafficSignals):
            self.assertIsInstance(each, TrafficSignals)

    # test if TypeError raises when objects are instantiated by different classes
    def test_get_objects_TypeError(self):
        for item in get_objects(TEST_GIVEN_LIST1, Intersections):
            with self.assertRaises(TypeError):
                self.assertNotIsInstance(
                    get_objects(item, Intersections), TrafficSignals
                )
        for item in get_objects(TEST_GIVEN_LIST2, TrafficSignals):
            with self.assertRaises(TypeError):
                self.assertNotIsInstance(
                    get_objects(item, TrafficSignals), Intersections
                )

    # test if given list of objects can successfuly generate lists of attributes
    def test_get_locations_from_objects(self):
        self.assertIsInstance(self.test_objects1, list)
        self.assertIsInstance(self.test_objects2, list)
        for each in get_locations_from_objects(self.test_objects1):
            self.assertIsNotNone(each)
        for each in get_locations_from_objects(self.test_objects2):
            self.assertIsNotNone(each)

    # test if AttributeError raises if given objects don't have requested attributes
    def test_locations_errors(self):
        objects_intersections = get_objects(TEST_GIVEN_LIST1, Intersections)
        for each in objects_intersections:
            with self.assertRaises(AttributeError):
                each.unknown_attribute
        objects_signals = get_objects(TEST_GIVEN_LIST2, TrafficSignals)
        for each in objects_signals:
            with self.assertRaises(AttributeError):
                each.unknown_attribute

    # test if given list of objects can successfuly generate lists of attributes
    def test_get_type_from_objects(self):
        self.assertIsInstance(self.test_type, list)
        for each in self.test_type:
            self.assertIsNotNone(each)

    # test if AttributeError raises if given objects don't have requested attributes
    def test_type_errors(self):
        objects_signals = get_objects([], TrafficSignals)
        for each in objects_signals:
            with self.assertRaises(AttributeError):
                each.unknown_attribute

    # test if values of the dictionary are integers
    def test_count_dictionary(self):
        for val in get_count_dictionary(TEST_GIVEN_LIST1).values():
            self.assertIsInstance(val, int)
        for val in get_count_dictionary(TEST_GIVEN_LIST2).values():
            self.assertIsInstance(val, int)

    # test if an invalid parameter raises ValueError
    def test_count_dictionary_errors(self):
        with self.assertRaises(ValueError):
            get_count_dictionary(None)

    # test if function successfully generates a list
    def test_get_xticklabels(self):
        self.assertIsNotNone(get_xticklabels(self.count_geo1))
        self.assertIsNotNone(get_xticklabels(self.count_type))

    # test if key of dict is not str
    def test_get_xticklabels_error(self):
        self.count_type[4] = "test_type"
        with self.assertRaises(ValueError):
            get_xticklabels(self.count_type)
        self.count_type[(4)] = "test_type"
        with self.assertRaises(ValueError):
            get_xticklabels(self.count_type)

    # test if the function creates a tuple of lists
    def test_data_combine(self):
        self.assertIsInstance(data_combine(self.count_geo1, self.count_geo2), tuple)
        self.assertEqual(len(data_combine(self.count_geo1, self.count_geo2)), 4)
        for each in data_combine(self.count_geo1, self.count_geo2):
            self.assertIsInstance(each, list)

    # #test if errors are raised in edge cases
    def test_data_combine_type_error(self):
        with self.assertRaises(TypeError):
            data_combine(self.count_type, "")
        with self.assertRaises(TypeError):
            data_combine([], self.count_geo1)
        with self.assertRaises(TypeError):
            data_combine([], self.count_type)

    # test if geo has not been sorted, error happends
    def test_data_combine_value_error(self):
        with self.assertRaises(ValueError):
            self.assertFalse(
                data_combine(
                    {"Downtown": 10, "Sunset": 20},
                    {"Sunset": "new_geo2", "Downtown": "new_geo1"},
                )
            )
        with self.assertRaises(ValueError):
            self.assertFalse(data_combine(self.count_geo1, self.count_type))

    # test if divisor equals zero
    def test_data_combine_divisor_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.count_geo1["DownTown"] = 0
            self.count_geo2["DownTown"] = 1
            data_combine(self.count_geo1, self.count_geo2)
        with self.assertRaises(ZeroDivisionError):
            self.count_geo1["Killarney"] = 0
            data_combine(self.count_geo1, self.count_geo2)

    # test if dataframe could be made
    def test_create_data_frame(self):
        self.assertIsInstance(
            create_data_frame(HEADERS, data_combine(self.count_geo1, self.count_geo2)),
            pd.DataFrame,
        )

    # test if ValueError raises when two pairing lists are not equal in length
    def test_create_data_frame_error(self):
        with self.assertRaises(ValueError):
            create_data_frame([], TEST_GIVEN_LIST2)
        with self.assertRaises(ValueError):
            create_data_frame(TEST_GIVEN_LIST1, [])
        with self.assertRaises(ValueError):
            create_data_frame([HEADERS[0], HEADERS[1]], [])

    # test attributes of Tkinteraction
    # Methods data_derive_xticklabels and data_derive_lists_for_dataframe are used to create applicable lists according to users' choice, functions invoked inside them have been tested
    def test_visualization_init(self):
        self.assertEqual(self.test_visualization.name, "TKinteraction")
        self.assertEqual(
            self.test_visualization.geometry, self.root.geometry("500x400+200+150")
        )
        self.assertEqual(
            self.test_visualization.title,
            self.root.title("Panel of Intersections-Signals"),
        )

    # test if given parameter is callable
    def test_show_each_geo(self):
        with self.assertRaises(AttributeError):
            self.test_visualization.show_each_geo(
                self.test_visualization, "test_botton"
            )

    # test if instance of class TKinteraction output correctly
    def test_class_intersections_print(self):
        # test if information can be printed out
        self.assertEqual(
            str(self.test_visualization),
            "The class TKinteraction is titled as Panel of Intersections-Signals, which occupies a size 500x400+200+150 on the screen. It has methods.",
        )

    # test if instances of class TKinteraction are equal in attributes/methods
    # methods from different instances have different address, therefore not equal, we test if the instances have those objects
    def test_intersections_equal(self):
        self.assertTrue(hasattr(self.test_visualization, "show_numbers"))
        self.assertTrue(hasattr(TKinteraction(self.root), "show_numbers"))
        self.assertTrue(hasattr(self.test_visualization, "show_ratios_in_order"))
        self.assertTrue(hasattr(TKinteraction(self.root), "show_each_geo"))
        self.assertTrue(hasattr(self.test_visualization, "get_option_each_gui"))
        self.assertTrue(hasattr(self.test_visualization, "show_signal_types"))


def main():
    """
    Function -- main
        call the unittest and output test results
    Parameters: None
    Return nothing, but print out test results
    """
    VERBOSITY_LEVEL = 3
    unittest.main(verbosity=VERBOSITY_LEVEL)


if __name__ == "__main__":
    main()
