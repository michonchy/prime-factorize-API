import json

import pytest

from prime_factorize import app


def test_is_prime_factorize():
    assert app.is_prime_factorize(2021) == [43,47]