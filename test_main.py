"""
required packages for testing
    pip install pytest
    pip install coverage
    pip install pylint

1. Run pytest
    > pytest test_main.py -v

2. Run coverage on pytest
    > python -m coverage run --include=main.py -m pytest test_main.py

3. Generate coverage report
    > python -m coverage report

4. Generate coverage html report
    > python -m coverage html # a new folder called "htmlcov" get created with an index.html
"""

import pytest
import main


def test_insert_node():
    p = main.MinHeap()
    p.insert_node(5)
    p.insert_node(2)
    # min_heap = "2 5"
    assert p.print_heap() is None


if __name__ == "__main__":
    pytest.main()
