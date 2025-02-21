import warnings
import pytest
from click import __getattr__


def test_getattr_basecommand():
    # Test that accessing "BaseCommand" returns something and emits a DeprecationWarning.
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = __getattr__("BaseCommand")
        # Check that a DeprecationWarning was issued
        assert any(issubclass(warning.category, DeprecationWarning) for warning in w), \
            "Expected a DeprecationWarning when accessing 'BaseCommand'"
        # Check that the result is callable
        assert callable(result)

def test_getattr_multicommand():
    # This test covers the "MultiCommand" branch.
    with warnings.catch_warnings(record=True) as s:
        warnings.simplefilter("always")
        result = __getattr__("MultiCommand")
        # Check that a DeprecationWarning was issued
        assert any(issubclass(warning.category, DeprecationWarning) for warning in s), \
            "Expected a DeprecationWarning when accessing 'MultiCommand'"
        assert result is not None

def test_getattr_unknown():
    # Test that accessing an unknown attribute raises an AttributeError.
    with pytest.raises(AttributeError):
        __getattr__("NonExistentAttribute")