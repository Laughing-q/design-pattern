from abc import abstractmethod, ABCMeta


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f"{self.face}, {self.body}, {self.arm}, {self.leg}"


class PlayerBulder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBulder):
    def __init__(self) -> None:
        super().__init__()
        self.player = Player()

    def build_face(self):
        self.player.face = "beautiful face"

    def build_body(self):
        self.player.body = "slender"

    def build_arm(self):
        self.player.arm = "small"

    def build_leg(self):
        self.player.leg = "long"


class Monster(PlayerBulder):
    def __init__(self) -> None:
        super().__init__()
        self.player = Player()

    def build_face(self):
        self.player.face = "monster face"

    def build_body(self):
        self.player.body = "huge"

    def build_arm(self):
        self.player.arm = "big"

    def build_leg(self):
        self.player.leg = "short"

# 控制组装顺序
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player

# client
# builder = SexyGirlBuilder()
builder = Monster()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
