# tests/test_robustness.py
import unittest
import numpy as np
from modules.perception import preprocess_text
from modules.understanding import load_model, get_embeddings

class RobustnessTest(unittest.TestCase):
    def test_large_input(self):
        # Simulate very large input text
        large_text = "word " * 10000  # 10,000 words
        tokens = preprocess_text(large_text)
        self.assertTrue(len(tokens) > 1000)

    def test_embedding_stability(self):
        # Generate dummy embeddings and test for consistency
        dummy_text = "Test input for embedding."
        tokens = preprocess_text(dummy_text)
        processed_text = " ".join(tokens)
        tokenizer, model = load_model()
        emb1 = get_embeddings(processed_text, tokenizer, model)
        emb2 = get_embeddings(processed_text, tokenizer, model)
        self.assertTrue(np.allclose(emb1, emb2, atol=1e-5))

if __name__ == '__main__':
    unittest.main()