import sys
import rpyc
from rpyc.utils.server import ThreadedServer

SERVER = None


class MyService(rpyc.Service):
    # My service
    def exposed_echo(self, text):
        print(text)

    def exposed_exit(self):
        print('Server closing...')
        SERVER.close()


if __name__ == "__main__":
    SERVER = ThreadedServer(MyService, port=18812)
    SERVER.start()
