# tests/test_auto_code_generator.py
import unittest
from modules.auto_code_generator import generate_code_enhancement

class TestAutoCodeGenerator(unittest.TestCase):
    def test_tokenization_suggestion(self):
        prompt = "Tokenization process is inefficient."
        suggestion = generate_code_enhancement(prompt)
        self.assertIn("Optimize the tokenization", suggestion)

    def test_reasoning_suggestion(self):
        prompt = "Reasoning module performance is low."
        suggestion = generate_code_enhancement(prompt)
        self.assertIn("Enhance the reasoning", suggestion)
    
    def test_generic_suggestion(self):
        prompt = "General optimization needed."
        suggestion = generate_code_enhancement(prompt)
        self.assertIn("Review the module", suggestion)

if __name__ == '__main__':
    unittest.main()