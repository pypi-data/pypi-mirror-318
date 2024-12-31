

if __name__ == "__main__":
    from client import ByteClient

    # Initialize with your API key
    client = ByteClient(api_key="byte_...")

    # # Convert dataset to tokens
    tokens = client.tokenize("story.txt")
