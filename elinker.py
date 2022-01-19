from copy import copy
import uuid
from utils import *
from context import *


class ELinker:
    # для каждого suid хранит ссылки (точее suid-ы) на те программы, у которых этот suid первый шаг
    def __init__(self):
        self.events = {}  # suid: sen, [links]
        self.basic_suid = self.generate_uid()
        self.events[self.basic_suid]=[None, []]
        self.i=-1

    def generate_uid(self):
        #return uuid.uuid4()
        self.i = self.i+1
        return self.i

    def set_basic(self, s_uid):
        self.basic_suid = s_uid

    def is_basic(self, s_uid):
        if s_uid == self.basic:
            return True
        return False

    def add_sen(self, sen):
        self.events[sen.s_uid] = [sen, []]

    def get_sen(self, suid):
        return self.events[suid][0]

    def get_links(self, suid):
        return self.events[suid][1]

    def add_link(self, suid, link):
        self.events[suid][1].append(link)


class Runner:
    def __init__(self, linker):
        self.linker = linker
        self.sensor = SimpleSensor()

    def run_suid(self, suid, abspoint1, etalon=None):
        # возможно, это базовый сенсор...
        if self.linker.is_basic(suid):
            res = self.sensor.measure(abspoint1)
            if res == etalon:
                c = Context()
                c.add_point(abspoint1)
                return [c]
            else:
                return None
        # это составная программа, и надо запустить обе части
        sen=self.linker.get_sen(suid)
        sen1 = self.linker.get_sen(sen.suid1)
        sen2 = self.linker.get_sen(sen.suid2)
        # запускаем первую часть, точка запуска известна, возвращается None или [c1,c2,...]
        contexts1 = self.run_sen1(sen1, abspoint1, sen.etalon1)
        if contexts1 is None:
            return None
        # если выполнение первой подпрограммы было успешно, то мы можем запусить вторую:
        result_contexts = []
        for context1 in contexts1:
            abspoints2 = sen.act.get_all_variants(context1)
            for abspoint2 in abspoints2:
                contexts2 = self.run_sen2(sen2, abspoint2, sen.etalon2)
                if contexts2 is None:
                    continue # из этой точки запуск второй подпрограммы не успешен
                # один или несколько пуской второй подпрограммы были успешны
                if sen.is_fixed:
                    x = abspoint2.x + sen.act.dx
                    y = abspoint2.y + sen.act.dy
                    point=Point(x, y)
                    result_contexts.append(merge_context_and_point(context1, point))
                else: #floating context point setting
                    for c2 in contexts2:
                        result_contexts.append(merge_2_contexts(context1, c2))
        if len(result_contexts)==0:
            return None
        return result_contexts






def test_runner():
    from event import *
    linker = ELinker()
    runner = Runner(linker)

    act1=Act(dx=1,dt=1,index_in_context=0)
    act1.add_point(ddx=0,ddy=1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=1, dt=1, index_in_context=1)
    act2.add_point(ddx=0, ddy=1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    abspoint = get_point_handly(runner.sensor)
    contexts = runner.run_suid(sen2.s_uid, abspoint)
    print(contexts)



