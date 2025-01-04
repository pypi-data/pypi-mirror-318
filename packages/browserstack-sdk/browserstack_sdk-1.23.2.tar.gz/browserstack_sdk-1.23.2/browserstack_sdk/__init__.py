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
import atexit
import signal
import yaml
import socket
import datetime
import string
import random
import collections.abc
import traceback
import copy
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.measure import bstack1ll111l1_opy_
from bstack_utils.percy import *
from browserstack_sdk.bstack1ll1l11ll1_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1lll1lll1l_opy_ import bstack1l11ll1l_opy_
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l11ll11_opy_():
  global CONFIG
  headers = {
        bstack11l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack11l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1l1l1l1ll_opy_(CONFIG, bstack1ll1l11l1_opy_)
  try:
    response = requests.get(bstack1ll1l11l1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1111l1l_opy_ = response.json()[bstack11l1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1l11lll11l_opy_.format(response.json()))
      return bstack1l1111l1l_opy_
    else:
      logger.debug(bstack1l1l11ll1l_opy_.format(bstack11l1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack1l1l11ll1l_opy_.format(e))
def bstack11ll11ll1_opy_(hub_url):
  global CONFIG
  url = bstack11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack11l1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1llll111l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1111111l_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1ll11l11_opy_, stage=STAGE.SINGLE)
def bstack1l1111ll11_opy_():
  try:
    global bstack1l11l1l1l_opy_
    bstack1l1111l1l_opy_ = bstack1l11ll11_opy_()
    bstack11lll111l1_opy_ = []
    results = []
    for bstack1lll11111_opy_ in bstack1l1111l1l_opy_:
      bstack11lll111l1_opy_.append(bstack11l111l1_opy_(target=bstack11ll11ll1_opy_,args=(bstack1lll11111_opy_,)))
    for t in bstack11lll111l1_opy_:
      t.start()
    for t in bstack11lll111l1_opy_:
      results.append(t.join())
    bstack1l1llll111_opy_ = {}
    for item in results:
      hub_url = item[bstack11l1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack11l1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1l1llll111_opy_[hub_url] = latency
    bstack1111lll1_opy_ = min(bstack1l1llll111_opy_, key= lambda x: bstack1l1llll111_opy_[x])
    bstack1l11l1l1l_opy_ = bstack1111lll1_opy_
    logger.debug(bstack1l1llll11_opy_.format(bstack1111lll1_opy_))
  except Exception as e:
    logger.debug(bstack1ll1lllll1_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack11llll11_opy_
from bstack_utils.helper import bstack1l111l1l_opy_, bstack11ll1l11ll_opy_, bstack1l11l111ll_opy_, bstack1l1lll1lll_opy_, \
  bstack11lll1lll1_opy_, \
  Notset, bstack1l11l1l1_opy_, \
  bstack11l1llll_opy_, bstack1ll1lll1ll_opy_, bstack1lll1ll1l_opy_, bstack1l11ll1111_opy_, bstack1l1lll111l_opy_, bstack1llll1lll1_opy_, \
  bstack111l111l_opy_, \
  bstack111l111l1_opy_, bstack1llll11l_opy_, bstack1lll1ll111_opy_, bstack11l1ll1ll_opy_, \
  bstack11lll1ll1_opy_, bstack1l111ll11_opy_, bstack1111ll1l1_opy_, bstack1l1ll1llll_opy_
from bstack_utils.bstack11l11l11_opy_ import bstack1l11ll111l_opy_
from bstack_utils.bstack1111l1111_opy_ import bstack11l1ll1l_opy_
from bstack_utils.bstack1llllll1ll_opy_ import bstack11l1111ll_opy_, bstack1lll1l11ll_opy_
from bstack_utils.bstack11l1l111_opy_ import bstack11l1l111_opy_
from bstack_utils.proxy import bstack1l1111l1ll_opy_, bstack1l1l1l1ll_opy_, bstack1ll11ll111_opy_, bstack11ll1lll1l_opy_
from browserstack_sdk.bstack11llll1l_opy_ import *
from browserstack_sdk.bstack11llllll_opy_ import *
from bstack_utils.bstack1l1llll1l1_opy_ import bstack1ll1l11l11_opy_
from browserstack_sdk.bstack1111111l1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11llll11_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1ll1l1l1l_opy_, stage=STAGE.SINGLE)
def bstack11lll1l11l_opy_():
    global bstack1l11l1l1l_opy_
    try:
        bstack1ll111l1l1_opy_ = bstack11l1l1111_opy_()
        bstack111ll1ll1_opy_(bstack1ll111l1l1_opy_)
        hub_url = bstack1ll111l1l1_opy_.get(bstack11l1_opy_ (u"ࠨࡵࡳ࡮ࠥࢀ"), bstack11l1_opy_ (u"ࠢࠣࢁ"))
        if hub_url.endswith(bstack11l1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩࢂ")):
            hub_url = hub_url.rsplit(bstack11l1_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪࢃ"), 1)[0]
        if hub_url.startswith(bstack11l1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫࢄ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭ࢅ")):
            hub_url = hub_url[8:]
        bstack1l11l1l1l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11l1l1111_opy_():
    global CONFIG
    bstack1ll1ll11l_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢆ"), {}).get(bstack11l1_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨࢇ"), bstack11l1_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭࢈"))
    if not isinstance(bstack1ll1ll11l_opy_, str):
        raise ValueError(bstack11l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧࢉ"))
    try:
        bstack1ll111l1l1_opy_ = bstack1111ll11_opy_(bstack1ll1ll11l_opy_)
        return bstack1ll111l1l1_opy_
    except Exception as e:
        logger.error(bstack11l1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣࢊ").format(str(e)))
        return {}
def bstack1111ll11_opy_(bstack1ll1ll11l_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࢋ")] or not CONFIG[bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧࢌ")]:
            raise ValueError(bstack11l1_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢࢍ"))
        url = bstack11l1111l_opy_ + bstack1ll1ll11l_opy_
        auth = (CONFIG[bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࢎ")], CONFIG[bstack11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ࢏")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l1lll11l_opy_ = json.loads(response.text)
            return bstack1l1lll11l_opy_
    except ValueError as ve:
        logger.error(bstack11l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ࢐").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ࢑").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111ll1ll1_opy_(bstack11ll1111l_opy_):
    global CONFIG
    if bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ࢒") not in CONFIG or str(CONFIG[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ࢓")]).lower() == bstack11l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࢔"):
        CONFIG[bstack11l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ࢕")] = False
    elif bstack11l1_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ࢖") in bstack11ll1111l_opy_:
        bstack1llll1ll11_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢗ"), {})
        logger.debug(bstack11l1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ࢘"), bstack1llll1ll11_opy_)
        bstack1llllll1l1_opy_ = bstack11ll1111l_opy_.get(bstack11l1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷ࢙ࠧ"), [])
        bstack1l1ll11l_opy_ = bstack11l1_opy_ (u"ࠦ࠱ࠨ࢚").join(bstack1llllll1l1_opy_)
        logger.debug(bstack11l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵ࢛ࠥ"), bstack1l1ll11l_opy_)
        bstack11l1ll11l_opy_ = {
            bstack11l1_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ࢜"): bstack11l1_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨ࢝"),
            bstack11l1_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧ࢞"): bstack11l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࢟"),
            bstack11l1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧࢠ"): bstack1l1ll11l_opy_
        }
        bstack1llll1ll11_opy_.update(bstack11l1ll11l_opy_)
        logger.debug(bstack11l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣࢡ"), bstack1llll1ll11_opy_)
        CONFIG[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢢ")] = bstack1llll1ll11_opy_
        logger.debug(bstack11l1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣࢣ"), CONFIG)
def bstack1lll11l1_opy_():
    bstack1ll111l1l1_opy_ = bstack11l1l1111_opy_()
    if not bstack1ll111l1l1_opy_[bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧࢤ")]:
      raise ValueError(bstack11l1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥࢥ"))
    return bstack1ll111l1l1_opy_[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩࢦ")] + bstack11l1_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪࢧ")
@measure(event_name=EVENTS.bstack1l11111lll_opy_, stage=STAGE.SINGLE)
def bstack11l11llll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࢨ")], CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࢩ")])
        url = bstack111llll11_opy_
        logger.debug(bstack11l1_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥࢪ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l1_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨࢫ"): bstack11l1_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦࢬ")})
            if response.status_code == 200:
                bstack1llll1l11_opy_ = json.loads(response.text)
                bstack1l11ll11l1_opy_ = bstack1llll1l11_opy_.get(bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩࢭ"), [])
                if bstack1l11ll11l1_opy_:
                    bstack1l11l11l11_opy_ = bstack1l11ll11l1_opy_[0]
                    bstack1l11l1ll_opy_ = bstack1l11l11l11_opy_.get(bstack11l1_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ࢮ"))
                    bstack11l1llll1_opy_ = bstack1l11llll11_opy_ + bstack1l11l1ll_opy_
                    result.extend([bstack1l11l1ll_opy_, bstack11l1llll1_opy_])
                    logger.info(bstack111llll1l_opy_.format(bstack11l1llll1_opy_))
                    bstack1lll111l11_opy_ = CONFIG[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧࢯ")]
                    if bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢰ") in CONFIG:
                      bstack1lll111l11_opy_ += bstack11l1_opy_ (u"࠭ࠠࠨࢱ") + CONFIG[bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࢲ")]
                    if bstack1lll111l11_opy_ != bstack1l11l11l11_opy_.get(bstack11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ࢳ")):
                      logger.debug(bstack1l1ll1l11l_opy_.format(bstack1l11l11l11_opy_.get(bstack11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧࢴ")), bstack1lll111l11_opy_))
                    return result
                else:
                    logger.debug(bstack11l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢࢵ"))
            else:
                logger.debug(bstack11l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢶ"))
        except Exception as e:
            logger.error(bstack11l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧࢷ").format(str(e)))
    else:
        logger.debug(bstack11l1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢸ"))
    return [None, None]
import bstack_utils.bstack11llll11l_opy_ as bstack1lll1ll11l_opy_
import bstack_utils.bstack1l1lll11_opy_ as bstack1ll11ll1l_opy_
bstack1ll11l11ll_opy_ = bstack11l1_opy_ (u"ࠧࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠠࠡ࡫ࡩࠬࡵࡧࡧࡦࠢࡀࡁࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠠࡼ࡞ࡱࠤࠥࠦࡴࡳࡻࡾࡠࡳࠦࡣࡰࡰࡶࡸࠥ࡬ࡳࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࡡ࠭ࡦࡴ࡞ࠪ࠭ࡀࡢ࡮ࠡࠢࠣࠤࠥ࡬ࡳ࠯ࡣࡳࡴࡪࡴࡤࡇ࡫࡯ࡩࡘࡿ࡮ࡤࠪࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠬࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡳࡣ࡮ࡴࡤࡦࡺࠬࠤ࠰ࠦࠢ࠻ࠤࠣ࠯ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࠬࡦࡽࡡࡪࡶࠣࡲࡪࡽࡐࡢࡩࡨ࠶࠳࡫ࡶࡢ࡮ࡸࡥࡹ࡫ࠨࠣࠪࠬࠤࡂࡄࠠࡼࡿࠥ࠰ࠥࡢࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡨࡧࡷࡗࡪࡹࡳࡪࡱࡱࡈࡪࡺࡡࡪ࡮ࡶࠦࢂࡢࠧࠪࠫࠬ࡟ࠧ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠣ࡟ࠬࠤ࠰ࠦࠢ࠭࡞࡟ࡲࠧ࠯࡜࡯ࠢࠣࠤࠥࢃࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡽ࡝ࡰࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠧࢹ")
bstack11l11lll1_opy_ = bstack11l1_opy_ (u"ࠨ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠࡠࡳࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬࡠࡳࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࡢ࡮ࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻ࡝ࡰ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࡡࡴࡴࡳࡻࠣࡿࡡࡴࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࡞ࡱࠤࠥࢃࠠࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࠣࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽ࡟ࡲࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࡠࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠦࡾࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪࡿࡣ࠰ࡡࡴࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࡢ࡮ࠡࠢࢀ࠭ࡡࡴࡽ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠧࢺ")
from ._version import __version__
bstack11l11ll1l_opy_ = None
CONFIG = {}
bstack111l1llll_opy_ = {}
bstack1ll1l1l11l_opy_ = {}
bstack1l1l1ll1l_opy_ = None
bstack1l1l1lll_opy_ = None
bstack1l111l111_opy_ = None
bstack1l11lll1l_opy_ = -1
bstack1l1ll111l_opy_ = 0
bstack1ll1ll1ll_opy_ = bstack1llll1111l_opy_
bstack1lllll11l_opy_ = 1
bstack1l1ll11l11_opy_ = False
bstack1ll111l1l_opy_ = False
bstack1llll11l1l_opy_ = bstack11l1_opy_ (u"ࠩࠪࢻ")
bstack1ll1lllll_opy_ = bstack11l1_opy_ (u"ࠪࠫࢼ")
bstack11llll1l1l_opy_ = False
bstack1l1l1lll1l_opy_ = True
bstack1l1111llll_opy_ = bstack11l1_opy_ (u"ࠫࠬࢽ")
bstack1ll111l111_opy_ = []
bstack1l11l1l1l_opy_ = bstack11l1_opy_ (u"ࠬ࠭ࢾ")
bstack11l11ll11_opy_ = False
bstack111ll1l1l_opy_ = None
bstack1ll1l1l1_opy_ = None
bstack111l11ll_opy_ = None
bstack111l1l11l_opy_ = -1
bstack1llll11ll_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"࠭ࡾࠨࢿ")), bstack11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧࣀ"), bstack11l1_opy_ (u"ࠨ࠰ࡵࡳࡧࡵࡴ࠮ࡴࡨࡴࡴࡸࡴ࠮ࡪࡨࡰࡵ࡫ࡲ࠯࡬ࡶࡳࡳ࠭ࣁ"))
bstack11ll11l11_opy_ = 0
bstack1ll1ll1l1_opy_ = 0
bstack1l11111l1_opy_ = []
bstack1l1ll11l1l_opy_ = []
bstack1llll1l1_opy_ = []
bstack1l11ll1l11_opy_ = []
bstack1l111llll1_opy_ = bstack11l1_opy_ (u"ࠩࠪࣂ")
bstack1l1l111111_opy_ = bstack11l1_opy_ (u"ࠪࠫࣃ")
bstack1l1ll11111_opy_ = False
bstack1ll11ll1_opy_ = False
bstack1l111ll1l1_opy_ = {}
bstack1lll1111l_opy_ = None
bstack1ll1l111l1_opy_ = None
bstack1ll111llll_opy_ = None
bstack1ll1ll1ll1_opy_ = None
bstack1l1l11111_opy_ = None
bstack1l1l1l1l11_opy_ = None
bstack111l11l1_opy_ = None
bstack11llllll1l_opy_ = None
bstack1llll1111_opy_ = None
bstack1l1l1l111_opy_ = None
bstack1ll1111l1l_opy_ = None
bstack111ll1lll_opy_ = None
bstack1ll1l1lll1_opy_ = None
bstack11llll1ll1_opy_ = None
bstack1ll1l11l_opy_ = None
bstack11ll111l_opy_ = None
bstack1ll1111l11_opy_ = None
bstack1l1ll1l1ll_opy_ = None
bstack1lllll11_opy_ = None
bstack1l111lll11_opy_ = None
bstack1ll111ll11_opy_ = None
bstack1ll1ll111l_opy_ = None
bstack1lll11lll_opy_ = False
bstack1l11ll1l1_opy_ = bstack11l1_opy_ (u"ࠦࠧࣄ")
logger = bstack11llll11_opy_.get_logger(__name__, bstack1ll1ll1ll_opy_)
bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
percy = bstack1l1l1ll11l_opy_()
bstack1l1l111l11_opy_ = bstack1l11ll1l_opy_()
bstack1ll1llll11_opy_ = bstack1111111l1_opy_()
def bstack11lll111ll_opy_():
  global CONFIG
  global bstack1l1ll11111_opy_
  global bstack1l1l1lll1_opy_
  bstack1llll11lll_opy_ = bstack1l11ll1ll1_opy_(CONFIG)
  if bstack11lll1lll1_opy_(CONFIG):
    if (bstack11l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࣅ") in bstack1llll11lll_opy_ and str(bstack1llll11lll_opy_[bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࣆ")]).lower() == bstack11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬࣇ")):
      bstack1l1ll11111_opy_ = True
    bstack1l1l1lll1_opy_.bstack111111ll1_opy_(bstack1llll11lll_opy_.get(bstack11l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬࣈ"), False))
  else:
    bstack1l1ll11111_opy_ = True
    bstack1l1l1lll1_opy_.bstack111111ll1_opy_(True)
def bstack11lll11l1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1lll11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1lll1l111_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l1_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡦࡳࡳ࡬ࡩࡨࡨ࡬ࡰࡪࠨࣉ") == args[i].lower() or bstack11l1_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡧ࡫ࡪࠦ࣊") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1111llll_opy_
      bstack1l1111llll_opy_ += bstack11l1_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠡࠩ࣋") + path
      return path
  return None
bstack1ll1l1ll_opy_ = re.compile(bstack11l1_opy_ (u"ࡷࠨ࠮ࠫࡁ࡟ࠨࢀ࠮࠮ࠫࡁࠬࢁ࠳࠰࠿ࠣ࣌"))
def bstack11lll1l1l1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1ll1l1ll_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l1_opy_ (u"ࠨࠤࡼࠤ࣍") + group + bstack11l1_opy_ (u"ࠢࡾࠤ࣎"), os.environ.get(group))
  return value
def bstack11lllll1l1_opy_():
  bstack1llll111ll_opy_ = bstack1lll1l111_opy_()
  if bstack1llll111ll_opy_ and os.path.exists(os.path.abspath(bstack1llll111ll_opy_)):
    fileName = bstack1llll111ll_opy_
  if bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉ࣏ࠬ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࣐࠭")])) and not bstack11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩ࣑ࠬ") in locals():
    fileName = os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ࣒")]
  if bstack11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫࣓ࠧ") in locals():
    bstack1l1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1ll_opy_ = bstack11l1_opy_ (u"࠭ࠧࣔ")
  bstack11lll11ll1_opy_ = os.getcwd()
  bstack11ll1ll1l_opy_ = bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪࣕ")
  bstack11l1l1ll_opy_ = bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬࣖ")
  while (not os.path.exists(bstack1l1ll_opy_)) and bstack11lll11ll1_opy_ != bstack11l1_opy_ (u"ࠤࠥࣗ"):
    bstack1l1ll_opy_ = os.path.join(bstack11lll11ll1_opy_, bstack11ll1ll1l_opy_)
    if not os.path.exists(bstack1l1ll_opy_):
      bstack1l1ll_opy_ = os.path.join(bstack11lll11ll1_opy_, bstack11l1l1ll_opy_)
    if bstack11lll11ll1_opy_ != os.path.dirname(bstack11lll11ll1_opy_):
      bstack11lll11ll1_opy_ = os.path.dirname(bstack11lll11ll1_opy_)
    else:
      bstack11lll11ll1_opy_ = bstack11l1_opy_ (u"ࠥࠦࣘ")
  if not os.path.exists(bstack1l1ll_opy_):
    bstack1l11ll11l_opy_(
      bstack1llll1l1l_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1ll_opy_, bstack11l1_opy_ (u"ࠫࡷ࠭ࣙ")) as stream:
      yaml.add_implicit_resolver(bstack11l1_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࣚ"), bstack1ll1l1ll_opy_)
      yaml.add_constructor(bstack11l1_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢࣛ"), bstack11lll1l1l1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1l1ll_opy_, bstack11l1_opy_ (u"ࠧࡳࠩࣜ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1l11ll11l_opy_(bstack11llll111l_opy_.format(str(exc)))
def bstack1lll1111ll_opy_(config):
  bstack1llll11l11_opy_ = bstack111l1ll1_opy_(config)
  for option in list(bstack1llll11l11_opy_):
    if option.lower() in bstack11111l1l_opy_ and option != bstack11111l1l_opy_[option.lower()]:
      bstack1llll11l11_opy_[bstack11111l1l_opy_[option.lower()]] = bstack1llll11l11_opy_[option]
      del bstack1llll11l11_opy_[option]
  return config
def bstack11lllll1ll_opy_():
  global bstack1ll1l1l11l_opy_
  for key, bstack1ll111l11_opy_ in bstack1l1l1l11l_opy_.items():
    if isinstance(bstack1ll111l11_opy_, list):
      for var in bstack1ll111l11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll1l1l11l_opy_[key] = os.environ[var]
          break
    elif bstack1ll111l11_opy_ in os.environ and os.environ[bstack1ll111l11_opy_] and str(os.environ[bstack1ll111l11_opy_]).strip():
      bstack1ll1l1l11l_opy_[key] = os.environ[bstack1ll111l11_opy_]
  if bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪࣝ") in os.environ:
    bstack1ll1l1l11l_opy_[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࣞ")] = {}
    bstack1ll1l1l11l_opy_[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣟ")][bstack11l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")] = os.environ[bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ࣡")]
def bstack111111l11_opy_():
  global bstack111l1llll_opy_
  global bstack1l1111llll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack11l1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣢").lower() == val.lower():
      bstack111l1llll_opy_[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࣣࠫ")] = {}
      bstack111l1llll_opy_[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣤ")][bstack11l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣥ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack11lll111_opy_ in bstack111llll1_opy_.items():
    if isinstance(bstack11lll111_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11lll111_opy_:
          if idx < len(sys.argv) and bstack11l1_opy_ (u"ࠪ࠱࠲ࣦ࠭") + var.lower() == val.lower() and not key in bstack111l1llll_opy_:
            bstack111l1llll_opy_[key] = sys.argv[idx + 1]
            bstack1l1111llll_opy_ += bstack11l1_opy_ (u"ࠫࠥ࠳࠭ࠨࣧ") + var + bstack11l1_opy_ (u"ࠬࠦࠧࣨ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack11l1_opy_ (u"࠭࠭࠮ࣩࠩ") + bstack11lll111_opy_.lower() == val.lower() and not key in bstack111l1llll_opy_:
          bstack111l1llll_opy_[key] = sys.argv[idx + 1]
          bstack1l1111llll_opy_ += bstack11l1_opy_ (u"ࠧࠡ࠯࠰ࠫ࣪") + bstack11lll111_opy_ + bstack11l1_opy_ (u"ࠨࠢࠪ࣫") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1ll1llll1_opy_(config):
  bstack11ll1l1l1l_opy_ = config.keys()
  for bstack1l1lll1l1l_opy_, bstack1111llll_opy_ in bstack11l11l1ll_opy_.items():
    if bstack1111llll_opy_ in bstack11ll1l1l1l_opy_:
      config[bstack1l1lll1l1l_opy_] = config[bstack1111llll_opy_]
      del config[bstack1111llll_opy_]
  for bstack1l1lll1l1l_opy_, bstack1111llll_opy_ in bstack1l111l11l1_opy_.items():
    if isinstance(bstack1111llll_opy_, list):
      for bstack11ll11111_opy_ in bstack1111llll_opy_:
        if bstack11ll11111_opy_ in bstack11ll1l1l1l_opy_:
          config[bstack1l1lll1l1l_opy_] = config[bstack11ll11111_opy_]
          del config[bstack11ll11111_opy_]
          break
    elif bstack1111llll_opy_ in bstack11ll1l1l1l_opy_:
      config[bstack1l1lll1l1l_opy_] = config[bstack1111llll_opy_]
      del config[bstack1111llll_opy_]
  for bstack11ll11111_opy_ in list(config):
    for bstack11ll1llll_opy_ in bstack11lllllll1_opy_:
      if bstack11ll11111_opy_.lower() == bstack11ll1llll_opy_.lower() and bstack11ll11111_opy_ != bstack11ll1llll_opy_:
        config[bstack11ll1llll_opy_] = config[bstack11ll11111_opy_]
        del config[bstack11ll11111_opy_]
  bstack11lllll1l_opy_ = [{}]
  if not config.get(bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࣬")):
    config[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࣭࠭")] = [{}]
  bstack11lllll1l_opy_ = config[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹ࣮ࠧ")]
  for platform in bstack11lllll1l_opy_:
    for bstack11ll11111_opy_ in list(platform):
      for bstack11ll1llll_opy_ in bstack11lllllll1_opy_:
        if bstack11ll11111_opy_.lower() == bstack11ll1llll_opy_.lower() and bstack11ll11111_opy_ != bstack11ll1llll_opy_:
          platform[bstack11ll1llll_opy_] = platform[bstack11ll11111_opy_]
          del platform[bstack11ll11111_opy_]
  for bstack1l1lll1l1l_opy_, bstack1111llll_opy_ in bstack1l111l11l1_opy_.items():
    for platform in bstack11lllll1l_opy_:
      if isinstance(bstack1111llll_opy_, list):
        for bstack11ll11111_opy_ in bstack1111llll_opy_:
          if bstack11ll11111_opy_ in platform:
            platform[bstack1l1lll1l1l_opy_] = platform[bstack11ll11111_opy_]
            del platform[bstack11ll11111_opy_]
            break
      elif bstack1111llll_opy_ in platform:
        platform[bstack1l1lll1l1l_opy_] = platform[bstack1111llll_opy_]
        del platform[bstack1111llll_opy_]
  for bstack111111111_opy_ in bstack11l1l111l_opy_:
    if bstack111111111_opy_ in config:
      if not bstack11l1l111l_opy_[bstack111111111_opy_] in config:
        config[bstack11l1l111l_opy_[bstack111111111_opy_]] = {}
      config[bstack11l1l111l_opy_[bstack111111111_opy_]].update(config[bstack111111111_opy_])
      del config[bstack111111111_opy_]
  for platform in bstack11lllll1l_opy_:
    for bstack111111111_opy_ in bstack11l1l111l_opy_:
      if bstack111111111_opy_ in list(platform):
        if not bstack11l1l111l_opy_[bstack111111111_opy_] in platform:
          platform[bstack11l1l111l_opy_[bstack111111111_opy_]] = {}
        platform[bstack11l1l111l_opy_[bstack111111111_opy_]].update(platform[bstack111111111_opy_])
        del platform[bstack111111111_opy_]
  config = bstack1lll1111ll_opy_(config)
  return config
def bstack1l11llllll_opy_(config):
  global bstack1ll1lllll_opy_
  bstack11lllll11_opy_ = False
  if bstack11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦ࣯ࠩ") in config and str(config[bstack11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࣰࠪ")]).lower() != bstack11l1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪࣱ࠭"):
    if bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࣲࠬ") not in config or str(config[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ࣳ")]).lower() == bstack11l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩࣴ"):
      config[bstack11l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪࣵ")] = False
    else:
      bstack1ll111l1l1_opy_ = bstack11l1l1111_opy_()
      if bstack11l1_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࣶࠪ") in bstack1ll111l1l1_opy_:
        if not bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࣷ") in config:
          config[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࣸ")] = {}
        config[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࣹࠬ")][bstack11l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࣺࠫ")] = bstack11l1_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩࣻ")
        bstack11lllll11_opy_ = True
        bstack1ll1lllll_opy_ = config[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࣼ")].get(bstack11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣽ"))
  if bstack11lll1lll1_opy_(config) and bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪࣾ") in config and str(config[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫࣿ")]).lower() != bstack11l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧऀ") and not bstack11lllll11_opy_:
    if not bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ँ") in config:
      config[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧं")] = {}
    if not config[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨः")].get(bstack11l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩऄ")) and not bstack11l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨअ") in config[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫआ")]:
      bstack11l1l1lll_opy_ = datetime.datetime.now()
      bstack1l1l111ll_opy_ = bstack11l1l1lll_opy_.strftime(bstack11l1_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬइ"))
      hostname = socket.gethostname()
      bstack11111lll1_opy_ = bstack11l1_opy_ (u"ࠩࠪई").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l1_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬउ").format(bstack1l1l111ll_opy_, hostname, bstack11111lll1_opy_)
      config[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऊ")][bstack11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऋ")] = identifier
    bstack1ll1lllll_opy_ = config[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪऌ")].get(bstack11l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩऍ"))
  return config
def bstack1llll1ll_opy_():
  bstack1lllll1l1l_opy_ =  bstack1l11ll1111_opy_()[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧऎ")]
  return bstack1lllll1l1l_opy_ if bstack1lllll1l1l_opy_ else -1
def bstack11111111_opy_(bstack1lllll1l1l_opy_):
  global CONFIG
  if not bstack11l1_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫए") in CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬऐ")]:
    return
  CONFIG[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ऑ")] = CONFIG[bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऒ")].replace(
    bstack11l1_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨओ"),
    str(bstack1lllll1l1l_opy_)
  )
def bstack11lll1ll11_opy_():
  global CONFIG
  if not bstack11l1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭औ") in CONFIG[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪक")]:
    return
  bstack11l1l1lll_opy_ = datetime.datetime.now()
  bstack1l1l111ll_opy_ = bstack11l1l1lll_opy_.strftime(bstack11l1_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧख"))
  CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬग")] = CONFIG[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭घ")].replace(
    bstack11l1_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫङ"),
    bstack1l1l111ll_opy_
  )
def bstack11lll11l1_opy_():
  global CONFIG
  if bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨच") in CONFIG and not bool(CONFIG[bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩछ")]):
    del CONFIG[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪज")]
    return
  if not bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫझ") in CONFIG:
    CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬञ")] = bstack11l1_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧट")
  if bstack11l1_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫठ") in CONFIG[bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨड")]:
    bstack11lll1ll11_opy_()
    os.environ[bstack11l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫढ")] = CONFIG[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪण")]
  if not bstack11l1_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫत") in CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬथ")]:
    return
  bstack1lllll1l1l_opy_ = bstack11l1_opy_ (u"ࠫࠬद")
  bstack1ll11ll11_opy_ = bstack1llll1ll_opy_()
  if bstack1ll11ll11_opy_ != -1:
    bstack1lllll1l1l_opy_ = bstack11l1_opy_ (u"ࠬࡉࡉࠡࠩध") + str(bstack1ll11ll11_opy_)
  if bstack1lllll1l1l_opy_ == bstack11l1_opy_ (u"࠭ࠧन"):
    bstack1l11l1ll11_opy_ = bstack1lll1ll1_opy_(CONFIG[bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪऩ")])
    if bstack1l11l1ll11_opy_ != -1:
      bstack1lllll1l1l_opy_ = str(bstack1l11l1ll11_opy_)
  if bstack1lllll1l1l_opy_:
    bstack11111111_opy_(bstack1lllll1l1l_opy_)
    os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬप")] = CONFIG[bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫफ")]
def bstack1l11lllll_opy_(bstack111l111ll_opy_, bstack1l1ll1l1l_opy_, path):
  bstack1ll1l11l1l_opy_ = {
    bstack11l1_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧब"): bstack1l1ll1l1l_opy_
  }
  if os.path.exists(path):
    bstack1lll1l11l1_opy_ = json.load(open(path, bstack11l1_opy_ (u"ࠫࡷࡨࠧभ")))
  else:
    bstack1lll1l11l1_opy_ = {}
  bstack1lll1l11l1_opy_[bstack111l111ll_opy_] = bstack1ll1l11l1l_opy_
  with open(path, bstack11l1_opy_ (u"ࠧࡽࠫࠣम")) as outfile:
    json.dump(bstack1lll1l11l1_opy_, outfile)
def bstack1lll1ll1_opy_(bstack111l111ll_opy_):
  bstack111l111ll_opy_ = str(bstack111l111ll_opy_)
  bstack1llllllll_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"࠭ࡾࠨय")), bstack11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧर"))
  try:
    if not os.path.exists(bstack1llllllll_opy_):
      os.makedirs(bstack1llllllll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠨࢀࠪऱ")), bstack11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩल"), bstack11l1_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬळ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l1_opy_ (u"ࠫࡼ࠭ऴ")):
        pass
      with open(file_path, bstack11l1_opy_ (u"ࠧࡽࠫࠣव")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l1_opy_ (u"࠭ࡲࠨश")) as bstack1ll1l11lll_opy_:
      bstack1llllll111_opy_ = json.load(bstack1ll1l11lll_opy_)
    if bstack111l111ll_opy_ in bstack1llllll111_opy_:
      bstack111l1l111_opy_ = bstack1llllll111_opy_[bstack111l111ll_opy_][bstack11l1_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫष")]
      bstack1l1lll11l1_opy_ = int(bstack111l1l111_opy_) + 1
      bstack1l11lllll_opy_(bstack111l111ll_opy_, bstack1l1lll11l1_opy_, file_path)
      return bstack1l1lll11l1_opy_
    else:
      bstack1l11lllll_opy_(bstack111l111ll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11111llll_opy_.format(str(e)))
    return -1
def bstack1ll11ll1l1_opy_(config):
  if not config[bstack11l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪस")] or not config[bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬह")]:
    return True
  else:
    return False
def bstack11ll1ll1_opy_(config, index=0):
  global bstack11llll1l1l_opy_
  bstack1ll1l11111_opy_ = {}
  caps = bstack1111l1ll_opy_ + bstack1ll1l111_opy_
  if config.get(bstack11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧऺ"), False):
    bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨऻ")] = True
    bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴ़ࠩ")] = config.get(bstack11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪऽ"), {})
  if bstack11llll1l1l_opy_:
    caps += bstack1l111l1ll_opy_
  for key in config:
    if key in caps + [bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪा")]:
      continue
    bstack1ll1l11111_opy_[key] = config[key]
  if bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫि") in config:
    for bstack1lllllll11_opy_ in config[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬी")][index]:
      if bstack1lllllll11_opy_ in caps:
        continue
      bstack1ll1l11111_opy_[bstack1lllllll11_opy_] = config[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ु")][index][bstack1lllllll11_opy_]
  bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ू")] = socket.gethostname()
  if bstack11l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ृ") in bstack1ll1l11111_opy_:
    del (bstack1ll1l11111_opy_[bstack11l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧॄ")])
  return bstack1ll1l11111_opy_
def bstack111lll1l1_opy_(config):
  global bstack11llll1l1l_opy_
  bstack11111ll1l_opy_ = {}
  caps = bstack1ll1l111_opy_
  if bstack11llll1l1l_opy_:
    caps += bstack1l111l1ll_opy_
  for key in caps:
    if key in config:
      bstack11111ll1l_opy_[key] = config[key]
  return bstack11111ll1l_opy_
def bstack1ll1111lll_opy_(bstack1ll1l11111_opy_, bstack11111ll1l_opy_):
  bstack1l1l1l1lll_opy_ = {}
  for key in bstack1ll1l11111_opy_.keys():
    if key in bstack11l11l1ll_opy_:
      bstack1l1l1l1lll_opy_[bstack11l11l1ll_opy_[key]] = bstack1ll1l11111_opy_[key]
    else:
      bstack1l1l1l1lll_opy_[key] = bstack1ll1l11111_opy_[key]
  for key in bstack11111ll1l_opy_:
    if key in bstack11l11l1ll_opy_:
      bstack1l1l1l1lll_opy_[bstack11l11l1ll_opy_[key]] = bstack11111ll1l_opy_[key]
    else:
      bstack1l1l1l1lll_opy_[key] = bstack11111ll1l_opy_[key]
  return bstack1l1l1l1lll_opy_
def bstack11ll1l11l_opy_(config, index=0):
  global bstack11llll1l1l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l111l1lll_opy_ = bstack1l111l1l_opy_(bstack1l1l1l1111_opy_, config, logger)
  bstack11111ll1l_opy_ = bstack111lll1l1_opy_(config)
  bstack1ll1lll1l_opy_ = bstack1ll1l111_opy_
  bstack1ll1lll1l_opy_ += bstack1lllll1lll_opy_
  bstack11111ll1l_opy_ = update(bstack11111ll1l_opy_, bstack1l111l1lll_opy_)
  if bstack11llll1l1l_opy_:
    bstack1ll1lll1l_opy_ += bstack1l111l1ll_opy_
  if bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪॅ") in config:
    if bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ॆ") in config[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬे")][index]:
      caps[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨै")] = config[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॉ")][index][bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪॊ")]
    if bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧो") in config[bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪौ")][index]:
      caps[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯्ࠩ")] = str(config[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬॎ")][index][bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫॏ")])
    bstack1lll111ll1_opy_ = bstack1l111l1l_opy_(bstack1l1l1l1111_opy_, config[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॐ")][index], logger)
    bstack1ll1lll1l_opy_ += list(bstack1lll111ll1_opy_.keys())
    for bstack11l1ll111_opy_ in bstack1ll1lll1l_opy_:
      if bstack11l1ll111_opy_ in config[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ॑")][index]:
        if bstack11l1ll111_opy_ == bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ॒"):
          try:
            bstack1lll111ll1_opy_[bstack11l1ll111_opy_] = str(config[bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ॓")][index][bstack11l1ll111_opy_] * 1.0)
          except:
            bstack1lll111ll1_opy_[bstack11l1ll111_opy_] = str(config[bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ॔")][index][bstack11l1ll111_opy_])
        else:
          bstack1lll111ll1_opy_[bstack11l1ll111_opy_] = config[bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬॕ")][index][bstack11l1ll111_opy_]
        del (config[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ॖ")][index][bstack11l1ll111_opy_])
    bstack11111ll1l_opy_ = update(bstack11111ll1l_opy_, bstack1lll111ll1_opy_)
  bstack1ll1l11111_opy_ = bstack11ll1ll1_opy_(config, index)
  for bstack11ll11111_opy_ in bstack1ll1l111_opy_ + list(bstack1l111l1lll_opy_.keys()):
    if bstack11ll11111_opy_ in bstack1ll1l11111_opy_:
      bstack11111ll1l_opy_[bstack11ll11111_opy_] = bstack1ll1l11111_opy_[bstack11ll11111_opy_]
      del (bstack1ll1l11111_opy_[bstack11ll11111_opy_])
  if bstack1l11l1l1_opy_(config):
    bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫॗ")] = True
    caps.update(bstack11111ll1l_opy_)
    caps[bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭क़")] = bstack1ll1l11111_opy_
  else:
    bstack1ll1l11111_opy_[bstack11l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ख़")] = False
    caps.update(bstack1ll1111lll_opy_(bstack1ll1l11111_opy_, bstack11111ll1l_opy_))
    if bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬग़") in caps:
      caps[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩज़")] = caps[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")]
      del (caps[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨढ़")])
    if bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬफ़") in caps:
      caps[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧय़")] = caps[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧॠ")]
      del (caps[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨॡ")])
  return caps
def bstack1llll1ll1l_opy_():
  global bstack1l11l1l1l_opy_
  global CONFIG
  if bstack1l1lll11ll_opy_() <= version.parse(bstack11l1_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨॢ")):
    if bstack1l11l1l1l_opy_ != bstack11l1_opy_ (u"ࠩࠪॣ"):
      return bstack11l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ।") + bstack1l11l1l1l_opy_ + bstack11l1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ॥")
    return bstack1llllll11l_opy_
  if bstack1l11l1l1l_opy_ != bstack11l1_opy_ (u"ࠬ࠭०"):
    return bstack11l1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ१") + bstack1l11l1l1l_opy_ + bstack11l1_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ२")
  return bstack1l1l11l111_opy_
def bstack111lll1l_opy_(options):
  return hasattr(options, bstack11l1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ३"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1l1l11_opy_(options, bstack1l1l11ll11_opy_):
  for bstack1l1l11l1l_opy_ in bstack1l1l11ll11_opy_:
    if bstack1l1l11l1l_opy_ in [bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ४"), bstack11l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ५")]:
      continue
    if bstack1l1l11l1l_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1l11l1l_opy_] = update(options._experimental_options[bstack1l1l11l1l_opy_],
                                                         bstack1l1l11ll11_opy_[bstack1l1l11l1l_opy_])
    else:
      options.add_experimental_option(bstack1l1l11l1l_opy_, bstack1l1l11ll11_opy_[bstack1l1l11l1l_opy_])
  if bstack11l1_opy_ (u"ࠫࡦࡸࡧࡴࠩ६") in bstack1l1l11ll11_opy_:
    for arg in bstack1l1l11ll11_opy_[bstack11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪ७")]:
      options.add_argument(arg)
    del (bstack1l1l11ll11_opy_[bstack11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ८")])
  if bstack11l1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ९") in bstack1l1l11ll11_opy_:
    for ext in bstack1l1l11ll11_opy_[bstack11l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ॰")]:
      options.add_extension(ext)
    del (bstack1l1l11ll11_opy_[bstack11l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ॱ")])
def bstack1lll1l1l_opy_(options, bstack11l1lll1l_opy_):
  if bstack11l1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩॲ") in bstack11l1lll1l_opy_:
    for bstack1ll1l1ll11_opy_ in bstack11l1lll1l_opy_[bstack11l1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪॳ")]:
      if bstack1ll1l1ll11_opy_ in options._preferences:
        options._preferences[bstack1ll1l1ll11_opy_] = update(options._preferences[bstack1ll1l1ll11_opy_], bstack11l1lll1l_opy_[bstack11l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫॴ")][bstack1ll1l1ll11_opy_])
      else:
        options.set_preference(bstack1ll1l1ll11_opy_, bstack11l1lll1l_opy_[bstack11l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬॵ")][bstack1ll1l1ll11_opy_])
  if bstack11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬॶ") in bstack11l1lll1l_opy_:
    for arg in bstack11l1lll1l_opy_[bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ॷ")]:
      options.add_argument(arg)
def bstack1l1llll1_opy_(options, bstack111111l1l_opy_):
  if bstack11l1_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪॸ") in bstack111111l1l_opy_:
    options.use_webview(bool(bstack111111l1l_opy_[bstack11l1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫॹ")]))
  bstack11l1l1l11_opy_(options, bstack111111l1l_opy_)
def bstack11ll1l1l11_opy_(options, bstack1lll11ll_opy_):
  for bstack1l11111ll1_opy_ in bstack1lll11ll_opy_:
    if bstack1l11111ll1_opy_ in [bstack11l1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨॺ"), bstack11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪॻ")]:
      continue
    options.set_capability(bstack1l11111ll1_opy_, bstack1lll11ll_opy_[bstack1l11111ll1_opy_])
  if bstack11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫॼ") in bstack1lll11ll_opy_:
    for arg in bstack1lll11ll_opy_[bstack11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬॽ")]:
      options.add_argument(arg)
  if bstack11l1_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬॾ") in bstack1lll11ll_opy_:
    options.bstack1l1ll1ll_opy_(bool(bstack1lll11ll_opy_[bstack11l1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ॿ")]))
def bstack1111l1l11_opy_(options, bstack111l11ll1_opy_):
  for bstack11ll1l1ll1_opy_ in bstack111l11ll1_opy_:
    if bstack11ll1l1ll1_opy_ in [bstack11l1_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧঀ"), bstack11l1_opy_ (u"ࠫࡦࡸࡧࡴࠩঁ")]:
      continue
    options._options[bstack11ll1l1ll1_opy_] = bstack111l11ll1_opy_[bstack11ll1l1ll1_opy_]
  if bstack11l1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩং") in bstack111l11ll1_opy_:
    for bstack1ll111ll_opy_ in bstack111l11ll1_opy_[bstack11l1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪঃ")]:
      options.bstack11ll11l11l_opy_(
        bstack1ll111ll_opy_, bstack111l11ll1_opy_[bstack11l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ঄")][bstack1ll111ll_opy_])
  if bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭অ") in bstack111l11ll1_opy_:
    for arg in bstack111l11ll1_opy_[bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧআ")]:
      options.add_argument(arg)
def bstack111111lll_opy_(options, caps):
  if not hasattr(options, bstack11l1_opy_ (u"ࠪࡏࡊ࡟ࠧই")):
    return
  if options.KEY == bstack11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩঈ") and options.KEY in caps:
    bstack11l1l1l11_opy_(options, caps[bstack11l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪউ")])
  elif options.KEY == bstack11l1_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫঊ") and options.KEY in caps:
    bstack1lll1l1l_opy_(options, caps[bstack11l1_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬঋ")])
  elif options.KEY == bstack11l1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঌ") and options.KEY in caps:
    bstack11ll1l1l11_opy_(options, caps[bstack11l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ঍")])
  elif options.KEY == bstack11l1_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ঎") and options.KEY in caps:
    bstack1l1llll1_opy_(options, caps[bstack11l1_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬএ")])
  elif options.KEY == bstack11l1_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫঐ") and options.KEY in caps:
    bstack1111l1l11_opy_(options, caps[bstack11l1_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ঑")])
def bstack1lll11llll_opy_(caps):
  global bstack11llll1l1l_opy_
  if isinstance(os.environ.get(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ঒")), str):
    bstack11llll1l1l_opy_ = eval(os.getenv(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩও")))
  if bstack11llll1l1l_opy_:
    if bstack11lll11l1l_opy_() < version.parse(bstack11l1_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨঔ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪক")
    if bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩখ") in caps:
      browser = caps[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪগ")]
    elif bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧঘ") in caps:
      browser = caps[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨঙ")]
    browser = str(browser).lower()
    if browser == bstack11l1_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨচ") or browser == bstack11l1_opy_ (u"ࠩ࡬ࡴࡦࡪࠧছ"):
      browser = bstack11l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪজ")
    if browser == bstack11l1_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬঝ"):
      browser = bstack11l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬঞ")
    if browser not in [bstack11l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ট"), bstack11l1_opy_ (u"ࠧࡦࡦࡪࡩࠬঠ"), bstack11l1_opy_ (u"ࠨ࡫ࡨࠫড"), bstack11l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩঢ"), bstack11l1_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫণ")]:
      return None
    try:
      package = bstack11l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ত").format(browser)
      name = bstack11l1_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭থ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack111lll1l_opy_(options):
        return None
      for bstack11ll11111_opy_ in caps.keys():
        options.set_capability(bstack11ll11111_opy_, caps[bstack11ll11111_opy_])
      bstack111111lll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11l111lll_opy_(options, bstack111ll11ll_opy_):
  if not bstack111lll1l_opy_(options):
    return
  for bstack11ll11111_opy_ in bstack111ll11ll_opy_.keys():
    if bstack11ll11111_opy_ in bstack1lllll1lll_opy_:
      continue
    if bstack11ll11111_opy_ in options._caps and type(options._caps[bstack11ll11111_opy_]) in [dict, list]:
      options._caps[bstack11ll11111_opy_] = update(options._caps[bstack11ll11111_opy_], bstack111ll11ll_opy_[bstack11ll11111_opy_])
    else:
      options.set_capability(bstack11ll11111_opy_, bstack111ll11ll_opy_[bstack11ll11111_opy_])
  bstack111111lll_opy_(options, bstack111ll11ll_opy_)
  if bstack11l1_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬদ") in options._caps:
    if options._caps[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬধ")] and options._caps[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ন")].lower() != bstack11l1_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ঩"):
      del options._caps[bstack11l1_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩপ")]
def bstack1l1ll111ll_opy_(proxy_config):
  if bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨফ") in proxy_config:
    proxy_config[bstack11l1_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧব")] = proxy_config[bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪভ")]
    del (proxy_config[bstack11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫম")])
  if bstack11l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫয") in proxy_config and proxy_config[bstack11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬর")].lower() != bstack11l1_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪ঱"):
    proxy_config[bstack11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧল")] = bstack11l1_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬ঳")
  if bstack11l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫ঴") in proxy_config:
    proxy_config[bstack11l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ঵")] = bstack11l1_opy_ (u"ࠨࡲࡤࡧࠬশ")
  return proxy_config
def bstack1ll1ll11ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨষ") in config:
    return proxy
  config[bstack11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩস")] = bstack1l1ll111ll_opy_(config[bstack11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪহ")])
  if proxy == None:
    proxy = Proxy(config[bstack11l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ঺")])
  return proxy
def bstack11l11l111_opy_(self):
  global CONFIG
  global bstack111ll1lll_opy_
  try:
    proxy = bstack1ll11ll111_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l1_opy_ (u"࠭࠮ࡱࡣࡦࠫ঻")):
        proxies = bstack1l1111l1ll_opy_(proxy, bstack1llll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll1l11_opy_ = proxies.popitem()
          if bstack11l1_opy_ (u"ࠢ࠻࠱࠲়ࠦ") in bstack1ll1ll1l11_opy_:
            return bstack1ll1ll1l11_opy_
          else:
            return bstack11l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤঽ") + bstack1ll1ll1l11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨা").format(str(e)))
  return bstack111ll1lll_opy_(self)
def bstack11llll111_opy_():
  global CONFIG
  return bstack11ll1lll1l_opy_(CONFIG) and bstack1llll1lll1_opy_() and bstack1l1lll11ll_opy_() >= version.parse(bstack1l1ll11ll_opy_)
def bstack11llll1111_opy_():
  global CONFIG
  return (bstack11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ি") in CONFIG or bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨী") in CONFIG) and bstack111l111l_opy_()
def bstack111l1ll1_opy_(config):
  bstack1llll11l11_opy_ = {}
  if bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩু") in config:
    bstack1llll11l11_opy_ = config[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪূ")]
  if bstack11l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ৃ") in config:
    bstack1llll11l11_opy_ = config[bstack11l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧৄ")]
  proxy = bstack1ll11ll111_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ৅")) and os.path.isfile(proxy):
      bstack1llll11l11_opy_[bstack11l1_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭৆")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩে")):
        proxies = bstack1l1l1l1ll_opy_(config, bstack1llll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll1l11_opy_ = proxies.popitem()
          if bstack11l1_opy_ (u"ࠧࡀ࠯࠰ࠤৈ") in bstack1ll1ll1l11_opy_:
            parsed_url = urlparse(bstack1ll1ll1l11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l1_opy_ (u"ࠨ࠺࠰࠱ࠥ৉") + bstack1ll1ll1l11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1llll11l11_opy_[bstack11l1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪ৊")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1llll11l11_opy_[bstack11l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫো")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1llll11l11_opy_[bstack11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬৌ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1llll11l11_opy_[bstack11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ্࠭")] = str(parsed_url.password)
  return bstack1llll11l11_opy_
def bstack1l11ll1ll1_opy_(config):
  if bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩৎ") in config:
    return config[bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ৏")]
  return {}
def bstack1l1l111l1_opy_(caps):
  global bstack1ll1lllll_opy_
  if bstack11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ৐") in caps:
    caps[bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ৑")][bstack11l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ৒")] = True
    if bstack1ll1lllll_opy_:
      caps[bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ৓")][bstack11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ৔")] = bstack1ll1lllll_opy_
  else:
    caps[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩ৕")] = True
    if bstack1ll1lllll_opy_:
      caps[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭৖")] = bstack1ll1lllll_opy_
@measure(event_name=EVENTS.bstack1l1l1ll1l1_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11lll1ll_opy_():
  global CONFIG
  if not bstack11lll1lll1_opy_(CONFIG):
    return
  if bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪৗ") in CONFIG and bstack1111ll1l1_opy_(CONFIG[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ৘")]):
    if (
      bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ৙") in CONFIG
      and bstack1111ll1l1_opy_(CONFIG[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭৚")].get(bstack11l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧ৛")))
    ):
      logger.debug(bstack11l1_opy_ (u"ࠦࡑࡵࡣࡢ࡮ࠣࡦ࡮ࡴࡡࡳࡻࠣࡲࡴࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡣࡶࠤࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡪࡴࡡࡣ࡮ࡨࡨࠧড়"))
      return
    bstack1llll11l11_opy_ = bstack111l1ll1_opy_(CONFIG)
    bstack1lll1l1ll_opy_(CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨঢ়")], bstack1llll11l11_opy_)
def bstack1lll1l1ll_opy_(key, bstack1llll11l11_opy_):
  global bstack11l11ll1l_opy_
  logger.info(bstack1lll111l1_opy_)
  try:
    bstack11l11ll1l_opy_ = Local()
    bstack1l1lll1ll1_opy_ = {bstack11l1_opy_ (u"࠭࡫ࡦࡻࠪ৞"): key}
    bstack1l1lll1ll1_opy_.update(bstack1llll11l11_opy_)
    logger.debug(bstack1l1ll111_opy_.format(str(bstack1l1lll1ll1_opy_)))
    bstack11l11ll1l_opy_.start(**bstack1l1lll1ll1_opy_)
    if bstack11l11ll1l_opy_.isRunning():
      logger.info(bstack1l11l1llll_opy_)
  except Exception as e:
    bstack1l11ll11l_opy_(bstack1111lllll_opy_.format(str(e)))
def bstack1l111l11l_opy_():
  global bstack11l11ll1l_opy_
  if bstack11l11ll1l_opy_.isRunning():
    logger.info(bstack1l1l11ll_opy_)
    bstack11l11ll1l_opy_.stop()
  bstack11l11ll1l_opy_ = None
def bstack1l11ll1lll_opy_(bstack1l1ll1ll1l_opy_=[]):
  global CONFIG
  bstack1111ll1l_opy_ = []
  bstack1l1l11111l_opy_ = [bstack11l1_opy_ (u"ࠧࡰࡵࠪয়"), bstack11l1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫৠ"), bstack11l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ৡ"), bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬৢ"), bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩৣ"), bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭৤")]
  try:
    for err in bstack1l1ll1ll1l_opy_:
      bstack1lllllll1l_opy_ = {}
      for k in bstack1l1l11111l_opy_:
        val = CONFIG[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৥")][int(err[bstack11l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭০")])].get(k)
        if val:
          bstack1lllllll1l_opy_[k] = val
      if(err[bstack11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ১")] != bstack11l1_opy_ (u"ࠩࠪ২")):
        bstack1lllllll1l_opy_[bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ৩")] = {
          err[bstack11l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ৪")]: err[bstack11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ৫")]
        }
        bstack1111ll1l_opy_.append(bstack1lllllll1l_opy_)
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ৬") + str(e))
  finally:
    return bstack1111ll1l_opy_
def bstack1l11l1lll_opy_(file_name):
  bstack11llll11l1_opy_ = []
  try:
    bstack1l111l11ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l111l11ll_opy_):
      with open(bstack1l111l11ll_opy_) as f:
        bstack111ll1ll_opy_ = json.load(f)
        bstack11llll11l1_opy_ = bstack111ll1ll_opy_
      os.remove(bstack1l111l11ll_opy_)
    return bstack11llll11l1_opy_
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩ࡭ࡳࡪࡩ࡯ࡩࠣࡩࡷࡸ࡯ࡳࠢ࡯࡭ࡸࡺ࠺ࠡࠩ৭") + str(e))
    return bstack11llll11l1_opy_
def bstack1l11lll1ll_opy_():
  global bstack1l11ll1l1_opy_
  global bstack1ll111l111_opy_
  global bstack1l11111l1_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1llll1l1_opy_
  global bstack1l1l111111_opy_
  global CONFIG
  bstack11l1111l1_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ৮"))
  if bstack11l1111l1_opy_ in [bstack11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ৯"), bstack11l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩৰ")]:
    bstack1ll1l1l111_opy_()
  percy.shutdown()
  if bstack1l11ll1l1_opy_:
    logger.warning(bstack11ll11l1_opy_.format(str(bstack1l11ll1l1_opy_)))
  else:
    try:
      bstack1lll1l11l1_opy_ = bstack11l1llll_opy_(bstack11l1_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪৱ"), logger)
      if bstack1lll1l11l1_opy_.get(bstack11l1_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ৲")) and bstack1lll1l11l1_opy_.get(bstack11l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ৳")).get(bstack11l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ৴")):
        logger.warning(bstack11ll11l1_opy_.format(str(bstack1lll1l11l1_opy_[bstack11l1_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭৵")][bstack11l1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ৶")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1lllll1111_opy_)
  global bstack11l11ll1l_opy_
  if bstack11l11ll1l_opy_:
    bstack1l111l11l_opy_()
  try:
    for driver in bstack1ll111l111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1ll1lll_opy_)
  if bstack1l1l111111_opy_ == bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ৷"):
    bstack1llll1l1_opy_ = bstack1l11l1lll_opy_(bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ৸"))
  if bstack1l1l111111_opy_ == bstack11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ৹") and len(bstack1l1ll11l1l_opy_) == 0:
    bstack1l1ll11l1l_opy_ = bstack1l11l1lll_opy_(bstack11l1_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ৺"))
    if len(bstack1l1ll11l1l_opy_) == 0:
      bstack1l1ll11l1l_opy_ = bstack1l11l1lll_opy_(bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭৻"))
  bstack1ll1l1ll1_opy_ = bstack11l1_opy_ (u"ࠨࠩৼ")
  if len(bstack1l11111l1_opy_) > 0:
    bstack1ll1l1ll1_opy_ = bstack1l11ll1lll_opy_(bstack1l11111l1_opy_)
  elif len(bstack1l1ll11l1l_opy_) > 0:
    bstack1ll1l1ll1_opy_ = bstack1l11ll1lll_opy_(bstack1l1ll11l1l_opy_)
  elif len(bstack1llll1l1_opy_) > 0:
    bstack1ll1l1ll1_opy_ = bstack1l11ll1lll_opy_(bstack1llll1l1_opy_)
  elif len(bstack1l11ll1l11_opy_) > 0:
    bstack1ll1l1ll1_opy_ = bstack1l11ll1lll_opy_(bstack1l11ll1l11_opy_)
  if bool(bstack1ll1l1ll1_opy_):
    bstack11lllll11l_opy_(bstack1ll1l1ll1_opy_)
  else:
    bstack11lllll11l_opy_()
  bstack1ll1lll1ll_opy_(bstack1l1lll1l_opy_, logger)
  bstack11llll11_opy_.bstack1ll11l1ll1_opy_(CONFIG)
  if len(bstack1llll1l1_opy_) > 0:
    sys.exit(len(bstack1llll1l1_opy_))
def bstack11l11l1l_opy_(bstack11ll1ll1l1_opy_, frame):
  global bstack1l1l1lll1_opy_
  logger.error(bstack1l1lllll11_opy_)
  bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ৽"), bstack11ll1ll1l1_opy_)
  if hasattr(signal, bstack11l1_opy_ (u"ࠪࡗ࡮࡭࡮ࡢ࡮ࡶࠫ৾")):
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ৿"), signal.Signals(bstack11ll1ll1l1_opy_).name)
  else:
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ਀"), bstack11l1_opy_ (u"࠭ࡓࡊࡉࡘࡒࡐࡔࡏࡘࡐࠪਁ"))
  bstack11l1111l1_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨਂ"))
  if bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨਃ"):
    bstack1ll1llllll_opy_.stop(bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ਄")))
  bstack1l11lll1ll_opy_()
  sys.exit(1)
def bstack1l11ll11l_opy_(err):
  logger.critical(bstack1ll11lll1l_opy_.format(str(err)))
  bstack11lllll11l_opy_(bstack1ll11lll1l_opy_.format(str(err)), True)
  atexit.unregister(bstack1l11lll1ll_opy_)
  bstack1ll1l1l111_opy_()
  sys.exit(1)
def bstack111l1111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11lllll11l_opy_(message, True)
  atexit.unregister(bstack1l11lll1ll_opy_)
  bstack1ll1l1l111_opy_()
  sys.exit(1)
def bstack1l1l1ll1_opy_():
  global CONFIG
  global bstack111l1llll_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1l1l1lll1l_opy_
  CONFIG = bstack11lllll1l1_opy_()
  load_dotenv(CONFIG.get(bstack11l1_opy_ (u"ࠪࡩࡳࡼࡆࡪ࡮ࡨࠫਅ")))
  bstack11lllll1ll_opy_()
  bstack111111l11_opy_()
  CONFIG = bstack1ll1llll1_opy_(CONFIG)
  update(CONFIG, bstack1ll1l1l11l_opy_)
  update(CONFIG, bstack111l1llll_opy_)
  CONFIG = bstack1l11llllll_opy_(CONFIG)
  bstack1l1l1lll1l_opy_ = bstack11lll1lll1_opy_(CONFIG)
  os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧਆ")] = bstack1l1l1lll1l_opy_.__str__()
  bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ਇ"), bstack1l1l1lll1l_opy_)
  if (bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਈ") in CONFIG and bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪਉ") in bstack111l1llll_opy_) or (
          bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫਊ") in CONFIG and bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ਋") not in bstack1ll1l1l11l_opy_):
    if os.getenv(bstack11l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ਌")):
      CONFIG[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭਍")] = os.getenv(bstack11l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ਎"))
    else:
      bstack11lll11l1_opy_()
  elif (bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਏ") not in CONFIG and bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਐ") in CONFIG) or (
          bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ਑") in bstack1ll1l1l11l_opy_ and bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ਒") not in bstack111l1llll_opy_):
    del (CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬਓ")])
  if bstack1ll11ll1l1_opy_(CONFIG):
    bstack1l11ll11l_opy_(bstack11lll1l11_opy_)
  Config.bstack1l1l11lll1_opy_().bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨਔ"), CONFIG[bstack11l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧਕ")])
  bstack111ll1l1_opy_()
  bstack1l11l111_opy_()
  if bstack11llll1l1l_opy_:
    CONFIG[bstack11l1_opy_ (u"࠭ࡡࡱࡲࠪਖ")] = bstack11l11l1l1_opy_(CONFIG)
    logger.info(bstack1ll111111l_opy_.format(CONFIG[bstack11l1_opy_ (u"ࠧࡢࡲࡳࠫਗ")]))
  if not bstack1l1l1lll1l_opy_:
    CONFIG[bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਘ")] = [{}]
def bstack1l1l1l1l1l_opy_(config, bstack1lll1l1111_opy_):
  global CONFIG
  global bstack11llll1l1l_opy_
  CONFIG = config
  bstack11llll1l1l_opy_ = bstack1lll1l1111_opy_
def bstack1l11l111_opy_():
  global CONFIG
  global bstack11llll1l1l_opy_
  if bstack11l1_opy_ (u"ࠩࡤࡴࡵ࠭ਙ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack111l1111_opy_(e, bstack1ll1lll1l1_opy_)
    bstack11llll1l1l_opy_ = True
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩਚ"), True)
def bstack11l11l1l1_opy_(config):
  bstack1l11ll1l1l_opy_ = bstack11l1_opy_ (u"ࠫࠬਛ")
  app = config[bstack11l1_opy_ (u"ࠬࡧࡰࡱࠩਜ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l1lll_opy_:
      if os.path.exists(app):
        bstack1l11ll1l1l_opy_ = bstack11llll11ll_opy_(config, app)
      elif bstack1ll1l111l_opy_(app):
        bstack1l11ll1l1l_opy_ = app
      else:
        bstack1l11ll11l_opy_(bstack1lllll111_opy_.format(app))
    else:
      if bstack1ll1l111l_opy_(app):
        bstack1l11ll1l1l_opy_ = app
      elif os.path.exists(app):
        bstack1l11ll1l1l_opy_ = bstack11llll11ll_opy_(app)
      else:
        bstack1l11ll11l_opy_(bstack1l1l1l11ll_opy_)
  else:
    if len(app) > 2:
      bstack1l11ll11l_opy_(bstack11lll11111_opy_)
    elif len(app) == 2:
      if bstack11l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫਝ") in app and bstack11l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪਞ") in app:
        if os.path.exists(app[bstack11l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭ਟ")]):
          bstack1l11ll1l1l_opy_ = bstack11llll11ll_opy_(config, app[bstack11l1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧਠ")], app[bstack11l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ਡ")])
        else:
          bstack1l11ll11l_opy_(bstack1lllll111_opy_.format(app))
      else:
        bstack1l11ll11l_opy_(bstack11lll11111_opy_)
    else:
      for key in app:
        if key in bstack1ll11l1l_opy_:
          if key == bstack11l1_opy_ (u"ࠫࡵࡧࡴࡩࠩਢ"):
            if os.path.exists(app[key]):
              bstack1l11ll1l1l_opy_ = bstack11llll11ll_opy_(config, app[key])
            else:
              bstack1l11ll11l_opy_(bstack1lllll111_opy_.format(app))
          else:
            bstack1l11ll1l1l_opy_ = app[key]
        else:
          bstack1l11ll11l_opy_(bstack1l1l111lll_opy_)
  return bstack1l11ll1l1l_opy_
def bstack1ll1l111l_opy_(bstack1l11ll1l1l_opy_):
  import re
  bstack1ll1l1l11_opy_ = re.compile(bstack11l1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧਣ"))
  bstack111lllll1_opy_ = re.compile(bstack11l1_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥਤ"))
  if bstack11l1_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭ਥ") in bstack1l11ll1l1l_opy_ or re.fullmatch(bstack1ll1l1l11_opy_, bstack1l11ll1l1l_opy_) or re.fullmatch(bstack111lllll1_opy_, bstack1l11ll1l1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1lll11lll1_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11llll11ll_opy_(config, path, bstack1l1111l1l1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l1_opy_ (u"ࠨࡴࡥࠫਦ")).read()).hexdigest()
  bstack1ll1ll1lll_opy_ = bstack1ll1l1111_opy_(md5_hash)
  bstack1l11ll1l1l_opy_ = None
  if bstack1ll1ll1lll_opy_:
    logger.info(bstack1ll1l1lll_opy_.format(bstack1ll1ll1lll_opy_, md5_hash))
    return bstack1ll1ll1lll_opy_
  bstack11ll111lll_opy_ = MultipartEncoder(
    fields={
      bstack11l1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧਧ"): (os.path.basename(path), open(os.path.abspath(path), bstack11l1_opy_ (u"ࠪࡶࡧ࠭ਨ")), bstack11l1_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨ਩")),
      bstack11l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨਪ"): bstack1l1111l1l1_opy_
    }
  )
  response = requests.post(bstack11l11l11l_opy_, data=bstack11ll111lll_opy_,
                           headers={bstack11l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬਫ"): bstack11ll111lll_opy_.content_type},
                           auth=(config[bstack11l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩਬ")], config[bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫਭ")]))
  try:
    res = json.loads(response.text)
    bstack1l11ll1l1l_opy_ = res[bstack11l1_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪਮ")]
    logger.info(bstack11ll1ll11_opy_.format(bstack1l11ll1l1l_opy_))
    bstack1l1111111_opy_(md5_hash, bstack1l11ll1l1l_opy_)
  except ValueError as err:
    bstack1l11ll11l_opy_(bstack1l11l11l1_opy_.format(str(err)))
  return bstack1l11ll1l1l_opy_
def bstack111ll1l1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1lllll11l_opy_
  bstack1lll111111_opy_ = 1
  bstack11ll1l1111_opy_ = 1
  if bstack11l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪਯ") in CONFIG:
    bstack11ll1l1111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫਰ")]
  else:
    bstack11ll1l1111_opy_ = bstack11111111l_opy_(framework_name, args) or 1
  if bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ਱") in CONFIG:
    bstack1lll111111_opy_ = len(CONFIG[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਲ")])
  bstack1lllll11l_opy_ = int(bstack11ll1l1111_opy_) * int(bstack1lll111111_opy_)
def bstack11111111l_opy_(framework_name, args):
  if framework_name == bstack1l1111l11l_opy_ and args and bstack11l1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬਲ਼") in args:
      bstack1lll1l11l_opy_ = args.index(bstack11l1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭਴"))
      return int(args[bstack1lll1l11l_opy_ + 1]) or 1
  return 1
def bstack1ll1l1111_opy_(md5_hash):
  bstack1lllll1l11_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠩࢁࠫਵ")), bstack11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪਸ਼"), bstack11l1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ਷"))
  if os.path.exists(bstack1lllll1l11_opy_):
    bstack1l1l1111l1_opy_ = json.load(open(bstack1lllll1l11_opy_, bstack11l1_opy_ (u"ࠬࡸࡢࠨਸ")))
    if md5_hash in bstack1l1l1111l1_opy_:
      bstack1l1l1lllll_opy_ = bstack1l1l1111l1_opy_[md5_hash]
      bstack11lll1lll_opy_ = datetime.datetime.now()
      bstack11llll1lll_opy_ = datetime.datetime.strptime(bstack1l1l1lllll_opy_[bstack11l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩਹ")], bstack11l1_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ਺"))
      if (bstack11lll1lll_opy_ - bstack11llll1lll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1l1l1lllll_opy_[bstack11l1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭਻")]):
        return None
      return bstack1l1l1lllll_opy_[bstack11l1_opy_ (u"ࠩ࡬ࡨ਼ࠬ")]
  else:
    return None
def bstack1l1111111_opy_(md5_hash, bstack1l11ll1l1l_opy_):
  bstack1llllllll_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠪࢂࠬ਽")), bstack11l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫਾ"))
  if not os.path.exists(bstack1llllllll_opy_):
    os.makedirs(bstack1llllllll_opy_)
  bstack1lllll1l11_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠬࢄࠧਿ")), bstack11l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ੀ"), bstack11l1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨੁ"))
  bstack11ll1l11_opy_ = {
    bstack11l1_opy_ (u"ࠨ࡫ࡧࠫੂ"): bstack1l11ll1l1l_opy_,
    bstack11l1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ੃"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ੄")),
    bstack11l1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ੅"): str(__version__)
  }
  if os.path.exists(bstack1lllll1l11_opy_):
    bstack1l1l1111l1_opy_ = json.load(open(bstack1lllll1l11_opy_, bstack11l1_opy_ (u"ࠬࡸࡢࠨ੆")))
  else:
    bstack1l1l1111l1_opy_ = {}
  bstack1l1l1111l1_opy_[md5_hash] = bstack11ll1l11_opy_
  with open(bstack1lllll1l11_opy_, bstack11l1_opy_ (u"ࠨࡷࠬࠤੇ")) as outfile:
    json.dump(bstack1l1l1111l1_opy_, outfile)
def bstack1l1lllll_opy_(self):
  return
def bstack1ll11llll_opy_(self):
  return
def bstack1l11lll1l1_opy_(self):
  global bstack1ll1l1lll1_opy_
  bstack1ll1l1lll1_opy_(self)
def bstack1l1l1111l_opy_():
  global bstack111l11ll_opy_
  bstack111l11ll_opy_ = True
@measure(event_name=EVENTS.bstack1llllllll1_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11l111ll1_opy_(self):
  global bstack1llll11l1l_opy_
  global bstack1l1l1ll1l_opy_
  global bstack1ll1l111l1_opy_
  try:
    if bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧੈ") in bstack1llll11l1l_opy_ and self.session_id != None and bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ੉"), bstack11l1_opy_ (u"ࠩࠪ੊")) != bstack11l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫੋ"):
      bstack1lll1l111l_opy_ = bstack11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫੌ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨ੍ࠬ")
      if bstack1lll1l111l_opy_ == bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭੎"):
        bstack11lll1ll1_opy_(logger)
      if self != None:
        bstack11l1111ll_opy_(self, bstack1lll1l111l_opy_, bstack11l1_opy_ (u"ࠧ࠭ࠢࠪ੏").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l1_opy_ (u"ࠨࠩ੐")
    if bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩੑ") in bstack1llll11l1l_opy_ and getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ੒"), None):
      bstack11ll111ll1_opy_.bstack1lll1llll1_opy_(self, bstack1l111ll1l1_opy_, logger, wait=True)
    if bstack11l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ੓") in bstack1llll11l1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11l1111ll_opy_(self, bstack11l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ੔"))
      bstack1ll11ll1l_opy_.bstack1l111llll_opy_(self)
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢ੕") + str(e))
  bstack1ll1l111l1_opy_(self)
  self.session_id = None
def bstack11lll1l1ll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll11111l1_opy_
    global bstack1llll11l1l_opy_
    command_executor = kwargs.get(bstack11l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪ੖"), bstack11l1_opy_ (u"ࠨࠩ੗"))
    bstack1llll1lll_opy_ = False
    if type(command_executor) == str and bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ੘") in command_executor:
      bstack1llll1lll_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ਖ਼") in str(getattr(command_executor, bstack11l1_opy_ (u"ࠫࡤࡻࡲ࡭ࠩਗ਼"), bstack11l1_opy_ (u"ࠬ࠭ਜ਼"))):
      bstack1llll1lll_opy_ = True
    else:
      return bstack1lll1111l_opy_(self, *args, **kwargs)
    if bstack1llll1lll_opy_:
      bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(CONFIG, bstack1llll11l1l_opy_)
      if kwargs.get(bstack11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧੜ")):
        kwargs[bstack11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ੝")] = bstack1ll11111l1_opy_(kwargs[bstack11l1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩਫ਼")], bstack1llll11l1l_opy_, bstack1ll11lll_opy_)
      elif kwargs.get(bstack11l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ੟")):
        kwargs[bstack11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ੠")] = bstack1ll11111l1_opy_(kwargs[bstack11l1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ੡")], bstack1llll11l1l_opy_, bstack1ll11lll_opy_)
  except Exception as e:
    logger.error(bstack11l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧ੢").format(str(e)))
  return bstack1lll1111l_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l11l1l1l1_opy_(self, command_executor=bstack11l1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢ੣"), *args, **kwargs):
  bstack11l111l1l_opy_ = bstack11lll1l1ll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11l11l1l_opy_.on():
    return bstack11l111l1l_opy_
  try:
    logger.debug(bstack11l1_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫ੤").format(str(command_executor)))
    logger.debug(bstack11l1_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪ੥").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ੦") in command_executor._url:
      bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ੧"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ੨") in command_executor):
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭੩"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1lll111_opy_ = getattr(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ੪"), None)
  if bstack11l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ੫") in bstack1llll11l1l_opy_ or bstack11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ੬") in bstack1llll11l1l_opy_:
    bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
  if bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ੭") in bstack1llll11l1l_opy_ and bstack1l1lll111_opy_ and bstack1l1lll111_opy_.get(bstack11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ੮"), bstack11l1_opy_ (u"ࠫࠬ੯")) == bstack11l1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ੰ"):
    bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
  return bstack11l111l1l_opy_
def bstack1ll11l1l11_opy_(args):
  return bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧੱ") in str(args)
def bstack1l1ll11l1_opy_(self, driver_command, *args, **kwargs):
  global bstack1l111lll11_opy_
  global bstack1lll11lll_opy_
  bstack1ll111ll1l_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫੲ"), None) and bstack1l1lll1lll_opy_(
          threading.current_thread(), bstack11l1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧੳ"), None)
  bstack1111ll11l_opy_ = getattr(self, bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩੴ"), None) != None and getattr(self, bstack11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪੵ"), None) == True
  if not bstack1lll11lll_opy_ and bstack1l1l1lll1l_opy_ and bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ੶") in CONFIG and CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ੷")] == True and bstack11l1l111_opy_.bstack1lll111lll_opy_(driver_command) and (bstack1111ll11l_opy_ or bstack1ll111ll1l_opy_) and not bstack1ll11l1l11_opy_(args):
    try:
      bstack1lll11lll_opy_ = True
      logger.debug(bstack11l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨ੸").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬ੹").format(str(err)))
    bstack1lll11lll_opy_ = False
  response = bstack1l111lll11_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ੺") in str(bstack1llll11l1l_opy_).lower() or bstack11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ੻") in str(bstack1llll11l1l_opy_).lower()) and bstack1l11l11l1l_opy_.on():
    try:
      if driver_command == bstack11l1_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧ੼"):
        bstack1ll1llllll_opy_.bstack1l1ll1111_opy_({
            bstack11l1_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪ੽"): response[bstack11l1_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫ੾")],
            bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭੿"): bstack1ll1llllll_opy_.current_test_uuid() if bstack1ll1llllll_opy_.current_test_uuid() else bstack1l11l11l1l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l1l1l1l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l11111ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1l1ll1l_opy_
  global bstack1l11lll1l_opy_
  global bstack1l111l111_opy_
  global bstack1l1ll11l11_opy_
  global bstack1ll111l1l_opy_
  global bstack1llll11l1l_opy_
  global bstack1lll1111l_opy_
  global bstack1ll111l111_opy_
  global bstack111l1l11l_opy_
  global bstack1l111ll1l1_opy_
  CONFIG[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ઀")] = str(bstack1llll11l1l_opy_) + str(__version__)
  bstack1lll1l1l11_opy_ = os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ઁ")]
  bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(CONFIG, bstack1llll11l1l_opy_)
  CONFIG[bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬં")] = bstack1lll1l1l11_opy_
  CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬઃ")] = bstack1ll11lll_opy_
  command_executor = bstack1llll1ll1l_opy_()
  logger.debug(bstack1l1l1ll11_opy_.format(command_executor))
  proxy = bstack1ll1ll11ll_opy_(CONFIG, proxy)
  bstack1ll1111l_opy_ = 0 if bstack1l11lll1l_opy_ < 0 else bstack1l11lll1l_opy_
  try:
    if bstack1l1ll11l11_opy_ is True:
      bstack1ll1111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll111l1l_opy_ is True:
      bstack1ll1111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1ll1111l_opy_ = 0
  bstack111ll11ll_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1ll1111l_opy_)
  logger.debug(bstack1lll1l1lll_opy_.format(str(bstack111ll11ll_opy_)))
  if bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ઄") in CONFIG and bstack1111ll1l1_opy_(CONFIG[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩઅ")]):
    bstack1l1l111l1_opy_(bstack111ll11ll_opy_)
  if bstack1lll11ll1_opy_.bstack111l1ll1l_opy_(CONFIG, bstack1ll1111l_opy_) and bstack1lll11ll1_opy_.bstack1lll1l11_opy_(bstack111ll11ll_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    bstack1lll11ll1_opy_.set_capabilities(bstack111ll11ll_opy_, CONFIG)
  if desired_capabilities:
    bstack11ll11l1l1_opy_ = bstack1ll1llll1_opy_(desired_capabilities)
    bstack11ll11l1l1_opy_[bstack11l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭આ")] = bstack1l11l1l1_opy_(CONFIG)
    bstack1ll1l1l1ll_opy_ = bstack11ll1l11l_opy_(bstack11ll11l1l1_opy_)
    if bstack1ll1l1l1ll_opy_:
      bstack111ll11ll_opy_ = update(bstack1ll1l1l1ll_opy_, bstack111ll11ll_opy_)
    desired_capabilities = None
  if options:
    bstack11l111lll_opy_(options, bstack111ll11ll_opy_)
  if not options:
    options = bstack1lll11llll_opy_(bstack111ll11ll_opy_)
  bstack1l111ll1l1_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪઇ"))[bstack1ll1111l_opy_]
  if proxy and bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨઈ")):
    options.proxy(proxy)
  if options and bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨઉ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l1lll11ll_opy_() < version.parse(bstack11l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩઊ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack111ll11ll_opy_)
  logger.info(bstack1lll1lll1_opy_)
  bstack1ll111l1_opy_.end(EVENTS.bstack1ll1111l1_opy_.value, EVENTS.bstack1ll1111l1_opy_.value + bstack11l1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦઋ"), EVENTS.bstack1ll1111l1_opy_.value + bstack11l1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥઌ"), status=True, failure=None, test_name=bstack1l111l111_opy_)
  if bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ઍ")):
    bstack1lll1111l_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
  elif bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭઎")):
    bstack1lll1111l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨએ")):
    bstack1lll1111l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1lll1111l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l111ll11l_opy_ = bstack11l1_opy_ (u"ࠩࠪઐ")
    if bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫઑ")):
      bstack1l111ll11l_opy_ = self.caps.get(bstack11l1_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ઒"))
    else:
      bstack1l111ll11l_opy_ = self.capabilities.get(bstack11l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧઓ"))
    if bstack1l111ll11l_opy_:
      bstack1lll1ll111_opy_(bstack1l111ll11l_opy_)
      if bstack1l1lll11ll_opy_() <= version.parse(bstack11l1_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ઔ")):
        self.command_executor._url = bstack11l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣક") + bstack1l11l1l1l_opy_ + bstack11l1_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧખ")
      else:
        self.command_executor._url = bstack11l1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦગ") + bstack1l111ll11l_opy_ + bstack11l1_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦઘ")
      logger.debug(bstack11ll1l11l1_opy_.format(bstack1l111ll11l_opy_))
    else:
      logger.debug(bstack1lll1l1ll1_opy_.format(bstack11l1_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧઙ")))
  except Exception as e:
    logger.debug(bstack1lll1l1ll1_opy_.format(e))
  if bstack11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫચ") in bstack1llll11l1l_opy_:
    bstack11l1l11l1_opy_(bstack1l11lll1l_opy_, bstack111l1l11l_opy_)
  bstack1l1l1ll1l_opy_ = self.session_id
  if bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭છ") in bstack1llll11l1l_opy_ or bstack11l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧજ") in bstack1llll11l1l_opy_ or bstack11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧઝ") in bstack1llll11l1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1l1lll111_opy_ = getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪઞ"), None)
  if bstack11l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪટ") in bstack1llll11l1l_opy_ or bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪઠ") in bstack1llll11l1l_opy_:
    bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
  if bstack11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬડ") in bstack1llll11l1l_opy_ and bstack1l1lll111_opy_ and bstack1l1lll111_opy_.get(bstack11l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ઢ"), bstack11l1_opy_ (u"ࠧࠨણ")) == bstack11l1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩત"):
    bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
  bstack1ll111l111_opy_.append(self)
  if bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ") in CONFIG and bstack11l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨદ") in CONFIG[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧધ")][bstack1ll1111l_opy_]:
    bstack1l111l111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨન")][bstack1ll1111l_opy_][bstack11l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ઩")]
  logger.debug(bstack1111ll1ll_opy_.format(bstack1l1l1ll1l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1lll11l1_opy_
    def bstack1l11l11111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11l11ll11_opy_
      if(bstack11l1_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤપ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠨࢀࠪફ")), bstack11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩબ"), bstack11l1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬભ")), bstack11l1_opy_ (u"ࠫࡼ࠭મ")) as fp:
          fp.write(bstack11l1_opy_ (u"ࠧࠨય"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣર")))):
          with open(args[1], bstack11l1_opy_ (u"ࠧࡳࠩ઱")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l1_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧલ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll11l11ll_opy_)
            if bstack11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ળ") in CONFIG and str(CONFIG[bstack11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ઴")]).lower() != bstack11l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪવ"):
                bstack111lll11_opy_ = bstack1lll11l1_opy_()
                bstack11l11lll1_opy_ = bstack11l1_opy_ (u"ࠬ࠭ࠧࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࠼ࠌࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࠼ࠌࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽ࠍ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠ࡭ࡧࡷࠤࡨࡧࡰࡴ࠽ࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࡸࡷࡿࠠࡼࡽࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࠽ࠍࠤࠥࢃࡽࠡࡥࡤࡸࡨ࡮ࠠࠩࡧࡻ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࡩ࡯࡯ࡵࡲࡰࡪ࠴ࡥࡳࡴࡲࡶ࠭ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠺ࠣ࠮ࠣࡩࡽ࠯࠻ࠋࠢࠣࢁࢂࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼࡽࠍࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥ࠭ࡻࡤࡦࡳ࡙ࡷࡲࡽࠨࠢ࠮ࠤࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫ࠯ࠎࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࠎࠥࠦࡽࡾࠫ࠾ࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࡿࢀ࠿ࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࠬ࠭ࠧશ").format(bstack111lll11_opy_=bstack111lll11_opy_)
            lines.insert(1, bstack11l11lll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣષ")), bstack11l1_opy_ (u"ࠧࡸࠩસ")) as bstack1l1l11l1l1_opy_:
              bstack1l1l11l1l1_opy_.writelines(lines)
        CONFIG[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪહ")] = str(bstack1llll11l1l_opy_) + str(__version__)
        bstack1lll1l1l11_opy_ = os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ઺")]
        bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(CONFIG, bstack1llll11l1l_opy_)
        CONFIG[bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭઻")] = bstack1lll1l1l11_opy_
        CONFIG[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ઼࠭")] = bstack1ll11lll_opy_
        bstack1ll1111l_opy_ = 0 if bstack1l11lll1l_opy_ < 0 else bstack1l11lll1l_opy_
        try:
          if bstack1l1ll11l11_opy_ is True:
            bstack1ll1111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll111l1l_opy_ is True:
            bstack1ll1111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1ll1111l_opy_ = 0
        CONFIG[bstack11l1_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧઽ")] = False
        CONFIG[bstack11l1_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧા")] = True
        bstack111ll11ll_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1ll1111l_opy_)
        logger.debug(bstack1lll1l1lll_opy_.format(str(bstack111ll11ll_opy_)))
        if CONFIG.get(bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫિ")):
          bstack1l1l111l1_opy_(bstack111ll11ll_opy_)
        if bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫી") in CONFIG and bstack11l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧુ") in CONFIG[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૂ")][bstack1ll1111l_opy_]:
          bstack1l111l111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧૃ")][bstack1ll1111l_opy_][bstack11l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪૄ")]
        args.append(os.path.join(os.path.expanduser(bstack11l1_opy_ (u"࠭ࡾࠨૅ")), bstack11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ૆"), bstack11l1_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪે")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack111ll11ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦૈ"))
      bstack11l11ll11_opy_ = True
      return bstack1ll1l11l_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l1ll11_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1l11lll1l_opy_
    global bstack1l111l111_opy_
    global bstack1l1ll11l11_opy_
    global bstack1ll111l1l_opy_
    global bstack1llll11l1l_opy_
    CONFIG[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬૉ")] = str(bstack1llll11l1l_opy_) + str(__version__)
    bstack1lll1l1l11_opy_ = os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ૊")]
    bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(CONFIG, bstack1llll11l1l_opy_)
    CONFIG[bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨો")] = bstack1lll1l1l11_opy_
    CONFIG[bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨૌ")] = bstack1ll11lll_opy_
    bstack1ll1111l_opy_ = 0 if bstack1l11lll1l_opy_ < 0 else bstack1l11lll1l_opy_
    try:
      if bstack1l1ll11l11_opy_ is True:
        bstack1ll1111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll111l1l_opy_ is True:
        bstack1ll1111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1ll1111l_opy_ = 0
    CONFIG[bstack11l1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ્")] = True
    bstack111ll11ll_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1ll1111l_opy_)
    logger.debug(bstack1lll1l1lll_opy_.format(str(bstack111ll11ll_opy_)))
    if CONFIG.get(bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ૎")):
      bstack1l1l111l1_opy_(bstack111ll11ll_opy_)
    if bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૏") in CONFIG and bstack11l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨૐ") in CONFIG[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૑")][bstack1ll1111l_opy_]:
      bstack1l111l111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૒")][bstack1ll1111l_opy_][bstack11l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ૓")]
    import urllib
    import json
    if bstack11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ૔") in CONFIG and str(CONFIG[bstack11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ૕")]).lower() != bstack11l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ૖"):
        bstack1l11ll111_opy_ = bstack1lll11l1_opy_()
        bstack111lll11_opy_ = bstack1l11ll111_opy_ + urllib.parse.quote(json.dumps(bstack111ll11ll_opy_))
    else:
        bstack111lll11_opy_ = bstack11l1_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ૗") + urllib.parse.quote(json.dumps(bstack111ll11ll_opy_))
    browser = self.connect(bstack111lll11_opy_)
    return browser
except Exception as e:
    pass
def bstack1111l11l_opy_():
    global bstack11l11ll11_opy_
    global bstack1llll11l1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l1lll_opy_
        global bstack1l1l1lll1_opy_
        if not bstack1l1l1lll1l_opy_:
          global bstack1ll1ll111l_opy_
          if not bstack1ll1ll111l_opy_:
            from bstack_utils.helper import bstack111l1ll11_opy_, bstack1llll1ll1_opy_, bstack11lll1l1_opy_
            bstack1ll1ll111l_opy_ = bstack111l1ll11_opy_()
            bstack1llll1ll1_opy_(bstack1llll11l1l_opy_)
            bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(CONFIG, bstack1llll11l1l_opy_)
            bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨ૘"), bstack1ll11lll_opy_)
          BrowserType.connect = bstack1111l1lll_opy_
          return
        BrowserType.launch = bstack11l1ll11_opy_
        bstack11l11ll11_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l11l11111_opy_
      bstack11l11ll11_opy_ = True
    except Exception as e:
      pass
def bstack1ll11lll11_opy_(context, bstack11ll1111_opy_):
  try:
    context.page.evaluate(bstack11l1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ૙"), bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ૚")+ json.dumps(bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠢࡾࡿࠥ૛"))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ૜"), e)
def bstack1llllll11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l1_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ૝"), bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ૞") + json.dumps(message) + bstack11l1_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ૟") + json.dumps(level) + bstack11l1_opy_ (u"ࠬࢃࡽࠨૠ"))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤૡ"), e)
@measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack111l11lll_opy_(self, url):
  global bstack11llll1ll1_opy_
  try:
    bstack1lll1lll11_opy_(url)
  except Exception as err:
    logger.debug(bstack11l1l1ll1_opy_.format(str(err)))
  try:
    bstack11llll1ll1_opy_(self, url)
  except Exception as e:
    try:
      bstack11ll111ll_opy_ = str(e)
      if any(err_msg in bstack11ll111ll_opy_ for err_msg in bstack1l11ll11ll_opy_):
        bstack1lll1lll11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l1l1ll1_opy_.format(str(err)))
    raise e
def bstack1ll1ll11_opy_(self):
  global bstack1ll1l1l1_opy_
  bstack1ll1l1l1_opy_ = self
  return
def bstack1ll11l11l_opy_(self):
  global bstack111ll1l1l_opy_
  bstack111ll1l1l_opy_ = self
  return
def bstack1ll1lll11_opy_(test_name, bstack11ll111l1_opy_):
  global CONFIG
  if percy.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧૢ"):
    bstack1ll11l11l1_opy_ = os.path.relpath(bstack11ll111l1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1ll11l11l1_opy_)
    bstack1lll11l11l_opy_ = suite_name + bstack11l1_opy_ (u"ࠣ࠯ࠥૣ") + test_name
    threading.current_thread().percySessionName = bstack1lll11l11l_opy_
def bstack1llll1l11l_opy_(self, test, *args, **kwargs):
  global bstack1ll111llll_opy_
  test_name = None
  bstack11ll111l1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11ll111l1_opy_ = str(test.source)
  bstack1ll1lll11_opy_(test_name, bstack11ll111l1_opy_)
  bstack1ll111llll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll111l1l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1lll11l1l_opy_(driver, bstack1lll11l11l_opy_):
  if not bstack1l1ll11111_opy_ and bstack1lll11l11l_opy_:
      bstack11l1l11ll_opy_ = {
          bstack11l1_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ૤"): bstack11l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ૥"),
          bstack11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ૦"): {
              bstack11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ૧"): bstack1lll11l11l_opy_
          }
      }
      bstack1l1111ll_opy_ = bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ૨").format(json.dumps(bstack11l1l11ll_opy_))
      driver.execute_script(bstack1l1111ll_opy_)
  if bstack1l1l1lll_opy_:
      bstack1l111ll1ll_opy_ = {
          bstack11l1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ૩"): bstack11l1_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ૪"),
          bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ૫"): {
              bstack11l1_opy_ (u"ࠪࡨࡦࡺࡡࠨ૬"): bstack1lll11l11l_opy_ + bstack11l1_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭૭"),
              bstack11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ૮"): bstack11l1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ૯")
          }
      }
      if bstack1l1l1lll_opy_.status == bstack11l1_opy_ (u"ࠧࡑࡃࡖࡗࠬ૰"):
          bstack1ll11l111l_opy_ = bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭૱").format(json.dumps(bstack1l111ll1ll_opy_))
          driver.execute_script(bstack1ll11l111l_opy_)
          bstack11l1111ll_opy_(driver, bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ૲"))
      elif bstack1l1l1lll_opy_.status == bstack11l1_opy_ (u"ࠪࡊࡆࡏࡌࠨ૳"):
          reason = bstack11l1_opy_ (u"ࠦࠧ૴")
          bstack1l1lllllll_opy_ = bstack1lll11l11l_opy_ + bstack11l1_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭૵")
          if bstack1l1l1lll_opy_.message:
              reason = str(bstack1l1l1lll_opy_.message)
              bstack1l1lllllll_opy_ = bstack1l1lllllll_opy_ + bstack11l1_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭૶") + reason
          bstack1l111ll1ll_opy_[bstack11l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ૷")] = {
              bstack11l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ૸"): bstack11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨૹ"),
              bstack11l1_opy_ (u"ࠪࡨࡦࡺࡡࠨૺ"): bstack1l1lllllll_opy_
          }
          bstack1ll11l111l_opy_ = bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩૻ").format(json.dumps(bstack1l111ll1ll_opy_))
          driver.execute_script(bstack1ll11l111l_opy_)
          bstack11l1111ll_opy_(driver, bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬૼ"), reason)
          bstack1l111ll11_opy_(reason, str(bstack1l1l1lll_opy_), str(bstack1l11lll1l_opy_), logger)
@measure(event_name=EVENTS.bstack11111lll_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack111lll1ll_opy_(driver, test):
  if percy.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠨࡴࡳࡷࡨࠦ૽") and percy.bstack11ll11ll1l_opy_() == bstack11l1_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ૾"):
      bstack1111l11ll_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ૿"), None)
      bstack1lll1ll1l1_opy_(driver, bstack1111l11ll_opy_, test)
  if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭଀"), None) and bstack1l1lll1lll_opy_(
          threading.current_thread(), bstack11l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩଁ"), None):
      logger.info(bstack11l1_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦଂ"))
      bstack1lll11ll1_opy_.bstack1l1l1l111l_opy_(driver, name=test.name, path=test.source)
def bstack111ll11l1_opy_(test, bstack1lll11l11l_opy_):
    try:
      data = {}
      if test:
        data[bstack11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪଃ")] = bstack1lll11l11l_opy_
      if bstack1l1l1lll_opy_:
        if bstack1l1l1lll_opy_.status == bstack11l1_opy_ (u"࠭ࡐࡂࡕࡖࠫ଄"):
          data[bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧଅ")] = bstack11l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨଆ")
        elif bstack1l1l1lll_opy_.status == bstack11l1_opy_ (u"ࠩࡉࡅࡎࡒࠧଇ"):
          data[bstack11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪଈ")] = bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଉ")
          if bstack1l1l1lll_opy_.message:
            data[bstack11l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬଊ")] = str(bstack1l1l1lll_opy_.message)
      user = CONFIG[bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨଋ")]
      key = CONFIG[bstack11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪଌ")]
      url = bstack11l1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭଍").format(user, key, bstack1l1l1ll1l_opy_)
      headers = {
        bstack11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ଎"): bstack11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ଏ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1l1l11ll1_opy_.format(str(e)))
def bstack1l11l111l1_opy_(test, bstack1lll11l11l_opy_):
  global CONFIG
  global bstack111ll1l1l_opy_
  global bstack1ll1l1l1_opy_
  global bstack1l1l1ll1l_opy_
  global bstack1l1l1lll_opy_
  global bstack1l111l111_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack1l1l11111_opy_
  global bstack1l1l1l1l11_opy_
  global bstack1ll111ll11_opy_
  global bstack1ll111l111_opy_
  global bstack1l111ll1l1_opy_
  try:
    if not bstack1l1l1ll1l_opy_:
      with open(os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠫࢃ࠭ଐ")), bstack11l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ଑"), bstack11l1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ଒"))) as f:
        bstack1l111l11_opy_ = json.loads(bstack11l1_opy_ (u"ࠢࡼࠤଓ") + f.read().strip() + bstack11l1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪଔ") + bstack11l1_opy_ (u"ࠤࢀࠦକ"))
        bstack1l1l1ll1l_opy_ = bstack1l111l11_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1ll111l111_opy_:
    for driver in bstack1ll111l111_opy_:
      if bstack1l1l1ll1l_opy_ == driver.session_id:
        if test:
          bstack111lll1ll_opy_(driver, test)
        bstack1lll11l1l_opy_(driver, bstack1lll11l11l_opy_)
  elif bstack1l1l1ll1l_opy_:
    bstack111ll11l1_opy_(test, bstack1lll11l11l_opy_)
  if bstack111ll1l1l_opy_:
    bstack1l1l11111_opy_(bstack111ll1l1l_opy_)
  if bstack1ll1l1l1_opy_:
    bstack1l1l1l1l11_opy_(bstack1ll1l1l1_opy_)
  if bstack111l11ll_opy_:
    bstack1ll111ll11_opy_()
def bstack1llll1l111_opy_(self, test, *args, **kwargs):
  bstack1lll11l11l_opy_ = None
  if test:
    bstack1lll11l11l_opy_ = str(test.name)
  bstack1l11l111l1_opy_(test, bstack1lll11l11l_opy_)
  bstack1ll1ll1ll1_opy_(self, test, *args, **kwargs)
def bstack1l1111lll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack111l11l1_opy_
  global CONFIG
  global bstack1ll111l111_opy_
  global bstack1l1l1ll1l_opy_
  bstack111ll1111_opy_ = None
  try:
    if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩଖ"), None):
      try:
        if not bstack1l1l1ll1l_opy_:
          with open(os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠫࢃ࠭ଗ")), bstack11l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬଘ"), bstack11l1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨଙ"))) as f:
            bstack1l111l11_opy_ = json.loads(bstack11l1_opy_ (u"ࠢࡼࠤଚ") + f.read().strip() + bstack11l1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪଛ") + bstack11l1_opy_ (u"ࠤࢀࠦଜ"))
            bstack1l1l1ll1l_opy_ = bstack1l111l11_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1ll111l111_opy_:
        for driver in bstack1ll111l111_opy_:
          if bstack1l1l1ll1l_opy_ == driver.session_id:
            bstack111ll1111_opy_ = driver
    bstack1l1l11l11l_opy_ = bstack1lll11ll1_opy_.bstack1l111111ll_opy_(test.tags)
    if bstack111ll1111_opy_:
      threading.current_thread().isA11yTest = bstack1lll11ll1_opy_.bstack1l1l1l11_opy_(bstack111ll1111_opy_, bstack1l1l11l11l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1l1l11l11l_opy_
  except:
    pass
  bstack111l11l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l1l1lll_opy_
  bstack1l1l1lll_opy_ = self._test
def bstack11ll11ll11_opy_():
  global bstack1llll11ll_opy_
  try:
    if os.path.exists(bstack1llll11ll_opy_):
      os.remove(bstack1llll11ll_opy_)
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ଝ") + str(e))
def bstack1l11l1lll1_opy_():
  global bstack1llll11ll_opy_
  bstack1lll1l11l1_opy_ = {}
  try:
    if not os.path.isfile(bstack1llll11ll_opy_):
      with open(bstack1llll11ll_opy_, bstack11l1_opy_ (u"ࠫࡼ࠭ଞ")):
        pass
      with open(bstack1llll11ll_opy_, bstack11l1_opy_ (u"ࠧࡽࠫࠣଟ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1llll11ll_opy_):
      bstack1lll1l11l1_opy_ = json.load(open(bstack1llll11ll_opy_, bstack11l1_opy_ (u"࠭ࡲࡣࠩଠ")))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩଡ") + str(e))
  finally:
    return bstack1lll1l11l1_opy_
def bstack11l1l11l1_opy_(platform_index, item_index):
  global bstack1llll11ll_opy_
  try:
    bstack1lll1l11l1_opy_ = bstack1l11l1lll1_opy_()
    bstack1lll1l11l1_opy_[item_index] = platform_index
    with open(bstack1llll11ll_opy_, bstack11l1_opy_ (u"ࠣࡹ࠮ࠦଢ")) as outfile:
      json.dump(bstack1lll1l11l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧଣ") + str(e))
def bstack1l111lll1l_opy_(bstack11lll111l_opy_):
  global CONFIG
  bstack1lll11111l_opy_ = bstack11l1_opy_ (u"ࠪࠫତ")
  if not bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଥ") in CONFIG:
    logger.info(bstack11l1_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩଦ"))
  try:
    platform = CONFIG[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଧ")][bstack11lll111l_opy_]
    if bstack11l1_opy_ (u"ࠧࡰࡵࠪନ") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"ࠨࡱࡶࠫ଩")]) + bstack11l1_opy_ (u"ࠩ࠯ࠤࠬପ")
    if bstack11l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଫ") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧବ")]) + bstack11l1_opy_ (u"ࠬ࠲ࠠࠨଭ")
    if bstack11l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪମ") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫଯ")]) + bstack11l1_opy_ (u"ࠨ࠮ࠣࠫର")
    if bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ଱") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬଲ")]) + bstack11l1_opy_ (u"ࠫ࠱ࠦࠧଳ")
    if bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଴") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଵ")]) + bstack11l1_opy_ (u"ࠧ࠭ࠢࠪଶ")
    if bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଷ") in platform:
      bstack1lll11111l_opy_ += str(platform[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪସ")]) + bstack11l1_opy_ (u"ࠪ࠰ࠥ࠭ହ")
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫ଺") + str(e))
  finally:
    if bstack1lll11111l_opy_[len(bstack1lll11111l_opy_) - 2:] == bstack11l1_opy_ (u"ࠬ࠲ࠠࠨ଻"):
      bstack1lll11111l_opy_ = bstack1lll11111l_opy_[:-2]
    return bstack1lll11111l_opy_
def bstack1l1lllll1_opy_(path, bstack1lll11111l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll11l1111_opy_ = ET.parse(path)
    bstack1llll11ll1_opy_ = bstack1ll11l1111_opy_.getroot()
    bstack1ll1lll1_opy_ = None
    for suite in bstack1llll11ll1_opy_.iter(bstack11l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩ଼ࠬ")):
      if bstack11l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧଽ") in suite.attrib:
        suite.attrib[bstack11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ା")] += bstack11l1_opy_ (u"ࠩࠣࠫି") + bstack1lll11111l_opy_
        bstack1ll1lll1_opy_ = suite
    bstack11ll1ll111_opy_ = None
    for robot in bstack1llll11ll1_opy_.iter(bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩୀ")):
      bstack11ll1ll111_opy_ = robot
    bstack1ll1ll11l1_opy_ = len(bstack11ll1ll111_opy_.findall(bstack11l1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪୁ")))
    if bstack1ll1ll11l1_opy_ == 1:
      bstack11ll1ll111_opy_.remove(bstack11ll1ll111_opy_.findall(bstack11l1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫୂ"))[0])
      bstack1l111lllll_opy_ = ET.Element(bstack11l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬୃ"), attrib={bstack11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬୄ"): bstack11l1_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨ୅"), bstack11l1_opy_ (u"ࠩ࡬ࡨࠬ୆"): bstack11l1_opy_ (u"ࠪࡷ࠵࠭େ")})
      bstack11ll1ll111_opy_.insert(1, bstack1l111lllll_opy_)
      bstack1ll111l11l_opy_ = None
      for suite in bstack11ll1ll111_opy_.iter(bstack11l1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪୈ")):
        bstack1ll111l11l_opy_ = suite
      bstack1ll111l11l_opy_.append(bstack1ll1lll1_opy_)
      bstack1ll1l1l1l1_opy_ = None
      for status in bstack1ll1lll1_opy_.iter(bstack11l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ୉")):
        bstack1ll1l1l1l1_opy_ = status
      bstack1ll111l11l_opy_.append(bstack1ll1l1l1l1_opy_)
    bstack1ll11l1111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫ୊") + str(e))
def bstack1l11111l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1ll1l1ll_opy_
  global CONFIG
  if bstack11l1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦୋ") in options:
    del options[bstack11l1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧୌ")]
  bstack1ll1l11l1l_opy_ = bstack1l11l1lll1_opy_()
  for bstack11lll11l_opy_ in bstack1ll1l11l1l_opy_.keys():
    path = os.path.join(os.getcwd(), bstack11l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴ୍ࠩ"), str(bstack11lll11l_opy_), bstack11l1_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧ୎"))
    bstack1l1lllll1_opy_(path, bstack1l111lll1l_opy_(bstack1ll1l11l1l_opy_[bstack11lll11l_opy_]))
  bstack11ll11ll11_opy_()
  return bstack1l1ll1l1ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11ll11l1ll_opy_(self, ff_profile_dir):
  global bstack11llllll1l_opy_
  if not ff_profile_dir:
    return None
  return bstack11llllll1l_opy_(self, ff_profile_dir)
def bstack1l11l1l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll1lllll_opy_
  bstack1lll1ll11_opy_ = []
  if bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ୏") in CONFIG:
    bstack1lll1ll11_opy_ = CONFIG[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ୐")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢ୑")],
      pabot_args[bstack11l1_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣ୒")],
      argfile,
      pabot_args.get(bstack11l1_opy_ (u"ࠣࡪ࡬ࡺࡪࠨ୓")),
      pabot_args[bstack11l1_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧ୔")],
      platform[0],
      bstack1ll1lllll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥ୕")] or [(bstack11l1_opy_ (u"ࠦࠧୖ"), None)]
    for platform in enumerate(bstack1lll1ll11_opy_)
  ]
def bstack1ll11llll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll1ll1l1l_opy_=bstack11l1_opy_ (u"ࠬ࠭ୗ")):
  global bstack1l1l1l111_opy_
  self.platform_index = platform_index
  self.bstack1ll11l1l1_opy_ = bstack1ll1ll1l1l_opy_
  bstack1l1l1l111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll11l1ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll1111l1l_opy_
  global bstack1l1111llll_opy_
  bstack1l111ll1l_opy_ = copy.deepcopy(item)
  if not bstack11l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ୘") in item.options:
    bstack1l111ll1l_opy_.options[bstack11l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ୙")] = []
  bstack1111l1l1_opy_ = bstack1l111ll1l_opy_.options[bstack11l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ୚")].copy()
  for v in bstack1l111ll1l_opy_.options[bstack11l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ୛")]:
    if bstack11l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩଡ଼") in v:
      bstack1111l1l1_opy_.remove(v)
    if bstack11l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫଢ଼") in v:
      bstack1111l1l1_opy_.remove(v)
    if bstack11l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ୞") in v:
      bstack1111l1l1_opy_.remove(v)
  bstack1111l1l1_opy_.insert(0, bstack11l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨୟ").format(bstack1l111ll1l_opy_.platform_index))
  bstack1111l1l1_opy_.insert(0, bstack11l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧୠ").format(bstack1l111ll1l_opy_.bstack1ll11l1l1_opy_))
  bstack1l111ll1l_opy_.options[bstack11l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪୡ")] = bstack1111l1l1_opy_
  if bstack1l1111llll_opy_:
    bstack1l111ll1l_opy_.options[bstack11l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫୢ")].insert(0, bstack11l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭ୣ").format(bstack1l1111llll_opy_))
  return bstack1ll1111l1l_opy_(caller_id, datasources, is_last, bstack1l111ll1l_opy_, outs_dir)
def bstack11111l1l1_opy_(command, item_index):
  if bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ୤")):
    os.environ[bstack11l1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭୥")] = json.dumps(CONFIG[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ୦")][item_index % bstack1l1ll111l_opy_])
  global bstack1l1111llll_opy_
  if bstack1l1111llll_opy_:
    command[0] = command[0].replace(bstack11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭୧"), bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ୨") + str(
      item_index) + bstack11l1_opy_ (u"ࠩࠣࠫ୩") + bstack1l1111llll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ୪"),
                                    bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ୫") + str(item_index), 1)
def bstack1111111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1llll1111_opy_
  bstack11111l1l1_opy_(command, item_index)
  return bstack1llll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11lll11lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1llll1111_opy_
  bstack11111l1l1_opy_(command, item_index)
  return bstack1llll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack111llllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1llll1111_opy_
  bstack11111l1l1_opy_(command, item_index)
  return bstack1llll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11111l11l_opy_(self, runner, quiet=False, capture=True):
  global bstack1111l111_opy_
  bstack1l11111l_opy_ = bstack1111l111_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l1_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ୬")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l1_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ୭")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l11111l_opy_
def bstack1l1ll1l111_opy_(runner, hook_name, context, element, bstack1ll111l1ll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1ll1llll11_opy_.bstack1ll11ll11l_opy_(hook_name, element)
    bstack1ll111l1ll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1ll1llll11_opy_.bstack1lll11l1ll_opy_(element)
      if hook_name not in [bstack11l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫ୮"), bstack11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫ୯")] and args and hasattr(args[0], bstack11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩ୰")):
        args[0].error_message = bstack11l1_opy_ (u"ࠪࠫୱ")
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭୲").format(str(e)))
@measure(event_name=EVENTS.bstack1111l111l_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣ୳"), bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1lll1llll_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    if runner.hooks.get(bstack11l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ୴")).__name__ != bstack11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥ୵"):
      bstack1l1ll1l111_opy_(runner, name, context, runner, bstack1ll111l1ll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l111lll_opy_(bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ୶")) else context.browser
      runner.driver_initialised = bstack11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ୷")
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧ୸").format(str(e)))
def bstack11l1l1l1_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    bstack1l1ll1l111_opy_(runner, name, context, context.feature, bstack1ll111l1ll_opy_, *args)
    try:
      if not bstack1l1ll11111_opy_:
        bstack111ll1111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll_opy_(bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ୹")) else context.browser
        if is_driver_active(bstack111ll1111_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨ୺")
          bstack11ll1111_opy_ = str(runner.feature.name)
          bstack1ll11lll11_opy_(context, bstack11ll1111_opy_)
          bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ୻") + json.dumps(bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠧࡾࡿࠪ୼"))
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ୽").format(str(e)))
def bstack1lllll1ll_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    if hasattr(context, bstack11l1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ୾")):
        bstack1ll1llll11_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l1_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ୿")) else context.feature
    bstack1l1ll1l111_opy_(runner, name, context, target, bstack1ll111l1ll_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l11l11_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l11llll_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1ll1llll11_opy_.start_test(context)
    bstack1l1ll1l111_opy_(runner, name, context, context.scenario, bstack1ll111l1ll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1ll11ll1l_opy_.bstack1l1l1lll11_opy_(context, *args)
    try:
      bstack111ll1111_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ஀"), context.browser)
      if is_driver_active(bstack111ll1111_opy_):
        bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ஁"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣஂ")
        if (not bstack1l1ll11111_opy_):
          scenario_name = args[0].name
          feature_name = bstack11ll1111_opy_ = str(runner.feature.name)
          bstack11ll1111_opy_ = feature_name + bstack11l1_opy_ (u"ࠧࠡ࠯ࠣࠫஃ") + scenario_name
          if runner.driver_initialised == bstack11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥ஄"):
            bstack1ll11lll11_opy_(context, bstack11ll1111_opy_)
            bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧஅ") + json.dumps(bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠪࢁࢂ࠭ஆ"))
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬஇ").format(str(e)))
@measure(event_name=EVENTS.bstack1111l111l_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤஈ"), bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l1l11llll_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    bstack1l1ll1l111_opy_(runner, name, context, args[0], bstack1ll111l1ll_opy_, *args)
    try:
      bstack111ll1111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll_opy_(bstack11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬஉ")) else context.browser
      if is_driver_active(bstack111ll1111_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧஊ")
        bstack1ll1llll11_opy_.bstack1ll111ll1_opy_(args[0])
        if runner.driver_initialised == bstack11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ஋"):
          feature_name = bstack11ll1111_opy_ = str(runner.feature.name)
          bstack11ll1111_opy_ = feature_name + bstack11l1_opy_ (u"ࠩࠣ࠱ࠥ࠭஌") + context.scenario.name
          bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ஍") + json.dumps(bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠫࢂࢃࠧஎ"))
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩஏ").format(str(e)))
@measure(event_name=EVENTS.bstack1111l111l_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤஐ"), bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11l111l11_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
  bstack1ll1llll11_opy_.bstack1l11l1l1ll_opy_(args[0])
  try:
    bstack11ll1l1l1_opy_ = args[0].status.name
    bstack111ll1111_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭஑") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111ll1111_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l1_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨஒ")
        feature_name = bstack11ll1111_opy_ = str(runner.feature.name)
        bstack11ll1111_opy_ = feature_name + bstack11l1_opy_ (u"ࠩࠣ࠱ࠥ࠭ஓ") + context.scenario.name
        bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨஔ") + json.dumps(bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠫࢂࢃࠧக"))
    if str(bstack11ll1l1l1_opy_).lower() == bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ஖"):
      bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"࠭ࠧ஗")
      bstack1ll11l1lll_opy_ = bstack11l1_opy_ (u"ࠧࠨ஘")
      bstack1ll11ll1ll_opy_ = bstack11l1_opy_ (u"ࠨࠩங")
      try:
        import traceback
        bstack1l1ll1l11_opy_ = runner.exception.__class__.__name__
        bstack1l1l1l1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11l1lll_opy_ = bstack11l1_opy_ (u"ࠩࠣࠫச").join(bstack1l1l1l1l_opy_)
        bstack1ll11ll1ll_opy_ = bstack1l1l1l1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
      bstack1l1ll1l11_opy_ += bstack1ll11ll1ll_opy_
      bstack1llllll11_opy_(context, json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ஛") + str(bstack1ll11l1lll_opy_)),
                          bstack11l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥஜ"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ஝"):
        bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"࠭ࡰࡢࡩࡨࠫஞ"), None), bstack11l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢட"), bstack1l1ll1l11_opy_)
        bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭஠") + json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ஡") + str(bstack1ll11l1lll_opy_)) + bstack11l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ஢"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤண"):
        bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬத"), bstack11l1_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ஥") + str(bstack1l1ll1l11_opy_))
    else:
      bstack1llllll11_opy_(context, bstack11l1_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣ஦"), bstack11l1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ஧"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢந"):
        bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨன"), None), bstack11l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦப"))
      bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ஫") + json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥ஬")) + bstack11l1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭஭"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨம"):
        bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤய"))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩர").format(str(e)))
  bstack1l1ll1l111_opy_(runner, name, context, args[0], bstack1ll111l1ll_opy_, *args)
@measure(event_name=EVENTS.bstack1ll11111l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1llllll1l_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
  bstack1ll1llll11_opy_.end_test(args[0])
  try:
    bstack111l1l1l1_opy_ = args[0].status.name
    bstack111ll1111_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪற"), context.browser)
    bstack1ll11ll1l_opy_.bstack1l111llll_opy_(bstack111ll1111_opy_)
    if str(bstack111l1l1l1_opy_).lower() == bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬல"):
      bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"࠭ࠧள")
      bstack1ll11l1lll_opy_ = bstack11l1_opy_ (u"ࠧࠨழ")
      bstack1ll11ll1ll_opy_ = bstack11l1_opy_ (u"ࠨࠩவ")
      try:
        import traceback
        bstack1l1ll1l11_opy_ = runner.exception.__class__.__name__
        bstack1l1l1l1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11l1lll_opy_ = bstack11l1_opy_ (u"ࠩࠣࠫஶ").join(bstack1l1l1l1l_opy_)
        bstack1ll11ll1ll_opy_ = bstack1l1l1l1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
      bstack1l1ll1l11_opy_ += bstack1ll11ll1ll_opy_
      bstack1llllll11_opy_(context, json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤஷ") + str(bstack1ll11l1lll_opy_)),
                          bstack11l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥஸ"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢஹ") or runner.driver_initialised == bstack11l1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭஺"):
        bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"ࠧࡱࡣࡪࡩࠬ஻"), None), bstack11l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ஼"), bstack1l1ll1l11_opy_)
        bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ஽") + json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤா") + str(bstack1ll11l1lll_opy_)) + bstack11l1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫி"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢீ") or runner.driver_initialised == bstack11l1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ு"):
        bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧூ"), bstack11l1_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ௃") + str(bstack1l1ll1l11_opy_))
    else:
      bstack1llllll11_opy_(context, bstack11l1_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥ௄"), bstack11l1_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ௅"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨெ") or runner.driver_initialised == bstack11l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬே"):
        bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"࠭ࡰࡢࡩࡨࠫை"), None), bstack11l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ௉"))
      bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ொ") + json.dumps(str(args[0].name) + bstack11l1_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨோ")) + bstack11l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩௌ"))
      if runner.driver_initialised == bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ்") or runner.driver_initialised == bstack11l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ௎"):
        bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ௏"))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩௐ").format(str(e)))
  bstack1l1ll1l111_opy_(runner, name, context, context.scenario, bstack1ll111l1ll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1llll111l_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪ௑")) else context.feature
    bstack1l1ll1l111_opy_(runner, name, context, target, bstack1ll111l1ll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1ll1ll11_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    try:
      bstack111ll1111_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ௒"), context.browser)
      bstack1l11lllll1_opy_ = bstack11l1_opy_ (u"ࠪࠫ௓")
      if context.failed is True:
        bstack1l111111_opy_ = []
        bstack1l111ll111_opy_ = []
        bstack1l1llll11l_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l111111_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack1l1l1l1l_opy_ = traceback.format_tb(exc_tb)
            bstack1lll1lllll_opy_ = bstack11l1_opy_ (u"ࠫࠥ࠭௔").join(bstack1l1l1l1l_opy_)
            bstack1l111ll111_opy_.append(bstack1lll1lllll_opy_)
            bstack1l1llll11l_opy_.append(bstack1l1l1l1l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
        bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"ࠬ࠭௕")
        for i in range(len(bstack1l111111_opy_)):
          bstack1l1ll1l11_opy_ += bstack1l111111_opy_[i] + bstack1l1llll11l_opy_[i] + bstack11l1_opy_ (u"࠭࡜࡯ࠩ௖")
        bstack1l11lllll1_opy_ = bstack11l1_opy_ (u"ࠧࠡࠩௗ").join(bstack1l111ll111_opy_)
        if runner.driver_initialised in [bstack11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ௘"), bstack11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ௙")]:
          bstack1llllll11_opy_(context, bstack1l11lllll1_opy_, bstack11l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ௚"))
          bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"ࠫࡵࡧࡧࡦࠩ௛"), None), bstack11l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ௜"), bstack1l1ll1l11_opy_)
          bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ௝") + json.dumps(bstack1l11lllll1_opy_) + bstack11l1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ௞"))
          bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ௟"), bstack11l1_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢ௠") + str(bstack1l1ll1l11_opy_))
          bstack11l1lll1_opy_ = bstack11l1ll1ll_opy_(bstack1l11lllll1_opy_, runner.feature.name, logger)
          if (bstack11l1lll1_opy_ != None):
            bstack1l11ll1l11_opy_.append(bstack11l1lll1_opy_)
      else:
        if runner.driver_initialised in [bstack11l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ௡"), bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ௢")]:
          bstack1llllll11_opy_(context, bstack11l1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ௣") + str(runner.feature.name) + bstack11l1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ௤"), bstack11l1_opy_ (u"ࠢࡪࡰࡩࡳࠧ௥"))
          bstack1lll1l11ll_opy_(getattr(context, bstack11l1_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭௦"), None), bstack11l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ௧"))
          bstack111ll1111_opy_.execute_script(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ௨") + json.dumps(bstack11l1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢ௩") + str(runner.feature.name) + bstack11l1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ௪")) + bstack11l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ௫"))
          bstack11l1111ll_opy_(bstack111ll1111_opy_, bstack11l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ௬"))
          bstack11l1lll1_opy_ = bstack11l1ll1ll_opy_(bstack1l11lllll1_opy_, runner.feature.name, logger)
          if (bstack11l1lll1_opy_ != None):
            bstack1l11ll1l11_opy_.append(bstack11l1lll1_opy_)
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ௭").format(str(e)))
    bstack1l1ll1l111_opy_(runner, name, context, context.feature, bstack1ll111l1ll_opy_, *args)
@measure(event_name=EVENTS.bstack1111l111l_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦ௮"), bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l1l111l_opy_(runner, name, context, bstack1ll111l1ll_opy_, *args):
    bstack1l1ll1l111_opy_(runner, name, context, runner, bstack1ll111l1ll_opy_, *args)
def bstack1lll1ll1ll_opy_(self, name, context, *args):
  if bstack1l1l1lll1l_opy_:
    platform_index = int(threading.current_thread()._name) % bstack1l1ll111l_opy_
    bstack1l11lll1_opy_ = CONFIG[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭௯")][platform_index]
    os.environ[bstack11l1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ௰")] = json.dumps(bstack1l11lll1_opy_)
  global bstack1ll111l1ll_opy_
  if not hasattr(self, bstack11l1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪ௱")):
    self.driver_initialised = None
  bstack11lll1l1l_opy_ = {
      bstack11l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪ௲"): bstack1lll1llll_opy_,
      bstack11l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ௳"): bstack11l1l1l1_opy_,
      bstack11l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬ௴"): bstack1lllll1ll_opy_,
      bstack11l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ௵"): bstack1l11llll_opy_,
      bstack11l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨ௶"): bstack1l1l11llll_opy_,
      bstack11l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨ௷"): bstack11l111l11_opy_,
      bstack11l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭௸"): bstack1llllll1l_opy_,
      bstack11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩ௹"): bstack1llll111l_opy_,
      bstack11l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ௺"): bstack1l1ll1ll11_opy_,
      bstack11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫ௻"): bstack1l1l111l_opy_
  }
  handler = bstack11lll1l1l_opy_.get(name, bstack1ll111l1ll_opy_)
  handler(self, name, context, bstack1ll111l1ll_opy_, *args)
  if name in [bstack11l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩ௼"), bstack11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ௽"), bstack11l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ௾")]:
    try:
      bstack111ll1111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll_opy_(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ௿")) else context.browser
      bstack1l1llll1l_opy_ = (
        (name == bstack11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩఀ") and self.driver_initialised == bstack11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦఁ")) or
        (name == bstack11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨం") and self.driver_initialised == bstack11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥః")) or
        (name == bstack11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫఄ") and self.driver_initialised in [bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨఅ"), bstack11l1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧఆ")]) or
        (name == bstack11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪఇ") and self.driver_initialised == bstack11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧఈ"))
      )
      if bstack1l1llll1l_opy_:
        self.driver_initialised = None
        bstack111ll1111_opy_.quit()
    except Exception:
      pass
def bstack1l11llll1_opy_(config, startdir):
  return bstack11l1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨఉ").format(bstack11l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣఊ"))
notset = Notset()
def bstack1111llll1_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11ll111l_opy_
  if str(name).lower() == bstack11l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪఋ"):
    return bstack11l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥఌ")
  else:
    return bstack11ll111l_opy_(self, name, default, skip)
def bstack11lll1111_opy_(item, when):
  global bstack1ll1111l11_opy_
  try:
    bstack1ll1111l11_opy_(item, when)
  except Exception as e:
    pass
def bstack11111ll1_opy_():
  return
def bstack1llll1l1l1_opy_(type, name, status, reason, bstack11ll1ll1ll_opy_, bstack1llll111_opy_):
  bstack11l1l11ll_opy_ = {
    bstack11l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ఍"): type,
    bstack11l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩఎ"): {}
  }
  if type == bstack11l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩఏ"):
    bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫఐ")][bstack11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ఑")] = bstack11ll1ll1ll_opy_
    bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ఒ")][bstack11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩఓ")] = json.dumps(str(bstack1llll111_opy_))
  if type == bstack11l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ఔ"):
    bstack11l1l11ll_opy_[bstack11l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩక")][bstack11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬఖ")] = name
  if type == bstack11l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫగ"):
    bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬఘ")][bstack11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪఙ")] = status
    if status == bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫచ"):
      bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨఛ")][bstack11l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭జ")] = json.dumps(str(reason))
  bstack1l1111ll_opy_ = bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬఝ").format(json.dumps(bstack11l1l11ll_opy_))
  return bstack1l1111ll_opy_
def bstack11l111111_opy_(driver_command, response):
    if driver_command == bstack11l1_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬఞ"):
        bstack1ll1llllll_opy_.bstack1l1ll1111_opy_({
            bstack11l1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨట"): response[bstack11l1_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩఠ")],
            bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫడ"): bstack1ll1llllll_opy_.current_test_uuid()
        })
def bstack11ll11lll_opy_(item, call, rep):
  global bstack1lllll11_opy_
  global bstack1ll111l111_opy_
  global bstack1l1ll11111_opy_
  name = bstack11l1_opy_ (u"ࠬ࠭ఢ")
  try:
    if rep.when == bstack11l1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫణ"):
      bstack1l1l1ll1l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l1ll11111_opy_:
          name = str(rep.nodeid)
          bstack1l1ll11lll_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨత"), name, bstack11l1_opy_ (u"ࠨࠩథ"), bstack11l1_opy_ (u"ࠩࠪద"), bstack11l1_opy_ (u"ࠪࠫధ"), bstack11l1_opy_ (u"ࠫࠬన"))
          threading.current_thread().bstack1l11l1111_opy_ = name
          for driver in bstack1ll111l111_opy_:
            if bstack1l1l1ll1l_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll11lll_opy_)
      except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ఩").format(str(e)))
      try:
        bstack1ll1l11l11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧప"):
          status = bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧఫ") if rep.outcome.lower() == bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨబ") else bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩభ")
          reason = bstack11l1_opy_ (u"ࠪࠫమ")
          if status == bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫయ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪర") if status == bstack11l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ఱ") else bstack11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ల")
          data = name + bstack11l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪళ") if status == bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩఴ") else name + bstack11l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭వ") + reason
          bstack1l11lll11_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭శ"), bstack11l1_opy_ (u"ࠬ࠭ష"), bstack11l1_opy_ (u"࠭ࠧస"), bstack11l1_opy_ (u"ࠧࠨహ"), level, data)
          for driver in bstack1ll111l111_opy_:
            if bstack1l1l1ll1l_opy_ == driver.session_id:
              driver.execute_script(bstack1l11lll11_opy_)
      except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ఺").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭఻").format(str(e)))
  bstack1lllll11_opy_(item, call, rep)
def bstack1lll1ll1l1_opy_(driver, bstack1l1l1111_opy_, test=None):
  global bstack1l11lll1l_opy_
  if test != None:
    bstack1llll11111_opy_ = getattr(test, bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ఼"), None)
    bstack111111l1_opy_ = getattr(test, bstack11l1_opy_ (u"ࠫࡺࡻࡩࡥࠩఽ"), None)
    PercySDK.screenshot(driver, bstack1l1l1111_opy_, bstack1llll11111_opy_=bstack1llll11111_opy_, bstack111111l1_opy_=bstack111111l1_opy_, bstack111lll11l_opy_=bstack1l11lll1l_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1l1111_opy_)
@measure(event_name=EVENTS.bstack1l111111l1_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11ll1l111l_opy_(driver):
  if bstack1l1l111l11_opy_.bstack1lllll1ll1_opy_() is True or bstack1l1l111l11_opy_.capturing() is True:
    return
  bstack1l1l111l11_opy_.bstack11llllll1_opy_()
  while not bstack1l1l111l11_opy_.bstack1lllll1ll1_opy_():
    bstack11l1lll11_opy_ = bstack1l1l111l11_opy_.bstack1l1l111ll1_opy_()
    bstack1lll1ll1l1_opy_(driver, bstack11l1lll11_opy_)
  bstack1l1l111l11_opy_.bstack1l1ll111l1_opy_()
def bstack11lll1ll1l_opy_(sequence, driver_command, response = None, bstack11l11ll1_opy_ = None, args = None):
    try:
      if sequence != bstack11l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬా"):
        return
      if percy.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧి"):
        return
      bstack11l1lll11_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪీ"), None)
      for command in bstack1lll1l1l1l_opy_:
        if command == driver_command:
          for driver in bstack1ll111l111_opy_:
            bstack11ll1l111l_opy_(driver)
      bstack1l1llllll1_opy_ = percy.bstack11ll11ll1l_opy_()
      if driver_command in bstack111ll111_opy_[bstack1l1llllll1_opy_]:
        bstack1l1l111l11_opy_.bstack1l1ll1ll1_opy_(bstack11l1lll11_opy_, driver_command)
    except Exception as e:
      pass
@measure(event_name=EVENTS.bstack1ll1111l1_opy_, stage=STAGE.bstack1111l1l1l_opy_)
def bstack1ll1ll1l_opy_(framework_name):
  if bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬు")):
      return
  bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭ూ"), True)
  global bstack1llll11l1l_opy_
  global bstack11l11ll11_opy_
  global bstack1ll11ll1_opy_
  bstack1llll11l1l_opy_ = framework_name
  logger.info(bstack1l11l1ll1_opy_.format(bstack1llll11l1l_opy_.split(bstack11l1_opy_ (u"ࠪ࠱ࠬృ"))[0]))
  bstack11lll111ll_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l1l1lll1l_opy_:
      Service.start = bstack1l1lllll_opy_
      Service.stop = bstack1ll11llll_opy_
      webdriver.Remote.get = bstack111l11lll_opy_
      WebDriver.close = bstack1l11lll1l1_opy_
      WebDriver.quit = bstack11l111ll1_opy_
      webdriver.Remote.__init__ = bstack1l11111ll_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1l1l1lll1l_opy_:
        webdriver.Remote.__init__ = bstack1l11l1l1l1_opy_
    WebDriver.execute = bstack1l1ll11l1_opy_
    bstack11l11ll11_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l1l1lll1l_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1l1111l_opy_
  except Exception as e:
    pass
  bstack1111l11l_opy_()
  if not bstack11l11ll11_opy_:
    bstack111l1111_opy_(bstack11l1_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨౄ"), bstack1l111l1l1_opy_)
  if bstack11llll111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._1ll1111ll1_opy_ = bstack11l11l111_opy_
    except Exception as e:
      logger.error(bstack11ll11llll_opy_.format(str(e)))
  if bstack11llll1111_opy_():
    bstack111l111l1_opy_(CONFIG, logger)
  if (bstack11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ౅") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠨࡴࡳࡷࡨࠦె"):
          bstack11l1ll1l_opy_(bstack11lll1ll1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11ll11l1ll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll11l11l_opy_
      except Exception as e:
        logger.warn(bstack1l11lll111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll1ll11_opy_
      except Exception as e:
        logger.debug(bstack1ll111111_opy_ + str(e))
    except Exception as e:
      bstack111l1111_opy_(e, bstack1l11lll111_opy_)
    Output.start_test = bstack1llll1l11l_opy_
    Output.end_test = bstack1llll1l111_opy_
    TestStatus.__init__ = bstack1l1111lll_opy_
    QueueItem.__init__ = bstack1ll11llll1_opy_
    pabot._create_items = bstack1l11l1l11_opy_
    try:
      from pabot import __version__ as bstack11ll1lll_opy_
      if version.parse(bstack11ll1lll_opy_) >= version.parse(bstack11l1_opy_ (u"ࠧ࠳࠰࠴࠹࠳࠶ࠧే")):
        pabot._run = bstack111llllll_opy_
      elif version.parse(bstack11ll1lll_opy_) >= version.parse(bstack11l1_opy_ (u"ࠨ࠴࠱࠵࠸࠴࠰ࠨై")):
        pabot._run = bstack11lll11lll_opy_
      else:
        pabot._run = bstack1111111l_opy_
    except Exception as e:
      pabot._run = bstack1111111l_opy_
    pabot._create_command_for_execution = bstack1ll11l1ll_opy_
    pabot._report_results = bstack1l11111l11_opy_
  if bstack11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ౉") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l1111_opy_(e, bstack111lll111_opy_)
    Runner.run_hook = bstack1lll1ll1ll_opy_
    Step.run = bstack11111l11l_opy_
  if bstack11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪొ") in str(framework_name).lower():
    if not bstack1l1l1lll1l_opy_:
      return
    try:
      if percy.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤో"):
          bstack11l1ll1l_opy_(bstack11lll1ll1l_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l11llll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11111ll1_opy_
      Config.getoption = bstack1111llll1_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11ll11lll_opy_
    except Exception as e:
      pass
def bstack1l111111l_opy_():
  global CONFIG
  if bstack11l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬౌ") in CONFIG and int(CONFIG[bstack11l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ్࠭")]) > 1:
    logger.warn(bstack1l1lll1ll_opy_)
def bstack1l1lll1l1_opy_(arg, bstack1lllll11ll_opy_, bstack11llll11l1_opy_=None):
  global CONFIG
  global bstack1l11l1l1l_opy_
  global bstack11llll1l1l_opy_
  global bstack1l1l1lll1l_opy_
  global bstack1l1l1lll1_opy_
  bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౎")
  if bstack1lllll11ll_opy_ and isinstance(bstack1lllll11ll_opy_, str):
    bstack1lllll11ll_opy_ = eval(bstack1lllll11ll_opy_)
  CONFIG = bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ౏")]
  bstack1l11l1l1l_opy_ = bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ౐")]
  bstack11llll1l1l_opy_ = bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ౑")]
  bstack1l1l1lll1l_opy_ = bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ౒")]
  bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭౓"), bstack1l1l1lll1l_opy_)
  os.environ[bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ౔")] = bstack11l1111l1_opy_
  os.environ[bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌౕ࠭")] = json.dumps(CONFIG)
  os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨౖ")] = bstack1l11l1l1l_opy_
  os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ౗")] = str(bstack11llll1l1l_opy_)
  os.environ[bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩౘ")] = str(True)
  if bstack1lll1ll1l_opy_(arg, [bstack11l1_opy_ (u"ࠫ࠲ࡴࠧౙ"), bstack11l1_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ౚ")]) != -1:
    os.environ[bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ౛")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll11lllll_opy_)
    return
  bstack1lllll111l_opy_()
  global bstack1lllll11l_opy_
  global bstack1l11lll1l_opy_
  global bstack1ll1lllll_opy_
  global bstack1l1111llll_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1ll11ll1_opy_
  global bstack1l1ll11l11_opy_
  arg.append(bstack11l1_opy_ (u"ࠢ࠮࡙ࠥ౜"))
  arg.append(bstack11l1_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡏࡲࡨࡺࡲࡥࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡱࡵࡵࡲࡵࡧࡧ࠾ࡵࡿࡴࡦࡵࡷ࠲ࡕࡿࡴࡦࡵࡷ࡛ࡦࡸ࡮ࡪࡰࡪࠦౝ"))
  arg.append(bstack11l1_opy_ (u"ࠤ࠰࡛ࠧ౞"))
  arg.append(bstack11l1_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡘ࡭࡫ࠠࡩࡱࡲ࡯࡮ࡳࡰ࡭ࠤ౟"))
  global bstack1lll1111l_opy_
  global bstack1ll1l111l1_opy_
  global bstack1l111lll11_opy_
  global bstack111l11l1_opy_
  global bstack11llllll1l_opy_
  global bstack1l1l1l111_opy_
  global bstack1ll1111l1l_opy_
  global bstack1ll1l1lll1_opy_
  global bstack11llll1ll1_opy_
  global bstack111ll1lll_opy_
  global bstack11ll111l_opy_
  global bstack1ll1111l11_opy_
  global bstack1lllll11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lll1111l_opy_ = webdriver.Remote.__init__
    bstack1ll1l111l1_opy_ = WebDriver.quit
    bstack1ll1l1lll1_opy_ = WebDriver.close
    bstack11llll1ll1_opy_ = WebDriver.get
    bstack1l111lll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11ll1lll1l_opy_(CONFIG) and bstack1llll1lll1_opy_():
    if bstack1l1lll11ll_opy_() < version.parse(bstack1l1ll11ll_opy_):
      logger.error(bstack1l1l11lll_opy_.format(bstack1l1lll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack111ll1lll_opy_ = RemoteConnection._1ll1111ll1_opy_
      except Exception as e:
        logger.error(bstack11ll11llll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11ll111l_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll1111l11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1ll11111ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1lllll11_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬౠ"))
  bstack1ll1lllll_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩౡ"), {}).get(bstack11l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨౢ"))
  bstack1l1ll11l11_opy_ = True
  bstack1ll1ll1l_opy_(bstack1l1l1l11l1_opy_)
  os.environ[bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨౣ")] = CONFIG[bstack11l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ౤")]
  os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ౥")] = CONFIG[bstack11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭౦")]
  os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ౧")] = bstack1l1l1lll1l_opy_.__str__()
  from _pytest.config import main as bstack11ll1lllll_opy_
  bstack111111ll_opy_ = []
  try:
    bstack11l11111_opy_ = bstack11ll1lllll_opy_(arg)
    if bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩ౨") in multiprocessing.current_process().__dict__.keys():
      for bstack1lll11ll11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111111ll_opy_.append(bstack1lll11ll11_opy_)
    try:
      bstack1ll1ll1111_opy_ = (bstack111111ll_opy_, int(bstack11l11111_opy_))
      bstack11llll11l1_opy_.append(bstack1ll1ll1111_opy_)
    except:
      bstack11llll11l1_opy_.append((bstack111111ll_opy_, bstack11l11111_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack111111ll_opy_.append({bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ౩"): bstack11l1_opy_ (u"ࠧࡑࡴࡲࡧࡪࡹࡳࠡࠩ౪") + os.environ.get(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ౫")), bstack11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ౬"): traceback.format_exc(), bstack11l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ౭"): int(os.environ.get(bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ౮")))})
    bstack11llll11l1_opy_.append((bstack111111ll_opy_, 1))
def bstack111l1111l_opy_(arg):
  global bstack1ll1ll1l1_opy_
  bstack1ll1ll1l_opy_(bstack1l1l11l1ll_opy_)
  os.environ[bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭౯")] = str(bstack11llll1l1l_opy_)
  from behave.__main__ import main as bstack1l11l11ll1_opy_
  status_code = bstack1l11l11ll1_opy_(arg)
  if status_code != 0:
    bstack1ll1ll1l1_opy_ = status_code
def bstack1l1111lll1_opy_():
  logger.info(bstack1ll1ll111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ౰"), help=bstack11l1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨ౱"))
  parser.add_argument(bstack11l1_opy_ (u"ࠨ࠯ࡸࠫ౲"), bstack11l1_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭౳"), help=bstack11l1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ౴"))
  parser.add_argument(bstack11l1_opy_ (u"ࠫ࠲ࡱࠧ౵"), bstack11l1_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫ౶"), help=bstack11l1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧ౷"))
  parser.add_argument(bstack11l1_opy_ (u"ࠧ࠮ࡨࠪ౸"), bstack11l1_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭౹"), help=bstack11l1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ౺"))
  bstack1ll111lll_opy_ = parser.parse_args()
  try:
    bstack1111l11l1_opy_ = bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧ౻")
    if bstack1ll111lll_opy_.framework and bstack1ll111lll_opy_.framework not in (bstack11l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ౼"), bstack11l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭౽")):
      bstack1111l11l1_opy_ = bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬ౾")
    bstack1llll1llll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1111l11l1_opy_)
    bstack11111l1ll_opy_ = open(bstack1llll1llll_opy_, bstack11l1_opy_ (u"ࠧࡳࠩ౿"))
    bstack1111111ll_opy_ = bstack11111l1ll_opy_.read()
    bstack11111l1ll_opy_.close()
    if bstack1ll111lll_opy_.username:
      bstack1111111ll_opy_ = bstack1111111ll_opy_.replace(bstack11l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨಀ"), bstack1ll111lll_opy_.username)
    if bstack1ll111lll_opy_.key:
      bstack1111111ll_opy_ = bstack1111111ll_opy_.replace(bstack11l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫಁ"), bstack1ll111lll_opy_.key)
    if bstack1ll111lll_opy_.framework:
      bstack1111111ll_opy_ = bstack1111111ll_opy_.replace(bstack11l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫಂ"), bstack1ll111lll_opy_.framework)
    file_name = bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧಃ")
    file_path = os.path.abspath(file_name)
    bstack11111l111_opy_ = open(file_path, bstack11l1_opy_ (u"ࠬࡽࠧ಄"))
    bstack11111l111_opy_.write(bstack1111111ll_opy_)
    bstack11111l111_opy_.close()
    logger.info(bstack1l1l111l1l_opy_)
    try:
      os.environ[bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨಅ")] = bstack1ll111lll_opy_.framework if bstack1ll111lll_opy_.framework != None else bstack11l1_opy_ (u"ࠢࠣಆ")
      config = yaml.safe_load(bstack1111111ll_opy_)
      config[bstack11l1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨಇ")] = bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨಈ")
      bstack1ll11l111_opy_(bstack1l11l1l111_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1l111ll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack111ll1l11_opy_.format(str(e)))
def bstack1ll11l111_opy_(bstack1l111l1ll1_opy_, config, bstack1ll1llll1l_opy_={}):
  global bstack1l1l1lll1l_opy_
  global bstack1l1l111111_opy_
  global bstack1l1l1lll1_opy_
  if not config:
    return
  bstack1ll1111111_opy_ = bstack1l11l1l11l_opy_ if not bstack1l1l1lll1l_opy_ else (
    bstack1l11111l1l_opy_ if bstack11l1_opy_ (u"ࠪࡥࡵࡶࠧಉ") in config else (
        bstack1l1111l111_opy_ if config.get(bstack11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨಊ")) else bstack1ll11lll1_opy_
    )
)
  bstack1111lll1l_opy_ = False
  bstack1l1l1llll1_opy_ = False
  if bstack1l1l1lll1l_opy_ is True:
      if bstack11l1_opy_ (u"ࠬࡧࡰࡱࠩಋ") in config:
          bstack1111lll1l_opy_ = True
      else:
          bstack1l1l1llll1_opy_ = True
  bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1l11111111_opy_(config, bstack1l1l111111_opy_)
  data = {
    bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨಌ"): config[bstack11l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ಍")],
    bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫಎ"): config[bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬಏ")],
    bstack11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧಐ"): bstack1l111l1ll1_opy_,
    bstack11l1_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ಑"): os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧಒ"), bstack1l1l111111_opy_),
    bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨಓ"): bstack1l111llll1_opy_,
    bstack11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭ࠩಔ"): bstack1llll11l_opy_(),
    bstack11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫಕ"): {
      bstack11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧಖ"): str(config[bstack11l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪಗ")]) if bstack11l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫಘ") in config else bstack11l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨಙ"),
      bstack11l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨಚ"): sys.version,
      bstack11l1_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩಛ"): bstack1lll1l1l1_opy_(os.getenv(bstack11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥಜ"), bstack11l1_opy_ (u"ࠤࠥಝ"))),
      bstack11l1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬಞ"): bstack11l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫಟ"),
      bstack11l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ಠ"): bstack1ll1111111_opy_,
      bstack11l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫಡ"): bstack1ll11lll_opy_,
      bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭ಢ"): os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ಣ")],
      bstack11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬತ"): bstack1l11ll111l_opy_(os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬಥ"), bstack1l1l111111_opy_)),
      bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧದ"): config[bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨಧ")] if config[bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩನ")] else bstack11l1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ಩"),
      bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪಪ"): str(config[bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫಫ")]) if bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬಬ") in config else bstack11l1_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧಭ"),
      bstack11l1_opy_ (u"ࠬࡵࡳࠨಮ"): sys.platform,
      bstack11l1_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨಯ"): socket.gethostname(),
      bstack11l1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩರ"): bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪಱ"))
    }
  }
  if not bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩಲ")) is None:
    data[bstack11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ಳ")][bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡓࡥࡵࡣࡧࡥࡹࡧࠧ಴")] = {
      bstack11l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬವ"): bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫಶ"),
      bstack11l1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧಷ"): bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨಸ")),
      bstack11l1_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࡐࡸࡱࡧ࡫ࡲࠨಹ"): bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭಺"))
    }
  if bstack1l111l1ll1_opy_ == bstack1l1ll11ll1_opy_:
    data[bstack11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ಻")][bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩ಼ࠪ")] = bstack1l1ll1llll_opy_(config)
    data[bstack11l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩಽ")][bstack11l1_opy_ (u"ࠧࡪࡵࡓࡩࡷࡩࡹࡂࡷࡷࡳࡊࡴࡡࡣ࡮ࡨࡨࠬಾ")] = percy.bstack11lllll1_opy_
    data[bstack11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫಿ")][bstack11l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡃࡷ࡬ࡰࡩࡏࡤࠨೀ")] = percy.bstack1l111l1l1l_opy_
  update(data[bstack11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ು")], bstack1ll1llll1l_opy_)
  try:
    response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠫࡕࡕࡓࡕࠩೂ"), bstack1l11l111ll_opy_(bstack1l11l11lll_opy_), data, {
      bstack11l1_opy_ (u"ࠬࡧࡵࡵࡪࠪೃ"): (config[bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨೄ")], config[bstack11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ೅")])
    })
    if response:
      logger.debug(bstack1l1l1l1l1_opy_.format(bstack1l111l1ll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1lll11l111_opy_.format(str(e)))
def bstack1lll1l1l1_opy_(framework):
  return bstack11l1_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧೆ").format(str(framework), __version__) if framework else bstack11l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥೇ").format(
    __version__)
def bstack1lllll111l_opy_():
  global CONFIG
  global bstack1ll1ll1ll_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l1l1ll1_opy_()
    logger.debug(bstack111ll111l_opy_.format(str(CONFIG)))
    bstack1ll1ll1ll_opy_ = bstack11llll11_opy_.bstack1l1lll1111_opy_(CONFIG, bstack1ll1ll1ll_opy_)
    bstack11lll111ll_opy_()
  except Exception as e:
    logger.error(bstack11l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢೈ") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l11l1111l_opy_
  atexit.register(bstack1l11lll1ll_opy_)
  signal.signal(signal.SIGINT, bstack11l11l1l_opy_)
  signal.signal(signal.SIGTERM, bstack11l11l1l_opy_)
def bstack1l11l1111l_opy_(exctype, value, traceback):
  global bstack1ll111l111_opy_
  try:
    for driver in bstack1ll111l111_opy_:
      bstack11l1111ll_opy_(driver, bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ೉"), bstack11l1_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣೊ") + str(value))
  except Exception:
    pass
  bstack11lllll11l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11lllll11l_opy_(message=bstack11l1_opy_ (u"࠭ࠧೋ"), bstack11llll1ll_opy_ = False):
  global CONFIG
  bstack11lll1l111_opy_ = bstack11l1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠩೌ") if bstack11llll1ll_opy_ else bstack11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸ್ࠧ")
  try:
    if message:
      bstack1ll1llll1l_opy_ = {
        bstack11lll1l111_opy_ : str(message)
      }
      bstack1ll11l111_opy_(bstack1l1ll11ll1_opy_, CONFIG, bstack1ll1llll1l_opy_)
    else:
      bstack1ll11l111_opy_(bstack1l1ll11ll1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l111lll1_opy_.format(str(e)))
def bstack1l1111ll1_opy_(bstack1llll1l1ll_opy_, size):
  bstack1l1llllll_opy_ = []
  while len(bstack1llll1l1ll_opy_) > size:
    bstack111ll11l_opy_ = bstack1llll1l1ll_opy_[:size]
    bstack1l1llllll_opy_.append(bstack111ll11l_opy_)
    bstack1llll1l1ll_opy_ = bstack1llll1l1ll_opy_[size:]
  bstack1l1llllll_opy_.append(bstack1llll1l1ll_opy_)
  return bstack1l1llllll_opy_
def bstack11ll11lll1_opy_(args):
  if bstack11l1_opy_ (u"ࠩ࠰ࡱࠬ೎") in args and bstack11l1_opy_ (u"ࠪࡴࡩࡨࠧ೏") in args:
    return True
  return False
def run_on_browserstack(bstack1l11l11l_opy_=None, bstack11llll11l1_opy_=None, bstack1l1llll1ll_opy_=False):
  global CONFIG
  global bstack1l11l1l1l_opy_
  global bstack11llll1l1l_opy_
  global bstack1l1l111111_opy_
  global bstack1l1l1lll1_opy_
  bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠫࠬ೐")
  bstack1ll1lll1ll_opy_(bstack1l1lll1l_opy_, logger)
  if bstack1l11l11l_opy_ and isinstance(bstack1l11l11l_opy_, str):
    bstack1l11l11l_opy_ = eval(bstack1l11l11l_opy_)
  if bstack1l11l11l_opy_:
    CONFIG = bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ೑")]
    bstack1l11l1l1l_opy_ = bstack1l11l11l_opy_[bstack11l1_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ೒")]
    bstack11llll1l1l_opy_ = bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ೓")]
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ೔"), bstack11llll1l1l_opy_)
    bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩೕ")
  bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬೖ"), uuid4().__str__())
  logger.debug(bstack11l1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩࡃࠧ೗") + bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ೘")))
  if not bstack1l1llll1ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll11lllll_opy_)
      return
    if sys.argv[1] == bstack11l1_opy_ (u"࠭࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩ೙") or sys.argv[1] == bstack11l1_opy_ (u"ࠧ࠮ࡸࠪ೚"):
      logger.info(bstack11l1_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡑࡻࡷ࡬ࡴࡴࠠࡔࡆࡎࠤࡻࢁࡽࠨ೛").format(__version__))
      return
    if sys.argv[1] == bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ೜"):
      bstack1l1111lll1_opy_()
      return
  args = sys.argv
  bstack1lllll111l_opy_()
  global bstack1lllll11l_opy_
  global bstack1l1ll111l_opy_
  global bstack1l1ll11l11_opy_
  global bstack1ll111l1l_opy_
  global bstack1l11lll1l_opy_
  global bstack1ll1lllll_opy_
  global bstack1l1111llll_opy_
  global bstack1l11111l1_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1ll11ll1_opy_
  global bstack11ll11l11_opy_
  bstack1l1ll111l_opy_ = len(CONFIG.get(bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೝ"), []))
  if not bstack11l1111l1_opy_:
    if args[1] == bstack11l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫೞ") or args[1] == bstack11l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭೟"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ೠ")
      args = args[2:]
    elif args[1] == bstack11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ೡ"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧೢ")
      args = args[2:]
    elif args[1] == bstack11l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨೣ"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ೤")
      args = args[2:]
    elif args[1] == bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ೥"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭೦")
      args = args[2:]
    elif args[1] == bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭೧"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ೨")
      args = args[2:]
    elif args[1] == bstack11l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ೩"):
      bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ೪")
      args = args[2:]
    else:
      if not bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭೫") in CONFIG or str(CONFIG[bstack11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ೬")]).lower() in [bstack11l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ೭"), bstack11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ೮")]:
        bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ೯")
        args = args[1:]
      elif str(CONFIG[bstack11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ೰")]).lower() == bstack11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨೱ"):
        bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩೲ")
        args = args[1:]
      elif str(CONFIG[bstack11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧೳ")]).lower() == bstack11l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ೴"):
        bstack11l1111l1_opy_ = bstack11l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ೵")
        args = args[1:]
      elif str(CONFIG[bstack11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ೶")]).lower() == bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ೷"):
        bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ೸")
        args = args[1:]
      elif str(CONFIG[bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭೹")]).lower() == bstack11l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ೺"):
        bstack11l1111l1_opy_ = bstack11l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ೻")
        args = args[1:]
      else:
        os.environ[bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ೼")] = bstack11l1111l1_opy_
        bstack1l11ll11l_opy_(bstack1l11ll1ll_opy_)
  os.environ[bstack11l1_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ೽")] = bstack11l1111l1_opy_
  bstack1l1l111111_opy_ = bstack11l1111l1_opy_
  global bstack1ll1l11l_opy_
  global bstack1ll1ll111l_opy_
  if bstack1l11l11l_opy_:
    try:
      os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ೾")] = bstack11l1111l1_opy_
      bstack1ll11l111_opy_(bstack11lllllll_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1lllll1l1_opy_.format(str(e)))
  global bstack1lll1111l_opy_
  global bstack1ll1l111l1_opy_
  global bstack1ll111llll_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack1l1l1l1l11_opy_
  global bstack1l1l11111_opy_
  global bstack111l11l1_opy_
  global bstack11llllll1l_opy_
  global bstack1llll1111_opy_
  global bstack1l1l1l111_opy_
  global bstack1ll1111l1l_opy_
  global bstack1ll1l1lll1_opy_
  global bstack1ll111l1ll_opy_
  global bstack1111l111_opy_
  global bstack11llll1ll1_opy_
  global bstack111ll1lll_opy_
  global bstack11ll111l_opy_
  global bstack1ll1111l11_opy_
  global bstack1l1ll1l1ll_opy_
  global bstack1lllll11_opy_
  global bstack1l111lll11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1lll1111l_opy_ = webdriver.Remote.__init__
    bstack1ll1l111l1_opy_ = WebDriver.quit
    bstack1ll1l1lll1_opy_ = WebDriver.close
    bstack11llll1ll1_opy_ = WebDriver.get
    bstack1l111lll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll1l11l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111l1ll11_opy_
    bstack1ll1ll111l_opy_ = bstack111l1ll11_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll111ll11_opy_
    from QWeb.keywords import browser
    bstack1ll111ll11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11ll1lll1l_opy_(CONFIG) and bstack1llll1lll1_opy_():
    if bstack1l1lll11ll_opy_() < version.parse(bstack1l1ll11ll_opy_):
      logger.error(bstack1l1l11lll_opy_.format(bstack1l1lll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack111ll1lll_opy_ = RemoteConnection._1ll1111ll1_opy_
      except Exception as e:
        logger.error(bstack11ll11llll_opy_.format(str(e)))
  if not CONFIG.get(bstack11l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ೿"), False) and not bstack1l11l11l_opy_:
    logger.info(bstack11llllll11_opy_)
  if bstack11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧഀ") in CONFIG and str(CONFIG[bstack11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨഁ")]).lower() != bstack11l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫം"):
    bstack11lll1l11l_opy_()
  elif bstack11l1111l1_opy_ != bstack11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ഃ") or (bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧഄ") and not bstack1l11l11l_opy_):
    bstack1l1111ll11_opy_()
  if (bstack11l1111l1_opy_ in [bstack11l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧഅ"), bstack11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨആ"), bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫഇ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11ll11l1ll_opy_
        bstack1l1l11111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l11lll111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1l1l1l11_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll111111_opy_ + str(e))
    except Exception as e:
      bstack111l1111_opy_(e, bstack1l11lll111_opy_)
    if bstack11l1111l1_opy_ != bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬഈ"):
      bstack11ll11ll11_opy_()
    bstack1ll111llll_opy_ = Output.start_test
    bstack1ll1ll1ll1_opy_ = Output.end_test
    bstack111l11l1_opy_ = TestStatus.__init__
    bstack1llll1111_opy_ = pabot._run
    bstack1l1l1l111_opy_ = QueueItem.__init__
    bstack1ll1111l1l_opy_ = pabot._create_command_for_execution
    bstack1l1ll1l1ll_opy_ = pabot._report_results
  if bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬഉ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack111l1111_opy_(e, bstack111lll111_opy_)
    bstack1ll111l1ll_opy_ = Runner.run_hook
    bstack1111l111_opy_ = Step.run
  if bstack11l1111l1_opy_ == bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ഊ"):
    try:
      from _pytest.config import Config
      bstack11ll111l_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll1111l11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1ll11111ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1lllll11_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨഋ"))
  try:
    framework_name = bstack11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧഌ") if bstack11l1111l1_opy_ in [bstack11l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ഍"), bstack11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩഎ"), bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬഏ")] else bstack11ll1lll1_opy_(bstack11l1111l1_opy_)
    bstack11l1l11l_opy_ = {
      bstack11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ഐ"): bstack11l1_opy_ (u"࠭ࡻ࠱ࡿ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬ഑").format(framework_name) if bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧഒ") and bstack1l1lll111l_opy_() else framework_name,
      bstack11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬഓ"): bstack1l11ll111l_opy_(framework_name),
      bstack11l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧഔ"): __version__,
      bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫക"): bstack11l1111l1_opy_
    }
    if bstack11l1111l1_opy_ in bstack1ll1lll111_opy_:
      if bstack1l1l1lll1l_opy_ and bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫഖ") in CONFIG and CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬഗ")] == True:
        if bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ഘ") in CONFIG:
          os.environ[bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨങ")] = os.getenv(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩച"), json.dumps(CONFIG[bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩഛ")]))
          CONFIG[bstack11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪജ")].pop(bstack11l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩഝ"), None)
          CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬഞ")].pop(bstack11l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫട"), None)
        bstack11l1l11l_opy_[bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧഠ")] = {
          bstack11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഡ"): bstack11l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫഢ"),
          bstack11l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫണ"): str(bstack1l1lll11ll_opy_())
        }
    if bstack11l1111l1_opy_ not in [bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬത")]:
      bstack1l111l1111_opy_ = bstack1ll1llllll_opy_.launch(CONFIG, bstack11l1l11l_opy_)
  except Exception as e:
    logger.debug(bstack111l1lll1_opy_.format(bstack11l1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ഥ"), str(e)))
  if bstack11l1111l1_opy_ == bstack11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ദ"):
    bstack1l1ll11l11_opy_ = True
    if bstack1l11l11l_opy_ and bstack1l1llll1ll_opy_:
      bstack1ll1lllll_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫധ"), {}).get(bstack11l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪന"))
      bstack1ll1ll1l_opy_(bstack1l11l1ll1l_opy_)
    elif bstack1l11l11l_opy_:
      bstack1ll1lllll_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ഩ"), {}).get(bstack11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬപ"))
      global bstack1ll111l111_opy_
      try:
        if bstack11ll11lll1_opy_(bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧഫ")]) and multiprocessing.current_process().name == bstack11l1_opy_ (u"ࠬ࠶ࠧബ"):
          bstack1l11l11l_opy_[bstack11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩഭ")].remove(bstack11l1_opy_ (u"ࠧ࠮࡯ࠪമ"))
          bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫയ")].remove(bstack11l1_opy_ (u"ࠩࡳࡨࡧ࠭ര"))
          bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭റ")] = bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧല")][0]
          with open(bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨള")], bstack11l1_opy_ (u"࠭ࡲࠨഴ")) as f:
            bstack1ll1l1llll_opy_ = f.read()
          bstack11111ll11_opy_ = bstack11l1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥവ").format(str(bstack1l11l11l_opy_))
          bstack1lllllllll_opy_ = bstack11111ll11_opy_ + bstack1ll1l1llll_opy_
          bstack11lll1111l_opy_ = bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫശ")] + bstack11l1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫഷ")
          with open(bstack11lll1111l_opy_, bstack11l1_opy_ (u"ࠪࡻࠬസ")):
            pass
          with open(bstack11lll1111l_opy_, bstack11l1_opy_ (u"ࠦࡼ࠱ࠢഹ")) as f:
            f.write(bstack1lllllllll_opy_)
          import subprocess
          bstack11ll11ll_opy_ = subprocess.run([bstack11l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧഺ"), bstack11lll1111l_opy_])
          if os.path.exists(bstack11lll1111l_opy_):
            os.unlink(bstack11lll1111l_opy_)
          os._exit(bstack11ll11ll_opy_.returncode)
        else:
          if bstack11ll11lll1_opy_(bstack1l11l11l_opy_[bstack11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦ഻ࠩ")]):
            bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧ഼ࠪ")].remove(bstack11l1_opy_ (u"ࠨ࠯ࡰࠫഽ"))
            bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬാ")].remove(bstack11l1_opy_ (u"ࠪࡴࡩࡨࠧി"))
            bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧീ")] = bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨു")][0]
          bstack1ll1ll1l_opy_(bstack1l11l1ll1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l11l11l_opy_[bstack11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩൂ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩൃ")] = bstack11l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪൄ")
          mod_globals[bstack11l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ൅")] = os.path.abspath(bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭െ")])
          exec(open(bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧേ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬൈ").format(str(e)))
          for driver in bstack1ll111l111_opy_:
            bstack11llll11l1_opy_.append({
              bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ൉"): bstack1l11l11l_opy_[bstack11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪൊ")],
              bstack11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧോ"): str(e),
              bstack11l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨൌ"): multiprocessing.current_process().name
            })
            bstack11l1111ll_opy_(driver, bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦ്ࠪ"), bstack11l1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢൎ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll111l111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11llll1l1l_opy_, CONFIG, logger)
      bstack11lll1ll_opy_()
      bstack1l111111l_opy_()
      bstack1lllll11ll_opy_ = {
        bstack11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ൏"): args[0],
        bstack11l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭൐"): CONFIG,
        bstack11l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ൑"): bstack1l11l1l1l_opy_,
        bstack11l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ൒"): bstack11llll1l1l_opy_
      }
      percy.bstack11lllll111_opy_()
      if bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൓") in CONFIG:
        bstack1l111ll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l1l1llll_opy_ = manager.list()
        if bstack11ll11lll1_opy_(args):
          for index, platform in enumerate(CONFIG[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ൔ")]):
            if index == 0:
              bstack1lllll11ll_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧൕ")] = args
            bstack1l111ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1lllll11ll_opy_, bstack1l1l1llll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨൖ")]):
            bstack1l111ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1lllll11ll_opy_, bstack1l1l1llll_opy_)))
        for t in bstack1l111ll1_opy_:
          t.start()
        for t in bstack1l111ll1_opy_:
          t.join()
        bstack1l11111l1_opy_ = list(bstack1l1l1llll_opy_)
      else:
        if bstack11ll11lll1_opy_(args):
          bstack1lllll11ll_opy_[bstack11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩൗ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lllll11ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll1ll1l_opy_(bstack1l11l1ll1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ൘")] = bstack11l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ൙")
          mod_globals[bstack11l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ൚")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ൛") or bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൜"):
    percy.init(bstack11llll1l1l_opy_, CONFIG, logger)
    percy.bstack11lllll111_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack111l1111_opy_(e, bstack1l11lll111_opy_)
    bstack11lll1ll_opy_()
    bstack1ll1ll1l_opy_(bstack1l1111l11l_opy_)
    if bstack1l1l1lll1l_opy_:
      bstack111ll1l1_opy_(bstack1l1111l11l_opy_, args)
      if bstack11l1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ൝") in args:
        i = args.index(bstack11l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ൞"))
        args.pop(i)
        args.pop(i)
      if bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪൟ") not in CONFIG:
        CONFIG[bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫൠ")] = [{}]
        bstack1l1ll111l_opy_ = 1
      if bstack1lllll11l_opy_ == 0:
        bstack1lllll11l_opy_ = 1
      args.insert(0, str(bstack1lllll11l_opy_))
      args.insert(0, str(bstack11l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧൡ")))
    if bstack1ll1llllll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1lll11ll1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1ll11111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l1_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥൢ"),
        ).parse_args(bstack1lll11ll1l_opy_)
        bstack11ll1lll11_opy_ = args.index(bstack1lll11ll1l_opy_[0]) if len(bstack1lll11ll1l_opy_) > 0 else len(args)
        args.insert(bstack11ll1lll11_opy_, str(bstack11l1_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨൣ")))
        args.insert(bstack11ll1lll11_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩ൤"))))
        if bstack1111ll1l1_opy_(os.environ.get(bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ൥"))) and str(os.environ.get(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ൦"), bstack11l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭൧"))) != bstack11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ൨"):
          for bstack1llll11l1_opy_ in bstack1ll11111_opy_:
            args.remove(bstack1llll11l1_opy_)
          bstack111l1l1ll_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ൩")).split(bstack11l1_opy_ (u"ࠫ࠱࠭൪"))
          for bstack1ll111lll1_opy_ in bstack111l1l1ll_opy_:
            args.append(bstack1ll111lll1_opy_)
      except Exception as e:
        logger.error(bstack11l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࠣ൫").format(e))
    pabot.main(args)
  elif bstack11l1111l1_opy_ == bstack11l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ൬"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack111l1111_opy_(e, bstack1l11lll111_opy_)
    for a in args:
      if bstack11l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭൭") in a:
        bstack1l11lll1l_opy_ = int(a.split(bstack11l1_opy_ (u"ࠨ࠼ࠪ൮"))[1])
      if bstack11l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭൯") in a:
        bstack1ll1lllll_opy_ = str(a.split(bstack11l1_opy_ (u"ࠪ࠾ࠬ൰"))[1])
      if bstack11l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ൱") in a:
        bstack1l1111llll_opy_ = str(a.split(bstack11l1_opy_ (u"ࠬࡀࠧ൲"))[1])
    bstack111l1l1l_opy_ = None
    if bstack11l1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ൳") in args:
      i = args.index(bstack11l1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭൴"))
      args.pop(i)
      bstack111l1l1l_opy_ = args.pop(i)
    if bstack111l1l1l_opy_ is not None:
      global bstack111l1l11l_opy_
      bstack111l1l11l_opy_ = bstack111l1l1l_opy_
    bstack1ll1ll1l_opy_(bstack1l1111l11l_opy_)
    run_cli(args)
    if bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ൵") in multiprocessing.current_process().__dict__.keys():
      for bstack1lll11ll11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11llll11l1_opy_.append(bstack1lll11ll11_opy_)
  elif bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ൶"):
    percy.init(bstack11llll1l1l_opy_, CONFIG, logger)
    percy.bstack11lllll111_opy_()
    bstack1l1l1ll1ll_opy_ = bstack11ll111ll1_opy_(args, logger, CONFIG, bstack1l1l1lll1l_opy_)
    bstack1l1l1ll1ll_opy_.bstack1l1ll1111l_opy_()
    bstack11lll1ll_opy_()
    bstack1ll111l1l_opy_ = True
    bstack1ll11ll1_opy_ = bstack1l1l1ll1ll_opy_.bstack11ll11l1l_opy_()
    bstack1l1l1ll1ll_opy_.bstack1lllll11ll_opy_(bstack1l1ll11111_opy_)
    bstack1ll1l11ll_opy_ = bstack1l1l1ll1ll_opy_.bstack1lllllll1_opy_(bstack1l1lll1l1_opy_, {
      bstack11l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ൷"): bstack1l11l1l1l_opy_,
      bstack11l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭൸"): bstack11llll1l1l_opy_,
      bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ൹"): bstack1l1l1lll1l_opy_
    })
    try:
      bstack111111ll_opy_, bstack11l11111l_opy_ = map(list, zip(*bstack1ll1l11ll_opy_))
      bstack1l1ll11l1l_opy_ = bstack111111ll_opy_[0]
      for status_code in bstack11l11111l_opy_:
        if status_code != 0:
          bstack11ll11l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦൺ").format(str(e)))
  elif bstack11l1111l1_opy_ == bstack11l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧൻ"):
    try:
      from behave.__main__ import main as bstack1l11l11ll1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack111l1111_opy_(e, bstack111lll111_opy_)
    bstack11lll1ll_opy_()
    bstack1ll111l1l_opy_ = True
    bstack1lll11l11_opy_ = 1
    if bstack11l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨർ") in CONFIG:
      bstack1lll11l11_opy_ = CONFIG[bstack11l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩൽ")]
    if bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ൾ") in CONFIG:
      bstack11ll1l111_opy_ = int(bstack1lll11l11_opy_) * int(len(CONFIG[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧൿ")]))
    else:
      bstack11ll1l111_opy_ = int(bstack1lll11l11_opy_)
    config = Configuration(args)
    bstack11l1ll1l1_opy_ = config.paths
    if len(bstack11l1ll1l1_opy_) == 0:
      import glob
      pattern = bstack11l1_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ඀")
      bstack11111l11_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11111l11_opy_)
      config = Configuration(args)
      bstack11l1ll1l1_opy_ = config.paths
    bstack1lll111ll_opy_ = [os.path.normpath(item) for item in bstack11l1ll1l1_opy_]
    bstack11ll1l1l_opy_ = [os.path.normpath(item) for item in args]
    bstack111l11l11_opy_ = [item for item in bstack11ll1l1l_opy_ if item not in bstack1lll111ll_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l1_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧඁ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lll111ll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1lllll11l1_opy_)))
                    for bstack1lllll11l1_opy_ in bstack1lll111ll_opy_]
    bstack1l1l1111ll_opy_ = []
    for spec in bstack1lll111ll_opy_:
      bstack1l111l1l11_opy_ = []
      bstack1l111l1l11_opy_ += bstack111l11l11_opy_
      bstack1l111l1l11_opy_.append(spec)
      bstack1l1l1111ll_opy_.append(bstack1l111l1l11_opy_)
    execution_items = []
    for bstack1l111l1l11_opy_ in bstack1l1l1111ll_opy_:
      if bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪං") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫඃ")]):
          item = {}
          item[bstack11l1_opy_ (u"ࠩࡤࡶ࡬࠭඄")] = bstack11l1_opy_ (u"ࠪࠤࠬඅ").join(bstack1l111l1l11_opy_)
          item[bstack11l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪආ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l1_opy_ (u"ࠬࡧࡲࡨࠩඇ")] = bstack11l1_opy_ (u"࠭ࠠࠨඈ").join(bstack1l111l1l11_opy_)
        item[bstack11l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ඉ")] = 0
        execution_items.append(item)
    bstack1ll1l1111l_opy_ = bstack1l1111ll1_opy_(execution_items, bstack11ll1l111_opy_)
    for execution_item in bstack1ll1l1111l_opy_:
      bstack1l111ll1_opy_ = []
      for item in execution_item:
        bstack1l111ll1_opy_.append(bstack11l111l1_opy_(name=str(item[bstack11l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧඊ")]),
                                             target=bstack111l1111l_opy_,
                                             args=(item[bstack11l1_opy_ (u"ࠩࡤࡶ࡬࠭උ")],)))
      for t in bstack1l111ll1_opy_:
        t.start()
      for t in bstack1l111ll1_opy_:
        t.join()
  else:
    bstack1l11ll11l_opy_(bstack1l11ll1ll_opy_)
  if not bstack1l11l11l_opy_:
    bstack1ll1l1l111_opy_()
  bstack11llll11_opy_.bstack1l1111l11_opy_()
def browserstack_initialize(bstack11ll11l111_opy_=None):
  run_on_browserstack(bstack11ll11l111_opy_, None, True)
@measure(event_name=EVENTS.bstack1l111l111l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1ll1l1l111_opy_():
  global CONFIG
  global bstack1l1l111111_opy_
  global bstack11ll11l11_opy_
  global bstack1ll1ll1l1_opy_
  global bstack1l1l1lll1_opy_
  bstack1ll1llllll_opy_.stop()
  bstack1l11l11l1l_opy_.bstack111l1l11_opy_()
  if bstack11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧඌ") in CONFIG and str(CONFIG[bstack11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨඍ")]).lower() != bstack11l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫඎ"):
    bstack1111ll111_opy_, bstack11l1llll1_opy_ = bstack11l11llll_opy_()
  else:
    bstack1111ll111_opy_, bstack11l1llll1_opy_ = get_build_link()
  bstack111lllll_opy_(bstack1111ll111_opy_)
  if bstack1111ll111_opy_ is not None and bstack1llll1ll_opy_() != -1:
    sessions = bstack11ll1llll1_opy_(bstack1111ll111_opy_)
    bstack1lll111l_opy_(sessions, bstack11l1llll1_opy_)
  if bstack1l1l111111_opy_ == bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ඏ") and bstack11ll11l11_opy_ != 0:
    sys.exit(bstack11ll11l11_opy_)
  if bstack1l1l111111_opy_ == bstack11l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧඐ") and bstack1ll1ll1l1_opy_ != 0:
    sys.exit(bstack1ll1ll1l1_opy_)
def bstack111lllll_opy_(new_id):
    global bstack1l111llll1_opy_
    bstack1l111llll1_opy_ = new_id
def bstack11ll1lll1_opy_(bstack1ll11l1l1l_opy_):
  if bstack1ll11l1l1l_opy_:
    return bstack1ll11l1l1l_opy_.capitalize()
  else:
    return bstack11l1_opy_ (u"ࠨࠩඑ")
@measure(event_name=EVENTS.bstack11lll11ll_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack111l11111_opy_(bstack1l1ll1lll1_opy_):
  if bstack11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧඒ") in bstack1l1ll1lll1_opy_ and bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨඓ")] != bstack11l1_opy_ (u"ࠫࠬඔ"):
    return bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪඕ")]
  else:
    bstack1lll11l11l_opy_ = bstack11l1_opy_ (u"ࠨࠢඖ")
    if bstack11l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ඗") in bstack1l1ll1lll1_opy_ and bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ඘")] != None:
      bstack1lll11l11l_opy_ += bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ඙")] + bstack11l1_opy_ (u"ࠥ࠰ࠥࠨක")
      if bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠫࡴࡹࠧඛ")] == bstack11l1_opy_ (u"ࠧ࡯࡯ࡴࠤග"):
        bstack1lll11l11l_opy_ += bstack11l1_opy_ (u"ࠨࡩࡐࡕࠣࠦඝ")
      bstack1lll11l11l_opy_ += (bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫඞ")] or bstack11l1_opy_ (u"ࠨࠩඟ"))
      return bstack1lll11l11l_opy_
    else:
      bstack1lll11l11l_opy_ += bstack11ll1lll1_opy_(bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪච")]) + bstack11l1_opy_ (u"ࠥࠤࠧඡ") + (
              bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ජ")] or bstack11l1_opy_ (u"ࠬ࠭ඣ")) + bstack11l1_opy_ (u"ࠨࠬࠡࠤඤ")
      if bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠧࡰࡵࠪඥ")] == bstack11l1_opy_ (u"࡙ࠣ࡬ࡲࡩࡵࡷࡴࠤඦ"):
        bstack1lll11l11l_opy_ += bstack11l1_opy_ (u"ࠤ࡚࡭ࡳࠦࠢට")
      bstack1lll11l11l_opy_ += bstack1l1ll1lll1_opy_[bstack11l1_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧඨ")] or bstack11l1_opy_ (u"ࠫࠬඩ")
      return bstack1lll11l11l_opy_
@measure(event_name=EVENTS.bstack11l1lllll_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l1111ll1l_opy_(bstack111l11l1l_opy_):
  if bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠧࡪ࡯࡯ࡧࠥඪ"):
    return bstack11l1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡅࡲࡱࡵࡲࡥࡵࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩණ")
  elif bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢඬ"):
    return bstack11l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡆࡢ࡫࡯ࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫත")
  elif bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤථ"):
    return bstack11l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡖࡡࡴࡵࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪද")
  elif bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥධ"):
    return bstack11l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡉࡷࡸ࡯ࡳ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧන")
  elif bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ඲"):
    return bstack11l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࠦࡩࡪࡧ࠳࠳࠸࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࠨ࡫ࡥࡢ࠵࠵࠺ࠧࡄࡔࡪ࡯ࡨࡳࡺࡺ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬඳ")
  elif bstack111l11l1l_opy_ == bstack11l1_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠤප"):
    return bstack11l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࡗࡻ࡮࡯࡫ࡱ࡫ࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪඵ")
  else:
    return bstack11l1_opy_ (u"ࠪࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࠧබ") + bstack11ll1lll1_opy_(
      bstack111l11l1l_opy_) + bstack11l1_opy_ (u"ࠫࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪභ")
def bstack1111l1ll1_opy_(session):
  return bstack11l1_opy_ (u"ࠬࡂࡴࡳࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡵࡳࡼࠨ࠾࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠢࡶࡩࡸࡹࡩࡰࡰ࠰ࡲࡦࡳࡥࠣࡀ࠿ࡥࠥ࡮ࡲࡦࡨࡀࠦࢀࢃࠢࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤࡢࡦࡱࡧ࡮࡬ࠤࡁࡿࢂࡂ࠯ࡢࡀ࠿࠳ࡹࡪ࠾ࡼࡿࡾࢁࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼࠰ࡶࡵࡂࠬම").format(
    session[bstack11l1_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪඹ")], bstack111l11111_opy_(session), bstack1l1111ll1l_opy_(session[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡵࡣࡷࡹࡸ࠭ය")]),
    bstack1l1111ll1l_opy_(session[bstack11l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨර")]),
    bstack11ll1lll1_opy_(session[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ඼")] or session[bstack11l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪල")] or bstack11l1_opy_ (u"ࠫࠬ඾")) + bstack11l1_opy_ (u"ࠧࠦࠢ඿") + (session[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨව")] or bstack11l1_opy_ (u"ࠧࠨශ")),
    session[bstack11l1_opy_ (u"ࠨࡱࡶࠫෂ")] + bstack11l1_opy_ (u"ࠤࠣࠦස") + session[bstack11l1_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧහ")], session[bstack11l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ළ")] or bstack11l1_opy_ (u"ࠬ࠭ෆ"),
    session[bstack11l1_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪ෇")] if session[bstack11l1_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫ෈")] else bstack11l1_opy_ (u"ࠨࠩ෉"))
@measure(event_name=EVENTS.bstack1lll1111_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1lll111l_opy_(sessions, bstack11l1llll1_opy_):
  try:
    bstack1l1ll1l1_opy_ = bstack11l1_opy_ (u"ࠤ්ࠥ")
    if not os.path.exists(bstack11lll11l11_opy_):
      os.mkdir(bstack11lll11l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1_opy_ (u"ࠪࡥࡸࡹࡥࡵࡵ࠲ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨ෋")), bstack11l1_opy_ (u"ࠫࡷ࠭෌")) as f:
      bstack1l1ll1l1_opy_ = f.read()
    bstack1l1ll1l1_opy_ = bstack1l1ll1l1_opy_.replace(bstack11l1_opy_ (u"ࠬࢁࠥࡓࡇࡖ࡙ࡑ࡚ࡓࡠࡅࡒ࡙ࡓ࡚ࠥࡾࠩ෍"), str(len(sessions)))
    bstack1l1ll1l1_opy_ = bstack1l1ll1l1_opy_.replace(bstack11l1_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠩࢂ࠭෎"), bstack11l1llll1_opy_)
    bstack1l1ll1l1_opy_ = bstack1l1ll1l1_opy_.replace(bstack11l1_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊࠫࡽࠨා"),
                                              sessions[0].get(bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡣࡰࡩࠬැ")) if sessions[0] else bstack11l1_opy_ (u"ࠩࠪෑ"))
    with open(os.path.join(bstack11lll11l11_opy_, bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧි")), bstack11l1_opy_ (u"ࠫࡼ࠭ී")) as stream:
      stream.write(bstack1l1ll1l1_opy_.split(bstack11l1_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩු"))[0])
      for session in sessions:
        stream.write(bstack1111l1ll1_opy_(session))
      stream.write(bstack1l1ll1l1_opy_.split(bstack11l1_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪ෕"))[1])
    logger.info(bstack11l1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࡦࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡥࡹ࡮ࡲࡤࠡࡣࡵࡸ࡮࡬ࡡࡤࡶࡶࠤࡦࡺࠠࡼࡿࠪූ").format(bstack11lll11l11_opy_));
  except Exception as e:
    logger.debug(bstack1l11llll1l_opy_.format(str(e)))
def bstack11ll1llll1_opy_(bstack1111ll111_opy_):
  global CONFIG
  try:
    host = bstack11l1_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫ෗") if bstack11l1_opy_ (u"ࠩࡤࡴࡵ࠭ෘ") in CONFIG else bstack11l1_opy_ (u"ࠪࡥࡵ࡯ࠧෙ")
    user = CONFIG[bstack11l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ේ")]
    key = CONFIG[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨෛ")]
    bstack1lll1lll_opy_ = bstack11l1_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬො") if bstack11l1_opy_ (u"ࠧࡢࡲࡳࠫෝ") in CONFIG else (bstack11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬෞ") if CONFIG.get(bstack11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ෟ")) else bstack11l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ෠"))
    url = bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠲࡯ࡹ࡯࡯ࠩ෡").format(user, key, host, bstack1lll1lll_opy_,
                                                                                bstack1111ll111_opy_)
    headers = {
      bstack11l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ෢"): bstack11l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ෣"),
    }
    proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack11l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ෤")], response.json()))
  except Exception as e:
    logger.debug(bstack1l1l1ll111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l11l111l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def get_build_link():
  global CONFIG
  global bstack1l111llll1_opy_
  try:
    if bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ෥") in CONFIG:
      host = bstack11l1_opy_ (u"ࠩࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨࠬ෦") if bstack11l1_opy_ (u"ࠪࡥࡵࡶࠧ෧") in CONFIG else bstack11l1_opy_ (u"ࠫࡦࡶࡩࠨ෨")
      user = CONFIG[bstack11l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ෩")]
      key = CONFIG[bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ෪")]
      bstack1lll1lll_opy_ = bstack11l1_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭෫") if bstack11l1_opy_ (u"ࠨࡣࡳࡴࠬ෬") in CONFIG else bstack11l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ෭")
      url = bstack11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡿࢂ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠪ෮").format(user, key, host, bstack1lll1lll_opy_)
      headers = {
        bstack11l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ෯"): bstack11l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ෰"),
      }
      if bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ෱") in CONFIG:
        params = {bstack11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬෲ"): CONFIG[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫෳ")], bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ෴"): CONFIG[bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ෵")]}
      else:
        params = {bstack11l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ෶"): CONFIG[bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ෷")]}
      proxies = bstack1l1l1l1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1l1ll1l1l1_opy_ = response.json()[0][bstack11l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡦࡺ࡯࡬ࡥࠩ෸")]
        if bstack1l1ll1l1l1_opy_:
          bstack11l1llll1_opy_ = bstack1l1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫ෹")].split(bstack11l1_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣ࠮ࡤࡸ࡭ࡱࡪࠧ෺"))[0] + bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴ࠱ࠪ෻") + bstack1l1ll1l1l1_opy_[
            bstack11l1_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭෼")]
          logger.info(bstack111llll1l_opy_.format(bstack11l1llll1_opy_))
          bstack1l111llll1_opy_ = bstack1l1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ෽")]
          bstack1lll111l11_opy_ = CONFIG[bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ෾")]
          if bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ෿") in CONFIG:
            bstack1lll111l11_opy_ += bstack11l1_opy_ (u"ࠧࠡࠩ฀") + CONFIG[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪก")]
          if bstack1lll111l11_opy_ != bstack1l1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧข")]:
            logger.debug(bstack1l1ll1l11l_opy_.format(bstack1l1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨฃ")], bstack1lll111l11_opy_))
          return [bstack1l1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧค")], bstack11l1llll1_opy_]
    else:
      logger.warn(bstack1ll1llll_opy_)
  except Exception as e:
    logger.debug(bstack11llllllll_opy_.format(str(e)))
  return [None, None]
def bstack1lll1lll11_opy_(url, bstack1ll1lll11l_opy_=False):
  global CONFIG
  global bstack1l11ll1l1_opy_
  if not bstack1l11ll1l1_opy_:
    hostname = bstack11l11lll_opy_(url)
    is_private = bstack1l1l11l1_opy_(hostname)
    if (bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩฅ") in CONFIG and not bstack1111ll1l1_opy_(CONFIG[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪฆ")])) and (is_private or bstack1ll1lll11l_opy_):
      bstack1l11ll1l1_opy_ = hostname
def bstack11l11lll_opy_(url):
  return urlparse(url).hostname
def bstack1l1l11l1_opy_(hostname):
  for bstack1l1l1l1ll1_opy_ in bstack11llll1l11_opy_:
    regex = re.compile(bstack1l1l1l1ll1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l111lll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111lll11_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l11lll1l_opy_
  bstack11l111ll_opy_ = not (bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫง"), None) and bstack1l1lll1lll_opy_(
          threading.current_thread(), bstack11l1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧจ"), None))
  bstack11llll1l1_opy_ = getattr(driver, bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩฉ"), None) != True
  if not bstack1lll11ll1_opy_.bstack111l1ll1l_opy_(CONFIG, bstack1l11lll1l_opy_) or (bstack11llll1l1_opy_ and bstack11l111ll_opy_):
    logger.warning(bstack11l1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨช"))
    return {}
  try:
    logger.debug(bstack11l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨซ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11l1l111_opy_.bstack1l1111l1_opy_)
    return results
  except Exception:
    logger.error(bstack11l1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢฌ"))
    return {}
@measure(event_name=EVENTS.bstack1l1lllll1l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l11lll1l_opy_
  bstack11l111ll_opy_ = not (bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪญ"), None) and bstack1l1lll1lll_opy_(
          threading.current_thread(), bstack11l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ฎ"), None))
  bstack11llll1l1_opy_ = getattr(driver, bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨฏ"), None) != True
  if not bstack1lll11ll1_opy_.bstack111l1ll1l_opy_(CONFIG, bstack1l11lll1l_opy_) or (bstack11llll1l1_opy_ and bstack11l111ll_opy_):
    logger.warning(bstack11l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽ࠳ࠨฐ"))
    return {}
  try:
    logger.debug(bstack11l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨฑ"))
    logger.debug(perform_scan(driver))
    bstack1ll1l1ll1l_opy_ = driver.execute_async_script(bstack11l1l111_opy_.bstack11lll1llll_opy_)
    return bstack1ll1l1ll1l_opy_
  except Exception:
    logger.error(bstack11l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧฒ"))
    return {}
@measure(event_name=EVENTS.bstack1l1lll1l11_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l11lll1l_opy_
  bstack11l111ll_opy_ = not (bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩณ"), None) and bstack1l1lll1lll_opy_(
          threading.current_thread(), bstack11l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬด"), None))
  bstack11llll1l1_opy_ = getattr(driver, bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧต"), None) != True
  if not bstack1lll11ll1_opy_.bstack111l1ll1l_opy_(CONFIG, bstack1l11lll1l_opy_) or (bstack11llll1l1_opy_ and bstack11l111ll_opy_):
    logger.warning(bstack11l1_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡷࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠥถ"))
    return {}
  try:
    bstack1l11l11ll_opy_ = driver.execute_async_script(bstack11l1l111_opy_.perform_scan, {bstack11l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩท"): kwargs.get(bstack11l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫธ"), None) or bstack11l1_opy_ (u"ࠫࠬน")})
    return bstack1l11l11ll_opy_
  except Exception:
    logger.error(bstack11l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦบ"))
    return {}