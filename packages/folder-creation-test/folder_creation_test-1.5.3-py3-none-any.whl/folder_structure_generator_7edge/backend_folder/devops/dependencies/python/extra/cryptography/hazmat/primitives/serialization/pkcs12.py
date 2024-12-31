# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function


def load_key_and_certificates(data, password, backend):
    return backend.load_key_and_certificates_from_pkcs12(data, password)
