"""Tests for package_name."""

import pytest

from src.donew import __version__


def test_version():
    """Test version is a string."""
    assert isinstance(__version__, str)
