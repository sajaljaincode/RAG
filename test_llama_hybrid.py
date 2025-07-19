#!/usr/bin/env python3
"""Test wrapper for llama_hybrid.py with automated input"""

import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Hybrid Search'))

def test_llama_hybrid_search():
    print("Testing llama_hybrid.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        print(f"{prompt}machine learning")
        return "machine learning"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import llama_hybrid
        print("✓ llama_hybrid.py executed successfully")
        
    except Exception as e:
        print(f"✗ llama_hybrid.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_llama_hybrid_search()
