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
import logging
import bstack_utils.bstack111lll111l_opy_ as bstack1lll11ll1_opy_
from bstack_utils.helper import bstack1l1lll1lll_opy_
logger = logging.getLogger(__name__)
def bstack1l111lll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l1l1lll11_opy_(context, *args):
    tags = getattr(args[0], bstack11l1_opy_ (u"࠭ࡴࡢࡩࡶࠫ။"), [])
    bstack1l1l11l11l_opy_ = bstack1lll11ll1_opy_.bstack1l111111ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l1l11l11l_opy_
    try:
      bstack111ll1111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll_opy_(bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭၌")) else context.browser
      if bstack111ll1111_opy_ and bstack111ll1111_opy_.session_id and bstack1l1l11l11l_opy_ and bstack1l1lll1lll_opy_(
              threading.current_thread(), bstack11l1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ၍"), None):
          threading.current_thread().isA11yTest = bstack1lll11ll1_opy_.bstack1l1l1l11_opy_(bstack111ll1111_opy_, bstack1l1l11l11l_opy_)
    except Exception as e:
       logger.debug(bstack11l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ၎").format(str(e)))
def bstack1l111llll_opy_(bstack111ll1111_opy_):
    if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ၏"), None) and bstack1l1lll1lll_opy_(
      threading.current_thread(), bstack11l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၐ"), None) and not bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨၑ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll11ll1_opy_.bstack1l1l1l111l_opy_(bstack111ll1111_opy_, name=bstack11l1_opy_ (u"ࠨࠢၒ"), path=bstack11l1_opy_ (u"ࠢࠣၓ"))