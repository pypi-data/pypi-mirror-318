# gpt2_tools/tokenizer.py

import os
import tiktoken
import numpy as np
from typing import List, Optional, Union
from pathlib import Path
import requests
from tqdm import tqdm

class TokenizerTool:
    """A tool for tokenizing text files for GPT-2 training."""
    
    def __init__(self, cache_dir: Optional[str] = None):
        """
        Initialize the tokenizer tool.
        
        Args:
            cache_dir: Directory to store processed files. If None, uses './data_cache'
        """
        self.enc = tiktoken.get_encoding("gpt2")
        self.cache_dir = Path(cache_dir) if cache_dir else Path('./data_cache')
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def encode(self, text: str) -> List[int]:
        """Encode text using GPT-2 tokenizer."""
        return self.enc.encode(text, allowed_special={'<|endoftext|>'})

    def _download_file(self, url: str, filename: str) -> None:
        """
        Download a file with progress bar.
        
        Args:
            url: URL to download from
            filename: Where to save the file
        """
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as f, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                pbar.update(size)

    def write_tokens(self, filename: str, tokens: List[int]) -> None:
        """
        Write tokens to a binary file.
        
        Args:
            filename: Output filename
            tokens: List of token IDs to write
        """
        array = np.array(tokens, dtype=np.int32)
        array.tofile(filename)
        print(f"Saved {len(tokens)} tokens to {filename}")

    def process_file(
        self,
        input_file: Union[str, Path],
        output_prefix: str,
        val_size: int = 32768,
        split_pattern: str = '\n\n',
        url: Optional[str] = None
    ) -> tuple[Path, Path]:
        """
        Process a text file into training and validation token files.
        
        Args:
            input_file: Path to input text file or URL
            output_prefix: Prefix for output files
            val_size: Number of tokens to use for validation
            split_pattern: Pattern to split documents
            url: Optional URL to download file from
            
        Returns:
            Tuple of (validation_file_path, training_file_path)
        """
        input_path = Path(input_file)
        
        # Download if URL provided
        if url and not input_path.exists():
            print(f"Downloading {url}...")
            self._download_file(url, input_path)
        
        # Read and process text
        print(f"Processing {input_path}...")
        text = input_path.read_text()
        
        # Add document separators
        text = "<|endoftext|>" + text
        text = text.replace(split_pattern, f'{split_pattern}<|endoftext|>')
        
        # Tokenize
        tokens = self.encode(text)
        
        # Split into train/val
        val_tokens = tokens[:val_size]
        train_tokens = tokens[val_size:]
        
        # Save files
        val_file = self.cache_dir / f"{output_prefix}_val.bin"
        train_file = self.cache_dir / f"{output_prefix}_train.bin"
        
        self.write_tokens(str(val_file), val_tokens)
        self.write_tokens(str(train_file), train_tokens)
        
        return val_file, train_file

def main():
    """CLI interface for tokenization tool."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Tokenize text files for GPT-2 training')
    parser.add_argument('input_file', help='Input text file to process')
    parser.add_argument('--output-prefix', default='tokenized',
                      help='Prefix for output files')
    parser.add_argument('--val-size', type=int, default=32768,
                      help='Number of tokens for validation')
    parser.add_argument('--cache-dir', default='./data_cache',
                      help='Directory to store processed files')
    parser.add_argument('--url', help='URL to download input file from')
    
    args = parser.parse_args()
    
    tokenizer = TokenizerTool(args.cache_dir)
    val_file, train_file = tokenizer.process_file(
        args.input_file,
        args.output_prefix,
        args.val_size,
        url=args.url
    )
    
    print(f"\nProcessing complete!")
    print(f"Validation file: {val_file}")
    print(f"Training file: {train_file}")

if __name__ == "__main__":
    main()