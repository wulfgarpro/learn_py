import rpyc
import datetime


CONN1 = rpyc.connect("localhost", 39738)
CONN2 = rpyc.connect("localhost", 39707)
TESTS = ['abc123', 'abc456']
CONNECTS = {}
CONNECTS[TESTS[0]] = CONN1
CONNECTS[TESTS[1]] = CONN2


def do_tests():
    for test, con in CONNECTS.items():
        for i in range(100):
            msg = "{}:{}:helo:{}".format(i, test, str(datetime.datetime.now()))
            con.root.echo(msg)


def done():
    for con in CONNECTS.values():
        try:
            con.root.exit()
        except EOFError:
            pass


if __name__ == '__main__':
    do_tests()
    done()
