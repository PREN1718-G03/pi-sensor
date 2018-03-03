class TargetModel(object):
    """\
    Model for the target platform in PREN02 2018 HSLU
    """
    def __init__(self):
        self.target_found = False
        self.polygons = []
        self.distance = None

    def __init__(self, target_found, polygons, distance):
        """\
        Initialise the Target with attributes

        Keyword arguments:
            target_found Boolean -- Was the target recognized
            polygons List -- List with polygons determined to be the target platform
            distance Float -- Calculated distance from sensor to target platform
        """
        self.__init__()
        if isinstance(target_found, bool):
            self.target_found = target_found
        else:
            raise TypeError('target_found not of type boolean')
        if isinstance(polygons, list):
            self.polygons = polygons
        else:
            raise TypeError('polygons not of type list')
        if isinstance(distance,float):
            self.distance = distance
        else:
            raise TypeError('distance not of type float')
