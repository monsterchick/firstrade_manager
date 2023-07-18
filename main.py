import json
import os


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

class DataStore(Subject):
    def __init__(self):
        super().__init__()
        self.data = {}

    def update_data(self, symbol):
        # symbol
        # print(symbol["symbol"])

        self.data[symbol["symbol"]] = symbol
        # print(self.data)

class JsonWriter:
    def update(self, data):
        json_data = json.dumps(data)

        if os.path.exists("data.json"):
            # 读取内容
            with open("data.json", "r") as file:
                # print(file.read())
                old_content = file.read()
            # 去掉 '}'
            old_content = old_content[:-1]
            # 加上逗号
            old_content += ','

            # 删除新数据第一个 '{'
            new_content = json_data
            new_content = new_content[1:]
            print(new_content)

            # 合并新内容
            new_content = old_content + new_content
            print(new_content)
            # print(old_content)
            # 续写内容
            with open('data.json','w') as file:
                file.write(new_content)

        else:
            with open("data.json","w") as file:
                file.write(json_data)




# 初始化數據存儲對象
data_store = DataStore()

# 初始化JSON寫入觀察者
json_writer = JsonWriter()

# 將觀察者附加到數據存儲對象
data_store.attach(json_writer)

qqq = {"symbol": "qqq", "hold": 1, "quantity": 1, "average_price": 1.2, "amount": 222}
data_store.update_data(qqq)

json_writer.update(data_store.data)

