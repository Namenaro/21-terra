
from memory import *
from exp import *
from event import *

linker = ELinker()
elementary_sensor = SimpleSensor()

#элементарный эксперимент - хардкодим
elementary_uset = USet()
elementary_exp = Exp(elementary_uset)

# элементарное событие - хардкодим
elementary_uid = linker.generate_uid()
elementary_event = Event(uid=elementary_uid, event_etalon=1, parent_exp=elementary_exp) # by Ilia
# FILL EVENT DATA:
# 1. надо статистику активаций p для elementary_event
elementary_event.p = 0.01 # measure_p_for_event(event_uid) собираем выборку 100 пусков евента из случайной точки
# 2. находим нетривиальные предсказания для эвента
# 3. находим след шаг для евента



