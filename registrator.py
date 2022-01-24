
class Registrator:
    def __init__(self):
        self.is_on=False
        self.map = {} # point -> [suid, ...]

    def register(self, suid, abspoint):
        if not self.is_on:
            return
        if (abspoint.x, abspoint.y) not in self.map:
            self.map[(abspoint.x, abspoint.y)]=[suid]
        else:
            self.map[(abspoint.x, abspoint.y)].append(suid)

    def clean(self):
        self.map = {}

    def is_trivial(self, suid, abspoint):
        if (abspoint.x, abspoint.y) not in self.map:
            return False
        if suid not in self.map[(abspoint.x, abspoint.y)]:
            return False
        return True

    def filter_trivials_from_list(self,suids):
        return suids








