
class Registrator:
    def __init__(self):
        self.is_on=False
        self.map = {} # point -> [suid, ...]

    def register(self, suid, abspoint):
        if not self.is_on:
            return
        if abspoint not in self.map:
            self.map[abspoint]=[suid]
        else:
            self.map[abspoint].append(suid)

    def is_trivial(self, suid, abspoint):
        if abspoint not in self.map:
            return False
        if suid not in self.map[abspoint]:
            return False
        return True








