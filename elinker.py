from copy import copy
import uuid

class ELinker:
    def __init__(self):
        self.events = {}
        self.basic = None

    def generate_uid(self):
        return uuid.uuid4()

    def set_basic(self, s_uid):
        self.basic = s_uid

    def is_basic(self,s_uid):
        if s_uid == self.basic:
            return True
        return False

    def __getitem__(self, uid):
        return self.events[uid]

    def __setitem__(self, uid, event):
        self.events[uid]= event




































