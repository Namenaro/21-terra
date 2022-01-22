from elinker import ELinker
import uuid
from context import *
from utils import *

class Runner:
    def __init__(self, linker):
        self.linker = linker
        self.sensor = SimpleSensor()

    def reset3(self):
        pic = get_random_pic_of_type(3)
        self.sensor.reset_picture(pic)

    def reset(self):
        self.sensor.reset_picture(etalons_of3()[0])

    def reset_random(self):
        pic = get_random_pic_of_type()
        self.sensor.reset_picture(pic)

    def _run_bsen(self, abspoint, etalon):
        res = self.sensor.measure(abspoint)
        if res == etalon:
            c = Context()
            c.add_point(abspoint)
            return 1, [c]
        else:
            return 0, []

    def run_sen(self, suid, abspoint, etalon):
        if self.linker.is_basic(suid):
            res, contexts=self._run_bsen( abspoint, etalon)
            return res, contexts

        sen = self.linker.get_sen(suid)
        # запускаем первую часть, точка запуска известна
        res1, contexts1 = self.run_sen(sen.suid1, abspoint, sen.etalon1)
        if res1 == 0:
            return 0, []
        # если выполнение первой подпрограммы было успешно, то
        # мы можем запусить вторую, делая ее центром СК одну
        # из точек конктекста, сгенерированного первой подпрограммой :
        result_contexts = []

        if not sen.is_fixed: #floating context point setting
            for context1 in contexts1:
                abspoints2 = sen.act.get_all_variants(context1)
                for abspoint2 in abspoints2:
                    res2, contexts2 = self.run_sen(sen.suid2, abspoint2, sen.etalon2)
                    if res2 == 0: # из этой точки запуск второй подпрограммы не успешен
                        continue
                    for c2 in contexts2:
                        c = merge_2_contexts(context1, c2)
                        result_contexts.append(c)
        else: #fixed context point setting
            for context1 in contexts1:
                abspoints2 = sen.act.get_all_variants(context1)
                c2_from_this_p = []
                for abspoint2 in abspoints2:
                    res2, contexts2 = self.run_sen(sen.suid2, abspoint2, sen.etalon2)
                    if len(contexts2)!=0:
                        c2_from_this_p=c2_from_this_p+contexts2
                if len(c2_from_this_p)>0:
                    #cpoint=sen.act.get_center(context1)
                    #c1new = merge_context_and_point(context1, cpoint)
                    c2mean = mean_contexts(c2_from_this_p)
                    cc = merge_2_contexts(context1, c2mean)
                    result_contexts.append(cc)
        if len(result_contexts) == 0:
            res =0
        else:
            res = 1
        if res == 1 and etalon==1:
            return 1, result_contexts
        if res == 0 and etalon==0:
            return 1, []
        return 0, []

    def run_half2_of_sen(self, suid, abspoint):
        sen = self.linker.get_sen(suid)
        abspoints = sen.act.get_by_abspoint(abspoint)
        cs = []
        for point in abspoints:
            res, contexts = self.run_sen(sen.suid2, point, sen.etalon2 )
            if len(contexts)!=0:
                cs = cs + contexts
        if len(cs)!=0:
            if  sen.is_fixed:
                context = mean_contexts(cs)
                return 1, [context]
            else:
                return 1, contexts
        return 0, []









