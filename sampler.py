from runner import *
from event import *
from utils import *
from context import *
max_attempts = 50000000

def conditional_sample(runner, suid, suid_etalon, t_suid, t_act, n):
    sample = []
    for i in range(max_attempts):
        if len(sample)==n:
            break
        runner.reset3()  # случайну картинку троцку
        abspoint = get_random_point()
        res, contexts = runner.run_sen(suid, abspoint, suid_etalon)

        if res == 0:
            continue

        for context in contexts:
            abspoint2 = context.get_by_index(t_act.index_in_context)
            res, _ = runner.run_sen(t_suid, abspoint2, None)
            sample.append(res)
    return sample


def conditional_sample_2half_sen(runner, suid, t_suid, t_act, n):
    sample = []

    for i in range(max_attempts):
        if len(sample)==n:
            break
        runner.reset3()  # случайну картинку троцку
        abspoint = get_random_point()
        res, contexts = runner.run_half2_of_sen(suid, abspoint)
        if res == 0:
            continue

        for context in contexts:
            abspoint2 = context.get_by_index(t_act.index_in_context)
            res, _ = runner.run_sen(t_suid, abspoint2, None)
            sample.append(res)
    return sample

def measure_p_of_c2act_by_c1(runner, suid, sample_size):
    sen = runner.linker.get_sen(suid)
    sample = []
    while True:
        if len(sample) == sample_size:
            break
        runner.reset3()  # случайну картинку троцку
        abspoint = get_random_point()
        res, _ = runner.run_sen(sen.suid1, abspoint, sen.etalon1)
        if res == 0:
            continue
        res2, _ = runner.run_sen(suid, abspoint, None)
        sample.append(res2)

    return sum(sample)/len(sample)

def measure_p_of_suid(runner, suid, nattempts):
    sample = []
    for i in range(nattempts):
        runner.reset3()  # случайну картинку троцку
        abspoint = get_random_point()
        res, _ = runner.run_sen(suid, abspoint, None)
        sample.append(res)
    return sum(sample) / len(sample)

