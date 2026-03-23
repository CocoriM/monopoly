import json
import sys


NAMES = ["Peter", "Billy", "Charlotte", "Sweedal"]
STARTING_MONEY = 16
STARTING_POSITION = 0
GO_MONNEY = 1
RENT_MUTLIPLYER = 2


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def create_players():
    """
    Create a list of player and wrap the player's attributes into a dictionary,
    set money and position to default values.
    """
    return [
        {"name": name, "money": STARTING_MONEY, "position": STARTING_POSITION}
        for name in NAMES
    ]


def buy_property(player, space):
    """If the space is an unowned property, the player buys it"""
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
    """If the space is owned by someone else, pay rent to the owner"""
    is_property = space["type"] == "property"
    has_owner = space.get("owner") is not None
    is_not_mine = space.get("owner") != player["name"]

    if is_property and has_owner and is_not_mine:
        rent = space["price"]
        # Double rent if owner has all properties of this colour
        if owns_all_of_colour(space["owner"], space["colour"], board):
            rent *= RENT_MUTLIPLYER
        player["money"] = player["money"] - rent
        # Find the owner and give them the rent
        for player in players:
            if player["name"] == space["owner"]:
                player["money"] = player["money"] + rent


def find_winner(players):
    """Find the player with the most money"""
    winner = players[0]
    for player in players:
        if player["money"] > winner["money"]:
            winner = player
    return winner


def is_bankrupt(player):
    """A player is bankrupt if their money goes below zero."""
    return player["money"] < 0


def move_player(player, dice_roll, board_size):
    """Move a player forward by dice_roll steps, wrapping around the board."""
    old_position = player["position"]
    new_position = (old_position + dice_roll) % board_size
    player["position"] = new_position

    # If new position is smaller, it means they passed GO
    if new_position <= old_position:
        player["money"] += GO_MONNEY


def play_game(board_file, rolls_file):
    """Run one complete game with the given board and rolls files."""
    board = load_json(board_file)
    rolls = load_json(rolls_file)
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

        if is_bankrupt(current_player):
            print(f"{current_player['name']} is bankrupt!")
            break

        landed_on = landed_space["name"]
        print(
            f"{current_player['name']} rolls {dice_roll}, "
            f"lands on {landed_on} "
            f"(position {current_player['position']}), "
            f"money=${current_player['money']}"
        )

        turn_index += 1

    # Game over - print results
    print(f"\n=== Game Over ===")
    for player in players:
        space_name = board[player["position"]]["name"]
        print(f"  {player['name']}: money=${player['money']}, position={space_name}")

    winner = find_winner(players)
    print(f"Winner: {winner['name']} with ${winner['money']}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        board_file = sys.argv[1]
        rolls_file = sys.argv[2]
        play_game(board_file, rolls_file)
    else:
        print("Usage: python3 monopoly.py <board_file> <rolls_file>")
