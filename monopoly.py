import json

def _read_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    content = f.read()
    f.close() 
    return content

def _parse_json(text):
    return json.loads(text)

def load_board(file_path):
    txt = _read_file(file_path)
    return _parse_json(txt)

def load_rolls(file_path):
    txt = _read_file(file_path)
    return _parse_json(txt)

def create_players():
    """
    Create a list of player and wrap the player's attributes into a dictionary,
    set money and position to default values.
    """
    names = ["Peter", "Billy", "Charlotte", "Sweedal"]
    players = []

    for name in names:
        player_dict = {"name": name, "money": 16, "position": 0}
        players.append(player_dict)
    return players

def move_player(player, dice_roll, board_size):
    """Move a player forward by dice_roll steps, wrapping around the board."""
    old_position = player["position"]
    new_position = (old_position + dice_roll) % board_size
    player["position"] = new_position

    # If new position is smaller, it means they passed GO
    if new_position <= old_position:
        player["money"] += 1

def buy_property(player, space):
    """If the space is an unowned property, the player buy it."""
    is_property = space["type"] == "property"
    has_no_owner = space.get("owner") is None

    if is_property and has_no_owner:
        price = space["price"]
        player["money"] = player["money"] - price
        space["owner"] = player["name"]


board = load_board("board.json")
rolls = load_rolls("rolls_1.json")
players = create_players()

total_rolls = len(rolls)
turn_index = 0

while turn_index < total_rolls:
    dice_roll = rolls[turn_index]

    current_player = players[turn_index % len(players)]

    move_player(current_player, dice_roll, len(board))

    landed_on = board[current_player["position"]]["name"]
    print(
        f"{current_player['name']} rolls {dice_roll}, "
        f"lands on {landed_on} "
        f"(position {current_player['position']}), "
        f"money=${current_player['money']}"
    )

    turn_index += 1
