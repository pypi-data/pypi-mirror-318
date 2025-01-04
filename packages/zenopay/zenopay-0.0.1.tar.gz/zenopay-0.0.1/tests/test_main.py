"""Main Test."""

import os
import uuid

import pytest
from dotenv import load_dotenv

from zenopay import ZenoPay


@pytest.fixture
def gateway():
    return ZenoPay(
        account_id=os.getenv("ACCOUNT_ID"),
    )
