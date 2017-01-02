from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name="plastic garbage", clean=False):

        self.name = name
        self.is_clean = clean

    def clean(self):

        self.is_clean = True
