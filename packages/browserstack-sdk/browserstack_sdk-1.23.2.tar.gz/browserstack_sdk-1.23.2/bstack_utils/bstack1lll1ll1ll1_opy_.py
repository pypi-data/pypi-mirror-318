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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack111111llll_opy_
from browserstack_sdk.bstack11llll1l_opy_ import bstack11ll111ll1_opy_
def _1lll1l1ll1l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1lll1ll111l_opy_:
    def __init__(self, handler):
        self._1lll1lll1ll_opy_ = {}
        self._1lll1ll11l1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11ll111ll1_opy_.version()
        if bstack111111llll_opy_(pytest_version, bstack11l1_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢᕇ")) >= 0:
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᕈ")] = Module._register_setup_function_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᕉ")] = Module._register_setup_module_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᕊ")] = Class._register_setup_class_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᕋ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᕌ"))
            Module._register_setup_module_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᕍ"))
            Class._register_setup_class_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᕎ"))
            Class._register_setup_method_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᕏ"))
        else:
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᕐ")] = Module._inject_setup_function_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᕑ")] = Module._inject_setup_module_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᕒ")] = Class._inject_setup_class_fixture
            self._1lll1lll1ll_opy_[bstack11l1_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᕓ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᕔ"))
            Module._inject_setup_module_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᕕ"))
            Class._inject_setup_class_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᕖ"))
            Class._inject_setup_method_fixture = self.bstack1lll1l1llll_opy_(bstack11l1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᕗ"))
    def bstack1lll1ll1l1l_opy_(self, bstack1lll1ll1111_opy_, hook_type):
        bstack1lll1ll1lll_opy_ = id(bstack1lll1ll1111_opy_.__class__)
        if (bstack1lll1ll1lll_opy_, hook_type) in self._1lll1ll11l1_opy_:
            return
        meth = getattr(bstack1lll1ll1111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1lll1ll11l1_opy_[(bstack1lll1ll1lll_opy_, hook_type)] = meth
            setattr(bstack1lll1ll1111_opy_, hook_type, self.bstack1lll1ll1l11_opy_(hook_type, bstack1lll1ll1lll_opy_))
    def bstack1lll1ll11ll_opy_(self, instance, bstack1lll1lll1l1_opy_):
        if bstack1lll1lll1l1_opy_ == bstack11l1_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᕘ"):
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᕙ"))
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥᕚ"))
        if bstack1lll1lll1l1_opy_ == bstack11l1_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᕛ"):
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢᕜ"))
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦᕝ"))
        if bstack1lll1lll1l1_opy_ == bstack11l1_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᕞ"):
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤᕟ"))
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨᕠ"))
        if bstack1lll1lll1l1_opy_ == bstack11l1_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᕡ"):
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨᕢ"))
            self.bstack1lll1ll1l1l_opy_(instance.obj, bstack11l1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥᕣ"))
    @staticmethod
    def bstack1lll1l1l1ll_opy_(hook_type, func, args):
        if hook_type in [bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᕤ"), bstack11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᕥ")]:
            _1lll1l1ll1l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1lll1ll1l11_opy_(self, hook_type, bstack1lll1ll1lll_opy_):
        def bstack1lll1l1lll1_opy_(arg=None):
            self.handler(hook_type, bstack11l1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᕦ"))
            result = None
            try:
                bstack1lll1lll111_opy_ = self._1lll1ll11l1_opy_[(bstack1lll1ll1lll_opy_, hook_type)]
                self.bstack1lll1l1l1ll_opy_(hook_type, bstack1lll1lll111_opy_, (arg,))
                result = Result(result=bstack11l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᕧ"))
            except Exception as e:
                result = Result(result=bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᕨ"), exception=e)
                self.handler(hook_type, bstack11l1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᕩ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᕪ"), result)
        def bstack1lll1lll11l_opy_(this, arg=None):
            self.handler(hook_type, bstack11l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᕫ"))
            result = None
            exception = None
            try:
                self.bstack1lll1l1l1ll_opy_(hook_type, self._1lll1ll11l1_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᕬ"))
            except Exception as e:
                result = Result(result=bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᕭ"), exception=e)
                self.handler(hook_type, bstack11l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᕮ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᕯ"), result)
        if hook_type in [bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᕰ"), bstack11l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᕱ")]:
            return bstack1lll1lll11l_opy_
        return bstack1lll1l1lll1_opy_
    def bstack1lll1l1llll_opy_(self, bstack1lll1lll1l1_opy_):
        def bstack1lll1l1ll11_opy_(this, *args, **kwargs):
            self.bstack1lll1ll11ll_opy_(this, bstack1lll1lll1l1_opy_)
            self._1lll1lll1ll_opy_[bstack1lll1lll1l1_opy_](this, *args, **kwargs)
        return bstack1lll1l1ll11_opy_