from runner import *
from event import *
from utils import *
from context import *

def conditional_sample(runner, suid, t_suid, t_act, nattempts):
    sample=[]
    for i in range(nattempts):
        runner.reset3() # случайну картинку троцку
        abspoint = get_random_point()
        res, contexts = runner.run_sen(suid, abspoint)
        if res == 0:
            continue

        for context in contexts:
            abspoint2=context.get_by_index(t_act.index_in_context)
            res, _= runner.run_sen(t_suid, abspoint2)
            sample.append(res)

def conditional_sample_2half_sen(runner, suid, t_suid, t_act, nattempts)
    sample = []
    for i in range(nattempts):
        runner.reset3()  # случайну картинку троцку
        abspoint = get_random_point()
        res, contexts = runner.run_half2_of_sen(suid,abspoint)
        if res == 0:
            continue

        for context in contexts:
            abspoint2=context.get_by_index(t_act.index_in_context)
            res, _= runner.run_sen(t_suid, abspoint2)
            sample.append(res)