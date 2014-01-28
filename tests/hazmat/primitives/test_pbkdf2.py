# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

import pytest

from cryptography import utils
from cryptography.exceptions import (
    InvalidKey, UnsupportedAlgorithm, AlreadyFinalized
)
from cryptography.hazmat.primitives import hashes, interfaces
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.backends import default_backend


@utils.register_interface(interfaces.HashAlgorithm)
class UnsupportedDummyHash(object):
    name = "unsupported-dummy-hash"


class TestPBKDF2(object):
    def test_already_finalized(self):
        kdf = PBKDF2(hashes.SHA1(), 20, b"salt", 10, default_backend())
        kdf.derive(b"password")
        with pytest.raises(AlreadyFinalized):
            kdf.derive(b"password2")

        kdf = PBKDF2(hashes.SHA1(), 20, b"salt", 10, default_backend())
        key = kdf.derive(b"password")
        with pytest.raises(AlreadyFinalized):
            kdf.verify(b"password", key)

        kdf = PBKDF2(hashes.SHA1(), 20, b"salt", 10, default_backend())
        kdf.verify(b"password", key)
        with pytest.raises(AlreadyFinalized):
            kdf.verify(b"password", key)

    def test_unsupported_algorithm(self):
        with pytest.raises(UnsupportedAlgorithm):
            PBKDF2(UnsupportedDummyHash(), 20, b"salt", 10, default_backend())

    def test_invalid_key(self):
        kdf = PBKDF2(hashes.SHA1(), 20, b"salt", 10, default_backend())
        key = kdf.derive(b"password")

        kdf = PBKDF2(hashes.SHA1(), 20, b"salt", 10, default_backend())
        with pytest.raises(InvalidKey):
            kdf.verify(b"password2", key)
