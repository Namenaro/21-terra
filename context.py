from utils import *
from copy import deepcopy

def dist(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)

class Context:
    def __init__(self):
        self.points = []

    def append_context(self, context):
        if len(context.points)>0:
            self.points.append(context.points)

    def add_point(self,point):
        self.points.append(point)

    def get_by_index(self, index):
        return self.points[index]

    def find_nearest_points_indexes(self, point):
        if len(self.points)==0:
            return None
        indexes_dist= {}
        for i in range(len(self.points)):
            indexes_dist[i] = dist(self.points[i], point)
        sorted_indexes = sorted(indexes_dist, key=indexes_dist.get)
        return sorted_indexes

    def add_context_as_point(self, context):
        xs = 0
        ys = 0
        n = len(context.points)
        if n > 0:
            for point in context.points:
                xs += point.x
                ys += point.y
        meanx= int(xs/n)
        meany = int(ys/n)
        self.add_point(Point(meanx,meany))


def merge_2_contexts(c1, c2):
    c3 = deepcopy(c1)
    c3.append_context(c2)
    return c3

def merge_context_and_point(c1, point):
    c2 = deepcopy(c1)
    c2.add_point(point)
    return c2