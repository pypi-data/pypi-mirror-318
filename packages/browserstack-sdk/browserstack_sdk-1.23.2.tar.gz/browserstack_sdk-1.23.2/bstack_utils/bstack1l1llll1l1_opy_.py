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
import re
from bstack_utils.bstack1llllll1ll_opy_ import bstack1ll11llll1l_opy_
def bstack1ll1l111111_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᚣ")):
        return bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᚤ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᚥ")):
        return bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨᚦ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᚧ")):
        return bstack11l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᚨ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᚩ")):
        return bstack11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᚪ")
def bstack1ll1l1111ll_opy_(fixture_name):
    return bool(re.match(bstack11l1_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࡼ࡮ࡱࡧࡹࡱ࡫ࠩࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᚫ"), fixture_name))
def bstack1ll1l11111l_opy_(fixture_name):
    return bool(re.match(bstack11l1_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᚬ"), fixture_name))
def bstack1ll11llllll_opy_(fixture_name):
    return bool(re.match(bstack11l1_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᚭ"), fixture_name))
def bstack1ll11lll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᚮ")):
        return bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᚯ"), bstack11l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᚰ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᚱ")):
        return bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᚲ"), bstack11l1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᚳ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᚴ")):
        return bstack11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᚵ"), bstack11l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᚶ")
    elif fixture_name.startswith(bstack11l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᚷ")):
        return bstack11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᚸ"), bstack11l1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᚹ")
    return None, None
def bstack1ll11lll111_opy_(hook_name):
    if hook_name in [bstack11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᚺ"), bstack11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᚻ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1ll11lllll1_opy_(hook_name):
    if hook_name in [bstack11l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᚼ"), bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᚽ")]:
        return bstack11l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᚾ")
    elif hook_name in [bstack11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬᚿ"), bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᛀ")]:
        return bstack11l1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᛁ")
    elif hook_name in [bstack11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᛂ"), bstack11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᛃ")]:
        return bstack11l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᛄ")
    elif hook_name in [bstack11l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᛅ"), bstack11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᛆ")]:
        return bstack11l1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᛇ")
    return hook_name
def bstack1ll11ll1lll_opy_(node, scenario):
    if hasattr(node, bstack11l1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᛈ")):
        parts = node.nodeid.rsplit(bstack11l1_opy_ (u"ࠤ࡞ࠦᛉ"))
        params = parts[-1]
        return bstack11l1_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥᛊ").format(scenario.name, params)
    return scenario.name
def bstack1ll11lll1l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l1_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᛋ")):
            examples = list(node.callspec.params[bstack11l1_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫᛌ")].values())
        return examples
    except:
        return []
def bstack1ll11llll11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1ll11lll1ll_opy_(report):
    try:
        status = bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᛍ")
        if report.passed or (report.failed and hasattr(report, bstack11l1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᛎ"))):
            status = bstack11l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᛏ")
        elif report.skipped:
            status = bstack11l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᛐ")
        bstack1ll11llll1l_opy_(status)
    except:
        pass
def bstack1ll1l11l11_opy_(status):
    try:
        bstack1ll1l1111l1_opy_ = bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᛑ")
        if status == bstack11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᛒ"):
            bstack1ll1l1111l1_opy_ = bstack11l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᛓ")
        elif status == bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᛔ"):
            bstack1ll1l1111l1_opy_ = bstack11l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᛕ")
        bstack1ll11llll1l_opy_(bstack1ll1l1111l1_opy_)
    except:
        pass
def bstack1ll1l111l11_opy_(item=None, report=None, summary=None, extra=None):
    return