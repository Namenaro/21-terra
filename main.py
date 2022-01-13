
from memory import *
from exp import *
from event import *

linker = ELinker()
elementary_sensor = SimpleSensor()


elementary_uset = USet()
elementary_exp = Exp(elementary_uset)
elementary_uid = linker.generate_uid()
elementary_event = Event(uid=elementary_uid, event_etalon=1, parent_exp=elementary_exp)

