import pytest

from .utils import encrypt_test


class TestEncryptTest(object):
    def test_skips_if_only_if_returns_false(self):
        with pytest.raises(pytest.skip.Exception) as exc_info:
            encrypt_test(
                None, None, None, None,
                only_if=lambda api: False,
                skip_message="message!"
            )
        assert exc_info.value.args[0] == "message!"
