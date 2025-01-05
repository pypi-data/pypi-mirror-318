"""Tests the api."""

import pytest

import openwebif.api


def test_create() -> None:
    """Test creating a new device."""
    # Bogus config
    with pytest.raises(TypeError):
        openwebif.api.OpenWebIfDevice()  # type: ignore[call-arg]


def test_get_picon_name() -> None:
    """Tests whether the Picon name conversion works."""
    assert openwebif.api.OpenWebIfDevice.get_picon_name("RTÉ One") == "rteone"
