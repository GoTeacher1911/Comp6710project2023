def method1(arg1, arg2):
    pass

def method2(arg1, arg2, arg3):
    pass

def method3(arg1):
    pass

def method4(arg1, arg2):
    pass

def method5(arg1, arg2, arg3, arg4):
    pass
from hypothesis import given, strategies as st
import example

@given(st.integers(), st.integers())
def test_method1(arg1, arg2):
    example.method1(arg1, arg2)

@given(st.integers(), st.integers(), st.integers())
def test_method2(arg1, arg2, arg3):
    example.method2(arg1, arg2, arg3)

@given(st.integers())
def test_method3(arg1):
    example.method3(arg1)

@given(st.integers(), st.integers())
def test_method4(arg1, arg2):
    example.method4(arg1, arg2)

@given(st.integers(), st.integers(), st.integers(), st.integers())
def test_method5(arg1, arg2, arg3, arg4):
    example.method5(arg1, arg2, arg3, arg4)

if __name__ == "__main__":
    test_method1()
    test_method2()
    test_method3()
    test_method4()
    test_method5()
- name: Install fuzzing dependencies
  run: |
    python -m pip install --upgrade pip
    pip install hypothesis

- name: Run fuzzing tests
  run: |
    python fuzz.py
