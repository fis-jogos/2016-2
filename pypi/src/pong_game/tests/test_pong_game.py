import pytest
import pong_game


def test_project_defines_author_and_version():
    assert hasattr(pong_game, '__author__')
    assert hasattr(pong_game, '__version__')
