from monopoly import move_player, buy_property, pay_rent, is_bankrupt


def test_move_player_basic():
    player = {"name": "Test", "money": 16, "position": 0}
    move_player(player, 3, 9)
    assert player["position"] == 3


def test_move_player_wraps_around_and_gets_go_bonus():
    player = {"name": "Test", "money": 16, "position": 7}
    move_player(player, 3, 9)
    # 7 + 3 = 10, 10 % 9 = 1, wrapped around
    assert player["position"] == 1
    # Passed GO, should get $1
    assert player["money"] == 17


def test_buy_property():
    player = {"name": "Test", "money": 16, "position": 1}
    space = {"name": "The Burvale", "price": 1, "colour": "Brown", "type": "property"}
    buy_property(player, space)
    assert player["money"] == 15
    assert space["owner"] == "Test"


def test_pay_rent_basic():
    player = {"name": "Billy", "money": 16, "position": 1}
    owner = {"name": "Peter", "money": 16, "position": 0}
    players = [owner, player]
    space = {"name": "The Burvale", "price": 1, "colour": "Brown", "type": "property", "owner": "Peter"}
    board = [
        {"name": "GO", "type": "go"},
        space,
        {"name": "Fast Kebabs", "price": 1, "colour": "Brown", "type": "property"},
    ]
    pay_rent(player, space, players, board)
    assert player["money"] == 15   
    # Billy paid $1
    assert owner["money"] == 17    
    # Peter received $1


def test_pay_rent_double_when_owns_all_colour():
    player = {"name": "Billy", "money": 16, "position": 1}
    owner = {"name": "Peter", "money": 16, "position": 0}
    players = [owner, player]
    space = {"name": "The Burvale", "price": 1, "colour": "Brown", "type": "property", "owner": "Peter"}
    board = [
        {"name": "GO", "type": "go"},
        space,
        {"name": "Fast Kebabs", "price": 1, "colour": "Brown", "type": "property", "owner": "Peter"},
    ]
    pay_rent(player, space, players, board)
    assert player["money"] == 14   
    # Billy paid $1 * 2 = $2
    assert owner["money"] == 18    
    # Peter received $2


def test_is_bankrupt():
    player_broke = {"name": "Test", "money": -1, "position": 0}
    player_ok = {"name": "Test2", "money": 0, "position": 0}
    assert is_bankrupt(player_broke) == True
    assert is_bankrupt(player_ok) == False
