#!/usr/bin/env python3
"""Master test script to run all RAG script tests"""

import subprocess
import sys
import os

def run_test(test_script, description):
    """Run a test script and return success status"""
    print(f"\n{'='*60}")
    print(f"Running {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([
            sys.executable, test_script
        ], capture_output=True, text=True, timeout=60)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print(f"✓ {description} - SUCCESS")
            return True
        else:
            print(f"✗ {description} - FAILED (return code: {result.returncode})")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ {description} - TIMEOUT (>60s)")
        return False
    except Exception as e:
        print(f"✗ {description} - ERROR: {e}")
        return False

def main():
    print("RAG Repository - Comprehensive Test Suite")
    print("Testing all Python scripts for runnability...")
    
    tests = [
        ("test_keyword_1.py", "Keyword Search (Basic)"),
        ("test_keyword_2.py", "Keyword Search (PDF)"),
        ("test_vector.py", "Vector Search (FAISS)"),
        ("test_llama_1.py", "Vector Search (LlamaIndex)"),
        ("test_hybrid_1.py", "Hybrid Search (LangChain)"),
        ("test_llama_hybrid.py", "Hybrid Search (LlamaIndex)"),
        ("test_rag_with_context.py", "RAG with Context Memory")
    ]
    
    results = []
    for test_script, description in tests:
        success = run_test(test_script, description)
        results.append((description, success))
    
    print(f"\n{'='*60}")
    print("FINAL RESULTS")
    print(f"{'='*60}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for description, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status:8} {description}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! RAG repository is fully runnable.")
        return 0
    else:
        print(f"⚠️  {total - passed} tests failed. See details above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
