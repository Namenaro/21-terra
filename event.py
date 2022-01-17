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

class Event:
    def __init__(self, uid, event_etalon, parent_exp):
        self.uid = uid
        self.etalon = event_etalon #1 OR 0
        self.next_uid = None
        self.index_in_context = None #
        self.nontrivial_predictions = None

        self.link_to_parent_exp = parent_exp
        self.p = None  # безусловная частота наступления этого события


class MergedEvent:
    def __init__(self, steps_to_merge):
        self.events
        #add cloud to context
