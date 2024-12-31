import unittest
from byteai.tokenizer import tokenize  # Replace with your actual function or module

# class TestTokenizer(unittest.TestCase):
#     def test_tokenize(self):
#         input_text = "This is a test"
#         expected_output = ["This", "is", "a", "test"]
#         self.assertEqual(tokenize(input_text), expected_output)

if __name__ == "__main__":
    from byteai import ByteClient

    # Initialize with your API key
    client = ByteClient(api_key="byte_...")

    # # Convert dataset to tokens
    tokens = client.tokenize("story.txt")
