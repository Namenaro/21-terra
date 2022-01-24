from event import *
from sampler import *
import numpy as np
import scipy.stats.distributions as dist
from statsmodels.stats.proportion import proportions_ztest

class Evaluator:
    def __init__(self, runner, sen, t_suid, t_act1, t_act2, t_act12):
        self.runner = runner
        self.sen = sen
        self.t_suid = t_suid

        self.t_act1 = t_act1
        self.t_act2 = t_act2
        self.t_act12 = t_act12

        self.sample_by_suid1 = []
        self.sample_by_suid2 = []
        self.sample_by_suid12 = []

        self.n_max_12=10
        self.n_max_1=100
        self.n_max_2=100

    def get_sample_by_suid1(self, n):
        return conditional_sample(self.runner, self.sen.suid1, self.t_suid, self.t_act1, n)

    def get_sample_by_suid2(self, nattempts):
        return conditional_sample_2half_sen(self.runner, self.sen.suid,self.t_suid, self.t_act2,nattempts)

    def get_sample_by_suid12(self,  n):
        return conditional_sample(self.runner, self.sen.suid, self.t_suid, self.t_act12, n)

    def get_sample_s2_c_s1(self, sample_size):
        return measure_p_of_c2act_by_c1(self.runner, self.sen.suid, sample_size)

    def test_2_samples(self, sample1, sample2):
        n1 = sum(sample1)  # кол-во единиц в первой серии
        N1 = len(sample1)  # кол-во бинарных испытаний в первой серии
        n2 =  sum(sample2)  # кол-во единиц во 2й серии
        N2 = len(sample2) # кол-во бинарных испытаний во 2й серии
        counts = np.array([n1, n2])
        nobs = np.array([N1, N2])
        stat, pval = proportions_ztest(counts, nobs)
        return pval

    def check_diff(self, sample1, sample2):
        p11 = self.sample_to_p(sample1)
        p21 = self.sample_to_p(sample2)
        return abs(p11-p21)

    def sample_to_p(self, sample):
        p_of_1 = sum(sample)/len(sample)
        return p_of_1

    def update_samples(self, runner, f1, f2, f12):
        n = 5
        if f1:
            dsample_by_suid1 = self.get_sample_by_suid1(runner, n)
            if len(dsample_by_suid1) != 0:
                self.sample_by_suid1 = self.sample_by_suid1 + dsample_by_suid1
        if f2:
            dsample_by_suid2 = self.get_sample_by_suid2(runner, n)
            if len(dsample_by_suid2) != 0:
                self.sample_by_suid2 = self.sample_by_suid2 + dsample_by_suid2
        if f12:
            dsample_by_suid12 = self.get_sample_by_suid12(runner, n)
            if len(dsample_by_suid12 != 0):
                self.sample_by_suid12 = self.sample_by_suid12 + dsample_by_suid12


    def check_stop_criteria(self):
        flag1 = False
        flag2 = False
        flag12 = False
        if len(self.sample_by_suid1)>=self.n_max_1:
            flag1=True
        if len(self.sample_by_suid2)>=self.n_max_2:
            flag1=True
        if len(self.sample_by_suid12)>=self.n_max_12:
            flag1=True
        return flag1, flag2, flag12



    def eval_significange(self, runner): # 0 - min, no significance
        p_thr = 0.0001

        while True:
            f1,f2,f12 = self.check_stop_criteria()
            if f1 and f2 and f12:
                return 0

            self.update_samples(runner, f1, f2, f12)

            p_1_vs_12 = self.test_2_samples(self.sample_by_suid1, self.sample_by_suid12)
            p_2_vs_12 = self.test_2_samples(self.sample_by_suid2, self.sample_by_suid12)

            if p_1_vs_12 <=p_thr and p_2_vs_12 <=p_thr:
               diff1 = self.check_diff(self.sample_by_suid1, self.sample_by_suid12)
               diff2 = self.check_diff(self.sample_by_suid2, self.sample_by_suid12)
               return diff1 + diff2


