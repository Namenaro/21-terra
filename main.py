from elinker import *
from runner import Runner
from event import Act, Sen
from utils import *
from evaluator import *

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


if __name__ == "__main__":
    test_sampler()




