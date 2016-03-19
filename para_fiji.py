from ipyparallel import Client
import os

def myjob(arg):
    import os
    os.system('fiji --headless -batch /data/miyamoto/fiji_macro/invert.ijm %s' % arg)


def do_parallel(filelist):
    rc = Client()

    print('# of engines : %d' % len(rc.ids))
    print('# of job : %d' % len(filelist))

    lv = rc.load_balanced_view()
    result = lv.map_async(myjob, filelist)
    result.wait_interactive()


def do_single(filelist):
    for arg in filelist:
        os.system('fiji --headless -batch /data/miyamoto/fiji_macro/invert.ijm %s' % arg)


if __name__ == '__main__':
    filelist_file = '/data/registration/filelist.txt'
    #filelist_file = '/data/registration/filelist_small.txt'

    filelist = []
    for line in open(filelist_file):
        filelist.append(line)

    do_parallel(filelist)
    #do_single(filelist)
