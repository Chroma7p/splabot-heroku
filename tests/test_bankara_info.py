

def test_bankara_info_open():
    import sys
    sys.path.append('./')
    from get_bankara_info import maketext
    txt = maketext(True)
    assert txt != "情報の取得に失敗しました"
    assert "バンカラオープン" in txt


def test_bankara_info_challenge():
    import sys
    sys.path.append('./')
    from get_bankara_info import maketext
    txt = maketext(False)
    assert txt != "情報の取得に失敗しました"
    assert "バンカラチャレンジ" in txt
