SUCCESS =1
FAIL =0

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Context:
    def __init__(self):
        pass
    def add_other_context(self, context):
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
        self.step_memorized       # return contexts!
        self.on_events
        self.new_point_is_fixed # either action set center or all points of triggering of on_event


class OnEvent:
    def __init__(self):
        self.uid
        self.event_checker
        self.next_step
        self.index_in_context
        self.predictions_corrector

class MergedStep:
    def __init__(self, steps_to_merge):
        self.steps


def run_pure_recognition(step, point):
    on_event, context = step.get_on_event(point)
    while True:
        top_uid = on_event.uid
        step = on_event.next_step
        if step is None:
            break
        point = context.get_by_index(on_event.index_in_context)
        on_event, new_context = step.get_on_event(point)
        context.add_other_context(new_context)
    return top_uid






















