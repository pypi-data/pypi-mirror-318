# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack1l1ll1l_opy_ = 7
def bstack11l1_opy_ (bstack1l111l_opy_):
    global bstack11lll_opy_
    bstack1l11111_opy_ = ord (bstack1l111l_opy_ [-1])
    bstack111l1_opy_ = bstack1l111l_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l11111_opy_ % len (bstack111l1_opy_)
    bstack11l1l1_opy_ = bstack111l1_opy_ [:bstack1l1llll_opy_] + bstack111l1_opy_ [bstack1l1llll_opy_:]
    if bstack111111l_opy_:
        bstack11l111_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack1111l1l_opy_ + bstack1l11111_opy_) % bstack1l1ll1l_opy_) for bstack1111l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l111_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack1111l1l_opy_ + bstack1l11111_opy_) % bstack1l1ll1l_opy_) for bstack1111l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l111_opy_)
import threading
bstack1ll11l1ll1l_opy_ = 1000
bstack1ll11l1ll11_opy_ = 5
bstack1ll11ll1l11_opy_ = 30
bstack1ll11l1l1ll_opy_ = 2
class bstack1ll11ll1111_opy_:
    def __init__(self, handler, bstack1ll11ll11ll_opy_=bstack1ll11l1ll1l_opy_, bstack1ll11ll1ll1_opy_=bstack1ll11l1ll11_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1ll11ll11ll_opy_ = bstack1ll11ll11ll_opy_
        self.bstack1ll11ll1ll1_opy_ = bstack1ll11ll1ll1_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1ll11l1lll1_opy_()
    def bstack1ll11l1lll1_opy_(self):
        self.timer = threading.Timer(self.bstack1ll11ll1ll1_opy_, self.bstack1ll11ll111l_opy_)
        self.timer.start()
    def bstack1ll11ll11l1_opy_(self):
        self.timer.cancel()
    def bstack1ll11l1llll_opy_(self):
        self.bstack1ll11ll11l1_opy_()
        self.bstack1ll11l1lll1_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1ll11ll11ll_opy_:
                t = threading.Thread(target=self.bstack1ll11ll111l_opy_)
                t.start()
                self.bstack1ll11l1llll_opy_()
    def bstack1ll11ll111l_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1ll11ll11ll_opy_]
        del self.queue[:self.bstack1ll11ll11ll_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1ll11ll11l1_opy_()
        while len(self.queue) > 0:
            self.bstack1ll11ll111l_opy_()