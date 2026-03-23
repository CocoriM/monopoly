## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)


### Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?


The specifics and implementation of this code is completely up to you!

### What we are looking for:
* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code.  You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.
# monopoly

---

# My Solution

## How to run

Run a game with a board file and a dice rolls file:

```bash
python3 monopoly.py board.json rolls_1.json
```

You can also use a different set of dice rolls:

```bash
python3 monopoly.py board.json rolls_2.json
```

## How to run tests

```bash
python3 -m pytest test_monopoly.py -v
```

## How I built this

I broke the game into small steps and built them one at a time:

1. Load the board and dice rolls from JSON files.
2. Create 4 players, each starting with $16 at the GO space.
3. Players take turns rolling a dice and moving forward. The board wraps around.
4. When a player passes GO, they get $1.
5. If a player lands on a property with no owner, they buy it automatically.
6. If a player lands on someone else's property, they pay rent equal to the price.
7. If the owner has all properties of the same colour, rent is doubled.
8. When a player's money goes below $0, they are bankrupt and the game ends.
9. The player with the most money wins.

## Design decisions

- I used **dictionaries** to represent players and board spaces. They are simple and easy to read. I did not use classes because there was no need for methods or complex behaviour.
- I used a **list** to store players, because the game needs a fixed turn order.
- I kept everything in **one file** because the project is small. Splitting into multiple files would just make it harder to follow.
- The game logic is wrapped in a `play_game()` function, so it is easy to run multiple games with different dice rolls.
