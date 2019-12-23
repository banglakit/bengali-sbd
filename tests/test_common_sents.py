import bengali_sbd


def test_no_punct():
    assert bengali_sbd.split('আমি বাংলায় গান গাই তুমি কি কর') == ['আমি বাংলায় গান গাই তুমি কি কর']


def test_terminal_punct_at_end():
    assert bengali_sbd.split('আমি বাংলায় গান গাই।') == ['আমি বাংলায় গান গাই।']


def test_terminal_punct_in_text():
    assert bengali_sbd.split('আমি বাংলায় গান গাই। তুমি কই যাও?') == ['আমি বাংলায় গান গাই।', 'তুমি কই যাও?']
