"""
Created on 2024-11-26
@author: Liu Jiajie(Chris)
@contact: chris.liu@scania.com.cn
"""
import logging
from simpleCan.util import xldriver
from simpleCan.util.task import Task
from simpleCan.util.signal_table import Signal_table_store

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.INFO)

class Canalyzer:
    def __init__(self):
        self.tasklist = [] #create a list to store all messages sending to DDU
        self.sts = Signal_table_store()
        xldriver.setup()
    def tasklist_setup(self,duration = 360):
        for i in range(len(self.sts.messageList)):
            self.tasklist.append(Task(message_id=self.sts.messageList[i].id,
                                      data=self.sts.messageList[i].data,
                                      period=self.sts.messageList[i].period,
                                      duration=duration))
    def tasklist_start(self):
        for task in self.tasklist:
            task.task_run()

    def sendMessage(self, message_id, data, period, duration = 10):
        task = Task(message_id=message_id,
                    data = data,
                    period = period,
                    duration = duration)
        self.tasklist.append(task)
        task.task_run()


    def modifyMessage(self, message_id, data):
        try:
            for task in self.tasklist:
                if task.get_messageID() == message_id:
                    task.task_modifyData(newData = data)
        except Exception as e:
            logging.error(e)

    def endAllTasks(self):
        for task in self.tasklist:
            task.task_stop()






