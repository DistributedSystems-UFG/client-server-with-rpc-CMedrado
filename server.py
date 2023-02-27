import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    def __init__(self):
        self.value = []

    def exposed_append(self, data):
        self.value.append(data)
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_search(self, data):
        if data in self.value:
            print(f"O elemento {data} está na lista")
        else:
            print(f"O elemento {data} não está na lista")

    def exposed_remove(self, data):
        self.value.remove(data)
        return self.value

    def exposed_insert(self, index, data):
        self.value.insert(index, data)
        return self.value

    def exposed_sort(self):
        self.value.sort()
        return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
