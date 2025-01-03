import pandas
import simpleCan.dataStructure as ds


class Signal_table_store:
    global messageList
    excel_table = ''
    def __init__(self):
        self.messageList = []
        try:
            data_frame = pandas.read_excel(self.excel_table)
            for i in range(len(data_frame)):
                message = ds.CanMessage(id = int(data_frame['id'][i], 16), data = [int(x, 16) for x in str(data_frame['data'][i]).split(',')],
                                        period = float(data_frame['periodic'][i]))
                self.messageList.append(message)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def printMessageList(self):
        for i in range(len(self.messageList)):
            print(self.messageList[i].id)
            print(self.messageList[i].data)
            print(self.messageList[i].period)









