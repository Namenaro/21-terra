from elinker import *
from runner import Runner
from event import Act, Sen
from utils import *
from evaluator import *
from predsfinder import *

def test_runner():
    linker = ELinker()
    runner = Runner(linker)

    act1=Act(dx=1,dy=-1,index_in_context=0)
    act1.add_point(ddx=0,ddy=1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=1, dy=-1, index_in_context=1)
    act2.add_point(ddx=0, ddy=1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=sen1.s_uid, etalon2=1,
               is_fixed=False
               )
    linker.add_sen(sen2)
    act3 = Act(dx=1, dy=-1, index_in_context=3)
    act3.add_point(ddx=0, ddy=1)
    sen3 = Sen(suid=linker.generate_uid(),
               suid1=sen2.s_uid, etalon1=1,
               act=act3,
               suid2=sen1.s_uid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen3)
    print("created test suids..")
    abspoint = get_point_handly(runner.sensor.pic)

    r,c = runner.run_sen(sen3.s_uid, abspoint,1)
    print(c)
    if r==1:
        plot_contexts(c, runner.sensor.pic)
        plt.show()

def test_sampler():
    linker = ELinker()
    runner = Runner(linker)
    act1 = Act(dx=1, dy=-1, index_in_context=0)
    act1.add_point(ddx=0, ddy=1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=1, dy=-1, index_in_context=1)
    act2.add_point(ddx=0, ddy=1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=sen1.s_uid, etalon2=1,
               is_fixed=False
               )
    linker.add_sen(sen2)
    p = measure_p_of_suid(runner, sen2.s_uid, nattempts=1000)
    print(p)

def test_predsfinder1(logger):
    linker = ELinker()
    runner = Runner(linker)


    act1 = Act(dx=5, dy=0, index_in_context=0)
    act1.set_raduis_of_uncert(0)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)
    #p = measure_p_of_suid(runner, sen1.s_uid, nattempts=1000)
    #print("P="+ str(p))
    preds_finder = PredsFinder(sen1.s_uid, runner)
    sign, p_of_s2, pred_entries = preds_finder.run()
    print(sign)
    print(p_of_s2)

    fig = visualise_preds(sen1.s_uid, pred_entries, runner)
    logger.add_fig(fig)

def hor(linker):
    act1 = Act(dx=3, dy=0, index_in_context=0)
    act1.set_raduis_of_uncert(1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=3, dy=0, index_in_context=1)
    act2.set_raduis_of_uncert(1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    return sen2.s_uid

def ver(linker):
    act1 = Act(dx=0, dy=2, index_in_context=0)
    act1.set_raduis_of_uncert(1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=0, dy=3, index_in_context=1)
    act2.set_raduis_of_uncert(1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=sen1.s_uid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    return sen2.s_uid

def hv(linker):
    suidv = ver(linker)
    suidh = hor(linker)
    act2 = Act(dx=1, dy=1, index_in_context=2)
    act2.set_raduis_of_uncert(1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=suidh, etalon1=1,
               act=act2,
               suid2=suidv, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    return sen2.s_uid

def zmeyka(linker):
    act1 = Act(dx=2, dy=-1, index_in_context=0)
    act1.set_raduis_of_uncert(1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)
    act2 = Act(dx=2, dy=-1, index_in_context=1)
    act2.set_raduis_of_uncert(1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=sen1.s_uid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    act3 = Act(dx=2, dy=-1, index_in_context=4)
    act3.set_raduis_of_uncert(1)
    sen3 = Sen(suid=linker.generate_uid(),
               suid1=sen2.s_uid, etalon1=1,
               act=act2,
               suid2=sen2.s_uid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen3)
    return sen3.s_uid

def test_predsfinder2(logger):
    linker = ELinker()
    runner = Runner(linker)
    zmeyka(linker)
    suid = hv(linker)

    # p = measure_p_of_suid(runner, sen1.s_uid, nattempts=1000)
    # print("P="+ str(p))
    preds_finder = PredsFinder(suid, runner)
    sign, p_of_s2, pred_entries = preds_finder.run()
    print(sign)
    print(p_of_s2)

    fig = visualise_preds(suid, pred_entries, runner)
    logger.add_fig(fig)

if __name__ == "__main__":
    logger = HtmlLogger('bbb1')
    test_predsfinder1(logger)
    logger.close()
    logger = HtmlLogger('bbb2')
    test_predsfinder2(logger)
    logger.close()





