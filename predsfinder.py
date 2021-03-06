from sampler import *
from evaluator import *

# для данного тестового сен найдем разные ентривиальные предсказания и замерим их суммарную силу

class PredEntry:
    def __init__(self, suid, act):
        self.suid=suid
        self.act=act
        self.p=None

class PredsFinder:
    def __init__(self, suid, runner):
        self.runner=runner
        self.suid = suid
        self.preds = []  #[pred_entry1,...]
        self.num_attempts_allowed=100

    def run(self):
        sign = 0

        for i in range(self.num_attempts_allowed):
            print("finding "+ str(i)+ "'th pred for suid "+ str(self.suid))
            pred_entry, significance = self.find_next_pred()
            print("found pred with significance = " +str(significance))
            sign +=significance
            if significance>0:
                self.preds.append(pred_entry)
                if len(self.preds)>4:
                    break


        p_of_s2 = measure_p_of_c2act_by_c1(self.runner, self.suid, sample_size=20)
        print ("overall sinidicance of + act_c2 is "+ str(sign))
        print("overall p(act_c2=et)  is " + str(p_of_s2))
        return sign, p_of_s2, self.preds


    def create_act_for_pred(self, t_suid, t_abspoint, context):
        acts = []
        radius = 0
        max_raduis = 4
        while True:
            print(radius)
            X, Y = get_coords_less_or_eq_raduis(t_abspoint.x, t_abspoint.y, radius)
            can_expand = True
            for i in range(len(X)):
                if self.runner.registrator.is_trivial(t_suid, Point(X[i], Y[i])):
                    can_expand = False
                    break
            if can_expand == False:
                break
            # можно включить эту неопределенность при этом радиусе как нетривиальную:
            dxs, dys = get_coords_less_or_eq_raduis(0, 0, radius)
            index_in_context = context.find_nearest_points_indexes(t_abspoint)[0]
            nearest_point = context.points[index_in_context]
            dx=t_abspoint.x - nearest_point.x
            dy=t_abspoint.y - nearest_point.y

            act = Act(dx,dy,index_in_context)
            act.ddxs=dxs
            act.ddys = dys
            acts.append(act)
            radius += 2
            if radius > max_raduis:
                break

        return acts


    def find_next_pred(self):
        self.runner.registrator.clean()
        self.runner.registrator.is_on = False
        while True:
            self.runner.reset3()
            abspoint = get_random_point()
            res, contexts = self.runner.run_sen(self.suid, abspoint, None)
            if res == 0:
                continue
            print ("good situation: " + str(contexts))
            # нашли ситуацию, где надо искать событие для формирования предсказания
            # сначала узнаем длину первго контекста:
            sen = self.runner.linker.get_sen(self.suid)
            _, c1_contexts = self.runner.run_sen(sen.suid1, abspoint, sen.etalon1)
            len_of_c1 = len(c1_contexts[0].points)

            # теперь внесем в регистратор суид1, суид2 и предсказания
            self.runner.registrator.is_on = True
            _, contexts = self.runner.run_sen(self.suid, abspoint, None)
            context = random.choice(contexts)
            self.run_predictions(context)
            self.runner.registrator.is_on = False
            print("registered all trivial")
            # можно искать редкие сущности в округе:
            while True:
                t_abspoint = get_random_point()
                t_suids = self.runner.get_all_suids_in_point(t_abspoint)
                t_suids = self.runner.registrator.filter_trivials_from_list(t_suids)
                if len(t_suids)==0:
                    continue
                selected_t_suid = max(t_suids)
                print("found nontrivial event, suid " + str(selected_t_suid))
                someacts = self.create_act_for_pred(selected_t_suid, t_abspoint, context)
                print("created acts:" + str(len(someacts)))
                signs = []
                for act12 in someacts:
                    print("eval act: ")
                    c1 = Context()
                    c1.points = context.points[:len_of_c1]
                    t_act1 = act12.copy_to_other_context(context, c1)

                    c2 = Context()
                    c2.points = context.points[len_of_c1:]
                    t_act2 = act12.copy_to_other_context(context, c2)

                    ev = Evaluator(self.runner, sen, selected_t_suid, 1,t_act1, t_act2, act12)
                    sign = ev.eval_significange()
                    print("significange for act ="+ str(sign))
                    signs.append(sign)
                if len(signs)!=0:
                    if max(signs) > 0:
                        index = signs.index(max(signs))
                        best_pred = PredEntry(selected_t_suid, someacts[index])
                        return best_pred, signs[index]
                return None, 0


    def run_predictions(self, context):
        for pred_entry in self.preds:
            abspoints = pred_entry.act.get_all_variants(context)
            for abspoint in abspoints:
                _, _ = self.runner.run_sen(pred_entry.suid, abspoint, None)


def visualise_preds(suid, preds, runner):
    contexts=None
    while True:
        runner.reset3()
        abspoint = get_random_point()
        res, contexts = runner.run_sen(suid, abspoint, None)
        if res == 0:
            continue
        break
    fig, ax = plt.subplots()
    plt.imshow(runner.sensor.pic, cmap='gray_r')
    c = random.choice(contexts)
    i=0
    for point in c.points:
        strmarker = '$c' + str(i) + '$'
        plt.scatter(point.x, point.y, s=100, c='yellow', marker=strmarker, alpha=0.9)

    for pred_entry in preds:
        color = np.random.rand(3, )
        abspoints = pred_entry.act.get_all_variants(c)
        for point in abspoints:
            strmarker = '$' + str(pred_entry.suid) + '$'
            plt.scatter(point.x, point.y, s=100, c=[color], marker=strmarker, alpha=0.9)

    return fig
