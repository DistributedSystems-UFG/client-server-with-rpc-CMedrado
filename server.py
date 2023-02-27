import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_search(self, data):
        result = []
        for item in self.value:
            if data in item:
                result.append(item)
        return result

    def exposed_remove(self, data):
        self.value = [item for item in self.value if data not in item]
        return self.value

    def exposed_insert(self, data, index):
        self.value.insert(index, data)
        return self.value

    def exposed_sort(self):
        self.value = sorted(self.value)
        return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
