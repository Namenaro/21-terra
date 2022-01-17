from copy import copy
import uuid

class ELinker:
    def __init__(self):
        self.events = {}

    def generate_uid(self):
        return uuid.uuid4()

    def __getitem__(self, uid):
        return self.events[uid]

    def __setitem__(self, uid, event):
        self.events[uid]= event




































