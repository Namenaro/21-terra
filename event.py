from elinker import *
from event import *
from utils import *
from predict import *

linker = ELinker()
elementary_sensor = SimpleSensor()

class BasicSen:
    def __init__(self):
        s_uid = linker.generate_uid()
        linker.set_basic(s_uid)

    def run(self, abspoint):
        res = elementary_sensor.measure(abspoint)
        return res

basic_sen = BasicSen()
linker[basic_sen.s_uid] = basic_sen

class Act:
    def __init__(self, shift, du, index_in_context):
        self.shift
        self.du
        self.index_in_context


class Sen:
    def __init__(self, suid1, etalon1, act, suid2, etalon2): #начиннается с сенсора, запускается из abspoint
        self.s_uid = linker.generate_uid()
        self.suid1 = suid1
        self.act = act
        self.next_suid =suid2

        self.etalon1 = etalon1
        self.etalon2 = etalon2
        self.preds = []

class Pred:
    def __init__(self, act, s_uid, corr_p1):
        self.act =act
        self.s_uid = s_uid
        self.corr_p1=corr_p1

some_act = Act(shift= (2,3), du=[[0,0],[0,1]], index_in_context=0)
sen2 = Sen(suid1=basic_sen.s_uid, act= some_act, next_suid=basic_sen.s_uid)
sen3 = Sen(suid1=sen2.s_uid, act=some_act, next_suid=basic_sen.s_uid)
sen4 = Sen(suid1=sen2.s_uid, act=some_act, next_suid=sen3.s_uid)






















