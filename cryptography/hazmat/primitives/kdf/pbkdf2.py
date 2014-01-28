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

from cryptography import utils
from cryptography.exceptions import (
    InvalidKey, UnsupportedAlgorithm, AlreadyFinalized
)
from cryptography.hazmat.primitives import constant_time, interfaces


@utils.register_interface(interfaces.KeyDerivationFunction)
class PBKDF2HMAC(object):
    def __init__(self, algorithm, length, salt, iterations, backend):
        if not backend.pbkdf2_hmac_supported(algorithm):
            raise UnsupportedAlgorithm(
                "{0} is not supported for PBKDF2 by this backend".format(
                    algorithm.name)
            )
        self._called = False
        self.algorithm = algorithm
        self._length = length
        self._salt = salt
        self.iterations = iterations
        self._backend = backend

    def derive(self, key_material):
        if self._called:
            raise AlreadyFinalized("PBKDF2 instances can only be called once")
        else:
            self._called = True
        return self._backend.derive_pbkdf2_hmac(
            self.algorithm,
            self._length,
            self._salt,
            self.iterations,
            key_material
        )

    def verify(self, key_material, expected_key):
        derived_key = self.derive(key_material)
        if not constant_time.bytes_eq(derived_key, expected_key):
            raise InvalidKey("Keys do not match.")
