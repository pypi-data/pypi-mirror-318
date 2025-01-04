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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1l11ll_opy_, bstack1l11ll1111_opy_, get_host_info, bstack1llllll111l_opy_, \
 bstack11lll1lll1_opy_, bstack1l1lll1lll_opy_, bstack11l11l1l1l_opy_, bstack111111l1ll_opy_, bstack11l1l1lll_opy_
import bstack_utils.bstack111lll111l_opy_ as bstack1lll11ll1_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11l11l1l_opy_
from bstack_utils.percy import bstack1l1l1ll11l_opy_
from bstack_utils.config import Config
bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l1l1ll11l_opy_()
@bstack11l11l1l1l_opy_(class_method=False)
def bstack1l1llllll11_opy_(bs_config, bstack11l1l11l_opy_):
  try:
    data = {
        bstack11l1_opy_ (u"ࠩࡩࡳࡷࡳࡡࡵࠩᠼ"): bstack11l1_opy_ (u"ࠪ࡮ࡸࡵ࡮ࠨᠽ"),
        bstack11l1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡤࡴࡡ࡮ࡧࠪᠾ"): bs_config.get(bstack11l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᠿ"), bstack11l1_opy_ (u"࠭ࠧᡀ")),
        bstack11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᡁ"): bs_config.get(bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᡂ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᡃ"): bs_config.get(bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᡄ")),
        bstack11l1_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᡅ"): bs_config.get(bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᡆ"), bstack11l1_opy_ (u"࠭ࠧᡇ")),
        bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᡈ"): bstack11l1l1lll_opy_(),
        bstack11l1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᡉ"): bstack1llllll111l_opy_(bs_config),
        bstack11l1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠬᡊ"): get_host_info(),
        bstack11l1_opy_ (u"ࠪࡧ࡮ࡥࡩ࡯ࡨࡲࠫᡋ"): bstack1l11ll1111_opy_(),
        bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡶࡺࡴ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᡌ"): os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᡍ")),
        bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࡸࡥࡳࡷࡱࠫᡎ"): os.environ.get(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬᡏ"), False),
        bstack11l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡡࡦࡳࡳࡺࡲࡰ࡮ࠪᡐ"): bstack111l1l11ll_opy_(),
        bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᡑ"): bstack1l1lll1l11l_opy_(),
        bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡤࡦࡶࡤ࡭ࡱࡹࠧᡒ"): bstack1l1lll1ll11_opy_(bstack11l1l11l_opy_),
        bstack11l1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩᡓ"): bstack1l11111111_opy_(bs_config, bstack11l1l11l_opy_.get(bstack11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ᡔ"), bstack11l1_opy_ (u"࠭ࠧᡕ"))),
        bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᡖ"): bstack11lll1lll1_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡶࡡࡺ࡮ࡲࡥࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤᡗ").format(str(error)))
    return None
def bstack1l1lll1ll11_opy_(framework):
  return {
    bstack11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩᡘ"): framework.get(bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫᡙ"), bstack11l1_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᡚ")),
    bstack11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᡛ"): framework.get(bstack11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪᡜ")),
    bstack11l1_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᡝ"): framework.get(bstack11l1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᡞ")),
    bstack11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫᡟ"): bstack11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᡠ"),
    bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᡡ"): framework.get(bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᡢ"))
  }
def bstack1l11111111_opy_(bs_config, framework):
  bstack1111lll1l_opy_ = False
  bstack1l1l1llll1_opy_ = False
  bstack1l1lll1l111_opy_ = False
  if bstack11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᡣ") in bs_config:
    bstack1l1lll1l111_opy_ = True
  elif bstack11l1_opy_ (u"ࠧࡢࡲࡳࠫᡤ") in bs_config:
    bstack1111lll1l_opy_ = True
  else:
    bstack1l1l1llll1_opy_ = True
  bstack1ll11lll_opy_ = {
    bstack11l1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᡥ"): bstack1l11l11l1l_opy_.bstack1l1lll1l1ll_opy_(bs_config, framework),
    bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᡦ"): bstack1lll11ll1_opy_.bstack111l11l11l_opy_(bs_config),
    bstack11l1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᡧ"): bs_config.get(bstack11l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᡨ"), False),
    bstack11l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᡩ"): bstack1l1l1llll1_opy_,
    bstack11l1_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᡪ"): bstack1111lll1l_opy_,
    bstack11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᡫ"): bstack1l1lll1l111_opy_
  }
  return bstack1ll11lll_opy_
@bstack11l11l1l1l_opy_(class_method=False)
def bstack1l1lll1l11l_opy_():
  try:
    bstack1l1lll1l1l1_opy_ = json.loads(os.getenv(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᡬ"), bstack11l1_opy_ (u"ࠩࡾࢁࠬᡭ")))
    return {
        bstack11l1_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬᡮ"): bstack1l1lll1l1l1_opy_
    }
  except Exception as error:
    logger.error(bstack11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠠࡧࡱࡵࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࠠࡼࡿࠥᡯ").format(str(error)))
    return {}
def bstack1ll1111l111_opy_(array, bstack1l1lll11ll1_opy_, bstack1l1lll11lll_opy_):
  result = {}
  for o in array:
    key = o[bstack1l1lll11ll1_opy_]
    result[key] = o[bstack1l1lll11lll_opy_]
  return result
def bstack1l1llll1lll_opy_(bstack1l111l1ll1_opy_=bstack11l1_opy_ (u"ࠬ࠭ᡰ")):
  bstack1l1llll1111_opy_ = bstack1lll11ll1_opy_.on()
  bstack1l1lll1lll1_opy_ = bstack1l11l11l1l_opy_.on()
  bstack1l1lll1ll1l_opy_ = percy.bstack11ll1l1lll_opy_()
  if bstack1l1lll1ll1l_opy_ and not bstack1l1lll1lll1_opy_ and not bstack1l1llll1111_opy_:
    return bstack1l111l1ll1_opy_ not in [bstack11l1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᡱ"), bstack11l1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᡲ")]
  elif bstack1l1llll1111_opy_ and not bstack1l1lll1lll1_opy_:
    return bstack1l111l1ll1_opy_ not in [bstack11l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᡳ"), bstack11l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᡴ"), bstack11l1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᡵ")]
  return bstack1l1llll1111_opy_ or bstack1l1lll1lll1_opy_ or bstack1l1lll1ll1l_opy_
@bstack11l11l1l1l_opy_(class_method=False)
def bstack1ll1111llll_opy_(bstack1l111l1ll1_opy_, test=None):
  bstack1l1lll1llll_opy_ = bstack1lll11ll1_opy_.on()
  if not bstack1l1lll1llll_opy_ or bstack1l111l1ll1_opy_ not in [bstack11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᡶ")] or test == None:
    return None
  return {
    bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᡷ"): bstack1l1lll1llll_opy_ and bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᡸ"), None) == True and bstack1lll11ll1_opy_.bstack1l111111ll_opy_(test[bstack11l1_opy_ (u"ࠧࡵࡣࡪࡷࠬ᡹")])
  }