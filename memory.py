

from copy import copy
import uuid

class ELinker:
    def __init__(self):
        self.d = {}
        self.nd = {}
        self.first_lavel_uids ={}

    def generate_uid(self):
        return uuid.uuid4()

    def get_unconditional_p(self,uid):
        return p,1-p

    def __getitem__(self, uid):
        return self.d[uid], self.nd[uid]

    def __setitem__(self, uid, event, nevent):
        self.d[uid]= event
        self.nd[uid] = nevent

    def get_first_level_uids(self):
        return self.first_lavel_uids



































