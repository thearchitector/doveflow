import pytest
from gevent import Greenlet

from doveflow.types import Canvas, Processor


@pytest.fixture
def mock_processors():
    return Processor(), Processor()


def test_build_canvas_basic(mock_processors):
    p, _ = mock_processors

    c = Canvas(p, p)
    assert isinstance(c, Canvas)

    c = c.build()
    assert isinstance(c, Greenlet)
    assert c.get() == (42, 42)


def test_build_canvas_onerror(mock_processors):
    p, p2 = mock_processors

    def err_callback(results, error, **kwargs):
        assert isinstance(results, tuple)
        assert isinstance(error, Exception)
        assert kwargs["treedata"] == (
            {"successful": True, "partial": 42},
            {"successful": False, "partial": None},
        )

        raise error

    c = Canvas(p, p2, onerror=err_callback).build()

    with pytest.raises(ZeroDivisionError):
        c.start()
