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
import os
import logging
from uuid import uuid4
from bstack_utils.bstack11ll111111_opy_ import bstack11l1ll1111_opy_, bstack11l1lll11l_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11l11l1l_opy_
from bstack_utils.helper import bstack1l1lll1lll_opy_, bstack11l1l1lll_opy_, Result
from bstack_utils.bstack11l1l1l111_opy_ import bstack1ll1llllll_opy_
from bstack_utils.capture import bstack11l1ll11ll_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack1111111l1_opy_:
    def __init__(self):
        self.bstack11l1llll11_opy_ = bstack11l1ll11ll_opy_(self.bstack11ll1111ll_opy_)
        self.tests = {}
    @staticmethod
    def bstack11ll1111ll_opy_(log):
        if not (log[bstack11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫโ")] and log[bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬใ")].strip()):
            return
        active = bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_()
        log = {
            bstack11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫไ"): log[bstack11l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬๅ")],
            bstack11l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪๆ"): bstack11l1l1lll_opy_(),
            bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ็"): log[bstack11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧ่ࠪ")],
        }
        if active:
            if active[bstack11l1_opy_ (u"ࠪࡸࡾࡶࡥࠨ้")] == bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬๊ࠩ"):
                log[bstack11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨ๋ࠬ")] = active[bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭์")]
            elif active[bstack11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬํ")] == bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭๎"):
                log[bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๏")] = active[bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ๐")]
        bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_([log])
    def start_test(self, attrs):
        bstack11l1llll1l_opy_ = uuid4().__str__()
        self.tests[bstack11l1llll1l_opy_] = {}
        self.bstack11l1llll11_opy_.start()
        driver = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ๑"), None)
        bstack11ll111111_opy_ = bstack11l1lll11l_opy_(
            name=attrs.scenario.name,
            uuid=bstack11l1llll1l_opy_,
            bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11l1_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨ๒"),
            framework=bstack11l1_opy_ (u"࠭ࡂࡦࡪࡤࡺࡪ࠭๓"),
            scope=[attrs.feature.name],
            bstack11l1lllll1_opy_=bstack1ll1llllll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[bstack11l1llll1l_opy_][bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ๔")] = bstack11ll111111_opy_
        threading.current_thread().current_test_uuid = bstack11l1llll1l_opy_
        bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ๕"), bstack11ll111111_opy_)
    def end_test(self, attrs):
        bstack11ll1111l1_opy_ = {
            bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ๖"): attrs.feature.name,
            bstack11l1_opy_ (u"ࠥࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣ๗"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack11ll111111_opy_ = self.tests[current_test_uuid][bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ๘")]
        meta = {
            bstack11l1_opy_ (u"ࠧ࡬ࡥࡢࡶࡸࡶࡪࠨ๙"): bstack11ll1111l1_opy_,
            bstack11l1_opy_ (u"ࠨࡳࡵࡧࡳࡷࠧ๚"): bstack11ll111111_opy_.meta.get(bstack11l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭๛"), []),
            bstack11l1_opy_ (u"ࠣࡵࡦࡩࡳࡧࡲࡪࡱࠥ๜"): {
                bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ๝"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack11ll111111_opy_.bstack11l1l1l1l1_opy_(meta)
        bstack11ll111111_opy_.bstack11l1lll1l1_opy_(bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࠨ๞"), []))
        bstack11l1l1l1ll_opy_, exception = self._11l1llllll_opy_(attrs)
        bstack11l1lll1ll_opy_ = Result(result=attrs.status.name, exception=exception, bstack11l1lll111_opy_=[bstack11l1l1l1ll_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ๟")].stop(time=bstack11l1l1lll_opy_(), duration=int(attrs.duration)*1000, result=bstack11l1lll1ll_opy_)
        bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ๠"), self.tests[threading.current_thread().current_test_uuid][bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ๡")])
    def bstack1ll111ll1_opy_(self, attrs):
        bstack11l1l1ll1l_opy_ = {
            bstack11l1_opy_ (u"ࠧࡪࡦࠪ๢"): uuid4().__str__(),
            bstack11l1_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩ๣"): attrs.keyword,
            bstack11l1_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩ๤"): [],
            bstack11l1_opy_ (u"ࠪࡸࡪࡾࡴࠨ๥"): attrs.name,
            bstack11l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ๦"): bstack11l1l1lll_opy_(),
            bstack11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ๧"): bstack11l1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ๨"),
            bstack11l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ๩"): bstack11l1_opy_ (u"ࠨࠩ๪")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ๫")].add_step(bstack11l1l1ll1l_opy_)
        threading.current_thread().current_step_uuid = bstack11l1l1ll1l_opy_[bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭๬")]
    def bstack1l11l1l1ll_opy_(self, attrs):
        current_test_id = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ๭"), None)
        current_step_uuid = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡵࡧࡳࡣࡺࡻࡩࡥࠩ๮"), None)
        bstack11l1l1l1ll_opy_, exception = self._11l1llllll_opy_(attrs)
        bstack11l1lll1ll_opy_ = Result(result=attrs.status.name, exception=exception, bstack11l1lll111_opy_=[bstack11l1l1l1ll_opy_])
        self.tests[current_test_id][bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ๯")].bstack11l1l1llll_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack11l1lll1ll_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack1ll11ll11l_opy_(self, name, attrs):
        try:
            bstack11ll11111l_opy_ = uuid4().__str__()
            self.tests[bstack11ll11111l_opy_] = {}
            self.bstack11l1llll11_opy_.start()
            scopes = []
            driver = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭๰"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭๱")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11ll11111l_opy_)
            if name in [bstack11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ๲"), bstack11l1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡤࡰࡱࠨ๳")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ๴"), bstack11l1_opy_ (u"ࠧࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ๵")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11l1_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧ๶")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack11l1ll1111_opy_(
                name=name,
                uuid=bstack11ll11111l_opy_,
                bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
                file_path=file_path,
                framework=bstack11l1_opy_ (u"ࠢࡃࡧ࡫ࡥࡻ࡫ࠢ๷"),
                bstack11l1lllll1_opy_=bstack1ll1llllll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11l1_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤ๸"),
                hook_type=name
            )
            self.tests[bstack11ll11111l_opy_][bstack11l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠧ๹")] = hook_data
            current_test_id = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠥࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠢ๺"), None)
            if current_test_id:
                hook_data.bstack11l1ll11l1_opy_(current_test_id)
            if name == bstack11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ๻"):
                threading.current_thread().before_all_hook_uuid = bstack11ll11111l_opy_
            threading.current_thread().current_hook_uuid = bstack11ll11111l_opy_
            bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩࠨ๼"), hook_data)
        except Exception as e:
            logger.debug(bstack11l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡪࡰࠣࡷࡹࡧࡲࡵࠢ࡫ࡳࡴࡱࠠࡦࡸࡨࡲࡹࡹࠬࠡࡪࡲࡳࡰࠦ࡮ࡢ࡯ࡨ࠾ࠥࠫࡳ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠨࡷࠧ๽"), name, e)
    def bstack1lll11l1ll_opy_(self, attrs):
        bstack11l1ll1l1l_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ๾"), None)
        hook_data = self.tests[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ๿")]
        status = bstack11l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ຀")
        exception = None
        bstack11l1l1l1ll_opy_ = None
        if hook_data.name == bstack11l1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡡࡤࡰࡱࠨກ"):
            self.bstack11l1llll11_opy_.reset()
            bstack11l1l1ll11_opy_ = self.tests[bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫຂ"), None)][bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ຃")].result.result
            if bstack11l1l1ll11_opy_ == bstack11l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨຄ"):
                if attrs.hook_failures == 1:
                    status = bstack11l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ຅")
                elif attrs.hook_failures == 2:
                    status = bstack11l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣຆ")
            elif attrs.bstack11l1ll1lll_opy_:
                status = bstack11l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤງ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧຈ") and attrs.hook_failures == 1:
                status = bstack11l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦຉ")
            elif hasattr(attrs, bstack11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬຊ")) and attrs.error_message:
                status = bstack11l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ຋")
            bstack11l1l1l1ll_opy_, exception = self._11l1llllll_opy_(attrs)
        bstack11l1lll1ll_opy_ = Result(result=status, exception=exception, bstack11l1lll111_opy_=[bstack11l1l1l1ll_opy_])
        hook_data.stop(time=bstack11l1l1lll_opy_(), duration=0, result=bstack11l1lll1ll_opy_)
        bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩຌ"), self.tests[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫຍ")])
        threading.current_thread().current_hook_uuid = None
    def _11l1llllll_opy_(self, attrs):
        try:
            import traceback
            bstack1l1l1l1l_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1l1l1ll_opy_ = bstack1l1l1l1l_opy_[-1] if bstack1l1l1l1l_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡷࡧࡣࡦࡤࡤࡧࡰࠨຎ"))
            bstack11l1l1l1ll_opy_ = None
            exception = None
        return bstack11l1l1l1ll_opy_, exception