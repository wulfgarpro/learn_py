import sys
import rpyc
import logging
from rpyc.utils.server import ThreadedServer

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger('MyService')
LOGGER.setLevel(logging.DEBUG)

SERVER = None


class MyService(rpyc.Service):
    # My service
    def exposed_echo(self, text):
        LOGGER.info(text)

    def exposed_exit(self):
        LOGGER.info('Server is closing...')
        SERVER.close()


if __name__ == "__main__":
    SERVER = ThreadedServer(MyService)  # , port=18813)
    LOGGER.debug('Server will run on port: %d', SERVER.port)
    SERVER.start()
