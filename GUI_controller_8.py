DATA_INTERSECTION = "https://opendata.vancouver.ca/explore/dataset/street-intersections/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
DATA_SIGNALS = "https://opendata.vancouver.ca/explore/dataset/traffic-signals/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
HEADERS = ["Area", "Number_signals", "Number_Intersections", "Ratio"]
LABEL_N = "Numbers of Signals - Intersections in geo-areas"
LABEL_R = "Ratio of Signals - Intersections in geo-areas"
TOTAL_COLUMN_INTERSECTIONS = 5
GET_STREET_INTERSECTIONS = 2
GET_LOCATION_INTERSECTIONS = 4
TOTAL_COLUMN_SIGNALS = 3
GET_TYPE_SIGNALS = 0
GET_LOCATION_SIGNALS = 2
HEADERS_LENGTH_TEST = 2
PIE_CHART_ELEMENTS_DISPLAY = 4
GEOMETRY = "500x400+200+150"
ROOT_TITLE = "Panel of Intersections-Signals"
ADD_SIGNAL_TYPE = "Others"

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
from matplotlib_method_7 import (
    make_bar_graph_from_dictionary,
    make_bar_graph_from_data_frame,
    make_pie_chart_from_list,
)


class TKinteraction:
    """
    Class TKinteraction has several attributes, in which master is the root of instance, geometry is used for setting the size of the panel, and title is assigned by given descriptions
    Also, we store some pre-loaded data from websites to increase efficiency, but each method captures required data to create data strucutes and display graphs.
    Class TKinteraction has 8 methods, each of them derives a certain type of data structure and is called in the dashboard_GUI.
    Methods data_derive_xticklabels and data_derive_lists_for_dataframe are used to create applicable lists according to users' choice, functions invoked inside them have been tested
    Methods __str__() and __eq__() are also included in the class.
    """

    def __init__(self, master):
        """
        Function -- __init__
            Define attribues of the class
        Parameters:
            -- self, type: object
            -- master, type: object
        ErrorRaised: None
        Return Nothing
        """
        self.name = "TKinteraction"
        self.master = master
        self.geometry = master.geometry(GEOMETRY)
        self.title = master.title(ROOT_TITLE)
        # store pre-loaded data and create objects
        self.get_url_intersections = get_url_from_web(DATA_INTERSECTION)
        self.get_url_signals = get_url_from_web(DATA_SIGNALS)
        self.parsed_intersections = data_parse(self.get_url_intersections)
        self.parsed_signals = data_parse(self.get_url_signals)
        self.attri_intersections = get_attri_lists(
            self.parsed_intersections,
            TOTAL_COLUMN_INTERSECTIONS,
            GET_STREET_INTERSECTIONS,
            GET_LOCATION_INTERSECTIONS,
        )
        self.attri_signals = get_attri_lists(
            self.parsed_signals,
            TOTAL_COLUMN_SIGNALS,
            GET_TYPE_SIGNALS,
            GET_LOCATION_SIGNALS,
        )
        self.instances_intersections = get_objects(
            self.attri_intersections, Intersections
        )
        self.instances_signals = get_objects(self.attri_signals, TrafficSignals)

    def xticklabels_for_combobox(self):
        """
        Function -- xticklabels_for_combobox
            Create xticklabels_for_combobox
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return xticklabels_geo, based on description of geo
        """
        attri_intersections_geo = get_locations_from_objects(
            self.instances_intersections
        )
        get_dictionanry_intersections_geo = get_count_dictionary(
            attri_intersections_geo
        )
        xticklabels_geo = get_xticklabels(get_dictionanry_intersections_geo)

        return xticklabels_geo

    def show_data_frame(self):
        """
        Function -- show_data_frame
            Create and display dataframe with geo_areas from two classes
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return nothing, but display the entire dataframe as interaction
        """
        attri_intersections_geo = get_locations_from_objects(
            self.instances_intersections
        )
        attri_signals_geo = get_locations_from_objects(self.instances_signals)
        get_dictionanry_intersections_geo = get_count_dictionary(
            attri_intersections_geo
        )
        get_dictionanry_signals_geo = get_count_dictionary(attri_signals_geo)

        lists_for_data_frame = data_combine(
            get_dictionanry_intersections_geo, get_dictionanry_signals_geo
        )
        print(create_data_frame(HEADERS, lists_for_data_frame))

    def show_numbers(self):
        """
        Function -- show_numbers
            As the first choice in the dashboard
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return nothing, but display a bar chart of geo_area, number of intersections, and that of signals from dataframe, which is specified based on users' choice
        """
        attri_intersections_geo = get_locations_from_objects(
            self.instances_intersections
        )
        attri_signals_geo = get_locations_from_objects(self.instances_signals)
        get_dictionanry_intersections_geo = get_count_dictionary(
            attri_intersections_geo
        )
        get_dictionanry_signals_geo = get_count_dictionary(attri_signals_geo)
        xticklabels_geo = get_xticklabels(get_dictionanry_intersections_geo)

        lists_for_data_frame = data_combine(
            get_dictionanry_intersections_geo, get_dictionanry_signals_geo
        )

        # we use the first three headers for the dataframe and gragh, excluding ratio
        make_data_frame = create_data_frame((HEADERS[:-1]), (lists_for_data_frame[:-1]))
        make_bar_graph_from_data_frame(make_data_frame, xticklabels_geo, LABEL_N)

    def show_ratios_in_order(self):
        """
        Function -- show_ratios_in_order
            As the second choice in the dashboard
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return nothing, but display a bar chart of geo_area and ratio in a reverse order from dataframe, which is specified based on users' choice
        """
        attri_intersections_geo = get_locations_from_objects(
            self.instances_intersections
        )
        attri_signals_geo = get_locations_from_objects(self.instances_signals)
        get_dictionanry_intersections_geo = get_count_dictionary(
            attri_intersections_geo
        )
        get_dictionanry_signals_geo = get_count_dictionary(attri_signals_geo)

        lists_for_data_frame = data_combine(
            get_dictionanry_intersections_geo, get_dictionanry_signals_geo
        )
        new_dict = dict(
            zip(
                lists_for_data_frame[HEADERS.index(HEADERS[0])],
                lists_for_data_frame[HEADERS.index(HEADERS[-1])],
            )
        )

        # sort dictionary based on values
        lists_sorted = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
        name_ordered = []
        ratio_ordered = []
        for i in range(len(lists_sorted)):
            name_ordered.append(lists_sorted[i][0])
            ratio_ordered.append(lists_sorted[i][1])
        make_data_frame = create_data_frame(
            ([HEADERS[0], HEADERS[-1]]), (name_ordered, ratio_ordered)
        )
        make_bar_graph_from_data_frame(make_data_frame, name_ordered, LABEL_R)

    def show_signal_types(self):
        """
        Function -- show_signal_types
            As the third choice in the dashboard
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return nothing, but display a pie chart of signal types its numbers, which is specified based on users' choice
        """
        attri_signals_types = get_types_from_objects(self.instances_signals)
        get_dict_signal_types = get_count_dictionary(attri_signals_types)
        # sort dictionary based on values
        new_dict = dict(
            zip(get_dict_signal_types.keys(), get_dict_signal_types.values())
        )
        lists_sorted = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
        signal_type = []
        signal_number = []
        # get the first largest 4 percentages and their corresponding types
        for i in range(len(lists_sorted[:PIE_CHART_ELEMENTS_DISPLAY])):
            signal_type.append(lists_sorted[i][0])
            signal_number.append(lists_sorted[i][1])
        # count the rest signals types
        count = 0
        for each in lists_sorted[PIE_CHART_ELEMENTS_DISPLAY:]:
            count += each[1]
        # append the extra string "others" and its number to lists
        signal_number.append(count)
        signal_type.append(ADD_SIGNAL_TYPE)
        make_pie_chart_from_list(signal_type, signal_number)

    def get_option_each_gui(self, lists_for_data_frame, given_xticklabels, choice):
        """
        Function -- show_signal_types
            As the a combobox choice in the dashboard
        Parameters:
            -- self, type: instance
            -- lists_for_data_frame, type: list
            -- given_xticklabels, type: list
            -- choice, type: str
        ErrorRaised:
            -- ValueError, notifiy if the headers has less columns than those are required for creating dataframe
        Return nothing, but display a pie chart of signal types its numbers, which is specified based on users' choice
        """
        geo_index = given_xticklabels.index(choice)
        make_data_frame = create_data_frame(HEADERS, lists_for_data_frame)
        get_target_list = make_data_frame.iloc[geo_index].values.tolist()
        target_dict = dict()
        for i in range(1, (len(HEADERS) - 1)):
            target_dict[HEADERS[i]] = get_target_list[i]
        make_bar_graph_from_dictionary(
            target_dict, self.xticklabels_for_combobox()[geo_index]
        )

    def show_each_geo(self, event, botton):
        """
        Function -- show_each_geo
            A help function that capture user's click and give corresponding content to activate graphs
        Parameters:
            -- self, type: instance
            -- event, type: instance, for binding event to combobox
            -- botton, type: instance, pinpoint the instance of botton
        ErrorRaised:
            -- AttributeError: test if given paramter is callable
        Return nothing, but get the content of each combobox, from which corresponding bar chart is invoked
        """
        attri_intersections_geo = get_locations_from_objects(
            self.instances_intersections
        )
        attri_signals_geo = get_locations_from_objects(self.instances_signals)
        get_dictionanry_intersections_geo = get_count_dictionary(
            attri_intersections_geo
        )
        get_dictionanry_signals_geo = get_count_dictionary(attri_signals_geo)

        xticklabels = get_xticklabels(get_dictionanry_intersections_geo)
        lists_for_data_frame = data_combine(
            get_dictionanry_intersections_geo, get_dictionanry_signals_geo
        )
        # catch the content of combobox
        if not hasattr(botton, "get"):
            raise AttributeError(
                "Error happens in show_each_geo(). Given botton has no required attribute."
            )
        click_content = botton.get()
        self.get_option_each_gui(lists_for_data_frame, xticklabels, click_content)

    def __str__(self):
        """
        Function -- __str__
            Print out instances
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return output, a string presentation
        """
        output = f"The class {self.name} is titled as {ROOT_TITLE}, which occupies a size {GEOMETRY} on the screen. It has methods."
        return output

    def __eq__(self, other):
        """
        Function -- divide
            Test if object, attributes or functions of instances are equal
        Parameters:
            -- self, type: instance
            -- other: type: instance
        ErrorRaised: None
        Return None
        """
        if isinstance(other, TKinteraction):
            if (
                (self.xticklabels_for_combobox == other.xticklabels_for_combobox)
                and (self.show_numbers == other.show_numbers)
                and (self.show_ratios_in_order == other.show_ratios_in_order)
                and (self.show_each_geo == other.show_each_geo)
                and (self.get_option_each_gui == other.get_option_each_gui)
                and (self.show_signal_types == other.show_signal_types)
            ):
                return True
            else:
                return False
        else:
            return False
