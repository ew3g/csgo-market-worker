import time
from threading import Thread, Event


class CreateWorkerThread(Thread):
    def __init__(self, my_param=1):
        super(CreateWorkerThread, self).__init__()
        self.my_param = my_param
        self._stopevent = Event()
        self._sleepperiod = 10.0

    def run(self):
        print("Started")
        self._stopevent.clear()
        while not self._stopevent.is_set():
            print(1 == self.my_param)
            self._stopevent.wait(self._sleepperiod)

    def join(self, timeout=None):
        self._stopevent.set()
        Thread.join(self, timeout)


runner = CreateWorkerThread()
runner.start()
runner.join()
