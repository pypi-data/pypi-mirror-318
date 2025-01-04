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
from browserstack_sdk.bstack11llll1l_opy_ import bstack11ll111ll1_opy_
from browserstack_sdk.bstack11l111ll1l_opy_ import RobotHandler
def bstack1l11ll111l_opy_(framework):
    if framework.lower() == bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭፩"):
        return bstack11ll111ll1_opy_.version()
    elif framework.lower() == bstack11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭፪"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ፫"):
        import behave
        return behave.__version__
    else:
        return bstack11l1_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ፬")