ALIGN = "center"
STARTANGLE = 90
AXIS = "equal"
GRAPH = "bar"
AUTOPCT = "%1.1f%%"
FIG_SIZE = (9, 6)
PIE_TEXT = "Percentages of signal types"
BAR_FORMAT_SINGLE = "%.0f"
FONT_SIZE_SINGE = 12
HA = "center"
VA = "bottom"


import matplotlib.pyplot as plt


def make_bar_graph_from_dictionary(dictn1, title):
    """
    Function -- make_bar_graph_from_dictionary
        Generate a bar graph from dictionary
    Parameters:
        -- dictn1, type: dictionary
        -- title, type: str
    ErrorRaised: None
    Return nothing but display a bar graph
    """
    plt.bar(range(len(dictn1)), list(dictn1.values()), align=ALIGN)
    plt.xticks(range(len(dictn1)), list(dictn1.keys()))
    plt.title(title)
    # give text to each bar
    for i in range(len(dictn1)):
        plt.text(
            i,
            dictn1[list(dictn1.keys())[i]],
            BAR_FORMAT_SINGLE % dictn1[list(dictn1.keys())[i]],
            ha=HA,
            va=VA,
            fontsize=FONT_SIZE_SINGE,
        )
    plt.show()


def make_bar_graph_from_data_frame(df1, xticklabels, title):
    """
    Function -- make_bar_graph_from_data_frame
        Generate a bar graph from dataframe
    Parameters:
        -- df1, type: dictionary
        -- xticklabels, type: list
        -- title, type: str
    ErrorRaised: None
    Return nothing but display a bar graph
    """
    figure1, ax1 = plt.subplots(figsize=FIG_SIZE)
    graph = df1.plot(kind=GRAPH, legend=True, ax=ax1)
    ax1.set_xticklabels(xticklabels)
    ax1.set_title(title)
    figure1.autofmt_xdate()
    plt.show()


def make_pie_chart_from_list(labels, sizes):
    """
    Function -- make_pie_chart_from_list
        Generate a pie graph from two given lists
    Parameters:
        -- labels, type: list
        -- sizes, type: list
    ErrorRaised: None
    Return nothing but display a pie graph
    """
    fig1, ax1 = plt.subplots(figsize=FIG_SIZE)
    ax1.pie(
        sizes,
        labels=labels,
        autopct=AUTOPCT,
        shadow=True,
        startangle=STARTANGLE,
        radius=0.5,
    )
    ax1.set(title=PIE_TEXT)
    ax1.axis(AXIS)
    plt.show()
