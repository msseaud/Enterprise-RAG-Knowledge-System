class VectorStore:
    def __init__(self):
        self.data = []

    def add(self, items):
        self.data.extend(items)

    def search(self, query):
        return self.data[:3]
