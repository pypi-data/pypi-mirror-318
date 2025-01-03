import pytest

from naverdict.search import search


@pytest.mark.parametrize(
    "search_term, expected_outcome",
    [
        ("하다", ["do", "have", "give", "make", "play"]),
        ("가다", ["go", "venture", "do", "climb", "cover"]),
        ("wait", ["기다리다", "참다", "가만", "대기하다", "말이야 방구야"]),
    ],
)
def test_search(search_term: str, expected_outcome: list[str]):
    """Test if Naver dictionary works for 3 cases"""
    assert set(search(search_term)) == set(expected_outcome)
