
class Event:
    def __init__(self, uid, event_etalon, parent_exp):
        self.uid = uid
        self.event_etalon = event_etalon
        self.next_exp = None
        self.index_in_context = None
        self.nontrivial_predictions = None

        self.link_to_parent_exp = parent_exp