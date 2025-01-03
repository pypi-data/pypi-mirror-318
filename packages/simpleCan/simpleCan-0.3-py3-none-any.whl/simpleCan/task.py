import threading
import time
import logging
import xldriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# one instance of Task class contains one thread
class Task:
    def __init__(self, message_id, data, period = 0, duration = 0):
        self.message_id = message_id
        self.data = data
        self.period = period
        self.duration = duration
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self.thread = threading.Thread(target=self.sendData_task)

    def get_messageID(self):
        return self.message_id

    def get_messageData(self):
        return self.data

    def sendData_task(self): # append sendData task with parameter period and duration
        end_time = time.time() + self.duration
        while time.time() < end_time:
            xldriver.sendData(messageID=self.message_id, data=self.data)
            time.sleep(self.period)
            if self._stop_event.is_set():
                break

    def task_run(self):
        self.thread.start()

    def task_modifyData(self, newData):
        with self._lock:
            self.data = newData

    def task_stop(self):
        self._stop_event.set()
        self.thread.join()




