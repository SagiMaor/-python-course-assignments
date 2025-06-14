from color_module import choose_color

def test_choose_color_valid():
    assert choose_color(['Red', 'Blue', 'Green'], 1) == 'Red'

def test_choose_color_out_of_range():
    assert choose_color(['Red'], 5) is None
