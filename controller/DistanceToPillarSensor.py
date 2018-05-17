from controller.UltraSonicSensor import UltraSonicSensor


class DistanceToPillarSensor(UltraSonicSensor):
    def __init__(self):
        super(DistanceToPillarSensor, self).__init__(5, 6)

    def get_distance(self):
        measurement1 = self.measure()
        measurement2 = self.measure()
        measurement3 = self.measure()
        average = (measurement1 + measurement2 + measurement3) / 3
        return average

    def close(self):
        super(DistanceToPillarSensor, self).close()
