from unavailable_object import (
    UnavailableObject,
    check_available,
    UnavailableObjectError,
)
import pytest


def test_OptionalObject():
    foo_bar_baz = UnavailableObject("foo_bar_baz")

    with pytest.raises(UnavailableObjectError):
        check_available(foo_bar_baz)

    with pytest.raises(UnavailableObjectError):
        foo_bar_baz.spam

    with pytest.raises(UnavailableObjectError):
        foo_bar_baz["spam"]

    with pytest.raises(UnavailableObjectError):
        foo_bar_baz()