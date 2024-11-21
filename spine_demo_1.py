from SpineClass import *

window = pg.window.Window()
#
# label = pg.text.Label('Hi',
#                       font_name='Consolas',
#                       color=(255, 255, 255)
#                       )

testEntity = SpineEntity(window.width//2, window.height//2)
testEntity.addBranch(Branch((50, -50)))
testEntity.addBranch(Branch((45, -45)))
testEntity.addBranch(Branch((40, -40)))
testEntity.addBranch(Branch((35, -35)))
testEntity.addBranch(Branch((30, -30)))
testEntity.addBranch(Branch((25, -25)))
testEntity.addBranch(Branch((20, -20)))
testEntity.addBranch(Branch((15, -15)))
testEntity.addBranch(Branch((10, -10)))
testEntity.addBranch(Branch((5, -5)))


@window.event
def on_draw():
    window.clear()
    testEntity.draw()
    # br.draw(0, 0)
    testEntity.rotate([x / 100 * ((-1) ** (x // 2)) for x in range(1, 11)])


if __name__ == '__main__':
    pg.app.run()
