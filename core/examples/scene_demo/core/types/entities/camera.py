from pygame import Rect


class Camera(object):
    def __init__(self, width, height):
        # self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        try:
            return target.rect.move(self.state.topleft)
        except AttributeError:
            return map(sum, zip(target, self.state.topleft))

    def update(self, target):
        self.state = self.complex_camera(target.rect)

    def complex_camera(self, target_rect):
        from core.examples.scene_demo.core.consts import (
            HALF_HEIGHT,
            HALF_WIDTH,
            WIN_HEIGHT,
            WIN_WIDTH,
        )

        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

        l = min(0, l)  # stop scrolling left
        l = max(-(self.state.width - WIN_WIDTH), l)  # stop scrolling right
        t = max(-(self.state.height - WIN_HEIGHT), t)  # stop scrolling bottom

        return Rect(l, t, w, h)
