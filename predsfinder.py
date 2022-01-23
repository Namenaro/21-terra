from sampler import *
# для данного тестового сен найдем разные ентривиальные предсказания и замерим их суммарную силу

class PredEntry:
    def __init__(self):
        self.suid
        self.act
        self.p=None

class PredsFinder:
    def __init__(self, sen, runner):
        self.runner=runner
        self.sen = sen
        self.preds = []  #[pred_entry1,...]
        self.num_attempts_allowed=5

    def run(self):
        res = 0
        for i in range(self.num_attempts_allowed):
            res_i = self.find_next_pred()
            res+=res_i

        p_of_s2 = measure_p_of_c2act_by_c1(self.runner, self.sen.s_uid, sample_size=20)
        return res, p_of_s2


    def find_rare_nontrivial(self, registrator):
        return suid, abspoint

    def create_act(self, suid, abspoint, context, registrator):
        # эвристика1 - чем больше дист, тем больше радиус неопределенности
        # эври 2: неопредленность это компакт
        # эври 3: чем больше редкое событие, тем больше радиус
        return acts


    def find_next_pred(self, registrator):

        self.runner.reset3()
        registrator.is_on=True



    def visualise_preds(self):
        #finf sen=1 pic, show it and all acts from preds
        pass

