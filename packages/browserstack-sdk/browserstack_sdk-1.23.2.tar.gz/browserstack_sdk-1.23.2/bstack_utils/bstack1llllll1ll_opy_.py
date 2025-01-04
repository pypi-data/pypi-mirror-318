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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111111lll1_opy_, bstack11l11lll_opy_, bstack1l1lll1lll_opy_, bstack1l1l11l1_opy_, \
    bstack1lll1lllll1_opy_
from bstack_utils.measure import measure
def bstack1l11lll1ll_opy_(bstack1ll11l111ll_opy_):
    for driver in bstack1ll11l111ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11l1lllll_opy_, stage=STAGE.SINGLE)
def bstack11l1111ll_opy_(driver, status, reason=bstack11l1_opy_ (u"ࠪࠫᛘ")):
    bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
    if bstack1l1l1lll1_opy_.bstack111lll1111_opy_():
        return
    bstack1l1ll11lll_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᛙ"), bstack11l1_opy_ (u"ࠬ࠭ᛚ"), status, reason, bstack11l1_opy_ (u"࠭ࠧᛛ"), bstack11l1_opy_ (u"ࠧࠨᛜ"))
    driver.execute_script(bstack1l1ll11lll_opy_)
@measure(event_name=EVENTS.bstack11l1lllll_opy_, stage=STAGE.SINGLE)
def bstack1lll1l11ll_opy_(page, status, reason=bstack11l1_opy_ (u"ࠨࠩᛝ")):
    try:
        if page is None:
            return
        bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
        if bstack1l1l1lll1_opy_.bstack111lll1111_opy_():
            return
        bstack1l1ll11lll_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᛞ"), bstack11l1_opy_ (u"ࠪࠫᛟ"), status, reason, bstack11l1_opy_ (u"ࠫࠬᛠ"), bstack11l1_opy_ (u"ࠬ࠭ᛡ"))
        page.evaluate(bstack11l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᛢ"), bstack1l1ll11lll_opy_)
    except Exception as e:
        print(bstack11l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡾࢁࠧᛣ"), e)
def bstack1llll1l1l1_opy_(type, name, status, reason, bstack11ll1ll1ll_opy_, bstack1llll111_opy_):
    bstack11l1l11ll_opy_ = {
        bstack11l1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨᛤ"): type,
        bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᛥ"): {}
    }
    if type == bstack11l1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬᛦ"):
        bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᛧ")][bstack11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᛨ")] = bstack11ll1ll1ll_opy_
        bstack11l1l11ll_opy_[bstack11l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᛩ")][bstack11l1_opy_ (u"ࠧࡥࡣࡷࡥࠬᛪ")] = json.dumps(str(bstack1llll111_opy_))
    if type == bstack11l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ᛫"):
        bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᛬")][bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ᛭")] = name
    if type == bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᛮ"):
        bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᛯ")][bstack11l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᛰ")] = status
        if status == bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᛱ") and str(reason) != bstack11l1_opy_ (u"ࠣࠤᛲ"):
            bstack11l1l11ll_opy_[bstack11l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᛳ")][bstack11l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᛴ")] = json.dumps(str(reason))
    bstack1l1111ll_opy_ = bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᛵ").format(json.dumps(bstack11l1l11ll_opy_))
    return bstack1l1111ll_opy_
def bstack1lll1lll11_opy_(url, config, logger, bstack1ll1lll11l_opy_=False):
    hostname = bstack11l11lll_opy_(url)
    is_private = bstack1l1l11l1_opy_(hostname)
    try:
        if is_private or bstack1ll1lll11l_opy_:
            file_path = bstack111111lll1_opy_(bstack11l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᛶ"), bstack11l1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᛷ"), logger)
            if os.environ.get(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᛸ")) and eval(
                    os.environ.get(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᛹"))):
                return
            if (bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭᛺") in config and not config[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᛻")]):
                os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩ᛼")] = str(True)
                bstack1ll11l11l11_opy_ = {bstack11l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ᛽"): hostname}
                bstack1lll1lllll1_opy_(bstack11l1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ᛾"), bstack11l1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ᛿"), bstack1ll11l11l11_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l111l1_opy_(caps, bstack1ll11l11ll1_opy_):
    if bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜀ") in caps:
        caps[bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᜁ")][bstack11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᜂ")] = True
        if bstack1ll11l11ll1_opy_:
            caps[bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᜃ")][bstack11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᜄ")] = bstack1ll11l11ll1_opy_
    else:
        caps[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᜅ")] = True
        if bstack1ll11l11ll1_opy_:
            caps[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᜆ")] = bstack1ll11l11ll1_opy_
def bstack1ll11llll1l_opy_(bstack11l1111l11_opy_):
    bstack1ll11l11l1l_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᜇ"), bstack11l1_opy_ (u"ࠩࠪᜈ"))
    if bstack1ll11l11l1l_opy_ == bstack11l1_opy_ (u"ࠪࠫᜉ") or bstack1ll11l11l1l_opy_ == bstack11l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᜊ"):
        threading.current_thread().testStatus = bstack11l1111l11_opy_
    else:
        if bstack11l1111l11_opy_ == bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᜋ"):
            threading.current_thread().testStatus = bstack11l1111l11_opy_