#!/usr/bin/env python3
"""Test wrapper for vector.py with automated input"""

import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Vector Search'))

def test_vector_search():
    print("Testing vector.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        print(f"{prompt}machine learning")
        return "machine learning"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import vector
        print("✓ vector.py executed successfully")
        
    except Exception as e:
        print(f"✗ vector.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_vector_search()
