#!/usr/bin/env python3
"""Test wrapper for llama_1.py with automated input"""

import sys
import os
import asyncio
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Vector Search'))

def test_llama_vector_search():
    print("Testing llama_1.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        if "exit" in prompt.lower():
            print(f"{prompt}exit")
            return "exit"
        else:
            print(f"{prompt}machine learning")
            return "machine learning"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import llama_1
        print("✓ llama_1.py executed successfully")
        
    except Exception as e:
        print(f"✗ llama_1.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_llama_vector_search()
