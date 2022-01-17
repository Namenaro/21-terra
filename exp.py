class Exp:
    def __init(self, uset, sensor_exp="simple_sensor", parent_event_uid=None):
        self.uset = uset
        self.sensor_exp = sensor_exp

        self.tru_event_uid = None
        self.tru_uid_users = []

        self.false_event_uid = None
        self.false_uid_users = []

        self.is_floating = False

        self.parent_event_uid = parent_event_uid



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



