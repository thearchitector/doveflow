import pytest
from hypothesis import given, strategies as st

from doveflow.types import Processor


class MockProcessor(Processor):
    def execute(self, num1, num2):
        return num1 + num2


@given(st.integers(), st.integers())
def test_processor_direct(x: int, y: int):
    p = MockProcessor.spawn(x, y)

    assert isinstance(p, MockProcessor)
    assert x + y == p.get()
