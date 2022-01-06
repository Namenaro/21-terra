SUCCESS =1
FAIL =0

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Context:
    def __init__(self):
        pass
    def add_points(self, points):
        pass

    def add_point(self,point):
        pass

    def get_by_index(self, index):
        pass

    def find_nearest_point(self, point):
        pass

class UCompactSet:
    def __init__(self, dx, dy):
        pass

    def add(self, ddx, ddy):
        #recalc center of u-set
        pass
    def get_center(self):
        return dx,dy

    def make(self, context_point):
        return candidate_points

class EventChecker:
    def __init__(self, etalon):
        self.etalon = etalon

    def check(self, value):
        if value == self.etalon:
            return SUCCESS
        return FAIL

class Sensor:
    def __init__(self):
        pass
    def set_picture(self,picture):
        pass

    def measure(self, point):
        if self.picture[point]>5:
            return 1
        return 0

class Step:
    def __init(self):
        self.action_set # add fixed point or floating points to context
        self.effecter # return contexts!
        self.on_events
        self.is_fixed # either action set center or all points of triggering of on_event


class OnEvent:
    def __init__(self):
        self.event_checker
        self.next_effecter
        self.id_in_context
        self.predictions_corrector

class MergedStep:
    def __init__(self, steps_to_merge):
        pass
















