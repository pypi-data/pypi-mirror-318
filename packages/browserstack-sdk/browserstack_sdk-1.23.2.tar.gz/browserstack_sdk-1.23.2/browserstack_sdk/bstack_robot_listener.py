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
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11l111ll1l_opy_ import RobotHandler
from bstack_utils.capture import bstack11l1ll11ll_opy_
from bstack_utils.bstack11ll111111_opy_ import bstack11l1l111l1_opy_, bstack11l1ll1111_opy_, bstack11l1lll11l_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11l11l1l_opy_
from bstack_utils.bstack11l1l1l111_opy_ import bstack1ll1llllll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lll1lll_opy_, bstack11l1l1lll_opy_, Result, \
    bstack11l11l1l1l_opy_, bstack11l111l11l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧຏ"): [],
        bstack11l1_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪຐ"): [],
        bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩຑ"): []
    }
    bstack111llll11l_opy_ = []
    bstack11l11l11ll_opy_ = []
    @staticmethod
    def bstack11ll1111ll_opy_(log):
        if not (log[bstack11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧຒ")] and log[bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨຓ")].strip()):
            return
        active = bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_()
        log = {
            bstack11l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧດ"): log[bstack11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨຕ")],
            bstack11l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ຖ"): bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"ࠫ࡟࠭ທ"),
            bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ຘ"): log[bstack11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧນ")],
        }
        if active:
            if active[bstack11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬບ")] == bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ປ"):
                log[bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩຜ")] = active[bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪຝ")]
            elif active[bstack11l1_opy_ (u"ࠫࡹࡿࡰࡦࠩພ")] == bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࠪຟ"):
                log[bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ຠ")] = active[bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧມ")]
        bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._111llll1l1_opy_ = None
        self._11l1l11111_opy_ = None
        self._11l1111l1l_opy_ = OrderedDict()
        self.bstack11l1llll11_opy_ = bstack11l1ll11ll_opy_(self.bstack11ll1111ll_opy_)
    @bstack11l11l1l1l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11l111ll11_opy_()
        if not self._11l1111l1l_opy_.get(attrs.get(bstack11l1_opy_ (u"ࠨ࡫ࡧࠫຢ")), None):
            self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠩ࡬ࡨࠬຣ"))] = {}
        bstack11l1l11lll_opy_ = bstack11l1lll11l_opy_(
                bstack11l11l1ll1_opy_=attrs.get(bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭຤")),
                name=name,
                bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
                file_path=os.path.relpath(attrs[bstack11l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫລ")], start=os.getcwd()) if attrs.get(bstack11l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ຦")) != bstack11l1_opy_ (u"࠭ࠧວ") else bstack11l1_opy_ (u"ࠧࠨຨ"),
                framework=bstack11l1_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧຩ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11l1_opy_ (u"ࠩ࡬ࡨࠬສ"), None)
        self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭ຫ"))][bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧຬ")] = bstack11l1l11lll_opy_
    @bstack11l11l1l1l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11l111llll_opy_()
        self._11l1111ll1_opy_(messages)
        for bstack111llllll1_opy_ in self.bstack111llll11l_opy_:
            bstack111llllll1_opy_[bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧອ")][bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬຮ")].extend(self.store[bstack11l1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭ຯ")])
            bstack1ll1llllll_opy_.bstack11l111111l_opy_(bstack111llllll1_opy_)
        self.bstack111llll11l_opy_ = []
        self.store[bstack11l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧະ")] = []
    @bstack11l11l1l1l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11l1llll11_opy_.start()
        if not self._11l1111l1l_opy_.get(attrs.get(bstack11l1_opy_ (u"ࠩ࡬ࡨࠬັ")), None):
            self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭າ"))] = {}
        driver = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪຳ"), None)
        bstack11ll111111_opy_ = bstack11l1lll11l_opy_(
            bstack11l11l1ll1_opy_=attrs.get(bstack11l1_opy_ (u"ࠬ࡯ࡤࠨິ")),
            name=name,
            bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
            file_path=os.path.relpath(attrs[bstack11l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ີ")], start=os.getcwd()),
            scope=RobotHandler.bstack11l11ll1l1_opy_(attrs.get(bstack11l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧຶ"), None)),
            framework=bstack11l1_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧື"),
            tags=attrs[bstack11l1_opy_ (u"ࠩࡷࡥ࡬ࡹຸࠧ")],
            hooks=self.store[bstack11l1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴູࠩ")],
            bstack11l1lllll1_opy_=bstack1ll1llllll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11l1_opy_ (u"ࠦࢀࢃࠠ࡝ࡰࠣࡿࢂࠨ຺").format(bstack11l1_opy_ (u"ࠧࠦࠢົ").join(attrs[bstack11l1_opy_ (u"࠭ࡴࡢࡩࡶࠫຼ")]), name) if attrs[bstack11l1_opy_ (u"ࠧࡵࡣࡪࡷࠬຽ")] else name
        )
        self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠨ࡫ࡧࠫ຾"))][bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ຿")] = bstack11ll111111_opy_
        threading.current_thread().current_test_uuid = bstack11ll111111_opy_.bstack11l11l11l1_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭ເ"), None)
        self.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬແ"), bstack11ll111111_opy_)
    @bstack11l11l1l1l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11l1llll11_opy_.reset()
        bstack11l1111l11_opy_ = bstack11l111lll1_opy_.get(attrs.get(bstack11l1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬໂ")), bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧໃ"))
        self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠧࡪࡦࠪໄ"))][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ໅")].stop(time=bstack11l1l1lll_opy_(), duration=int(attrs.get(bstack11l1_opy_ (u"ࠩࡨࡰࡦࡶࡳࡦࡦࡷ࡭ࡲ࡫ࠧໆ"), bstack11l1_opy_ (u"ࠪ࠴ࠬ໇"))), result=Result(result=bstack11l1111l11_opy_, exception=attrs.get(bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩ່ࠬ")), bstack11l1lll111_opy_=[attrs.get(bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ້࠭"))]))
        self.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ໊"), self._11l1111l1l_opy_[attrs.get(bstack11l1_opy_ (u"ࠧࡪࡦ໋ࠪ"))][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ໌")], True)
        self.store[bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ໍ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11l11l1l1l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11l111ll11_opy_()
        current_test_id = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬ໎"), None)
        bstack111lllll1l_opy_ = current_test_id if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡩ࠭໏"), None) else bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡶ࡫ࡷࡩࡤ࡯ࡤࠨ໐"), None)
        if attrs.get(bstack11l1_opy_ (u"࠭ࡴࡺࡲࡨࠫ໑"), bstack11l1_opy_ (u"ࠧࠨ໒")).lower() in [bstack11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ໓"), bstack11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ໔")]:
            hook_type = bstack11l1111111_opy_(attrs.get(bstack11l1_opy_ (u"ࠪࡸࡾࡶࡥࠨ໕")), bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ໖"), None))
            hook_name = bstack11l1_opy_ (u"ࠬࢁࡽࠨ໗").format(attrs.get(bstack11l1_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭໘"), bstack11l1_opy_ (u"ࠧࠨ໙")))
            if hook_type in [bstack11l1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬ໚"), bstack11l1_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬ໛")]:
                hook_name = bstack11l1_opy_ (u"ࠪ࡟ࢀࢃ࡝ࠡࡽࢀࠫໜ").format(bstack11l11l1l11_opy_.get(hook_type), attrs.get(bstack11l1_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫໝ"), bstack11l1_opy_ (u"ࠬ࠭ໞ")))
            bstack111lllllll_opy_ = bstack11l1ll1111_opy_(
                bstack11l11l1ll1_opy_=bstack111lllll1l_opy_ + bstack11l1_opy_ (u"࠭࠭ࠨໟ") + attrs.get(bstack11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬ໠"), bstack11l1_opy_ (u"ࠨࠩ໡")).lower(),
                name=hook_name,
                bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໢")), start=os.getcwd()),
                framework=bstack11l1_opy_ (u"ࠪࡖࡴࡨ࡯ࡵࠩ໣"),
                tags=attrs[bstack11l1_opy_ (u"ࠫࡹࡧࡧࡴࠩ໤")],
                scope=RobotHandler.bstack11l11ll1l1_opy_(attrs.get(bstack11l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ໥"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack111lllllll_opy_.bstack11l11l11l1_opy_()
            threading.current_thread().current_hook_id = bstack111lllll1l_opy_ + bstack11l1_opy_ (u"࠭࠭ࠨ໦") + attrs.get(bstack11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬ໧"), bstack11l1_opy_ (u"ࠨࠩ໨")).lower()
            self.store[bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭໩")] = [bstack111lllllll_opy_.bstack11l11l11l1_opy_()]
            if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ໪"), None):
                self.store[bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࠨ໫")].append(bstack111lllllll_opy_.bstack11l11l11l1_opy_())
            else:
                self.store[bstack11l1_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ໬")].append(bstack111lllllll_opy_.bstack11l11l11l1_opy_())
            if bstack111lllll1l_opy_:
                self._11l1111l1l_opy_[bstack111lllll1l_opy_ + bstack11l1_opy_ (u"࠭࠭ࠨ໭") + attrs.get(bstack11l1_opy_ (u"ࠧࡵࡻࡳࡩࠬ໮"), bstack11l1_opy_ (u"ࠨࠩ໯")).lower()] = { bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ໰"): bstack111lllllll_opy_ }
            bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ໱"), bstack111lllllll_opy_)
        else:
            bstack11l1l1ll1l_opy_ = {
                bstack11l1_opy_ (u"ࠫ࡮ࡪࠧ໲"): uuid4().__str__(),
                bstack11l1_opy_ (u"ࠬࡺࡥࡹࡶࠪ໳"): bstack11l1_opy_ (u"࠭ࡻࡾࠢࡾࢁࠬ໴").format(attrs.get(bstack11l1_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧ໵")), attrs.get(bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭໶"), bstack11l1_opy_ (u"ࠩࠪ໷"))) if attrs.get(bstack11l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ໸"), []) else attrs.get(bstack11l1_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫ໹")),
                bstack11l1_opy_ (u"ࠬࡹࡴࡦࡲࡢࡥࡷ࡭ࡵ࡮ࡧࡱࡸࠬ໺"): attrs.get(bstack11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ໻"), []),
                bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ໼"): bstack11l1l1lll_opy_(),
                bstack11l1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ໽"): bstack11l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ໾"),
                bstack11l1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ໿"): attrs.get(bstack11l1_opy_ (u"ࠫࡩࡵࡣࠨༀ"), bstack11l1_opy_ (u"ࠬ࠭༁"))
            }
            if attrs.get(bstack11l1_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࠧ༂"), bstack11l1_opy_ (u"ࠧࠨ༃")) != bstack11l1_opy_ (u"ࠨࠩ༄"):
                bstack11l1l1ll1l_opy_[bstack11l1_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪ༅")] = attrs.get(bstack11l1_opy_ (u"ࠪࡰ࡮ࡨ࡮ࡢ࡯ࡨࠫ༆"))
            if not self.bstack11l11l11ll_opy_:
                self._11l1111l1l_opy_[self._111llll111_opy_()][bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ༇")].add_step(bstack11l1l1ll1l_opy_)
                threading.current_thread().current_step_uuid = bstack11l1l1ll1l_opy_[bstack11l1_opy_ (u"ࠬ࡯ࡤࠨ༈")]
            self.bstack11l11l11ll_opy_.append(bstack11l1l1ll1l_opy_)
    @bstack11l11l1l1l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11l111llll_opy_()
        self._11l1111ll1_opy_(messages)
        current_test_id = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨ༉"), None)
        bstack111lllll1l_opy_ = current_test_id if current_test_id else bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡸ࡭ࡹ࡫࡟ࡪࡦࠪ༊"), None)
        bstack11l11l1lll_opy_ = bstack11l111lll1_opy_.get(attrs.get(bstack11l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ་")), bstack11l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ༌"))
        bstack11l1l1111l_opy_ = attrs.get(bstack11l1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ།"))
        if bstack11l11l1lll_opy_ != bstack11l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ༎") and not attrs.get(bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭༏")) and self._111llll1l1_opy_:
            bstack11l1l1111l_opy_ = self._111llll1l1_opy_
        bstack11l1lll1ll_opy_ = Result(result=bstack11l11l1lll_opy_, exception=bstack11l1l1111l_opy_, bstack11l1lll111_opy_=[bstack11l1l1111l_opy_])
        if attrs.get(bstack11l1_opy_ (u"࠭ࡴࡺࡲࡨࠫ༐"), bstack11l1_opy_ (u"ࠧࠨ༑")).lower() in [bstack11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ༒"), bstack11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ༓")]:
            bstack111lllll1l_opy_ = current_test_id if current_test_id else bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭༔"), None)
            if bstack111lllll1l_opy_:
                bstack11l1ll1l1l_opy_ = bstack111lllll1l_opy_ + bstack11l1_opy_ (u"ࠦ࠲ࠨ༕") + attrs.get(bstack11l1_opy_ (u"ࠬࡺࡹࡱࡧࠪ༖"), bstack11l1_opy_ (u"࠭ࠧ༗")).lower()
                self._11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣ༘ࠪ")].stop(time=bstack11l1l1lll_opy_(), duration=int(attrs.get(bstack11l1_opy_ (u"ࠨࡧ࡯ࡥࡵࡹࡥࡥࡶ࡬ࡱࡪ༙࠭"), bstack11l1_opy_ (u"ࠩ࠳ࠫ༚"))), result=bstack11l1lll1ll_opy_)
                bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ༛"), self._11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ༜")])
        else:
            bstack111lllll1l_opy_ = current_test_id if current_test_id else bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣ࡮ࡪࠧ༝"), None)
            if bstack111lllll1l_opy_ and len(self.bstack11l11l11ll_opy_) == 1:
                current_step_uuid = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡶࡨࡴࡤࡻࡵࡪࡦࠪ༞"), None)
                self._11l1111l1l_opy_[bstack111lllll1l_opy_][bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ༟")].bstack11l1l1llll_opy_(current_step_uuid, duration=int(attrs.get(bstack11l1_opy_ (u"ࠨࡧ࡯ࡥࡵࡹࡥࡥࡶ࡬ࡱࡪ࠭༠"), bstack11l1_opy_ (u"ࠩ࠳ࠫ༡"))), result=bstack11l1lll1ll_opy_)
            else:
                self.bstack11l11llll1_opy_(attrs)
            self.bstack11l11l11ll_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11l1_opy_ (u"ࠪ࡬ࡹࡳ࡬ࠨ༢"), bstack11l1_opy_ (u"ࠫࡳࡵࠧ༣")) == bstack11l1_opy_ (u"ࠬࡿࡥࡴࠩ༤"):
                return
            self.messages.push(message)
            bstack11l11lllll_opy_ = []
            if bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_():
                bstack11l11lllll_opy_.append({
                    bstack11l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ༥"): bstack11l1l1lll_opy_(),
                    bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ༦"): message.get(bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ༧")),
                    bstack11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ༨"): message.get(bstack11l1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ༩")),
                    **bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_()
                })
                if len(bstack11l11lllll_opy_) > 0:
                    bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_(bstack11l11lllll_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1ll1llllll_opy_.bstack11l11ll11l_opy_()
    def bstack11l11llll1_opy_(self, bstack111llll1ll_opy_):
        if not bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_():
            return
        kwname = bstack11l1_opy_ (u"ࠫࢀࢃࠠࡼࡿࠪ༪").format(bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬ༫")), bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ༬"), bstack11l1_opy_ (u"ࠧࠨ༭"))) if bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭༮"), []) else bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩ༯"))
        error_message = bstack11l1_opy_ (u"ࠥ࡯ࡼࡴࡡ࡮ࡧ࠽ࠤࡡࠨࡻ࠱ࡿ࡟ࠦࠥࢂࠠࡴࡶࡤࡸࡺࡹ࠺ࠡ࡞ࠥࡿ࠶ࢃ࡜ࠣࠢࡿࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡ࡞ࠥࡿ࠷ࢃ࡜ࠣࠤ༰").format(kwname, bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ༱")), str(bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭༲"))))
        bstack11l11lll11_opy_ = bstack11l1_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠧ༳").format(kwname, bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ༴")))
        bstack11l1111lll_opy_ = error_message if bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦ༵ࠩ")) else bstack11l11lll11_opy_
        bstack11l11111l1_opy_ = {
            bstack11l1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ༶"): self.bstack11l11l11ll_opy_[-1].get(bstack11l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺ༷ࠧ"), bstack11l1l1lll_opy_()),
            bstack11l1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༸"): bstack11l1111lll_opy_,
            bstack11l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯༹ࠫ"): bstack11l1_opy_ (u"࠭ࡅࡓࡔࡒࡖࠬ༺") if bstack111llll1ll_opy_.get(bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ༻")) == bstack11l1_opy_ (u"ࠨࡈࡄࡍࡑ࠭༼") else bstack11l1_opy_ (u"ࠩࡌࡒࡋࡕࠧ༽"),
            **bstack1l11l11l1l_opy_.bstack11l1ll111l_opy_()
        }
        bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_([bstack11l11111l1_opy_])
    def _111llll111_opy_(self):
        for bstack11l11l1ll1_opy_ in reversed(self._11l1111l1l_opy_):
            bstack111lll1lll_opy_ = bstack11l11l1ll1_opy_
            data = self._11l1111l1l_opy_[bstack11l11l1ll1_opy_][bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭༾")]
            if isinstance(data, bstack11l1ll1111_opy_):
                if not bstack11l1_opy_ (u"ࠫࡊࡇࡃࡉࠩ༿") in data.bstack11l111l1l1_opy_():
                    return bstack111lll1lll_opy_
            else:
                return bstack111lll1lll_opy_
    def _11l1111ll1_opy_(self, messages):
        try:
            bstack111lllll11_opy_ = BuiltIn().get_variable_value(bstack11l1_opy_ (u"ࠧࠪࡻࡍࡑࡊࠤࡑࡋࡖࡆࡎࢀࠦཀ")) in (bstack11l1l111ll_opy_.DEBUG, bstack11l1l111ll_opy_.TRACE)
            for message, bstack11l1l11l1l_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11l1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧཁ"))
                level = message.get(bstack11l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ག"))
                if level == bstack11l1l111ll_opy_.FAIL:
                    self._111llll1l1_opy_ = name or self._111llll1l1_opy_
                    self._11l1l11111_opy_ = bstack11l1l11l1l_opy_.get(bstack11l1_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤགྷ")) if bstack111lllll11_opy_ and bstack11l1l11l1l_opy_ else self._11l1l11111_opy_
        except:
            pass
    @classmethod
    def bstack11l1ll1l11_opy_(self, event: str, bstack11l11ll111_opy_: bstack11l1l111l1_opy_, bstack11l11111ll_opy_=False):
        if event == bstack11l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫང"):
            bstack11l11ll111_opy_.set(hooks=self.store[bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧཅ")])
        if event == bstack11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬཆ"):
            event = bstack11l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧཇ")
        if bstack11l11111ll_opy_:
            bstack11l111l111_opy_ = {
                bstack11l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ཈"): event,
                bstack11l11ll111_opy_.bstack11l111l1ll_opy_(): bstack11l11ll111_opy_.bstack11l1l11l11_opy_(event)
            }
            self.bstack111llll11l_opy_.append(bstack11l111l111_opy_)
        else:
            bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(event, bstack11l11ll111_opy_)
class Messages:
    def __init__(self):
        self._11l11lll1l_opy_ = []
    def bstack11l111ll11_opy_(self):
        self._11l11lll1l_opy_.append([])
    def bstack11l111llll_opy_(self):
        return self._11l11lll1l_opy_.pop() if self._11l11lll1l_opy_ else list()
    def push(self, message):
        self._11l11lll1l_opy_[-1].append(message) if self._11l11lll1l_opy_ else self._11l11lll1l_opy_.append([message])
class bstack11l1l111ll_opy_:
    FAIL = bstack11l1_opy_ (u"ࠧࡇࡃࡌࡐࠬཉ")
    ERROR = bstack11l1_opy_ (u"ࠨࡇࡕࡖࡔࡘࠧཊ")
    WARNING = bstack11l1_opy_ (u"࡚ࠩࡅࡗࡔࠧཋ")
    bstack11l1l11ll1_opy_ = bstack11l1_opy_ (u"ࠪࡍࡓࡌࡏࠨཌ")
    DEBUG = bstack11l1_opy_ (u"ࠫࡉࡋࡂࡖࡉࠪཌྷ")
    TRACE = bstack11l1_opy_ (u"࡚ࠬࡒࡂࡅࡈࠫཎ")
    bstack11l11ll1ll_opy_ = [FAIL, ERROR]
def bstack11l11l111l_opy_(bstack11l11l1111_opy_):
    if not bstack11l11l1111_opy_:
        return None
    if bstack11l11l1111_opy_.get(bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩཏ"), None):
        return getattr(bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪཐ")], bstack11l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ད"), None)
    return bstack11l11l1111_opy_.get(bstack11l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧདྷ"), None)
def bstack11l1111111_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩན"), bstack11l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭པ")]:
        return
    if hook_type.lower() == bstack11l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫཕ"):
        if current_test_uuid is None:
            return bstack11l1_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪབ")
        else:
            return bstack11l1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬབྷ")
    elif hook_type.lower() == bstack11l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪམ"):
        if current_test_uuid is None:
            return bstack11l1_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬཙ")
        else:
            return bstack11l1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧཚ")