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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack111lll111l_opy_ as bstack1lll11ll1_opy_
from browserstack_sdk.bstack11llllll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1ll11111ll_opy_
class bstack11ll111ll1_opy_:
    def __init__(self, args, logger, bstack111ll1l111_opy_, bstack111ll11lll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1l111_opy_ = bstack111ll1l111_opy_
        self.bstack111ll11lll_opy_ = bstack111ll11lll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lll111ll_opy_ = []
        self.bstack111ll1llll_opy_ = None
        self.bstack1l1l1111ll_opy_ = []
        self.bstack111ll1l1ll_opy_ = self.bstack11ll11l1l_opy_()
        self.bstack1lll11l11_opy_ = -1
    def bstack1lllll11ll_opy_(self, bstack111lll11l1_opy_):
        self.parse_args()
        self.bstack111ll1ll11_opy_()
        self.bstack111ll11ll1_opy_(bstack111lll11l1_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111ll1l11l_opy_():
        import importlib
        if getattr(importlib, bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩཛ"), False):
            bstack111ll1l1l1_opy_ = importlib.find_loader(bstack11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧཛྷ"))
        else:
            bstack111ll1l1l1_opy_ = importlib.util.find_spec(bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨཝ"))
    def bstack111ll1ll1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lll11l11_opy_ = -1
        if self.bstack111ll11lll_opy_ and bstack11l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧཞ") in self.bstack111ll1l111_opy_:
            self.bstack1lll11l11_opy_ = int(self.bstack111ll1l111_opy_[bstack11l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨཟ")])
        try:
            bstack111lll11ll_opy_ = [bstack11l1_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫའ"), bstack11l1_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ཡ"), bstack11l1_opy_ (u"ࠫ࠲ࡶࠧར")]
            if self.bstack1lll11l11_opy_ >= 0:
                bstack111lll11ll_opy_.extend([bstack11l1_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ལ"), bstack11l1_opy_ (u"࠭࠭࡯ࠩཤ")])
            for arg in bstack111lll11ll_opy_:
                self.bstack111ll1ll1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111ll1ll11_opy_(self):
        bstack111ll1llll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll1llll_opy_ = bstack111ll1llll_opy_
        return bstack111ll1llll_opy_
    def bstack1l1ll1111l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111ll1l11l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1ll11111ll_opy_)
    def bstack111ll11ll1_opy_(self, bstack111lll11l1_opy_):
        bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
        if bstack111lll11l1_opy_:
            self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫཥ"))
            self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠨࡖࡵࡹࡪ࠭ས"))
        if bstack1l1l1lll1_opy_.bstack111lll1111_opy_():
            self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨཧ"))
            self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠪࡘࡷࡻࡥࠨཨ"))
        self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠫ࠲ࡶࠧཀྵ"))
        self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪཪ"))
        self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨཫ"))
        self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧཬ"))
        if self.bstack1lll11l11_opy_ > 1:
            self.bstack111ll1llll_opy_.append(bstack11l1_opy_ (u"ࠨ࠯ࡱࠫ཭"))
            self.bstack111ll1llll_opy_.append(str(self.bstack1lll11l11_opy_))
    def bstack111ll11l1l_opy_(self):
        bstack1l1l1111ll_opy_ = []
        for spec in self.bstack1lll111ll_opy_:
            bstack1l111l1l11_opy_ = [spec]
            bstack1l111l1l11_opy_ += self.bstack111ll1llll_opy_
            bstack1l1l1111ll_opy_.append(bstack1l111l1l11_opy_)
        self.bstack1l1l1111ll_opy_ = bstack1l1l1111ll_opy_
        return bstack1l1l1111ll_opy_
    def bstack11ll11l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111ll1l1ll_opy_ = True
            return True
        except Exception as e:
            self.bstack111ll1l1ll_opy_ = False
        return self.bstack111ll1l1ll_opy_
    def bstack1lllllll1_opy_(self, bstack111lll1ll1_opy_, bstack1lllll11ll_opy_):
        bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ཮")] = self.bstack111ll1l111_opy_
        multiprocessing.set_start_method(bstack11l1_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩ཯"))
        bstack1l111ll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l1l1llll_opy_ = manager.list()
        if bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ཰") in self.bstack111ll1l111_opy_:
            for index, platform in enumerate(self.bstack111ll1l111_opy_[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨཱ")]):
                bstack1l111ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111lll1ll1_opy_,
                                                            args=(self.bstack111ll1llll_opy_, bstack1lllll11ll_opy_, bstack1l1l1llll_opy_)))
            bstack111lll1l1l_opy_ = len(self.bstack111ll1l111_opy_[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴིࠩ")])
        else:
            bstack1l111ll1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111lll1ll1_opy_,
                                                        args=(self.bstack111ll1llll_opy_, bstack1lllll11ll_opy_, bstack1l1l1llll_opy_)))
            bstack111lll1l1l_opy_ = 1
        i = 0
        for t in bstack1l111ll1_opy_:
            os.environ[bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ཱིࠧ")] = str(i)
            if bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶུࠫ") in self.bstack111ll1l111_opy_:
                os.environ[bstack11l1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃཱུࠪ")] = json.dumps(self.bstack111ll1l111_opy_[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྲྀ")][i % bstack111lll1l1l_opy_])
            i += 1
            t.start()
        for t in bstack1l111ll1_opy_:
            t.join()
        return list(bstack1l1l1llll_opy_)
    @staticmethod
    def bstack1lll1llll1_opy_(driver, bstack111lll1l11_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨཷ"), None)
        if item and getattr(item, bstack11l1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧླྀ"), None) and not getattr(item, bstack11l1_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨཹ"), False):
            logger.info(
                bstack11l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨེ"))
            bstack111ll1lll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll11ll1_opy_.bstack1l1l1l111l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)