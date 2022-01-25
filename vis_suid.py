from utils import *
from runner import *
from registrator import *
from predsfinder import *

def show_suid(suid, runner, logger):
    for i in range(5):
        runner.reset3()
        cs=[]
        for y in range(0, 27):
            for x in range(0, 27):
                point = Point(x,y)
                res, contexts = runner.run_sen(suid, point, None)
                cs=cs+contexts
        fig = plot_contexts(cs, runner.sensor.pic)
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


if __name__ == "__main__":
    linker = ELinker()
    runner = Runner(linker)
    logger = HtmlLogger("GGG")

    suid = zmeyka(linker)
    show_suid(suid, runner, logger)
    logger.close()