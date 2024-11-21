from SpineClass import *

window = pg.window.Window()
#
# label = pg.text.Label('Hi',
#                       font_name='Consolas',
#                       color=(255, 255, 255)
#                       )

# testEntity = SpineEntity(window.width//2, window.height//2)

fishSpine = formFigure('fish')
fishSpine.offset_x = window.width//2
fishSpine.offset_y = window.height//2

squareSpine = formFigure('art2')
squareSpine.offset_x = window.width//2
squareSpine.offset_y = window.height//2


@window.event
def on_draw():
    window.clear()
    # testEntity.draw()
    # testEntity.rotate([x / 100 * ((-1) ** (x // 2)) for x in range(1, 11)])
    # fishSpine.draw()
    squareSpine.draw()
    squareSpine.rotate([0.04, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01])

if __name__ == '__main__':
    pg.app.run()
