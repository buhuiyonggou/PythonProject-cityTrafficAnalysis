class TrafficSignals:
    """
    A TrafficSignals has three main attributes, in which signal_type and geo will be given when objects instantiate.
    Methods __str__() and __eq__() are also included in the class.
    """

    def __init__(self, signal_type, geo):
        """
        Function -- __init__
            Define attribues of the class
        Parameters:
            -- self, type: instance
            -- signal_type, type: str
            -- geo, type: str
        ErrorRaised: None
        Return Nothing
        """
        self.name = "Traffic_Signals"
        if (not isinstance(signal_type, str)) or (not isinstance(geo, str)):
            raise ValueError("Attributes of TrafficSignals have to be str")
        self.signal_type = signal_type
        self.geo = geo

    def __str__(self):
        """
        Function -- __str__
            Print out instances
        Parameters:
            -- self, type: instance
        ErrorRaised: None
        Return output, a string presentation
        """
        output = f"The class TrafficSignals has three attributes, {self.name}, {self.signal_type} and {self.geo}."

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
        if isinstance(other, TrafficSignals):
            if (self.geo == other.geo) and (self.signal_type == other.signal_type):
                return True
            else:
                return False
        else:
            return False
