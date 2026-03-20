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

board = load_board("board.json")
rolls = load_rolls("rolls_1.json")

print("=== 棋盘 ===")
for i, space in enumerate(board):
    print(f"  格子 {i}: {space}")

print(f"\n=== 骰子 (共 {len(rolls)} 个) ===")
print(f"  前10个: {rolls[:10]}")


# def make_players():
#     """
#     Create a list of player and wrap the player's attributes into a dictionary,
#     set money and position to default values.
#     """
#     players = []

#     for n in names:
#         player_dict = {"name": n, "money": 16, "position": 0}
#         players.append(player_dict)
#     return players


# def colour_properties(board, colour):
#     """
#     type and colour are the keys in each square on the board.
#     board is a list of dictionaries.
#     colour specifies the colour to match.
#     with these two parameters, return all squares whose type is "property" and whose colour matches the given colour.
#     """
#     indices = []
    
#     for i, square in enumerate(board):
#         if square["type"] == "property" and square["colour"] == colour:
#             indices.append(i)
#     return indices

# def owns_all_colour(board, owner, colour):
#     colour_indices = colour_properties(board, colour)

#     for idx in colour_indices:
#         square = board[idx]
#         square_owner = square.get("owner")
#         if square_owner != owner:
#             return False
#     return True
