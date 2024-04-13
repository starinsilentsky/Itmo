def test_equal_tuples():
    assert ('home', 'work') == ('home', 'work')

def test_not_equal_strings():
    assert not ('QC') == ('QA')

def test_not_equal_lists():
    assert (1, 1, 2, 3, 5) != (2, 3, 5)
