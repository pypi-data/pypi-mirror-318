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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1111ll_opy_, bstack111l11llll_opy_, bstack11ll1l11ll_opy_, bstack11l11l1l1l_opy_, bstack1llll1ll1l1_opy_, bstack1llll1ll11l_opy_, bstack111111l1ll_opy_, bstack11l1l1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1ll11ll1l1l_opy_ import bstack1ll11ll1111_opy_
import bstack_utils.bstack11llll11l_opy_ as bstack1lll1ll11l_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11l11l1l_opy_
import bstack_utils.bstack111lll111l_opy_ as bstack1lll11ll1_opy_
from bstack_utils.bstack11l1l111_opy_ import bstack11l1l111_opy_
from bstack_utils.bstack11ll111111_opy_ import bstack11l1l111l1_opy_
bstack1l1llllllll_opy_ = bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᝋ")
logger = logging.getLogger(__name__)
class bstack1ll1llllll_opy_:
    bstack1ll11ll1l1l_opy_ = None
    bs_config = None
    bstack11l1l11l_opy_ = None
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1111l111l1_opy_, stage=STAGE.SINGLE)
    def launch(cls, bs_config, bstack11l1l11l_opy_):
        cls.bs_config = bs_config
        cls.bstack11l1l11l_opy_ = bstack11l1l11l_opy_
        try:
            cls.bstack1ll1111ll1l_opy_()
            bstack111l11111l_opy_ = bstack111l1111ll_opy_(bs_config)
            bstack111l1ll111_opy_ = bstack111l11llll_opy_(bs_config)
            data = bstack1lll1ll11l_opy_.bstack1l1llllll11_opy_(bs_config, bstack11l1l11l_opy_)
            config = {
                bstack11l1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᝌ"): (bstack111l11111l_opy_, bstack111l1ll111_opy_),
                bstack11l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᝍ"): cls.default_headers()
            }
            response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᝎ"), cls.request_url(bstack11l1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠴࠲ࡦࡺ࡯࡬ࡥࡵࠪᝏ")), data, config)
            if response.status_code != 200:
                bstack1l1llll111l_opy_ = response.json()
                if bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᝐ")] == False:
                    cls.bstack1l1lllllll1_opy_(bstack1l1llll111l_opy_)
                    return
                cls.bstack1ll111111ll_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᝑ")])
                cls.bstack1l1llll1l1l_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᝒ")])
                return None
            bstack1l1lllll1l1_opy_ = cls.bstack1ll1111111l_opy_(response)
            return bstack1l1lllll1l1_opy_
        except Exception as error:
            logger.error(bstack11l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࡾࢁࠧᝓ").format(str(error)))
            return None
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def stop(cls, bstack1ll1111l11l_opy_=None):
        if not bstack1l11l11l1l_opy_.on() and not bstack1lll11ll1_opy_.on():
            return
        if os.environ.get(bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᝔")) == bstack11l1_opy_ (u"ࠤࡱࡹࡱࡲࠢ᝕") or os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᝖")) == bstack11l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᝗"):
            logger.error(bstack11l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨ᝘"))
            return {
                bstack11l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭᝙"): bstack11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᝚"),
                bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᝛"): bstack11l1_opy_ (u"ࠩࡗࡳࡰ࡫࡮࠰ࡤࡸ࡭ࡱࡪࡉࡅࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤ࠭ࠢࡥࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡱ࡮࡭ࡨࡵࠢ࡫ࡥࡻ࡫ࠠࡧࡣ࡬ࡰࡪࡪࠧ᝜")
            }
        try:
            cls.bstack1ll11ll1l1l_opy_.shutdown()
            data = {
                bstack11l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᝝"): bstack11l1l1lll_opy_()
            }
            if not bstack1ll1111l11l_opy_ is None:
                data[bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠨ᝞")] = [{
                    bstack11l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ᝟"): bstack11l1_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫᝠ"),
                    bstack11l1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧᝡ"): bstack1ll1111l11l_opy_
                }]
            config = {
                bstack11l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᝢ"): cls.default_headers()
            }
            bstack111111l111_opy_ = bstack11l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡴࡰࡲࠪᝣ").format(os.environ[bstack11l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᝤ")])
            bstack1l1lllll1ll_opy_ = cls.request_url(bstack111111l111_opy_)
            response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠫࡕ࡛ࡔࠨᝥ"), bstack1l1lllll1ll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l1_opy_ (u"࡙ࠧࡴࡰࡲࠣࡶࡪࡷࡵࡦࡵࡷࠤࡳࡵࡴࠡࡱ࡮ࠦᝦ"))
        except Exception as error:
            logger.error(bstack11l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺࠻ࠢࠥᝧ") + str(error))
            return {
                bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᝨ"): bstack11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᝩ"),
                bstack11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᝪ"): str(error)
            }
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def bstack1ll1111111l_opy_(cls, response):
        bstack1l1llll111l_opy_ = response.json()
        bstack1l1lllll1l1_opy_ = {}
        if bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠪ࡮ࡼࡺࠧᝫ")) is None:
            os.environ[bstack11l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᝬ")] = bstack11l1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ᝭")
        else:
            os.environ[bstack11l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᝮ")] = bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠧ࡫ࡹࡷࠫᝯ"), bstack11l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᝰ"))
        os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ᝱")] = bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᝲ"), bstack11l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᝳ"))
        if bstack1l11l11l1l_opy_.bstack1ll11111l1l_opy_(cls.bs_config, cls.bstack11l1l11l_opy_.get(bstack11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭᝴"), bstack11l1_opy_ (u"࠭ࠧ᝵"))) is True:
            bstack1ll11111lll_opy_, bstack1l11l1ll_opy_, bstack1ll1111ll11_opy_ = cls.bstack1l1lllll11l_opy_(bstack1l1llll111l_opy_)
            if bstack1ll11111lll_opy_ != None and bstack1l11l1ll_opy_ != None:
                bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ᝶")] = {
                    bstack11l1_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫ᝷"): bstack1ll11111lll_opy_,
                    bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ᝸"): bstack1l11l1ll_opy_,
                    bstack11l1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ᝹"): bstack1ll1111ll11_opy_
                }
            else:
                bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ᝺")] = {}
        else:
            bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᝻")] = {}
        if bstack1lll11ll1_opy_.bstack111l11l11l_opy_(cls.bs_config) is True:
            bstack1l1llll1ll1_opy_, bstack1l11l1ll_opy_ = cls.bstack1l1llll11ll_opy_(bstack1l1llll111l_opy_)
            if bstack1l1llll1ll1_opy_ != None and bstack1l11l1ll_opy_ != None:
                bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᝼")] = {
                    bstack11l1_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫ᝽"): bstack1l1llll1ll1_opy_,
                    bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ᝾"): bstack1l11l1ll_opy_,
                }
            else:
                bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᝿")] = {}
        else:
            bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪក")] = {}
        if bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫខ")].get(bstack11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧគ")) != None or bstack1l1lllll1l1_opy_[bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ឃ")].get(bstack11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩង")) != None:
            cls.bstack1ll1111lll1_opy_(bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠨ࡬ࡺࡸࠬច")), bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫឆ")))
        return bstack1l1lllll1l1_opy_
    @classmethod
    def bstack1l1lllll11l_opy_(cls, bstack1l1llll111l_opy_):
        if bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪជ")) == None:
            cls.bstack1ll111111ll_opy_()
            return [None, None, None]
        if bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫឈ")][bstack11l1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ញ")] != True:
            cls.bstack1ll111111ll_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ដ")])
            return [None, None, None]
        logger.debug(bstack11l1_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫឋ"))
        os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧឌ")] = bstack11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧឍ")
        if bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠪ࡮ࡼࡺࠧណ")):
            os.environ[bstack11l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬត")] = bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠬࡰࡷࡵࠩថ")]
            os.environ[bstack11l1_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪទ")] = json.dumps({
                bstack11l1_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩធ"): bstack111l1111ll_opy_(cls.bs_config),
                bstack11l1_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪន"): bstack111l11llll_opy_(cls.bs_config)
            })
        if bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫប")):
            os.environ[bstack11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩផ")] = bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ព")]
        if bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬភ")].get(bstack11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧម"), {}).get(bstack11l1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫយ")):
            os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩរ")] = str(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩល")][bstack11l1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫវ")][bstack11l1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨឝ")])
        return [bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠬࡰࡷࡵࠩឞ")], bstack1l1llll111l_opy_[bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨស")], os.environ[bstack11l1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨហ")]]
    @classmethod
    def bstack1l1llll11ll_opy_(cls, bstack1l1llll111l_opy_):
        if bstack1l1llll111l_opy_.get(bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨឡ")) == None:
            cls.bstack1l1llll1l1l_opy_()
            return [None, None]
        if bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩអ")][bstack11l1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫឣ")] != True:
            cls.bstack1l1llll1l1l_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫឤ")])
            return [None, None]
        if bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬឥ")].get(bstack11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧឦ")):
            logger.debug(bstack11l1_opy_ (u"ࠧࡕࡧࡶࡸࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫឧ"))
            parsed = json.loads(os.getenv(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩឨ"), bstack11l1_opy_ (u"ࠩࡾࢁࠬឩ")))
            capabilities = bstack1lll1ll11l_opy_.bstack1ll1111l111_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪឪ")][bstack11l1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬឫ")][bstack11l1_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫឬ")], bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫឭ"), bstack11l1_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ឮ"))
            bstack1l1llll1ll1_opy_ = capabilities[bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭ឯ")]
            os.environ[bstack11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧឰ")] = bstack1l1llll1ll1_opy_
            parsed[bstack11l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫឱ")] = capabilities[bstack11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬឲ")]
            os.environ[bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ឳ")] = json.dumps(parsed)
            scripts = bstack1lll1ll11l_opy_.bstack1ll1111l111_opy_(bstack1l1llll111l_opy_[bstack11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭឴")][bstack11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ឵")][bstack11l1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩា")], bstack11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧិ"), bstack11l1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࠫី"))
            bstack11l1l111_opy_.bstack111l1ll11l_opy_(scripts)
            commands = bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫឹ")][bstack11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ឺ")][bstack11l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࡕࡱ࡚ࡶࡦࡶࠧុ")].get(bstack11l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩូ"))
            bstack11l1l111_opy_.bstack111l1ll1ll_opy_(commands)
            bstack11l1l111_opy_.store()
        return [bstack1l1llll1ll1_opy_, bstack1l1llll111l_opy_[bstack11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪួ")]]
    @classmethod
    def bstack1ll111111ll_opy_(cls, response=None):
        os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧើ")] = bstack11l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨឿ")
        os.environ[bstack11l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪៀ")] = bstack11l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫេ")
        os.environ[bstack11l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧែ")] = bstack11l1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬៃ")
        os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩោ")] = bstack11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧៅ")
        os.environ[bstack11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩំ")] = bstack11l1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤះ")
        os.environ[bstack11l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ៈ")] = bstack11l1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ៉")
        cls.bstack1l1lllllll1_opy_(response, bstack11l1_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ៊"))
        return [None, None, None]
    @classmethod
    def bstack1l1llll1l1l_opy_(cls, response=None):
        os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭់")] = bstack11l1_opy_ (u"ࠩࡱࡹࡱࡲࠧ៌")
        os.environ[bstack11l1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ៍")] = bstack11l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ៎")
        os.environ[bstack11l1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭៏")] = bstack11l1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ័")
        cls.bstack1l1lllllll1_opy_(response, bstack11l1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ៑"))
        return [None, None, None]
    @classmethod
    def bstack1ll1111lll1_opy_(cls, bstack1ll111111l1_opy_, bstack1l11l1ll_opy_):
        os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕ្ࠩ")] = bstack1ll111111l1_opy_
        os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ៓")] = bstack1l11l1ll_opy_
    @classmethod
    def bstack1l1lllllll1_opy_(cls, response=None, product=bstack11l1_opy_ (u"ࠥࠦ។")):
        if response == None:
            logger.error(product + bstack11l1_opy_ (u"ࠦࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠨ៕"))
        for error in response[bstack11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ៖")]:
            bstack1llll1ll111_opy_ = error[bstack11l1_opy_ (u"࠭࡫ࡦࡻࠪៗ")]
            error_message = error[bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ៘")]
            if error_message:
                if bstack1llll1ll111_opy_ == bstack11l1_opy_ (u"ࠣࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠢ៙"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l1_opy_ (u"ࠤࡇࡥࡹࡧࠠࡶࡲ࡯ࡳࡦࡪࠠࡵࡱࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࠥ៚") + product + bstack11l1_opy_ (u"ࠥࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣ៛"))
    @classmethod
    def bstack1ll1111ll1l_opy_(cls):
        if cls.bstack1ll11ll1l1l_opy_ is not None:
            return
        cls.bstack1ll11ll1l1l_opy_ = bstack1ll11ll1111_opy_(cls.bstack1ll1111l1ll_opy_)
        cls.bstack1ll11ll1l1l_opy_.start()
    @classmethod
    def bstack11l11ll11l_opy_(cls):
        if cls.bstack1ll11ll1l1l_opy_ is None:
            return
        cls.bstack1ll11ll1l1l_opy_.shutdown()
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def bstack1ll1111l1ll_opy_(cls, bstack11l11ll111_opy_, bstack1ll11111111_opy_=bstack11l1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪៜ")):
        config = {
            bstack11l1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭៝"): cls.default_headers()
        }
        response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"࠭ࡐࡐࡕࡗࠫ៞"), cls.request_url(bstack1ll11111111_opy_), bstack11l11ll111_opy_, config)
        bstack111l11ll1l_opy_ = response.json()
    @classmethod
    def bstack11l111111l_opy_(cls, bstack11l11ll111_opy_, bstack1ll11111111_opy_=bstack11l1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭៟")):
        if not bstack1lll1ll11l_opy_.bstack1l1llll1lll_opy_(bstack11l11ll111_opy_[bstack11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ០")]):
            return
        bstack1ll11lll_opy_ = bstack1lll1ll11l_opy_.bstack1ll1111llll_opy_(bstack11l11ll111_opy_[bstack11l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭១")], bstack11l11ll111_opy_.get(bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ២")))
        if bstack1ll11lll_opy_ != None:
            if bstack11l11ll111_opy_.get(bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭៣")) != None:
                bstack11l11ll111_opy_[bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ៤")][bstack11l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ៥")] = bstack1ll11lll_opy_
            else:
                bstack11l11ll111_opy_[bstack11l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ៦")] = bstack1ll11lll_opy_
        if bstack1ll11111111_opy_ == bstack11l1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ៧"):
            cls.bstack1ll1111ll1l_opy_()
            cls.bstack1ll11ll1l1l_opy_.add(bstack11l11ll111_opy_)
        elif bstack1ll11111111_opy_ == bstack11l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ៨"):
            cls.bstack1ll1111l1ll_opy_([bstack11l11ll111_opy_], bstack1ll11111111_opy_)
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1111l1ll11_opy_, stage=STAGE.SINGLE)
    def bstack1ll11l1ll1_opy_(cls, bstack11l11lllll_opy_):
        bstack1ll1111l1l1_opy_ = []
        for log in bstack11l11lllll_opy_:
            bstack1ll11111ll1_opy_ = {
                bstack11l1_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ៩"): bstack11l1_opy_ (u"࡙ࠫࡋࡓࡕࡡࡏࡓࡌ࠭៪"),
                bstack11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ៫"): log[bstack11l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ៬")],
                bstack11l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ៭"): log[bstack11l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ៮")],
                bstack11l1_opy_ (u"ࠩ࡫ࡸࡹࡶ࡟ࡳࡧࡶࡴࡴࡴࡳࡦࠩ៯"): {},
                bstack11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ៰"): log[bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ៱")],
            }
            if bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ៲") in log:
                bstack1ll11111ll1_opy_[bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭៳")] = log[bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ៴")]
            elif bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ៵") in log:
                bstack1ll11111ll1_opy_[bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ៶")] = log[bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ៷")]
            bstack1ll1111l1l1_opy_.append(bstack1ll11111ll1_opy_)
        cls.bstack11l111111l_opy_({
            bstack11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ៸"): bstack11l1_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ៹"),
            bstack11l1_opy_ (u"࠭࡬ࡰࡩࡶࠫ៺"): bstack1ll1111l1l1_opy_
        })
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def bstack1l1llll11l1_opy_(cls, steps):
        bstack1l1llll1l11_opy_ = []
        for step in steps:
            bstack1ll11111l11_opy_ = {
                bstack11l1_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ៻"): bstack11l1_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡕࡇࡓࠫ៼"),
                bstack11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ៽"): step[bstack11l1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ៾")],
                bstack11l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ៿"): step[bstack11l1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ᠀")],
                bstack11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᠁"): step[bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᠂")],
                bstack11l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ᠃"): step[bstack11l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ᠄")]
            }
            if bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᠅") in step:
                bstack1ll11111l11_opy_[bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᠆")] = step[bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᠇")]
            elif bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᠈") in step:
                bstack1ll11111l11_opy_[bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᠉")] = step[bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᠊")]
            bstack1l1llll1l11_opy_.append(bstack1ll11111l11_opy_)
        cls.bstack11l111111l_opy_({
            bstack11l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭᠋"): bstack11l1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ᠌"),
            bstack11l1_opy_ (u"ࠫࡱࡵࡧࡴࠩ᠍"): bstack1l1llll1l11_opy_
        })
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def bstack1l1ll1111_opy_(cls, screenshot):
        cls.bstack11l111111l_opy_({
            bstack11l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ᠎"): bstack11l1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ᠏"),
            bstack11l1_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ᠐"): [{
                bstack11l1_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭᠑"): bstack11l1_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠫ᠒"),
                bstack11l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭᠓"): datetime.datetime.utcnow().isoformat() + bstack11l1_opy_ (u"ࠫ࡟࠭᠔"),
                bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭᠕"): screenshot[bstack11l1_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ᠖")],
                bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᠗"): screenshot[bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᠘")]
            }]
        }, bstack1ll11111111_opy_=bstack11l1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ᠙"))
    @classmethod
    @bstack11l11l1l1l_opy_(class_method=True)
    def bstack11ll1l1ll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11l111111l_opy_({
            bstack11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ᠚"): bstack11l1_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ᠛"),
            bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ᠜"): {
                bstack11l1_opy_ (u"ࠨࡵࡶ࡫ࡧࠦ᠝"): cls.current_test_uuid(),
                bstack11l1_opy_ (u"ࠢࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸࠨ᠞"): cls.bstack11l1ll1ll1_opy_(driver)
            }
        })
    @classmethod
    def bstack11l1ll1l11_opy_(cls, event: str, bstack11l11ll111_opy_: bstack11l1l111l1_opy_):
        bstack11l111l111_opy_ = {
            bstack11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᠟"): event,
            bstack11l11ll111_opy_.bstack11l111l1ll_opy_(): bstack11l11ll111_opy_.bstack11l1l11l11_opy_(event)
        }
        cls.bstack11l111111l_opy_(bstack11l111l111_opy_)
        result = getattr(bstack11l11ll111_opy_, bstack11l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᠠ"), None)
        if event == bstack11l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᠡ"):
            threading.current_thread().bstackTestMeta = {bstack11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᠢ"): bstack11l1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᠣ")}
        elif event == bstack11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᠤ"):
            threading.current_thread().bstackTestMeta = {bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᠥ"): getattr(result, bstack11l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᠦ"), bstack11l1_opy_ (u"ࠩࠪᠧ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᠨ"), None) is None or os.environ[bstack11l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᠩ")] == bstack11l1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᠪ")) and (os.environ.get(bstack11l1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᠫ"), None) is None or os.environ[bstack11l1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᠬ")] == bstack11l1_opy_ (u"ࠣࡰࡸࡰࡱࠨᠭ")):
            return False
        return True
    @staticmethod
    def bstack1l1lllll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1llllll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᠮ"): bstack11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᠯ"),
            bstack11l1_opy_ (u"ࠫ࡝࠳ࡂࡔࡖࡄࡇࡐ࠳ࡔࡆࡕࡗࡓࡕ࡙ࠧᠰ"): bstack11l1_opy_ (u"ࠬࡺࡲࡶࡧࠪᠱ")
        }
        if os.environ.get(bstack11l1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᠲ"), None):
            headers[bstack11l1_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᠳ")] = bstack11l1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᠴ").format(os.environ[bstack11l1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠥᠵ")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l1_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩᠶ").format(bstack1l1llllllll_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᠷ"), None)
    @staticmethod
    def bstack11l1ll1ll1_opy_(driver):
        return {
            bstack1llll1ll1l1_opy_(): bstack1llll1ll11l_opy_(driver)
        }
    @staticmethod
    def bstack1l1llllll1l_opy_(exception_info, report):
        return [{bstack11l1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᠸ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111ll111l1_opy_(typename):
        if bstack11l1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᠹ") in typename:
            return bstack11l1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᠺ")
        return bstack11l1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᠻ")