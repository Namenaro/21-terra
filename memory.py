SUCCESS =1
FAIL =0

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Context:
    def __init__(self):
        pass
    def add_other_context(self, context):
        pass

    def add_point(self,point):
        pass

    def get_by_index(self, index):
        pass

    def find_nearest_point(self, point):
        pass

class UCompactSet:
    def __init__(self, dx, dy):
        pass

    def add(self, ddx, ddy):
        #recalc center of u-set
        pass
    def get_center(self):
        return dx,dy

    def make(self, context_point):
        return candidate_points

class EventChecker:
    def __init__(self, etalon):
        self.etalon = etalon

    def check(self, value):
        if value == self.etalon:
            return SUCCESS
        return FAIL

class Sensor:
    def __init__(self):
        pass
    def set_picture(self,picture):
        pass

    def measure(self, point):
        if self.picture[point]>5:
            return 1
        return 0

class Step:
    def __init(self):
        self.action_set # add fixed point or floating points to context
        self.step_memorized       # return contexts!
        self.on_events
        self.new_point_is_fixed # either action set center or all points of triggering of on_event

        self.link_to_parent_event

class OnEvent:
    def __init__(self):
        self.uid
        self.event_checker
        self.next_step
        self.index_in_context
        self.nontrivial_predictions

        self.link_to_parent_step

class Prediction:
    def __init__(self):
        self.condext_index
        self.step_memorzed
        self.action_set
        self.onevent_uid
        self.event_uid_probability

class MergedStep:
    def __init__(self, steps_to_merge):
        self.steps
        #add cloud to context

class PredictionsRegisterInSession: #in abs coords 28x28 (В ск, не связанной с ни одной из программ)
    def __init__(self):
        pass

    def register_corrector(self, nontrivial_predictions, context):
        pass

    def _register_new_nontrivial_prediction(self, x_abs,y_abs, step, distr_on_events_uids):
        pass

    def is_event_rare_by_current_prediction(self, x_abs, y_abs, step, event_uid):
        return probability_of_event_uid_in_current_situation

    def _make_default_prediction_for_event(self):
        pass

    def _gather_stat_for_binary_events(self):
        pass

def run_pure_recognition(step, point):
    on_event, context = step.get_on_event(point)
    while True:
        top_uid = on_event.uid
        step = on_event.next_step
        if step is None:
            break
        point = context.get_by_index(on_event.index_in_context)
        on_event, new_context = step.get_on_event(point)
        context.add_other_context(new_context)
    return top_uid


class HypoType1:
    pass

def run_with_finding_coincedences():
    #Случай1:
    #
    #  предикшен Б на пустом месте (т.е. в этой кооринате не предсказывалось редкое событие,
    # а оно случилось- тогда мы его учимся предсказывать)
    # тогда для формирования гипотезы нужны 3 редких события:
    # base_descr A + new_step U + prediction B (wich info(B|AU) > max(info(B), info(B|A), info(B|U))
    # результат: make hypothesys of type 1

    #Случай2:
    # Для координаты предсказывали редкое событие Б1, а случилось редкое событие Б2.
    # Делаем гипотезу о слиянии Б=Б1 или Б2
    # результат6 make hypothesys of type 2

    pass

def check_hypothesys_type1(hypothesys):
    pass






















