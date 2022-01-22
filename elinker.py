from copy import copy
import uuid
from utils import *
from context import *


class ELinker:
    # для каждого suid хранит ссылки (точее suid-ы) на те программы, у которых этот suid первый шаг
    def __init__(self):
        self.events = {}  # suid: sen, [links]
        self.uid = -1
        self.basic_suid = self.generate_uid()
        self.events[self.basic_suid]=[None, []]

    def generate_uid(self):
        #return uuid.uuid4()
        self.uid = self.uid+1
        return self.uid

    def set_basic(self, s_uid):
        self.basic_suid = s_uid

    def is_basic(self, s_uid):
        if s_uid == self.basic_suid:
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

    def get_preffered_siuds_for_grouth(self):
        # 1. самые высокие
        # 2.обавленные последними
        # случайными
        pass

    def get_sibling_suid(self, sen):
        #это для обнаружения ИЛИ
        pass

    def already_exists(self):
        # ищем инвертированный
        # для этого ревертим act и меняем местами suid1 и suid2
        pass












