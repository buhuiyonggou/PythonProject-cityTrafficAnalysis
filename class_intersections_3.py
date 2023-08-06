class Intersections:
    '''
    A Intersections has three main attributes, in which street_name and geo will be given when objects instantiate.
    Methods __str__() and __eq__() are also included in the class.
    '''
    def __init__(self, street_name, geo):
        '''
        Function -- __init__
            Define attribues of the class
        Parameters: 
            -- self, type: instance
            -- street_name, type: str
            -- geo, type: str
        ErrorRaised: None
        Return Nothing
        '''
        self.name = "Intersections"
        if (not isinstance(street_name, str)) or (not isinstance(geo, str)):
            raise ValueError("Attributes of Intersections have to be str")
        self.street_name = street_name
        self.geo = geo
    
    def __str__(self):
        '''
        Function -- __str__
            Print out instances
        Parameters: 
            -- self, type: instance
        ErrorRaised: None
        Return output, a string presentation 
        '''
        output = f"The class Intersections has three attributes, {self.name}, {self.street_name} and {self.geo}."
        
        return output

    def __eq__(self, other):
        '''
        Function -- divide
            Test if object, attributes or functions of instances are equal
        Parameters: 
            -- self, type: instance
            -- other: type: object
        ErrorRaised: None
        Return None
        '''
        if isinstance(other, Intersections):
            if (self.geo == other.geo) and (self.street_name == other.street_name):
                return True
            else:
                return False
        else:
            return False  
