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
import threading
from bstack_utils.helper import bstack1111ll1l1_opy_
from bstack_utils.constants import bstack1111l1lll1_opy_, EVENTS, STAGE
from bstack_utils.bstack11llll11_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11l11l1l_opy_:
    bstack1ll11ll1l1l_opy_ = None
    @classmethod
    def bstack111l1l11_opy_(cls):
        if cls.on():
            logger.info(
                bstack11l1_opy_ (u"ࠨࡘ࡬ࡷ࡮ࡺࠠࡩࡶࡷࡴࡸࡀ࠯࠰ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠫ᡺").format(os.environ[bstack11l1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣ᡻")]))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫ᡼"), None) is None or os.environ[bstack11l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬ᡽")] == bstack11l1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ᡾"):
            return False
        return True
    @classmethod
    def bstack1l1lll1l1ll_opy_(cls, bs_config, framework=bstack11l1_opy_ (u"ࠨࠢ᡿")):
        bstack1l1lll1111l_opy_ = False
        for fw in bstack1111l1lll1_opy_:
            if fw in framework:
                bstack1l1lll1111l_opy_ = True
        return bstack1111ll1l1_opy_(bs_config.get(bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᢀ"), bstack1l1lll1111l_opy_))
    @classmethod
    def bstack1l1lll111ll_opy_(cls, framework):
        return framework in bstack1111l1lll1_opy_
    @classmethod
    def bstack1ll11111l1l_opy_(cls, bs_config, framework):
        return cls.bstack1l1lll1l1ll_opy_(bs_config, framework) is True and cls.bstack1l1lll111ll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᢁ"), None)
    @staticmethod
    def bstack11l1ll111l_opy_():
        if getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᢂ"), None):
            return {
                bstack11l1_opy_ (u"ࠪࡸࡾࡶࡥࠨᢃ"): bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᢄ"),
                bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᢅ"): getattr(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᢆ"), None)
            }
        if getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᢇ"), None):
            return {
                bstack11l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᢈ"): bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᢉ"),
                bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᢊ"): getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᢋ"), None)
            }
        return None
    @staticmethod
    def bstack1l1ll1lllll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l11l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11l11ll1l1_opy_(test, hook_name=None):
        bstack1l1lll11l11_opy_ = test.parent
        if hook_name in [bstack11l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᢌ"), bstack11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᢍ"), bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᢎ"), bstack11l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᢏ")]:
            bstack1l1lll11l11_opy_ = test
        scope = []
        while bstack1l1lll11l11_opy_ is not None:
            scope.append(bstack1l1lll11l11_opy_.name)
            bstack1l1lll11l11_opy_ = bstack1l1lll11l11_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1l1lll11111_opy_(hook_type):
        if hook_type == bstack11l1_opy_ (u"ࠤࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠢᢐ"):
            return bstack11l1_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢ࡫ࡳࡴࡱࠢᢑ")
        elif hook_type == bstack11l1_opy_ (u"ࠦࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠣᢒ"):
            return bstack11l1_opy_ (u"࡚ࠧࡥࡢࡴࡧࡳࡼࡴࠠࡩࡱࡲ࡯ࠧᢓ")
    @staticmethod
    def bstack1l1lll11l1l_opy_(bstack1lll111ll_opy_):
        try:
            if not bstack1l11l11l1l_opy_.on():
                return bstack1lll111ll_opy_
            if os.environ.get(bstack11l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠦᢔ"), None) == bstack11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧᢕ"):
                tests = os.environ.get(bstack11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠧᢖ"), None)
                if tests is None or tests == bstack11l1_opy_ (u"ࠤࡱࡹࡱࡲࠢᢗ"):
                    return bstack1lll111ll_opy_
                bstack1lll111ll_opy_ = tests.split(bstack11l1_opy_ (u"ࠪ࠰ࠬᢘ"))
                return bstack1lll111ll_opy_
        except Exception as exc:
            logger.debug(bstack1l1lll111l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡪࡸࡵ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡴ࠽ࠤࢀࡹࡴࡳࠪࡨࡼࡨ࠯ࡽࠣᢙ"))
        return bstack1lll111ll_opy_