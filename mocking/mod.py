from package import mod_a
from package import mod_b

import time

class MyClass():

    @staticmethod
    def factory(something, timeout=1):
        print('calling sleep')
        now = time.time()
        while time.time() < timeout:
            print(time.time())
            time.sleep(10)
            if(False): break

        raise TimeoutError
