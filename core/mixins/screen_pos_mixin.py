from core.types.entities import Entity
from core.types.interfaces import (
    IMaterial,
    IRender,
)


class ScreenPosMixin(IMaterial, IRender):
    # FIXME: !!!
    BORDER_INACCURACY = 16

    def __init__(self, x, y, width, height):
        # for @property#position_info
        super().__init__(x, y, width, height)
        self._position_info = None

    @property
    def is_inside_the_screen(self):
        return not any(self.__passed_states)

    @property
    def __passed_states(self):
        return [
            self.left_border_passed,
            self.right_border_passed,
            self.top_border_passed,
            self.bottom_border_passed,
        ]

    @property
    def position_info(self):
        labels = [("OUT" if state else "INN") for state in self.__passed_states]
        info = "L:{L} | R:{R} | T:{T} | B:{B}".format(
            L=labels[0],
            R=labels[1],
            T=labels[2],
            B=labels[3],

        )

        IS_UNDEFINED = self._position_info is None
        IS_CHANGED = self._position_info != info
        if IS_UNDEFINED or IS_CHANGED:
            self._position_info = info
            # print(":::", self._position_info)
            return info

        return None

    @property
    def left_border_passed(self):
        return self.rect.left <= self.screen.rect.left + self.BORDER_INACCURACY

    @property
    def right_border_passed(self):
        return self.rect.right >= self.screen.rect.right - self.BORDER_INACCURACY

    @property
    def top_border_passed(self):
        return self.rect.top <= self.screen.rect.top + self.BORDER_INACCURACY

    @property
    def bottom_border_passed(self):
        return self.rect.bottom >= self.screen.rect.bottom - self.BORDER_INACCURACY
