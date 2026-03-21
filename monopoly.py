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


def owns_all_of_colour(owner_name, colour, board):
    """Check if a player owns all properties of a given colour."""
    for space in board:
        is_same_colour = space.get("colour") == colour
        owned_by_someone_else = space.get("owner") != owner_name
        if is_same_colour and owned_by_someone_else:
            return False
    return True


def pay_rent(player, space, players, board):
    """If the space is owned by someone else, pay rent to the owner."""
    is_property = space["type"] == "property"
    has_owner = space.get("owner") is not None
    is_not_mine = space.get("owner") != player["name"]

    if is_property and has_owner and is_not_mine:
        rent = space["price"]
        # Double rent if owner has all properties of this colour
        if owns_all_of_colour(space["owner"], space["colour"], board):
            rent = rent * 2
        player["money"] = player["money"] - rent
        # Find the owner and give them the rent
        for p in players:
            if p["name"] == space["owner"]:
                p["money"] = p["money"] + rent


board = load_board("board.json")
rolls = load_rolls("rolls_1.json")
players = create_players()

total_rolls = len(rolls)
turn_index = 0

while turn_index < total_rolls:
    dice_roll = rolls[turn_index]

    current_player = players[turn_index % len(players)]

    move_player(current_player, dice_roll, len(board))

    landed_space = board[current_player["position"]]
    buy_property(current_player, landed_space)
    pay_rent(current_player, landed_space, players, board)
    
    print(
        f"{current_player['name']} rolls {dice_roll}, "
        f"lands on {landed_on} "
        f"(position {current_player['position']}), "
        f"money=${current_player['money']}"
    )

    turn_index += 1
