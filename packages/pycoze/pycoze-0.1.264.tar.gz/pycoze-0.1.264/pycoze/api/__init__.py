from .lib.window_cls import WindowCls

class Api:
    def __init__(self) -> None:
        self.window = WindowCls()

oper = Api()

# from ps_view import ViewCls, WebsiteViewCls, FileViewCls, DirectoryViewCls, WorkflowCls