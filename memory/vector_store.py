class VectorStore:
    def __init__(self):
        self.data = []

    def add(self, items):
        self.data.extend(items)

    def search(self, query):
        # 模拟返回前3条
        return self.data[:3]
