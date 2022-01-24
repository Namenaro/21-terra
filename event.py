from elinker import *
from event import *
from utils import *

class Act:
    def __init__(self, dx, dy, index_in_context):
        self.dx = dx
        self.dy = dy
        self.ddxs = [0]
        self.ddys = [0]
        self.index_in_context = index_in_context

    def add_point(self, ddx,ddy):
        self.ddxs.append(ddx)
        self.ddys.append(ddy)

    def get_all_variants(self, context):
        abspoint = context.get_by_index(self.index_in_context)
        return self.get_by_abspoint(abspoint)

    def get_center(self, context):
        abspoint = context.get_by_index(self.index_in_context)
        cx = abspoint.x + self.dx
        cy = abspoint.y + self.dy
        return Point(cx, cy)

    def get_by_abspoint(self, abspoint):
        cx = abspoint.x + self.dx
        cy = abspoint.y + self.dy
        several_abspoints = []
        for i in range(len(self.ddxs)):
            x = cx + self.ddxs[i]
            y = cy + self.ddys[i]
            several_abspoints.append(Point(x, y))
        return several_abspoints

    def copy_to_other_context(self, context, new_context):
        abskeypoint = self.get_center(context)
        index_in_new = new_context.find_nearest_points_indexes(abskeypoint)[0]
        nearest = new_context.points[index_in_new]
        dx = abskeypoint.x - nearest.x
        dy = abskeypoint.y - nearest.y
        adapted_act = Act(dx,dy,index_in_new)
        adapted_act.ddxs = deepcopy(self.ddxs)
        adapted_act.ddys = deepcopy(self.ddys)
        return adapted_act

    def set_raduis_of_uncert(self, radius):
        ddx,ddy = get_coords_less_or_eq_raduis(0,0,radius)
        self.ddxs = ddx
        self.ddys =ddy


class Sen:
    def __init__(self, suid, suid1, etalon1, act, suid2, etalon2, is_fixed):  # начиннается с сенсора, запускается из abspoint
        self.s_uid = suid
        self.suid1 = suid1
        self.etalon1 = etalon1

        self.act = act
        self.suid2 = suid2
        self.etalon2 = etalon2
        self.is_fixed = is_fixed






