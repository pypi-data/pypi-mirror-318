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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack111l1l111l_opy_ as bstack111l111l11_opy_, EVENTS
from bstack_utils.bstack11l1l111_opy_ import bstack11l1l111_opy_
from bstack_utils.helper import bstack11l1l1lll_opy_, bstack11l111l11l_opy_, bstack11lll1lll1_opy_, bstack111l1111ll_opy_, \
  bstack111l11llll_opy_, bstack1l11ll1111_opy_, get_host_info, bstack111l1l11ll_opy_, bstack11ll1l11ll_opy_, bstack11l11l1l1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11llll11_opy_ import get_logger
from bstack_utils.bstack1ll111l1_opy_ import bstack111l1l11l1_opy_
logger = get_logger(__name__)
bstack1ll111l1_opy_ = bstack111l1l11l1_opy_()
@bstack11l11l1l1l_opy_(class_method=False)
def _111l1lll1l_opy_(driver, bstack111lll1l11_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l1_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ྀࠧ"): caps.get(bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪཱྀ࠭"), None),
        bstack11l1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬྂ"): bstack111lll1l11_opy_.get(bstack11l1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬྃ"), None),
        bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦ྄ࠩ"): caps.get(bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ྅"), None),
        bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ྆"): caps.get(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ྇"), None)
    }
  except Exception as error:
    logger.debug(bstack11l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫྈ") + str(error))
  return response
def on():
    if os.environ.get(bstack11l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ྉ"), None) is None or os.environ[bstack11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧྊ")] == bstack11l1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣྋ"):
        return False
    return True
def bstack111l11l11l_opy_(config):
  return config.get(bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫྌ"), False) or any([p.get(bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬྍ"), False) == True for p in config.get(bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྎ"), [])])
def bstack111l1ll1l_opy_(config, bstack1ll1111l_opy_):
  try:
    if not bstack11lll1lll1_opy_(config):
      return False
    bstack111l1l1l11_opy_ = config.get(bstack11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧྏ"), False)
    if int(bstack1ll1111l_opy_) < len(config.get(bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྐ"), [])) and config[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྑ")][bstack1ll1111l_opy_]:
      bstack111l1l1lll_opy_ = config[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྒ")][bstack1ll1111l_opy_].get(bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫྒྷ"), None)
    else:
      bstack111l1l1lll_opy_ = config.get(bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬྔ"), None)
    if bstack111l1l1lll_opy_ != None:
      bstack111l1l1l11_opy_ = bstack111l1l1lll_opy_
    bstack111l11ll11_opy_ = os.getenv(bstack11l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫྕ")) is not None and len(os.getenv(bstack11l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬྖ"))) > 0 and os.getenv(bstack11l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ྗ")) != bstack11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ྘")
    return bstack111l1l1l11_opy_ and bstack111l11ll11_opy_
  except Exception as error:
    logger.debug(bstack11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪྙ") + str(error))
  return False
def bstack1l111111ll_opy_(test_tags):
  bstack1111llll1l_opy_ = os.getenv(bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬྚ"))
  if bstack1111llll1l_opy_ is None:
    return True
  bstack1111llll1l_opy_ = json.loads(bstack1111llll1l_opy_)
  try:
    include_tags = bstack1111llll1l_opy_[bstack11l1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪྛ")] if bstack11l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫྜ") in bstack1111llll1l_opy_ and isinstance(bstack1111llll1l_opy_[bstack11l1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬྜྷ")], list) else []
    exclude_tags = bstack1111llll1l_opy_[bstack11l1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ྞ")] if bstack11l1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧྟ") in bstack1111llll1l_opy_ and isinstance(bstack1111llll1l_opy_[bstack11l1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨྠ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦྡ") + str(error))
  return False
def bstack111l1ll1l1_opy_(config, bstack111l11l1ll_opy_, bstack111ll11111_opy_, bstack111l111ll1_opy_):
  bstack111l11111l_opy_ = bstack111l1111ll_opy_(config)
  bstack111l1ll111_opy_ = bstack111l11llll_opy_(config)
  if bstack111l11111l_opy_ is None or bstack111l1ll111_opy_ is None:
    logger.error(bstack11l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭ྡྷ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧྣ"), bstack11l1_opy_ (u"ࠧࡼࡿࠪྤ")))
    data = {
        bstack11l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ྥ"): config[bstack11l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧྦ")],
        bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ྦྷ"): config.get(bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧྨ"), os.path.basename(os.getcwd())),
        bstack11l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨྩ"): bstack11l1l1lll_opy_(),
        bstack11l1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫྪ"): config.get(bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪྫ"), bstack11l1_opy_ (u"ࠨࠩྫྷ")),
        bstack11l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩྭ"): {
            bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪྮ"): bstack111l11l1ll_opy_,
            bstack11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧྯ"): bstack111ll11111_opy_,
            bstack11l1_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩྰ"): __version__,
            bstack11l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨྱ"): bstack11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧྲ"),
            bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨླ"): bstack11l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫྴ"),
            bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪྵ"): bstack111l111ll1_opy_
        },
        bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ྶ"): settings,
        bstack11l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭ྷ"): bstack111l1l11ll_opy_(),
        bstack11l1_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭ྸ"): bstack1l11ll1111_opy_(),
        bstack11l1_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩྐྵ"): get_host_info(),
        bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪྺ"): bstack11lll1lll1_opy_(config)
    }
    headers = {
        bstack11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨྻ"): bstack11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ྼ"),
    }
    config = {
        bstack11l1_opy_ (u"ࠫࡦࡻࡴࡩࠩ྽"): (bstack111l11111l_opy_, bstack111l1ll111_opy_),
        bstack11l1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭྾"): headers
    }
    response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"࠭ࡐࡐࡕࡗࠫ྿"), bstack111l111l11_opy_ + bstack11l1_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧ࿀"), data, config)
    bstack111l11ll1l_opy_ = response.json()
    if bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ࿁")]:
      parsed = json.loads(os.getenv(bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ࿂"), bstack11l1_opy_ (u"ࠪࡿࢂ࠭࿃")))
      parsed[bstack11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ࿄")] = bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠬࡪࡡࡵࡣࠪ࿅")][bstack11l1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴ࿆ࠧ")]
      os.environ[bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ࿇")] = json.dumps(parsed)
      bstack11l1l111_opy_.bstack111l1ll11l_opy_(bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭࿈")][bstack11l1_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ࿉")])
      bstack11l1l111_opy_.bstack111l1ll1ll_opy_(bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠪࡨࡦࡺࡡࠨ࿊")][bstack11l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭࿋")])
      bstack11l1l111_opy_.store()
      return bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠬࡪࡡࡵࡣࠪ࿌")][bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫ࿍")], bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠧࡥࡣࡷࡥࠬ࿎")][bstack11l1_opy_ (u"ࠨ࡫ࡧࠫ࿏")]
    else:
      logger.error(bstack11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪ࿐") + bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ࿑")])
      if bstack111l11ll1l_opy_[bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ࿒")] == bstack11l1_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧ࿓"):
        for bstack111l1lllll_opy_ in bstack111l11ll1l_opy_[bstack11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭࿔")]:
          logger.error(bstack111l1lllll_opy_[bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ࿕")])
      return None, None
  except Exception as error:
    logger.error(bstack11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤ࿖") +  str(error))
    return None, None
def bstack111l111111_opy_():
  if os.getenv(bstack11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ࿗")) is None:
    return {
        bstack11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ࿘"): bstack11l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ࿙"),
        bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭࿚"): bstack11l1_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬ࿛")
    }
  data = {bstack11l1_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨ࿜"): bstack11l1l1lll_opy_()}
  headers = {
      bstack11l1_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ࿝"): bstack11l1_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪ࿞") + os.getenv(bstack11l1_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣ࿟")),
      bstack11l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ࿠"): bstack11l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ࿡")
  }
  response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"࠭ࡐࡖࡖࠪ࿢"), bstack111l111l11_opy_ + bstack11l1_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩ࿣"), data, { bstack11l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ࿤"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥ࿥") + bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"ࠪ࡞ࠬ࿦"))
      return {bstack11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ࿧"): bstack11l1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭࿨"), bstack11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ࿩"): bstack11l1_opy_ (u"ࠧࠨ࿪")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦ࿫") + str(error))
    return {
        bstack11l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ࿬"): bstack11l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ࿭"),
        bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ࿮"): str(error)
    }
def bstack1lll1l11_opy_(caps, options, desired_capabilities={}):
  try:
    bstack111l1111l1_opy_ = caps.get(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭࿯"), {}).get(bstack11l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ࿰"), caps.get(bstack11l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿱"), bstack11l1_opy_ (u"ࠨࠩ࿲")))
    if bstack111l1111l1_opy_:
      logger.warn(bstack11l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ࿳"))
      return False
    if options:
      bstack111l11lll1_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack111l11lll1_opy_ = desired_capabilities
    else:
      bstack111l11lll1_opy_ = {}
    browser = caps.get(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ࿴"), bstack11l1_opy_ (u"ࠫࠬ࿵")).lower() or bstack111l11lll1_opy_.get(bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ࿶"), bstack11l1_opy_ (u"࠭ࠧ࿷")).lower()
    if browser != bstack11l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ࿸"):
      logger.warn(bstack11l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ࿹"))
      return False
    browser_version = caps.get(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ࿺")) or caps.get(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿻")) or bstack111l11lll1_opy_.get(bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ࿼")) or bstack111l11lll1_opy_.get(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭࿽"), {}).get(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ࿾")) or bstack111l11lll1_opy_.get(bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ࿿"), {}).get(bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪက"))
    if browser_version and browser_version != bstack11l1_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩခ") and int(browser_version.split(bstack11l1_opy_ (u"ࠪ࠲ࠬဂ"))[0]) <= 98:
      logger.warn(bstack11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥ࠿࠸࠯ࠤဃ"))
      return False
    if not options:
      bstack111l1l1ll1_opy_ = caps.get(bstack11l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪင")) or bstack111l11lll1_opy_.get(bstack11l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫစ"), {})
      if bstack11l1_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫဆ") in bstack111l1l1ll1_opy_.get(bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ဇ"), []):
        logger.warn(bstack11l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦဈ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧဉ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack111l1llll1_opy_ = config.get(bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫည"), {})
    bstack111l1llll1_opy_[bstack11l1_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨဋ")] = os.getenv(bstack11l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫဌ"))
    bstack111l111lll_opy_ = json.loads(os.getenv(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨဍ"), bstack11l1_opy_ (u"ࠨࡽࢀࠫဎ"))).get(bstack11l1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪဏ"))
    caps[bstack11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪတ")] = True
    if bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬထ") in caps:
      caps[bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ဒ")][bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ဓ")] = bstack111l1llll1_opy_
      caps[bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨန")][bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨပ")][bstack11l1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪဖ")] = bstack111l111lll_opy_
    else:
      caps[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩဗ")] = bstack111l1llll1_opy_
      caps[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪဘ")][bstack11l1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭မ")] = bstack111l111lll_opy_
  except Exception as error:
    logger.debug(bstack11l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢယ") +  str(error))
def bstack1l1l1l11_opy_(driver, bstack111l1lll11_opy_):
  try:
    setattr(driver, bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧရ"), True)
    session = driver.session_id
    if session:
      bstack111l1l1l1l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack111l1l1l1l_opy_ = False
      bstack111l1l1l1l_opy_ = url.scheme in [bstack11l1_opy_ (u"ࠣࡪࡷࡸࡵࠨလ"), bstack11l1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣဝ")]
      if bstack111l1l1l1l_opy_:
        if bstack111l1lll11_opy_:
          logger.info(bstack11l1_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥသ"))
      return bstack111l1lll11_opy_
  except Exception as e:
    logger.error(bstack11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢဟ") + str(e))
    return False
def bstack1l1l1l111l_opy_(driver, name, path):
  try:
    bstack111l111l1l_opy_ = {
        bstack11l1_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬဠ"): threading.current_thread().current_test_uuid,
        bstack11l1_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫအ"): os.environ.get(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬဢ"), bstack11l1_opy_ (u"ࠨࠩဣ")),
        bstack11l1_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ဤ"): os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫဥ"), bstack11l1_opy_ (u"ࠫࠬဦ"))
    }
    bstack1111lllll1_opy_ = bstack1ll111l1_opy_.bstack1111llllll_opy_(EVENTS.bstack1l1lll1l11_opy_.value)
    bstack1ll111l1_opy_.mark(bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧဧ"))
    logger.debug(bstack11l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩဨ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l1l111_opy_.perform_scan, {bstack11l1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢဩ"): name}))
      bstack1ll111l1_opy_.end(bstack1111lllll1_opy_, bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣဪ"), bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢါ"), True, None)
    except Exception as error:
      bstack1ll111l1_opy_.end(bstack1111lllll1_opy_, bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥာ"), bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤိ"), False, str(error))
    bstack1111lllll1_opy_ = bstack1ll111l1_opy_.bstack1111llllll_opy_(EVENTS.bstack111l11l111_opy_.value)
    bstack1ll111l1_opy_.mark(bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧီ"))
    try:
      logger.debug(driver.execute_async_script(bstack11l1l111_opy_.bstack111l1l1111_opy_, bstack111l111l1l_opy_))
      bstack1ll111l1_opy_.end(bstack1111lllll1_opy_, bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨု"), bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧူ"),True, None)
    except Exception as error:
      bstack1ll111l1_opy_.end(bstack1111lllll1_opy_, bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣေ"), bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢဲ"),False, str(error))
    logger.info(bstack11l1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨဳ"))
  except Exception as bstack111l11l1l1_opy_:
    logger.error(bstack11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨဴ") + str(path) + bstack11l1_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢဵ") + str(bstack111l11l1l1_opy_))