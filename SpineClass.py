import numpy as np
import pyglet as pg
from typing import Literal


class Branch:
    def __init__(self, newVector: tuple = (0, 0), newOrigin=None):
        self.image: str | None = None
        self.vector: np.array = np.array(newVector)
        self.origin: Branch | None = newOrigin
        self.tip: np.array = None
        self.relative_offset: np.array = np.array((0, 0))
        # self.color : tuple[int, int, int] = (255, 0, 0)
        self.getTip()

    def setOrigin(self, newOrigin):
        self.origin = newOrigin
        self.getTip()

    def increaseSize(self, multiplier):
        self.vector[0] *= multiplier
        self.vector[1] *= multiplier

    def getTip(self):
        if self.origin is not None:
            self.tip = self.origin.getTip() + self.vector
        else:
            self.tip = self.vector

        return self.tip

    def draw(self, offset_x, offset_y):
        x = 0
        y = 0
        if self.origin is not None:
            # x, y = self.origin.getTip()
            x, y = self.origin.tip

        o = pg.shapes.Circle(x=x + offset_x, y=y + offset_y, radius=5, color=(255, 0, 0))
        t = pg.shapes.Line(x=x + offset_x,
                           y=y + offset_y,
                           x2=x + offset_x + self.vector[0],
                           y2=y + offset_y + self.vector[1],
                           color=(0, 255, 0),
                           width=3)
        t.draw()
        o.draw()

    def render(self):
        pass


class SpineEntity:
    def __init__(self, offset_x: int = 0, offset_y: int = 0):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.branchList: list[Branch] = []

    def addBranch(self, newBranch: Branch, originIndex: int = -1, atOrigin: bool = False):
        if originIndex == -1 and len(self.branchList) > 0:
            originIndex += len(self.branchList)
        else:
            originIndex = max(min(originIndex, len(self.branchList)), 0)

        if not atOrigin and len(self.branchList) != 0:
            newBranch.setOrigin(self.branchList[originIndex])

        self.branchList.append(newBranch)

    def move(self, x, y):
        self.offset_x += x
        self.offset_y += y

    def draw(self):
        for b in self.branchList:
            b.draw(self.offset_x, self.offset_y)

    def rotate(self, theta: list):
        if len(theta) != len(self.branchList):
            return

        for i in range(len(self.branchList)):
            self.branchList[i].vector = np.dot(np.array([[np.cos(theta[i]), -np.sin(theta[i])], [np.sin(theta[i]), np.cos(theta[i])]]), self.branchList[i].vector)

        for b in self.branchList:
            b.getTip()


def formFigure(figureName: Literal['fish', '4legs', '2legs', 'human', 'art1', 'art2']):
    spen = SpineEntity()
    if figureName == 'fish':
        spen.addBranch(Branch((-60, 0)), atOrigin=True)
        spen.addBranch(Branch((-60, 0)), 0)
        spen.addBranch(Branch((-30, 30)), 0)
        spen.addBranch(Branch((-30, -30)), 0)
        spen.addBranch(Branch((-50, 50)), 1)
        spen.addBranch(Branch((-50, -50)), 1)

    elif figureName == 'art1':
        spen.addBranch(Branch((50, -50)))
        spen.addBranch(Branch((45, -45)))
        spen.addBranch(Branch((40, -40)))
        spen.addBranch(Branch((35, -35)))
        spen.addBranch(Branch((30, -30)))
        spen.addBranch(Branch((25, -25)))
        spen.addBranch(Branch((20, -20)))
        spen.addBranch(Branch((15, -15)))
        spen.addBranch(Branch((10, -10)))
        spen.addBranch(Branch((5, -5)))

    elif figureName == 'art2':
        spen.addBranch(Branch((50, 0)), atOrigin=True)
        spen.addBranch(Branch((0, 50)), atOrigin=True)
        spen.addBranch(Branch((50, 0)), 1)
        spen.addBranch(Branch((0, 50)), 0)
        spen.addBranch(Branch((40, 0)), 3)
        spen.addBranch(Branch((0, 40)), 3)
        spen.addBranch(Branch((40, 0)), 5)
        spen.addBranch(Branch((0, 40)), 4)
        spen.addBranch(Branch((30, 0)), 7)
        spen.addBranch(Branch((0, 30)), 7)
        spen.addBranch(Branch((30, 0)), 9)
        spen.addBranch(Branch((0, 30)), 8)
        spen.addBranch(Branch((20, 0)), 11)
        spen.addBranch(Branch((0, 20)), 11)
        spen.addBranch(Branch((20, 0)), 13)
        spen.addBranch(Branch((0, 20)), 12)

    return spen


if __name__ == '__main__':
    print("test")
