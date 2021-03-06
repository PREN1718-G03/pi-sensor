class TargetModel(object):
    """\
    Model for the target platform in PREN02 2018 HSLU
    """

    def __init__(self, target_found=False, contours=[], distance=None):
        """\
        Initialise the Target with attributes

        Keyword arguments:
            target_found Boolean -- Was the target recognized
            polygons List -- List with polygons determined to be the target platform
            distance Float -- Calculated distance from sensor to target platform
        """

        if isinstance(target_found, bool):
            self.target_found = target_found
        else:
            raise TypeError('target_found ' + str(type(target_found)) + ' not of type boolean')
        if isinstance(contours, list):
            self.contours = contours
        else:
            raise TypeError('contours ' + str(type(contours)) + ' not of type list')
        if isinstance(distance,float):
            self.distance = distance
        else:
            self.distance = None
