from copy import deepcopy

import pytest

from tokenlists import TokenList


@pytest.mark.parametrize("key", ["", "_extra", "to_dict", "tokenMap"])
def test_additional_list_properties_round_trip(key):
    payload = {
        "name": "Example",
        "timestamp": "2020-01-01T00:00:00Z",
        "version": {"major": 1, "minor": 0, "patch": 0},
        "tokens": [
            {
                "chainId": 1,
                "address": "0x0000000000000000000000000000000000000001",
                "name": "One",
                "decimals": 18,
                "symbol": "ONE",
            }
        ],
        key: {"nested": [None, True, 42]},
    }
    original = deepcopy(payload)
    token_list = TokenList.from_dict(payload)
    assert payload == original
    assert token_list.to_dict() == original
    payload[key]["nested"].append("caller mutation")
    assert token_list.to_dict() == original
    serialized = token_list.to_dict()
    serialized[key]["nested"].append("result mutation")
    assert token_list.to_dict() == original
