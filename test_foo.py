

from foo import foo
from unittest.mock import patch


@patch('foo.bar')
def test_bar_is_called_in_foo(mock):
    assert foo() == 42
    assert mock.called is True

