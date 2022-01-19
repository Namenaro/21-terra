from elinker import *
from event import Act, Sen
from utils import *

def test_runner():

    linker = ELinker()
    runner = Runner(linker)

    act1=Act(dx=1,dy=1,index_in_context=0)
    act1.add_point(ddx=0,ddy=1)
    sen1 = Sen(suid=linker.generate_uid(),
               suid1=linker.basic_suid, etalon1=1,
               act=act1,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen1)

    act2 = Act(dx=1, dy=1, index_in_context=1)
    act2.add_point(ddx=0, ddy=1)
    sen2 = Sen(suid=linker.generate_uid(),
               suid1=sen1.s_uid, etalon1=1,
               act=act2,
               suid2=linker.basic_suid, etalon2=1,
               is_fixed=True
               )
    linker.add_sen(sen2)
    print("created test suids..")
    abspoint = get_point_handly(runner.sensor.pic)
    contexts = runner.run_suid(sen2.s_uid, abspoint)
    print(contexts)

if __name__ == "__main__":
    test_runner()




