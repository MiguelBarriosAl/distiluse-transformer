import unittest
from sentence_transformers import evaluation, SentenceTransformer


class TestProcessing(unittest.TestCase):

    def test_embeddings(self):
        model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
        sentences = {0: "Hello World", 1: "Hello World!", 2: "The cat is on the table", 3: "On the table the cat is"}
        data_eval = evaluation.ParaphraseMiningEvaluator(sentences, [(0, 1), (2, 3)])
        score = data_eval(model)
        assert score > 0.99
