from elinker import ELinker
import uuid
from context import *
from utils import *

class Runner:
    def __init__(self, linker):
        self.linker = linker
        self.sensor = SimpleSensor()

    def _run_bsen(self, abspoint, etalon):
        res = self.sensor.measure(abspoint)
        if res == etalon:
            c = Context()
            c.add_point(abspoint)
            return 1, [c]
        else:
            return 0, []

    def run_sen(self, suid, abspoint, etalon=None):
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
        for context1 in contexts1:
            abspoints2 = sen.act.get_all_variants(context1)
            for abspoint2 in abspoints2:
                res2, contexts2 = self.run_sen(sen.suid2, abspoint2, sen.etalon2)
                if res2 == 0: # из этой точки запуск второй подпрограммы не успешен
                    continue
                # один или несколько пуской второй подпрограммы были успешны
                if sen.is_fixed:
                    x = abspoint2.x + sen.act.dx
                    y = abspoint2.y + sen.act.dy
                    point=Point(x, y)
                    result_contexts.append(merge_context_and_point(context1, point))
                else: #floating context point setting
                    for c2 in contexts2:
                        result_contexts.append(merge_2_contexts(context1, c2))
        if len(result_contexts) == 0:
            return 0, result_contexts
        return 1, result_contexts