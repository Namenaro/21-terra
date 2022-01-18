from elinker import *
from event import *
from utils import *
from predict import *


class Act:
    def __init__(self, dx, dy, index_in_context):
        self.dx = dx
        self.dy = dy
        self.ddxs = [0]
        self.ddys = [0]
        self.index_in_context = index_in_context

    def get_all_variants(self, context):
        abspoint = context.get_by_index(self.index_in_context)
        cx = abspoint.x + self.dx
        cy = abspoint.y + self.dy
        several_abspoints = []
        for i in range(len(self.ddxs)):
            x=cx+ self.ddxs[i]
            y=cy + self.ddys[i]
            several_abspoints.append(Point(x,y))
        return several_abspoints


class Sen:
    def __init__(self, suid, suid1, etalon1, act, suid2, etalon2):  # начиннается с сенсора, запускается из abspoint
        self.s_uid = suid
        self.suid1 = suid1
        self.act = act

        self.next_suid = suid2

        self.etalon1 = etalon1
        self.etalon2 = etalon2
        self.preds = []
        self.is_fixed = True


class Pred:
    def __init__(self, act, s_uid, corr_p1):
        self.act = act
        self.s_uid = s_uid
        self.corr_p1 = corr_p1


some_act = Act(shift=(2, 3), du=[[0, 0], [0, 1]], index_in_context=0)
sen2 = Sen(suid1=basic_sen.s_uid, act=some_act, next_suid=basic_sen.s_uid)
sen3 = Sen(suid1=sen2.s_uid, act=some_act, next_suid=basic_sen.s_uid)
sen4 = Sen(suid1=sen2.s_uid, act=some_act, next_suid=sen3.s_uid)
