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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111ll1l111_opy_, bstack111ll11lll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1l111_opy_ = bstack111ll1l111_opy_
        self.bstack111ll11lll_opy_ = bstack111ll11lll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11l11ll1l1_opy_(bstack111ll1111l_opy_):
        bstack111ll111ll_opy_ = []
        if bstack111ll1111l_opy_:
            tokens = str(os.path.basename(bstack111ll1111l_opy_)).split(bstack11l1_opy_ (u"ࠣࡡཻࠥ"))
            camelcase_name = bstack11l1_opy_ (u"ࠤོࠣࠦ").join(t.title() for t in tokens)
            suite_name, bstack111ll11l11_opy_ = os.path.splitext(camelcase_name)
            bstack111ll111ll_opy_.append(suite_name)
        return bstack111ll111ll_opy_
    @staticmethod
    def bstack111ll111l1_opy_(typename):
        if bstack11l1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨཽ") in typename:
            return bstack11l1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧཾ")
        return bstack11l1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨཿ")