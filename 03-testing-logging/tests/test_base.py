import search 

import logging

import pytest

@pytest.mark.parametrize('numbers,target,expected', [
    ([1, 2, 4, 5, 7], 4, 2),
    ([1, 2, 4, 4, 4, 5, 7], 4, 3),
    ([1, 2, 4, 4, 4, 5, 7], 5, 5) 
])
def test_basic(numbers, target, expected):
    assert search.binary_search(numbers, target) == expected

def test_with_f(numbers_f):
    assert search.binary_search(numbers_f, 2) == 1
    numbers_f.append(0)

def test_with_f_2_and_logs(numbers_f, caplog):
    with caplog.at_level(logging.WARNING):
        assert search.binary_search(numbers_f, 2) == 1
 
    assert 'start' in caplog.messages

def test_value_error():
    with pytest.raises(ValueError, match='numbers must be sorted'):
        search.binary_search([10, 1, 2, 4, 5, 7], 4)

def test_lookup_error():
    with pytest.raises(LookupError, match='100500'):
        search.binary_search([ 1, 2, 4, 5, 7], 100500)


def test_with_f_and_time(numbers_f, caplog, monkeypatch):
    x = iter([0.1, 0.2, 0.3])
    monkeypatch.setattr(search, 'perf_counter', lambda: next(x))
    with caplog.at_level(logging.DEBUG):
        assert search.binary_search(numbers_f, 2) == 1

    my_caplog_record = next(r for r in caplog.records if r.levelname == 'DEBUG')

    assert pytest.approx(my_caplog_record.elapsed) == 0.2

