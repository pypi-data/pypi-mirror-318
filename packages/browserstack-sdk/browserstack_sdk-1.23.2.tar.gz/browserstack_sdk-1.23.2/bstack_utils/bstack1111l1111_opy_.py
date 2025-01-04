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
class bstack11l1ll1l_opy_:
    def __init__(self, handler):
        self._1ll11l1l111_opy_ = None
        self.handler = handler
        self._1ll11l1l1l1_opy_ = self.bstack1ll11l1l11l_opy_()
        self.patch()
    def patch(self):
        self._1ll11l1l111_opy_ = self._1ll11l1l1l1_opy_.execute
        self._1ll11l1l1l1_opy_.execute = self.bstack1ll11l11lll_opy_()
    def bstack1ll11l11lll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᛖ"), driver_command, None, this, args)
            response = self._1ll11l1l111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l1_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᛗ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1ll11l1l1l1_opy_.execute = self._1ll11l1l111_opy_
    @staticmethod
    def bstack1ll11l1l11l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver