
from elinker import *
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
linker[elementary_uid]=elementary_event


# FILL EVENT DATA:
# 1. надо статистику активаций p для elementary_event
elementary_event.p = 0.01 # measure_p_for_event(event_uid) собираем выборку 100 пусков евента из случайной точки
# 2. находим нетривиальное предсказание для эвента А
# 2.1. для этого перебирвем ситуации где А=1 и находим рядом с ним yнарушенные предсказания
pic,point =get_random_situation_by_uid(uid=elementary_uid)
points = get_vicinity_of_rad(rad=1, point)
for test_point in points:
    uids_ranged, ps = undirected_recognition_from_point(test_point) #
    for test_uid in uids_ranged:
        hypo_on_prediction = HypoPrediction(test_uid, elementary_uid, shift )
        hypo_on_prediction.evaluate()





# 3. находим след шаг для евента



