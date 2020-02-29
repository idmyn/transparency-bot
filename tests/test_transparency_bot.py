from transparency_bot import img


def test_calc_dimensions():
    assert img.calc_dimensions(*(81724, 849)) == (512, 5)
    assert img.calc_dimensions(*(413, 212)) == (413, 212)
