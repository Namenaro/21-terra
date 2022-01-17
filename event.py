
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
