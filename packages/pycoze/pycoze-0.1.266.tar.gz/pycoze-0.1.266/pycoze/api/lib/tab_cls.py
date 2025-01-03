import os
from uuid import uuid4
from view import ViewCls, WebsiteViewCls, FileViewCls, DirectoryViewCls, WorkflowCls
import time
from typing import Union
from pycoze import utils


socket = utils.socket

class TabCls:

    def open_path(self, item_path: str) -> FileViewCls | DirectoryViewCls:
        if not os.path.isabs(item_path):
            item_path = os.path.abspath(item_path)
        if os.path.isdir(item_path):
            return self.open_dir(item_path)
        else:
            return self.open_file(item_path)

    def open_file(self, item_path: str) -> Union[FileViewCls, WebsiteViewCls, WorkflowCls]:
        if not os.path.isabs(item_path):
            item_path = os.path.abspath(item_path)
        location = ["FileOrDir", item_path]
        socket.post("add-tab", {"location": location, "name": os.path.basename(item_path)})
        lower_suffix = item_path.lower().split(".")[-1]
        if lower_suffix == 'workflow':
            return WorkflowCls(location)
        if len(location) > 1 and (location[0] == "Website" or location[1].endswith(".website") or location[1].endswith(".html") or location[1].endswith(".ipynb")):
            return WebsiteViewCls(location)
        return FileViewCls(location)

    def open_dir(self, item_path: str) -> DirectoryViewCls:
        if not os.path.isabs(item_path):
            item_path = os.path.abspath(item_path)
        location = ["FileOrDir", item_path]
        socket.post("add-tab", {"location": location, "name": os.path.basename(item_path)})
        return DirectoryViewCls(location)

    def open_website(self, url: str, uid:str=None) -> WebsiteViewCls:
        if uid is None:
            uid = str(uuid4())
        location = ["Website", url, uid]
        socket.post("add-tab", {"location": location, "name": url})
        return WebsiteViewCls(location)
    
    def get_active(self) -> ViewCls:
        result = socket.post_and_recv_result("get-active-tab", {})
        return self._result_to_view(result)

    def _result_to_view(self, result: list[str]) -> ViewCls:
        if result[0] == "Website":
            return WebsiteViewCls(result)
        elif result[0] == "FileOrDir":
            if os.path.isdir(result[1]):
                return DirectoryViewCls(result)
            else:
                if result[1].lower().split(".")[-1] == 'workflow':
                    return WorkflowCls(result)
                return FileViewCls(result)
        return ViewCls(result)
    
    def wait_for_tab_open(self, location: list[str] | ViewCls):
        times = 0
        while not self.is_tab_open(location):
            time.sleep(0.01)
            times += 1
            if times > 1000:
                raise Exception("Tab open timeout")

    def get_all(self) -> list[ViewCls]:
        results = socket.post_and_recv_result("get-all-tabs", {})
        return [self._result_to_view(result) for result in results]

    def close_tab(self, location: list[str] | ViewCls):
        if isinstance(location, ViewCls):
            location = location.location
        self.wait_for_tab_open(location)
        socket.post("close-tab", {"location": location})

    def switch_tab(self, location: list[str] | ViewCls):
        if isinstance(location, ViewCls):
            location = location.location
        self.wait_for_tab_open(location)
        socket.post("switchTab", {"location": location})

    def is_tab_open(self, location: list[str] | ViewCls):
        if isinstance(location, ViewCls):
            location = location.location
        result = socket.post_and_recv_result("is-tab-open", {"location": location})
        return result

    def pin_tab(self, location: list[str] | ViewCls):
        if isinstance(location, ViewCls):
            location = location.location
        self.wait_for_tab_open(location)
        socket.post("pin-tab", {"location": location})

    def unpin_tab(self, location: list[str] | ViewCls):
        if isinstance(location, ViewCls):
            location = location.location
        self.wait_for_tab_open(location)
        socket.post("unpin-tab", {"location": location})
