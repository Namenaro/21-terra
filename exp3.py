from utils import *
from runner import *
from registrator import *
from predsfinder import *
from evaluator import *

def fill_linker(linker):
    act1 = Act(dx=0, dy=-1, index_in_context=0)
    act1.set_raduis_of_uncert(0)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=0,
               is_fixed=True
               )
    linker.add_sen(sen1)
    return sen1.s_uid



def get_example_context(suid):
    runner.reset()
    cs = []
    for y in range(0, 27):
        for x in range(0, 27):
            point = Point(x, y)
            res, contexts = runner.run_sen(suid, point, None)
            cs = cs + contexts
    c = cs[1]
    fig = plot_contexts([c], runner.sensor.pic)
    plt.show()
    return c

def get_act(context, t_abspoint, radius):
    dxs, dys = get_coords_less_or_eq_raduis(0, 0, radius)
    index_in_context = context.find_nearest_points_indexes(t_abspoint)[0]
    nearest_point = context.points[index_in_context]
    dx = t_abspoint.x - nearest_point.x
    dy = t_abspoint.y - nearest_point.y

    act = Act(dx, dy, index_in_context)
    act.ddxs = dxs
    act.ddys = dys
    return act

def get_act1and2(context, act12, len_of_c1):
    c1 = Context()
    c1.points = context.points[:len_of_c1]
    t_act1 = act12.copy_to_other_context(context, c1)

    c2 = Context()
    c2.points = context.points[len_of_c1:]
    t_act2 = act12.copy_to_other_context(context, c2)
    return t_act1, t_act2

def get_len_of_c1(suid, runner):
    sen = runner.linker.get_sen(suid)
    for y in range(0, 27):
        for x in range(0, 27):
            point = Point(x, y)
            res, contexts = runner.run_sen(sen.suid1, point, sen.etalon1)
            if len(contexts)!=0:
                return len(contexts[0].points)


if __name__ == "__main__":
    linker = ELinker()
    runner = Runner(linker)
    logger = HtmlLogger("BBB")
    suid = fill_linker(linker)
    c = get_example_context(suid)
    print ("context="+ str(c.points))

    t_abspoint = get_point_handly(runner.sensor.pic)
    t_suids = runner.get_all_suids_in_point(t_abspoint)
    print("found suids: "+ str(t_suids))
    t_suid= max(t_suids)
    print("selected="+ str(t_suid))

    act12 = get_act(c, t_abspoint, radius=0)
    len_of_c1 = get_len_of_c1(suid, runner)
    t_act1, t_act2 =  get_act1and2(c, act12, len_of_c1)

    sen = runner.linker.get_sen(suid)
    t_etalon=1
    ev = Evaluator(runner, sen, t_suid, t_etalon, t_act1, t_act2, act12)
    sign = ev.eval_significange()
    print("significange for act =" + str(sign))






