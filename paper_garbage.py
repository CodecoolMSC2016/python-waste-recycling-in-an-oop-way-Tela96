from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name="paper garbage", squeezed=False):

        self.is_squeezed = squeezed
        self.name = name

    def squeeze(self):

        self.is_squeezed = True
