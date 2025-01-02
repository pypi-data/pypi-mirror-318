from .tab_cls import TabCls
from .window_cls import WindowCls

class Api:
    def __init__(self) -> None:
        self.tab = TabCls()
        self.window = WindowCls()

oper = Api()
