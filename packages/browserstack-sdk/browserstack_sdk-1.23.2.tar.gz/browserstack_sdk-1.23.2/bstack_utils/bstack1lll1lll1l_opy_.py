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
from collections import deque
from bstack_utils.constants import *
class bstack1l11ll1l_opy_:
    def __init__(self):
        self._1ll1l1ll1ll_opy_ = deque()
        self._1ll1l1ll1l1_opy_ = {}
        self._1ll1l1lllll_opy_ = False
    def bstack1ll1ll111l1_opy_(self, test_name, bstack1ll1ll11111_opy_):
        bstack1ll1l1lll11_opy_ = self._1ll1l1ll1l1_opy_.get(test_name, {})
        return bstack1ll1l1lll11_opy_.get(bstack1ll1ll11111_opy_, 0)
    def bstack1ll1l1l1lll_opy_(self, test_name, bstack1ll1ll11111_opy_):
        bstack1ll1l1lll1l_opy_ = self.bstack1ll1ll111l1_opy_(test_name, bstack1ll1ll11111_opy_)
        self.bstack1ll1l1ll11l_opy_(test_name, bstack1ll1ll11111_opy_)
        return bstack1ll1l1lll1l_opy_
    def bstack1ll1l1ll11l_opy_(self, test_name, bstack1ll1ll11111_opy_):
        if test_name not in self._1ll1l1ll1l1_opy_:
            self._1ll1l1ll1l1_opy_[test_name] = {}
        bstack1ll1l1lll11_opy_ = self._1ll1l1ll1l1_opy_[test_name]
        bstack1ll1l1lll1l_opy_ = bstack1ll1l1lll11_opy_.get(bstack1ll1ll11111_opy_, 0)
        bstack1ll1l1lll11_opy_[bstack1ll1ll11111_opy_] = bstack1ll1l1lll1l_opy_ + 1
    def bstack1l1ll1ll1_opy_(self, bstack1ll1l1l1l1l_opy_, bstack1ll1l1llll1_opy_):
        bstack1ll1ll1111l_opy_ = self.bstack1ll1l1l1lll_opy_(bstack1ll1l1l1l1l_opy_, bstack1ll1l1llll1_opy_)
        event_name = bstack1111l111ll_opy_[bstack1ll1l1llll1_opy_]
        bstack1ll1l1l1ll1_opy_ = bstack11l1_opy_ (u"ࠤࡾࢁ࠲ࢁࡽ࠮ࡽࢀࠦᙙ").format(bstack1ll1l1l1l1l_opy_, event_name, bstack1ll1ll1111l_opy_)
        self._1ll1l1ll1ll_opy_.append(bstack1ll1l1l1ll1_opy_)
    def bstack1lllll1ll1_opy_(self):
        return len(self._1ll1l1ll1ll_opy_) == 0
    def bstack1l1l111ll1_opy_(self):
        bstack1ll1l1ll111_opy_ = self._1ll1l1ll1ll_opy_.popleft()
        return bstack1ll1l1ll111_opy_
    def capturing(self):
        return self._1ll1l1lllll_opy_
    def bstack11llllll1_opy_(self):
        self._1ll1l1lllll_opy_ = True
    def bstack1l1ll111l1_opy_(self):
        self._1ll1l1lllll_opy_ = False