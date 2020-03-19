import finalProduct as gm

def test_snake_isValid():
    player = gm.Snake(4, (90, 0, 90))
    assert player.isValid(0, 0)

def test_snake_ateFruit():
    player = gm.Snake(4, (90, 0, 90))
    player.ateFruit()
    assert player.pause == 315

def test_moveFruit():
    player2 = gm.Snake(4, (90, 0, 90))
    gm.apple.x = -1
    gm.apple.y = -1
    gm.moveFruit(player2)
    assert gm.apple.x != -1 and gm.apple.y != -1

def test_now():
    assert gm.now() > 0
