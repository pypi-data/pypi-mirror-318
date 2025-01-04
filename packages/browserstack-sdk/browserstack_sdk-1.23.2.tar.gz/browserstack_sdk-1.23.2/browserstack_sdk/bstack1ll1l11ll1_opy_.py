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
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll111111_opy_ = {}
        bstack11ll111l11_opy_ = os.environ.get(bstack11l1_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧป"), bstack11l1_opy_ (u"ࠧࠨผ"))
        if not bstack11ll111l11_opy_:
            return bstack1lll111111_opy_
        try:
            bstack11ll111l1l_opy_ = json.loads(bstack11ll111l11_opy_)
            if bstack11l1_opy_ (u"ࠣࡱࡶࠦฝ") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠤࡲࡷࠧพ")] = bstack11ll111l1l_opy_[bstack11l1_opy_ (u"ࠥࡳࡸࠨฟ")]
            if bstack11l1_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣภ") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣม") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤย")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦร"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦฤ")))
            if bstack11l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥล") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣฦ") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤว")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨศ"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦษ")))
            if bstack11l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤส") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤห") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥฬ")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧอ"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧฮ")))
            if bstack11l1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧฯ") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥะ") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦั")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣา"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨำ")))
            if bstack11l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧิ") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥี") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦึ")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣื"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨุ")))
            if bstack11l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱูࠦ") in bstack11ll111l1l_opy_ or bstack11l1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱฺࠦ") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ฻")] = bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ฼"), bstack11ll111l1l_opy_.get(bstack11l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ฽")))
            if bstack11l1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣ฾") in bstack11ll111l1l_opy_:
                bstack1lll111111_opy_[bstack11l1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤ฿")] = bstack11ll111l1l_opy_[bstack11l1_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥเ")]
        except Exception as error:
            logger.error(bstack11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣแ") +  str(error))
        return bstack1lll111111_opy_