LABEL_TEXT1 = "Please choose a type of data"
LABEL_TEXT2 = "Please choose a geo-area"
FRAME_TEXT1 = "Data Overall"
FRAME_TEXT2 = "Data Specific"
LABEL_FONT = ("Arial", 16, "bold")
NOTEBOOK_SIZE = 400
TEXT_BOTTON1 = "Number of Intersections-Signals"
TEXT_BOTTON2 = "Ratio of Intersections-Signals"
TEXT_BOTTON3 = "Types of Signals"
BIND_METHOD = "<<ComboboxSelected>>"
WIDTH = 20
PADDING = 20
EXIT_TEXT = "Exit"

import tkinter as tk
from tkinter import ttk
from GUI_controller_8 import TKinteraction
from requests.exceptions import HTTPError


def main():
    """
    Function -- main
        Driver of the GUI module and request response from the controller
    Parameters: None
    Return Nothing
    """
    try:
        root = tk.Tk()
        visualization = TKinteraction(root)
        # create a notebook and two frames as the panel
        notebook = ttk.Notebook(root)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)

        tk.Label(frame1, text=LABEL_TEXT1, font=LABEL_FONT).pack()
        tk.Label(frame2, text=LABEL_TEXT2, font=LABEL_FONT).pack()
        notebook.add(frame1, text=FRAME_TEXT1)
        notebook.add(frame2, text=FRAME_TEXT2)
        notebook.config(width=NOTEBOOK_SIZE, height=NOTEBOOK_SIZE)
        notebook.pack()
        # display the entire dataframe
        visualization.show_data_frame()

        botton1 = ttk.Button(
            frame1,
            text=TEXT_BOTTON1,
            width=WIDTH,
            padding=PADDING,
            command=visualization.show_numbers,
        )
        botton1.pack()

        botton2 = ttk.Button(
            frame1,
            text=TEXT_BOTTON2,
            width=WIDTH,
            padding=PADDING,
            command=visualization.show_ratios_in_order,
        )
        botton2.pack()

        botton3 = ttk.Button(
            frame1,
            text=TEXT_BOTTON3,
            width=WIDTH,
            padding=PADDING,
            command=visualization.show_signal_types,
        )
        botton3.pack()

        # use combox button to display graphs based on users' click
        select_geo_area = tk.StringVar()
        botton4 = ttk.Combobox(
            frame2, textvariable=select_geo_area, width=WIDTH, height=PADDING
        )
        xticklabels = visualization.xticklabels_for_combobox()
        botton4.config(value=xticklabels)
        botton4.bind(
            BIND_METHOD, lambda event: visualization.show_each_geo(xticklabels, botton4)
        )
        botton4.pack()

        exit_button1 = ttk.Button(
            frame1, text=EXIT_TEXT, width=WIDTH, padding=PADDING, command=root.destroy
        )
        exit_button1.pack()

        exit_button2 = ttk.Button(
            frame2, text=EXIT_TEXT, width=WIDTH, padding=PADDING, command=root.destroy
        )
        exit_button2.pack()

        root.mainloop()

    # test if client servers have problems
    except HTTPError as error_http:
        print(type(error_http), error_http)
    # test if reading the file is interrupted
    except InterruptedError as error_interruption:
        print(type(error_interruption), error_interruption)
    # test if there are other os errors
    except OSError as error_os:
        print(type(error_os), error_os)
    # test if variable bounded
    except UnboundLocalError as error_unbound:
        print(type(error_unbound), error_unbound)
    # test if name correct
    except NameError as error_name:
        print(type(error_name), error_name)
    # test if index exceeded the range
    except IndexError as error_index:
        print(type(error_index), error_index)
    # test if object matches dictionary
    except AttributeError as error_attribute:
        print(type(error_attribute), error_attribute)
    # test if there is a dictionary instead of other data structures
    except TypeError as error_type:
        print(type(error_type), error_type)
    # test if value available
    except ValueError as error_value:
        print(type(error_value), error_value)
    except Exception as error_exception:
        print(type(error_exception), error_exception)


if __name__ == "__main__":
    main()
