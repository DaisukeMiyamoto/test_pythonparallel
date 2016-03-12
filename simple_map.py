from ipyparallel import Client


def do_parallel(num):
    rc = Client()
    print('# of engines : %d' % len(rc.ids))
    print('# of job : %d' % num)

    lv = rc.load_balanced_view()
    rs = lv.map_async(lambda x:x**10, range(num))
    rs.wait_interactive()


if __name__ == '__main__':
    do_parallel(1000)
    do_parallel(10000)
