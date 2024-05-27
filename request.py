class Request:
    db_request = []
    def push(self, item):
        self.db_request.append(item)
    def pop(self):
        self.db_request.pop()
    def get(self):
        if len(self.db_request) > 0:
            return self.db_request[len(self.db_request) - 1]
        return -1
    def first(self):
        if len(self.db_request) > 0:
            return self.db_request[0]
        return -1