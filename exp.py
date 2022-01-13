class Exp:
    def __init(self, uset, sensor_exp="simple_sensor", parent_event_uid=None):
        self.uset = uset
        self.sensor_exp = sensor_exp

        self.event_uid = None
        self.tru_uid_users = []
        self.false_uid_users = []

        self.is_floating = False

        self.parent_event_uid = parent_event_uid

class SimpleSensor:
    def __init__(self):
        pass
    def set_picture(self,picture):
        pass

    def measure(self, point):
        if self.picture[point]>5:
            return 1
        return 0

class USet:
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        self.ddxs=[0]
        self.ddys=[0]

    def add(self, ddx, ddy):
        self.ddxs.append(ddx)
        self.ddys.append(ddy)
        self.dx=
        self.dy=

    def get_center(self):
        return self.dx, self.dy

    def get_all_actions(self, point):
        return all_actions



