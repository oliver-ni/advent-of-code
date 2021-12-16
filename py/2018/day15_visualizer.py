from PIL import Image, ImageColor

from .day15 import Board, Unit

HUES = {"E": 240, "G": 0}


def get_color(unit: Unit):
    return ImageColor.getrgb(f"hsl({HUES[unit.team]}, 100%, {100 - unit.hp * 50 / 200}%)")


class VisualizerBoard(Board):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.t = 0

    def find_nearest(self, source: Unit):
        val = super().find_nearest(source)
        match val:
            case [_, *path, _], _:
                im = self.plot_board()
                for r, c in path:
                    im.putpixel((c, r), (0, 255, 0))
                im.save(f"images/output_{self.t:010}.png")
                self.t += 1
        return val

    def plot_board(self):
        im = Image.new("RGB", (self.num_cols, self.num_rows), (255, 255, 255))
        for r, c in self.walls:
            im.putpixel((c, r), (0, 0, 0))
        for unit, (r, c) in self.units.items():
            im.putpixel((c, r), get_color(unit))
        return im

    def move(self, unit: Unit, raise_on_elf_death: bool = False):
        val = super().move(unit, raise_on_elf_death=raise_on_elf_death)
        # if val:
        #     self.plot_board().save(f"images/output_{self.t:010}.png")
        #     self.t += 1
        return val


def p1(f):
    board = VisualizerBoard.from_str(f.read(), elf_ap=20)
    return board.run_game()
