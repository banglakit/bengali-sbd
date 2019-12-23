import pytest

import bengali_sbd


def test_no_punct():
    assert list(bengali_sbd.split('আমি বাংলায় গান গাই তুমি কি কর')) == ['আমি বাংলায় গান গাই তুমি কি কর']


def test_terminal_punct_at_end():
    assert list(bengali_sbd.split('আমি বাংলায় গান গাই।')) == ['আমি বাংলায় গান গাই।']


def test_terminal_punct_without_space():
    assert list(bengali_sbd.split('আমি বাংলায় গান গাই।তিনি তা জানেন।')) == ['আমি বাংলায় গান গাই।', 'তিনি তা জানেন।']


@pytest.mark.parametrize('given,out', [
    (
            'আমি বাংলায় গান গাই। তুমি কই যাও?',
            ['আমি বাংলায় গান গাই।', 'তুমি কই যাও?']
    ),
    (
            'বাবা, তোমার সাথে যাব! আমার সাথে যাবে না তুমি? আমি রাগ করব।',
            ['বাবা, তোমার সাথে যাব!', 'আমার সাথে যাবে না তুমি?', 'আমি রাগ করব।']
    )
])
def test_terminal_punct_in_text(given, out):
    assert list(bengali_sbd.split(given)) == out
