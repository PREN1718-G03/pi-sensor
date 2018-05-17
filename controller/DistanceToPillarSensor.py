from controller.UltraSonicSensor import UltraSonicSensor


class DistanceToPillarSensor(UltraSonicSensor):
    def __init__(self):
        super(DistanceToPillarSensor, self).__init__(5, 6)

    def measure(self):
        return super(DistanceToPillarSensor, self).measure()

    def get_distance(self):
        measurement1 = self.measure()
        measurement2 = self.measure()
        measurement3 = self.measure()
        if measurement1 is None or measurement2 is None or measurement3 is None:
            average = None
        else:
            average = (measurement1 + measurement2 + measurement3) / 3
        return average

    def close(self):
        super(DistanceToPillarSensor, self).close()
