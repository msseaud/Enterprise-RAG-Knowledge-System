class EmbeddingModel:
    def encode(self, texts):
        return [len(t) for t in texts]
