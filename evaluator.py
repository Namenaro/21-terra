from event import *

import numpy as np
import scipy.stats.distributions as dist

class Evaluator:
    def __init__(self, sen, t_suid, t_etalon, t_act, t_index):
        self.sen = sen
        self.t_suid = t_suid
        self.t_etalon = t_etalon
        self.t_act = t_act
        self.t_index = t_index

        self.sample_by_suid1 = []
        self.sample_by_suid2 = []
        self.sample_by_suids12 = []

        self.n_max_12=10
        self.n_max_1=100
        self.n_max_2=100

    def get_sample_by_suid1(self,runner, nattempts):
        pass

    def get_sample_by_suid2act(self, runner, nattempts):
        pass

    def get_sample_by_suids12(self, runner, nattempts):
        pass

    def get_sample_s2_c_s1(self):
        pass

    def test_2_samples(self, sample1, sample2):
        return p_val

    def check_diff(self, sample1, sample2):
        return diff

    def sample_to_p(self, sample):
        pass

    def update_samples(self, runner, f1, f2, f12):
        nattempts = 400
        if f1:
            dsample_by_suid1 = self.get_sample_by_suid1(runner, nattempts)
        if f2:
            dsample_by_suid2 = self.get_sample_by_suid2(runner, nattempts)
        if f12:
            dsample_by_suid12 = self.get_sample_by_suids12(runner, nattempts)

        if len(dsample_by_suid1)!=0:
            self.sample_by_suid1 = self.sample_by_suid1 + dsample_by_suid1
        if len(dsample_by_suid2)!=0:
            self.sample_by_suid2 = self.sample_by_suid2 + dsample_by_suid2
        if len(dsample_by_suid12!=0):
            self.sample_by_suid12 = self.sample_by_suid12 + dsample_by_suid12

    def check_stop_criteria(self):
        flag1 = False
        flag2 = False
        flag12 = False
        if len(self.sample_by_suid1)>=self.self.n_max_1:
            flag1=True
        if len(self.sample_by_suid2)>=self.self.n_max_2:
            flag1=True
        if len(self.sample_by_suid12)>=self.self.n_max_12:
            flag1=True
        return flag1, flag2, flag12



    def eval_significange(self, runner): # 0 - min, no significance
        p_thr = 0.0001

        while True:
            f1,f2,f12 = self.check_stop_criteria()
            if f1 and f2 and f12:
                return 0

            self.update_samples(runner, f1, f2, f12)

            p_1_vs_12 = self.test_2_samples(self.sample_by_suid1, self.sample_by_suids12)
            p_2_vs_12 = self.test_2_samples(self.sample_by_suid2, self.sample_by_suids12)

            if p_1_vs_12 <=p_thr and p_2_vs_12 <=p_thr:
               diff1 = self.check_diff(self.sample_by_suid1, self.sample_by_suids12)
               diff2 = self.check_diff(self.sample_by_suid2, self.sample_by_suids12)
               return diff1 + diff2
