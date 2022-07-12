from threading import Thread, Event
from dotenv import find_dotenv, load_dotenv
from api.MarketApi import MarketApi


class CreateWorkerThread(Thread):
    def __init__(self, my_param=1):
        super(CreateWorkerThread, self).__init__()
        load_dotenv(find_dotenv())
        self.my_param = my_param
        self.stop_event = Event()
        self.sleep_period = 10.0

        self.market_api = MarketApi()

    def run(self):
        print("Started")
        self.stop_event.clear()
        while not self.stop_event.is_set():
            print(self.market_api.get_item("62cc844f5c175ea059472700"))
            self.stop_event.wait(self.sleep_period)

    def join(self, timeout=None):
        self.stop_event.set()
        Thread.join(self, timeout)


runner = CreateWorkerThread()
runner.start()
