from pathlib import Path
from parser import darkest_parser


def test_game_darkest():
    for i in Path(r"D:\play_ground\DarkestDungeon").rglob("*.darkest"):
        try:
            text = open(i).read() + "\n"
        except Exception:
            continue
        print(i)
        darkest_parser.parse(text)


if __name__ == "__main__":
    test_game_darkest()
