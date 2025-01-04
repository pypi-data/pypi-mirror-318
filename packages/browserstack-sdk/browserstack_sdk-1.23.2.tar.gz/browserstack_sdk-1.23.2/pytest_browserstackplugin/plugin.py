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
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1ll111l1_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11ll1l11l_opy_, bstack1ll1llll1_opy_, update, bstack1lll11llll_opy_,
                                       bstack1l11llll1_opy_, bstack11111ll1_opy_, bstack1l1lllll_opy_, bstack1ll11llll_opy_,
                                       bstack1l11lll1l1_opy_, bstack11l111lll_opy_, bstack111l1111_opy_, bstack1l1l1l1l1l_opy_,
                                       bstack1ll1ll11ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll11l1l11_opy_)
from browserstack_sdk.bstack11llll1l_opy_ import bstack11ll111ll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11llll11_opy_
from bstack_utils.capture import bstack11l1ll11ll_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1llll1111l_opy_, bstack1l1ll11ll_opy_, bstack1l11ll11ll_opy_, \
    bstack1l1l1l11l1_opy_
from bstack_utils.helper import bstack1l1lll1lll_opy_, bstack11111l111l_opy_, bstack11l111l11l_opy_, bstack1llll1lll1_opy_, bstack1llllll11l1_opy_, bstack11l1l1lll_opy_, \
    bstack1llll1ll1ll_opy_, \
    bstack1llll1l11ll_opy_, bstack1l1lll11ll_opy_, bstack1llll1ll1l_opy_, bstack1llll111ll1_opy_, bstack1l1lll111l_opy_, Notset, \
    bstack1l11l1l1_opy_, bstack1llllll1lll_opy_, bstack1llllllll1l_opy_, Result, bstack1llll1lllll_opy_, bstack1lll1llll1l_opy_, bstack11l11l1l1l_opy_, \
    bstack1lll1ll111_opy_, bstack11lll1ll1_opy_, bstack1111ll1l1_opy_, bstack11111l1111_opy_
from bstack_utils.bstack1lll1ll1ll1_opy_ import bstack1lll1ll111l_opy_
from bstack_utils.messages import bstack1lll1l1ll1_opy_, bstack11ll1l11l1_opy_, bstack1lll1lll1_opy_, bstack1l1l1ll11_opy_, bstack1ll11111ll_opy_, \
    bstack11ll11llll_opy_, bstack1l1l11lll_opy_, bstack1lll1l1lll_opy_, bstack11l1l1ll1_opy_, bstack1111ll1ll_opy_, \
    bstack1l111l1l1_opy_, bstack1l11l1ll1_opy_
from bstack_utils.proxy import bstack1ll11ll111_opy_, bstack1l1111l1ll_opy_
from bstack_utils.bstack1l1llll1l1_opy_ import bstack1ll1l111l11_opy_, bstack1ll11lll111_opy_, bstack1ll11lllll1_opy_, bstack1ll1l11111l_opy_, \
    bstack1ll11llllll_opy_, bstack1ll11ll1lll_opy_, bstack1ll11llll11_opy_, bstack1ll1l11l11_opy_, bstack1ll11lll1ll_opy_
from bstack_utils.bstack1111l1111_opy_ import bstack11l1ll1l_opy_
from bstack_utils.bstack1llllll1ll_opy_ import bstack1llll1l1l1_opy_, bstack1lll1lll11_opy_, bstack1l1l111l1_opy_, \
    bstack11l1111ll_opy_, bstack1lll1l11ll_opy_
from bstack_utils.bstack11ll111111_opy_ import bstack11l1lll11l_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11l11l1l_opy_
import bstack_utils.bstack111lll111l_opy_ as bstack1lll11ll1_opy_
from bstack_utils.bstack11l1l1l111_opy_ import bstack1ll1llllll_opy_
from bstack_utils.bstack11l1l111_opy_ import bstack11l1l111_opy_
from browserstack_sdk.__init__ import bstack1lll11l1_opy_
bstack1lll1111l_opy_ = None
bstack1ll1l111l1_opy_ = None
bstack111l11l1_opy_ = None
bstack11llllll1l_opy_ = None
bstack1l1l1l111_opy_ = None
bstack1ll1111l1l_opy_ = None
bstack111ll1lll_opy_ = None
bstack1ll1l1lll1_opy_ = None
bstack11llll1ll1_opy_ = None
bstack1ll1l11l_opy_ = None
bstack11ll111l_opy_ = None
bstack1ll1111l11_opy_ = None
bstack1lllll11_opy_ = None
bstack1llll11l1l_opy_ = bstack11l1_opy_ (u"ࠬ࠭ᢚ")
CONFIG = {}
bstack11llll1l1l_opy_ = False
bstack1l11l1l1l_opy_ = bstack11l1_opy_ (u"࠭ࠧᢛ")
bstack1ll1lllll_opy_ = bstack11l1_opy_ (u"ࠧࠨᢜ")
bstack1l1ll11l11_opy_ = False
bstack1ll111l111_opy_ = []
bstack1ll1ll1ll_opy_ = bstack1llll1111l_opy_
bstack1l1ll11l111_opy_ = bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᢝ")
bstack1l111ll1l1_opy_ = {}
bstack1l111l111_opy_ = None
bstack1lll11lll_opy_ = False
logger = bstack11llll11_opy_.get_logger(__name__, bstack1ll1ll1ll_opy_)
store = {
    bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᢞ"): []
}
bstack1l1ll1ll1ll_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11l1111l1l_opy_ = {}
current_test_uuid = None
def bstack1ll11lll11_opy_(page, bstack11ll1111_opy_):
    try:
        page.evaluate(bstack11l1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᢟ"),
                      bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨᢠ") + json.dumps(
                          bstack11ll1111_opy_) + bstack11l1_opy_ (u"ࠧࢃࡽࠣᢡ"))
    except Exception as e:
        print(bstack11l1_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦᢢ"), e)
def bstack1llllll11_opy_(page, message, level):
    try:
        page.evaluate(bstack11l1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᢣ"), bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ᢤ") + json.dumps(
            message) + bstack11l1_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬᢥ") + json.dumps(level) + bstack11l1_opy_ (u"ࠪࢁࢂ࠭ᢦ"))
    except Exception as e:
        print(bstack11l1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢᢧ"), e)
def pytest_configure(config):
    bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
    config.args = bstack1l11l11l1l_opy_.bstack1l1lll11l1l_opy_(config.args)
    bstack1l1l1lll1_opy_.bstack111111ll1_opy_(bstack1111ll1l1_opy_(config.getoption(bstack11l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᢨ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1l1ll1ll111_opy_ = item.config.getoption(bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᢩ"))
    plugins = item.config.getoption(bstack11l1_opy_ (u"ࠢࡱ࡮ࡸ࡫࡮ࡴࡳࠣᢪ"))
    report = outcome.get_result()
    bstack1l1ll111ll1_opy_(item, call, report)
    if bstack11l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳࠨ᢫") not in plugins or bstack1l1lll111l_opy_():
        return
    summary = []
    driver = getattr(item, bstack11l1_opy_ (u"ࠤࡢࡨࡷ࡯ࡶࡦࡴࠥ᢬"), None)
    page = getattr(item, bstack11l1_opy_ (u"ࠥࡣࡵࡧࡧࡦࠤ᢭"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1l1ll111lll_opy_(item, report, summary, bstack1l1ll1ll111_opy_)
    if (page is not None):
        bstack1l1ll1l11l1_opy_(item, report, summary, bstack1l1ll1ll111_opy_)
def bstack1l1ll111lll_opy_(item, report, summary, bstack1l1ll1ll111_opy_):
    if report.when == bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ᢮") and report.skipped:
        bstack1ll11lll1ll_opy_(report)
    if report.when in [bstack11l1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ᢯"), bstack11l1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᢰ")]:
        return
    if not bstack1llllll11l1_opy_():
        return
    try:
        if (str(bstack1l1ll1ll111_opy_).lower() != bstack11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬᢱ")):
            item._driver.execute_script(
                bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ᢲ") + json.dumps(
                    report.nodeid) + bstack11l1_opy_ (u"ࠩࢀࢁࠬᢳ"))
        os.environ[bstack11l1_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭ᢴ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11l1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࡀࠠࡼ࠲ࢀࠦᢵ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᢶ")))
    bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"ࠨࠢᢷ")
    bstack1ll11lll1ll_opy_(report)
    if not passed:
        try:
            bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11l1_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢᢸ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1l11_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11l1_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᢹ")))
        bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"ࠤࠥᢺ")
        if not passed:
            try:
                bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥᢻ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1l11_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᢼ")
                    + json.dumps(bstack11l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠦࠨᢽ"))
                    + bstack11l1_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤᢾ")
                )
            else:
                item._driver.execute_script(
                    bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬᢿ")
                    + json.dumps(str(bstack1l1ll1l11_opy_))
                    + bstack11l1_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦᣀ")
                )
        except Exception as e:
            summary.append(bstack11l1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡢࡰࡱࡳࡹࡧࡴࡦ࠼ࠣࡿ࠵ࢃࠢᣁ").format(e))
def bstack1l1ll11ll11_opy_(test_name, error_message):
    try:
        bstack1l1ll11llll_opy_ = []
        bstack1ll1111l_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᣂ"), bstack11l1_opy_ (u"ࠫ࠵࠭ᣃ"))
        bstack11l1lll1_opy_ = {bstack11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᣄ"): test_name, bstack11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᣅ"): error_message, bstack11l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᣆ"): bstack1ll1111l_opy_}
        bstack1l1ll1l111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᣇ"))
        if os.path.exists(bstack1l1ll1l111l_opy_):
            with open(bstack1l1ll1l111l_opy_) as f:
                bstack1l1ll11llll_opy_ = json.load(f)
        bstack1l1ll11llll_opy_.append(bstack11l1lll1_opy_)
        with open(bstack1l1ll1l111l_opy_, bstack11l1_opy_ (u"ࠩࡺࠫᣈ")) as f:
            json.dump(bstack1l1ll11llll_opy_, f)
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡥࡳࡵ࡬ࡷࡹ࡯࡮ࡨࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡰࡺࡶࡨࡷࡹࠦࡥࡳࡴࡲࡶࡸࡀࠠࠨᣉ") + str(e))
def bstack1l1ll1l11l1_opy_(item, report, summary, bstack1l1ll1ll111_opy_):
    if report.when in [bstack11l1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᣊ"), bstack11l1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᣋ")]:
        return
    if (str(bstack1l1ll1ll111_opy_).lower() != bstack11l1_opy_ (u"࠭ࡴࡳࡷࡨࠫᣌ")):
        bstack1ll11lll11_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᣍ")))
    bstack1l1ll1l11_opy_ = bstack11l1_opy_ (u"ࠣࠤᣎ")
    bstack1ll11lll1ll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1ll1l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᣏ").format(e)
                )
        try:
            if passed:
                bstack1lll1l11ll_opy_(getattr(item, bstack11l1_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᣐ"), None), bstack11l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦᣑ"))
            else:
                error_message = bstack11l1_opy_ (u"ࠬ࠭ᣒ")
                if bstack1l1ll1l11_opy_:
                    bstack1llllll11_opy_(item._page, str(bstack1l1ll1l11_opy_), bstack11l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧᣓ"))
                    bstack1lll1l11ll_opy_(getattr(item, bstack11l1_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭ᣔ"), None), bstack11l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᣕ"), str(bstack1l1ll1l11_opy_))
                    error_message = str(bstack1l1ll1l11_opy_)
                else:
                    bstack1lll1l11ll_opy_(getattr(item, bstack11l1_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᣖ"), None), bstack11l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᣗ"))
                bstack1l1ll11ll11_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11l1_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀ࠶ࡽࠣᣘ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11l1_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᣙ"), default=bstack11l1_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧᣚ"), help=bstack11l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨᣛ"))
    parser.addoption(bstack11l1_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᣜ"), default=bstack11l1_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣᣝ"), help=bstack11l1_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤᣞ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11l1_opy_ (u"ࠦ࠲࠳ࡤࡳ࡫ࡹࡩࡷࠨᣟ"), action=bstack11l1_opy_ (u"ࠧࡹࡴࡰࡴࡨࠦᣠ"), default=bstack11l1_opy_ (u"ࠨࡣࡩࡴࡲࡱࡪࠨᣡ"),
                         help=bstack11l1_opy_ (u"ࠢࡅࡴ࡬ࡺࡪࡸࠠࡵࡱࠣࡶࡺࡴࠠࡵࡧࡶࡸࡸࠨᣢ"))
def bstack11ll1111ll_opy_(log):
    if not (log[bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᣣ")] and log[bstack11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᣤ")].strip()):
        return
    active = bstack11l1ll111l_opy_()
    log = {
        bstack11l1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᣥ"): log[bstack11l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᣦ")],
        bstack11l1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᣧ"): bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"࡚࠭ࠨᣨ"),
        bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᣩ"): log[bstack11l1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᣪ")],
    }
    if active:
        if active[bstack11l1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᣫ")] == bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᣬ"):
            log[bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᣭ")] = active[bstack11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᣮ")]
        elif active[bstack11l1_opy_ (u"࠭ࡴࡺࡲࡨࠫᣯ")] == bstack11l1_opy_ (u"ࠧࡵࡧࡶࡸࠬᣰ"):
            log[bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᣱ")] = active[bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᣲ")]
    bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_([log])
def bstack11l1ll111l_opy_():
    if len(store[bstack11l1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᣳ")]) > 0 and store[bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᣴ")][-1]:
        return {
            bstack11l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᣵ"): bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ᣶"),
            bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᣷"): store[bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ᣸")][-1]
        }
    if store.get(bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᣹"), None):
        return {
            bstack11l1_opy_ (u"ࠪࡸࡾࡶࡥࠨ᣺"): bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ᣻"),
            bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᣼"): store[bstack11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ᣽")]
        }
    return None
bstack11l1llll11_opy_ = bstack11l1ll11ll_opy_(bstack11ll1111ll_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        item._1l1ll1l11ll_opy_ = True
        bstack1l1l11l11l_opy_ = bstack1lll11ll1_opy_.bstack1l111111ll_opy_(bstack1llll1l11ll_opy_(item.own_markers))
        item._a11y_test_case = bstack1l1l11l11l_opy_
        if bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᣾"), None):
            driver = getattr(item, bstack11l1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ᣿"), None)
            item._a11y_started = bstack1lll11ll1_opy_.bstack1l1l1l11_opy_(driver, bstack1l1l11l11l_opy_)
        if not bstack1ll1llllll_opy_.on() or bstack1l1ll11l111_opy_ != bstack11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᤀ"):
            return
        global current_test_uuid, bstack11l1llll11_opy_
        bstack11l1llll11_opy_.start()
        bstack11l11l1111_opy_ = {
            bstack11l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᤁ"): uuid4().__str__(),
            bstack11l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᤂ"): bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"ࠬࡠࠧᤃ")
        }
        current_test_uuid = bstack11l11l1111_opy_[bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤄ")]
        store[bstack11l1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᤅ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᤆ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11l1111l1l_opy_[item.nodeid] = {**_11l1111l1l_opy_[item.nodeid], **bstack11l11l1111_opy_}
        bstack1l1ll11l11l_opy_(item, _11l1111l1l_opy_[item.nodeid], bstack11l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᤇ"))
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡧࡦࡲ࡬࠻ࠢࡾࢁࠬᤈ"), str(err))
def pytest_runtest_setup(item):
    global bstack1l1ll1ll1ll_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1llll111ll1_opy_():
        atexit.register(bstack1l11lll1ll_opy_)
        if not bstack1l1ll1ll1ll_opy_:
            try:
                bstack1l1ll11lll1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11111l1111_opy_():
                    bstack1l1ll11lll1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1l1ll11lll1_opy_:
                    signal.signal(s, bstack1l1ll1l1l1l_opy_)
                bstack1l1ll1ll1ll_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡩ࡬ࡷࡹ࡫ࡲࠡࡵ࡬࡫ࡳࡧ࡬ࠡࡪࡤࡲࡩࡲࡥࡳࡵ࠽ࠤࠧᤉ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1ll1l111l11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᤊ")
    try:
        if not bstack1ll1llllll_opy_.on():
            return
        bstack11l1llll11_opy_.start()
        uuid = uuid4().__str__()
        bstack11l11l1111_opy_ = {
            bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤋ"): uuid,
            bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᤌ"): bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"ࠨ࡜ࠪᤍ"),
            bstack11l1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᤎ"): bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᤏ"),
            bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᤐ"): bstack11l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᤑ"),
            bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᤒ"): bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᤓ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᤔ")] = item
        store[bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᤕ")] = [uuid]
        if not _11l1111l1l_opy_.get(item.nodeid, None):
            _11l1111l1l_opy_[item.nodeid] = {bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᤖ"): [], bstack11l1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᤗ"): []}
        _11l1111l1l_opy_[item.nodeid][bstack11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᤘ")].append(bstack11l11l1111_opy_[bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤙ")])
        _11l1111l1l_opy_[item.nodeid + bstack11l1_opy_ (u"ࠧ࠮ࡵࡨࡸࡺࡶࠧᤚ")] = bstack11l11l1111_opy_
        bstack1l1ll1llll1_opy_(item, bstack11l11l1111_opy_, bstack11l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᤛ"))
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬᤜ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1l111ll1l1_opy_
        bstack1ll1111l_opy_ = 0
        if bstack1l1ll11l11_opy_ is True:
            bstack1ll1111l_opy_ = int(os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᤝ")))
        if bstack1l1l1ll11l_opy_.bstack11ll1l1lll_opy_() == bstack11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᤞ"):
            if bstack1l1l1ll11l_opy_.bstack11ll11ll1l_opy_() == bstack11l1_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ᤟"):
                bstack1l1ll1lll1l_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᤠ"), None)
                bstack1111l11ll_opy_ = bstack1l1ll1lll1l_opy_ + bstack11l1_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥᤡ")
                driver = getattr(item, bstack11l1_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᤢ"), None)
                bstack1llll11111_opy_ = getattr(item, bstack11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᤣ"), None)
                bstack111111l1_opy_ = getattr(item, bstack11l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᤤ"), None)
                PercySDK.screenshot(driver, bstack1111l11ll_opy_, bstack1llll11111_opy_=bstack1llll11111_opy_, bstack111111l1_opy_=bstack111111l1_opy_, bstack111lll11l_opy_=bstack1ll1111l_opy_)
        if getattr(item, bstack11l1_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫᤥ"), False):
            bstack11ll111ll1_opy_.bstack1lll1llll1_opy_(getattr(item, bstack11l1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᤦ"), None), bstack1l111ll1l1_opy_, logger, item)
        if not bstack1ll1llllll_opy_.on():
            return
        bstack11l11l1111_opy_ = {
            bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᤧ"): uuid4().__str__(),
            bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᤨ"): bstack11l111l11l_opy_().isoformat() + bstack11l1_opy_ (u"ࠨ࡜ࠪᤩ"),
            bstack11l1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᤪ"): bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᤫ"),
            bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ᤬"): bstack11l1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ᤭"),
            bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ᤮"): bstack11l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ᤯")
        }
        _11l1111l1l_opy_[item.nodeid + bstack11l1_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫᤰ")] = bstack11l11l1111_opy_
        bstack1l1ll1llll1_opy_(item, bstack11l11l1111_opy_, bstack11l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᤱ"))
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩᤲ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1ll1llllll_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1ll1l11111l_opy_(fixturedef.argname):
        store[bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪᤳ")] = request.node
    elif bstack1ll11llllll_opy_(fixturedef.argname):
        store[bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪᤴ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᤵ"): fixturedef.argname,
            bstack11l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᤶ"): bstack1llll1ll1ll_opy_(outcome),
            bstack11l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪᤷ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᤸ")]
        if not _11l1111l1l_opy_.get(current_test_item.nodeid, None):
            _11l1111l1l_opy_[current_test_item.nodeid] = {bstack11l1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷ᤹ࠬ"): []}
        _11l1111l1l_opy_[current_test_item.nodeid][bstack11l1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭᤺")].append(fixture)
    except Exception as err:
        logger.debug(bstack11l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ᤻"), str(err))
if bstack1l1lll111l_opy_() and bstack1ll1llllll_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11l1111l1l_opy_[request.node.nodeid][bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ᤼")].bstack1ll111ll1_opy_(id(step))
        except Exception as err:
            print(bstack11l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬ᤽"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11l1111l1l_opy_[request.node.nodeid][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ᤾")].bstack11l1l1llll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭᤿"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11ll111111_opy_: bstack11l1lll11l_opy_ = _11l1111l1l_opy_[request.node.nodeid][bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭᥀")]
            bstack11ll111111_opy_.bstack11l1l1llll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ᥁"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1l1ll11l111_opy_
        try:
            if not bstack1ll1llllll_opy_.on() or bstack1l1ll11l111_opy_ != bstack11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ᥂"):
                return
            global bstack11l1llll11_opy_
            bstack11l1llll11_opy_.start()
            driver = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᥃"), None)
            if not _11l1111l1l_opy_.get(request.node.nodeid, None):
                _11l1111l1l_opy_[request.node.nodeid] = {}
            bstack11ll111111_opy_ = bstack11l1lll11l_opy_.bstack1ll111l1l11_opy_(
                scenario, feature, request.node,
                name=bstack1ll11ll1lll_opy_(request.node, scenario),
                bstack11l1l1l11l_opy_=bstack11l1l1lll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩ᥄"),
                tags=bstack1ll11llll11_opy_(feature, scenario),
                bstack11l1lllll1_opy_=bstack1ll1llllll_opy_.bstack11l1ll1ll1_opy_(driver) if driver and driver.session_id else {}
            )
            _11l1111l1l_opy_[request.node.nodeid][bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ᥅")] = bstack11ll111111_opy_
            bstack1l1ll111l1l_opy_(bstack11ll111111_opy_.uuid)
            bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ᥆"), bstack11ll111111_opy_)
        except Exception as err:
            print(bstack11l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ᥇"), str(err))
def bstack1l1ll11l1l1_opy_(bstack11ll11111l_opy_):
    if bstack11ll11111l_opy_ in store[bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ᥈")]:
        store[bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᥉")].remove(bstack11ll11111l_opy_)
def bstack1l1ll111l1l_opy_(bstack11l1llll1l_opy_):
    store[bstack11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ᥊")] = bstack11l1llll1l_opy_
    threading.current_thread().current_test_uuid = bstack11l1llll1l_opy_
@bstack1ll1llllll_opy_.bstack1l1lllll111_opy_
def bstack1l1ll111ll1_opy_(item, call, report):
    global bstack1l1ll11l111_opy_
    bstack11lll1lll_opy_ = bstack11l1l1lll_opy_()
    if hasattr(report, bstack11l1_opy_ (u"ࠧࡴࡶࡲࡴࠬ᥋")):
        bstack11lll1lll_opy_ = bstack1llll1lllll_opy_(report.stop)
    elif hasattr(report, bstack11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࠧ᥌")):
        bstack11lll1lll_opy_ = bstack1llll1lllll_opy_(report.start)
    try:
        if getattr(report, bstack11l1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ᥍"), bstack11l1_opy_ (u"ࠪࠫ᥎")) == bstack11l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ᥏"):
            bstack11l1llll11_opy_.reset()
        if getattr(report, bstack11l1_opy_ (u"ࠬࡽࡨࡦࡰࠪᥐ"), bstack11l1_opy_ (u"࠭ࠧᥑ")) == bstack11l1_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᥒ"):
            if bstack1l1ll11l111_opy_ == bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᥓ"):
                _11l1111l1l_opy_[item.nodeid][bstack11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᥔ")] = bstack11lll1lll_opy_
                bstack1l1ll11l11l_opy_(item, _11l1111l1l_opy_[item.nodeid], bstack11l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᥕ"), report, call)
                store[bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᥖ")] = None
            elif bstack1l1ll11l111_opy_ == bstack11l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᥗ"):
                bstack11ll111111_opy_ = _11l1111l1l_opy_[item.nodeid][bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᥘ")]
                bstack11ll111111_opy_.set(hooks=_11l1111l1l_opy_[item.nodeid].get(bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᥙ"), []))
                exception, bstack11l1lll111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11l1lll111_opy_ = [call.excinfo.exconly(), getattr(report, bstack11l1_opy_ (u"ࠨ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠧᥚ"), bstack11l1_opy_ (u"ࠩࠪᥛ"))]
                bstack11ll111111_opy_.stop(time=bstack11lll1lll_opy_, result=Result(result=getattr(report, bstack11l1_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫᥜ"), bstack11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᥝ")), exception=exception, bstack11l1lll111_opy_=bstack11l1lll111_opy_))
                bstack1ll1llllll_opy_.bstack11l1ll1l11_opy_(bstack11l1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᥞ"), _11l1111l1l_opy_[item.nodeid][bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᥟ")])
        elif getattr(report, bstack11l1_opy_ (u"ࠧࡸࡪࡨࡲࠬᥠ"), bstack11l1_opy_ (u"ࠨࠩᥡ")) in [bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᥢ"), bstack11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᥣ")]:
            bstack11l1ll1l1l_opy_ = item.nodeid + bstack11l1_opy_ (u"ࠫ࠲࠭ᥤ") + getattr(report, bstack11l1_opy_ (u"ࠬࡽࡨࡦࡰࠪᥥ"), bstack11l1_opy_ (u"࠭ࠧᥦ"))
            if getattr(report, bstack11l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᥧ"), False):
                hook_type = bstack11l1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᥨ") if getattr(report, bstack11l1_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᥩ"), bstack11l1_opy_ (u"ࠪࠫᥪ")) == bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᥫ") else bstack11l1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᥬ")
                _11l1111l1l_opy_[bstack11l1ll1l1l_opy_] = {
                    bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᥭ"): uuid4().__str__(),
                    bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ᥮"): bstack11lll1lll_opy_,
                    bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ᥯"): hook_type
                }
            _11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᥰ")] = bstack11lll1lll_opy_
            bstack1l1ll11l1l1_opy_(_11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᥱ")])
            bstack1l1ll1llll1_opy_(item, _11l1111l1l_opy_[bstack11l1ll1l1l_opy_], bstack11l1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᥲ"), report, call)
            if getattr(report, bstack11l1_opy_ (u"ࠬࡽࡨࡦࡰࠪᥳ"), bstack11l1_opy_ (u"࠭ࠧᥴ")) == bstack11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭᥵"):
                if getattr(report, bstack11l1_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ᥶"), bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᥷")) == bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᥸"):
                    bstack11l11l1111_opy_ = {
                        bstack11l1_opy_ (u"ࠫࡺࡻࡩࡥࠩ᥹"): uuid4().__str__(),
                        bstack11l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ᥺"): bstack11l1l1lll_opy_(),
                        bstack11l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᥻"): bstack11l1l1lll_opy_()
                    }
                    _11l1111l1l_opy_[item.nodeid] = {**_11l1111l1l_opy_[item.nodeid], **bstack11l11l1111_opy_}
                    bstack1l1ll11l11l_opy_(item, _11l1111l1l_opy_[item.nodeid], bstack11l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ᥼"))
                    bstack1l1ll11l11l_opy_(item, _11l1111l1l_opy_[item.nodeid], bstack11l1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᥽"), report, call)
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࢀࢃࠧ᥾"), str(err))
def bstack1l1ll111l11_opy_(test, bstack11l11l1111_opy_, result=None, call=None, bstack1l111l1ll1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11ll111111_opy_ = {
        bstack11l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ᥿"): bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠫࡺࡻࡩࡥࠩᦀ")],
        bstack11l1_opy_ (u"ࠬࡺࡹࡱࡧࠪᦁ"): bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࠫᦂ"),
        bstack11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᦃ"): test.name,
        bstack11l1_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᦄ"): {
            bstack11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᦅ"): bstack11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᦆ"),
            bstack11l1_opy_ (u"ࠫࡨࡵࡤࡦࠩᦇ"): inspect.getsource(test.obj)
        },
        bstack11l1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᦈ"): test.name,
        bstack11l1_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬᦉ"): test.name,
        bstack11l1_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧᦊ"): bstack1l11l11l1l_opy_.bstack11l11ll1l1_opy_(test),
        bstack11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫᦋ"): file_path,
        bstack11l1_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫᦌ"): file_path,
        bstack11l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᦍ"): bstack11l1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬᦎ"),
        bstack11l1_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪᦏ"): file_path,
        bstack11l1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᦐ"): bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᦑ")],
        bstack11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᦒ"): bstack11l1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᦓ"),
        bstack11l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭ᦔ"): {
            bstack11l1_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨᦕ"): test.nodeid
        },
        bstack11l1_opy_ (u"ࠬࡺࡡࡨࡵࠪᦖ"): bstack1llll1l11ll_opy_(test.own_markers)
    }
    if bstack1l111l1ll1_opy_ in [bstack11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᦗ"), bstack11l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᦘ")]:
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭ᦙ")] = {
            bstack11l1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᦚ"): bstack11l11l1111_opy_.get(bstack11l1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᦛ"), [])
        }
    if bstack1l111l1ll1_opy_ == bstack11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬᦜ"):
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᦝ")] = bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᦞ")
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᦟ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᦠ")]
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᦡ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᦢ")]
    if result:
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᦣ")] = result.outcome
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᦤ")] = result.duration * 1000
        bstack11ll111111_opy_[bstack11l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᦥ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᦦ")]
        if result.failed:
            bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᦧ")] = bstack1ll1llllll_opy_.bstack111ll111l1_opy_(call.excinfo.typename)
            bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᦨ")] = bstack1ll1llllll_opy_.bstack1l1llllll1l_opy_(call.excinfo, result)
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᦩ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᦪ")]
    if outcome:
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᦫ")] = bstack1llll1ll1ll_opy_(outcome)
        bstack11ll111111_opy_[bstack11l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ᦬")] = 0
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᦭")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᦮")]
        if bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᦯")] == bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᦰ"):
            bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᦱ")] = bstack11l1_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭ᦲ")  # bstack1l1ll1111l1_opy_
            bstack11ll111111_opy_[bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᦳ")] = [{bstack11l1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᦴ"): [bstack11l1_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬᦵ")]}]
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᦶ")] = bstack11l11l1111_opy_[bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᦷ")]
    return bstack11ll111111_opy_
def bstack1l1ll1ll11l_opy_(test, bstack111lllllll_opy_, bstack1l111l1ll1_opy_, result, call, outcome, bstack1l1ll1lll11_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᦸ")]
    hook_name = bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨᦹ")]
    hook_data = {
        bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᦺ"): bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᦻ")],
        bstack11l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᦼ"): bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᦽ"),
        bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᦾ"): bstack11l1_opy_ (u"ࠫࢀࢃࠧᦿ").format(bstack1ll11lll111_opy_(hook_name)),
        bstack11l1_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᧀ"): {
            bstack11l1_opy_ (u"࠭࡬ࡢࡰࡪࠫᧁ"): bstack11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᧂ"),
            bstack11l1_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᧃ"): None
        },
        bstack11l1_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨᧄ"): test.name,
        bstack11l1_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪᧅ"): bstack1l11l11l1l_opy_.bstack11l11ll1l1_opy_(test, hook_name),
        bstack11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧᧆ"): file_path,
        bstack11l1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧᧇ"): file_path,
        bstack11l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᧈ"): bstack11l1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᧉ"),
        bstack11l1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭᧊"): file_path,
        bstack11l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᧋"): bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᧌")],
        bstack11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ᧍"): bstack11l1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ᧎") if bstack1l1ll11l111_opy_ == bstack11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ᧏") else bstack11l1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ᧐"),
        bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ᧑"): hook_type
    }
    bstack1ll11l111l1_opy_ = bstack11l11l111l_opy_(_11l1111l1l_opy_.get(test.nodeid, None))
    if bstack1ll11l111l1_opy_:
        hook_data[bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧ᧒")] = bstack1ll11l111l1_opy_
    if result:
        hook_data[bstack11l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᧓")] = result.outcome
        hook_data[bstack11l1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ᧔")] = result.duration * 1000
        hook_data[bstack11l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᧕")] = bstack111lllllll_opy_[bstack11l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᧖")]
        if result.failed:
            hook_data[bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭᧗")] = bstack1ll1llllll_opy_.bstack111ll111l1_opy_(call.excinfo.typename)
            hook_data[bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ᧘")] = bstack1ll1llllll_opy_.bstack1l1llllll1l_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ᧙")] = bstack1llll1ll1ll_opy_(outcome)
        hook_data[bstack11l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ᧚")] = 100
        hook_data[bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᧛")] = bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᧜")]
        if hook_data[bstack11l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᧝")] == bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᧞"):
            hook_data[bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ᧟")] = bstack11l1_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ᧠")  # bstack1l1ll1111l1_opy_
            hook_data[bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᧡")] = [{bstack11l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ᧢"): [bstack11l1_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ᧣")]}]
    if bstack1l1ll1lll11_opy_:
        hook_data[bstack11l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᧤")] = bstack1l1ll1lll11_opy_.result
        hook_data[bstack11l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ᧥")] = bstack1llllll1lll_opy_(bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ᧦")], bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᧧")])
        hook_data[bstack11l1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᧨")] = bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᧩")]
        if hook_data[bstack11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᧪")] == bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᧫"):
            hook_data[bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭᧬")] = bstack1ll1llllll_opy_.bstack111ll111l1_opy_(bstack1l1ll1lll11_opy_.exception_type)
            hook_data[bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ᧭")] = [{bstack11l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ᧮"): bstack1llllllll1l_opy_(bstack1l1ll1lll11_opy_.exception)}]
    return hook_data
def bstack1l1ll11l11l_opy_(test, bstack11l11l1111_opy_, bstack1l111l1ll1_opy_, result=None, call=None, outcome=None):
    bstack11ll111111_opy_ = bstack1l1ll111l11_opy_(test, bstack11l11l1111_opy_, result, call, bstack1l111l1ll1_opy_, outcome)
    driver = getattr(test, bstack11l1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ᧯"), None)
    if bstack1l111l1ll1_opy_ == bstack11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ᧰") and driver:
        bstack11ll111111_opy_[bstack11l1_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫ᧱")] = bstack1ll1llllll_opy_.bstack11l1ll1ll1_opy_(driver)
    if bstack1l111l1ll1_opy_ == bstack11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ᧲"):
        bstack1l111l1ll1_opy_ = bstack11l1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ᧳")
    bstack11l111l111_opy_ = {
        bstack11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᧴"): bstack1l111l1ll1_opy_,
        bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ᧵"): bstack11ll111111_opy_
    }
    bstack1ll1llllll_opy_.bstack11l111111l_opy_(bstack11l111l111_opy_)
    if bstack1l111l1ll1_opy_ == bstack11l1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ᧶"):
        threading.current_thread().bstackTestMeta = {bstack11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ᧷"): bstack11l1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭᧸")}
    elif bstack1l111l1ll1_opy_ == bstack11l1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ᧹"):
        threading.current_thread().bstackTestMeta = {bstack11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ᧺"): getattr(result, bstack11l1_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ᧻"), bstack11l1_opy_ (u"ࠩࠪ᧼"))}
def bstack1l1ll1llll1_opy_(test, bstack11l11l1111_opy_, bstack1l111l1ll1_opy_, result=None, call=None, outcome=None, bstack1l1ll1lll11_opy_=None):
    hook_data = bstack1l1ll1ll11l_opy_(test, bstack11l11l1111_opy_, bstack1l111l1ll1_opy_, result, call, outcome, bstack1l1ll1lll11_opy_)
    bstack11l111l111_opy_ = {
        bstack11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ᧽"): bstack1l111l1ll1_opy_,
        bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭᧾"): hook_data
    }
    bstack1ll1llllll_opy_.bstack11l111111l_opy_(bstack11l111l111_opy_)
def bstack11l11l111l_opy_(bstack11l11l1111_opy_):
    if not bstack11l11l1111_opy_:
        return None
    if bstack11l11l1111_opy_.get(bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ᧿"), None):
        return getattr(bstack11l11l1111_opy_[bstack11l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᨀ")], bstack11l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᨁ"), None)
    return bstack11l11l1111_opy_.get(bstack11l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᨂ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1ll1llllll_opy_.on():
            return
        places = [bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᨃ"), bstack11l1_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᨄ"), bstack11l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᨅ")]
        bstack11l11lllll_opy_ = []
        for bstack1l1ll11ll1l_opy_ in places:
            records = caplog.get_records(bstack1l1ll11ll1l_opy_)
            bstack1l1ll11111l_opy_ = bstack11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᨆ") if bstack1l1ll11ll1l_opy_ == bstack11l1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᨇ") else bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᨈ")
            bstack1l1ll1111ll_opy_ = request.node.nodeid + (bstack11l1_opy_ (u"ࠨࠩᨉ") if bstack1l1ll11ll1l_opy_ == bstack11l1_opy_ (u"ࠩࡦࡥࡱࡲࠧᨊ") else bstack11l1_opy_ (u"ࠪ࠱ࠬᨋ") + bstack1l1ll11ll1l_opy_)
            bstack11l1llll1l_opy_ = bstack11l11l111l_opy_(_11l1111l1l_opy_.get(bstack1l1ll1111ll_opy_, None))
            if not bstack11l1llll1l_opy_:
                continue
            for record in records:
                if bstack1lll1llll1l_opy_(record.message):
                    continue
                bstack11l11lllll_opy_.append({
                    bstack11l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᨌ"): bstack11111l111l_opy_(record.created).isoformat() + bstack11l1_opy_ (u"ࠬࡠࠧᨍ"),
                    bstack11l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᨎ"): record.levelname,
                    bstack11l1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᨏ"): record.message,
                    bstack1l1ll11111l_opy_: bstack11l1llll1l_opy_
                })
        if len(bstack11l11lllll_opy_) > 0:
            bstack1ll1llllll_opy_.bstack1ll11l1ll1_opy_(bstack11l11lllll_opy_)
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡦࡳࡳࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥ࠻ࠢࡾࢁࠬᨐ"), str(err))
def bstack11l111111_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1lll11lll_opy_
    bstack1ll111ll1l_opy_ = bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ᨑ"), None) and bstack1l1lll1lll_opy_(
            threading.current_thread(), bstack11l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᨒ"), None)
    bstack1111ll11l_opy_ = getattr(driver, bstack11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫᨓ"), None) != None and getattr(driver, bstack11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬᨔ"), None) == True
    if sequence == bstack11l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭ᨕ") and driver != None:
      if not bstack1lll11lll_opy_ and bstack1llllll11l1_opy_() and bstack11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᨖ") in CONFIG and CONFIG[bstack11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᨗ")] == True and bstack11l1l111_opy_.bstack1lll111lll_opy_(driver_command) and (bstack1111ll11l_opy_ or bstack1ll111ll1l_opy_) and not bstack1ll11l1l11_opy_(args):
        try:
          bstack1lll11lll_opy_ = True
          logger.debug(bstack11l1_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡽࢀᨘࠫ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡦࡴࡩࡳࡷࡳࠠࡴࡥࡤࡲࠥࢁࡽࠨᨙ").format(str(err)))
        bstack1lll11lll_opy_ = False
    if sequence == bstack11l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᨚ"):
        if driver_command == bstack11l1_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩᨛ"):
            bstack1ll1llllll_opy_.bstack1l1ll1111_opy_({
                bstack11l1_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ᨜"): response[bstack11l1_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭᨝")],
                bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᨞"): store[bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᨟")]
            })
def bstack1l11lll1ll_opy_():
    global bstack1ll111l111_opy_
    bstack11llll11_opy_.bstack1l1111l11_opy_()
    logging.shutdown()
    bstack1ll1llllll_opy_.bstack11l11ll11l_opy_()
    for driver in bstack1ll111l111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1ll1l1l1l_opy_(*args):
    global bstack1ll111l111_opy_
    bstack1ll1llllll_opy_.bstack11l11ll11l_opy_()
    for driver in bstack1ll111l111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l11l1l1l1_opy_(self, *args, **kwargs):
    bstack11l111l1l_opy_ = bstack1lll1111l_opy_(self, *args, **kwargs)
    bstack1l1lll111_opy_ = getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫᨠ"), None)
    if bstack1l1lll111_opy_ and bstack1l1lll111_opy_.get(bstack11l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᨡ"), bstack11l1_opy_ (u"ࠬ࠭ᨢ")) == bstack11l1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧᨣ"):
        bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
    return bstack11l111l1l_opy_
@measure(event_name=EVENTS.bstack1ll1111l1_opy_, stage=STAGE.bstack1111l1l1l_opy_, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1ll1ll1l_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
    if bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫᨤ")):
        return
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬᨥ"), True)
    global bstack1llll11l1l_opy_
    global bstack11l11ll11_opy_
    bstack1llll11l1l_opy_ = framework_name
    logger.info(bstack1l11l1ll1_opy_.format(bstack1llll11l1l_opy_.split(bstack11l1_opy_ (u"ࠩ࠰ࠫᨦ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1llllll11l1_opy_():
            Service.start = bstack1l1lllll_opy_
            Service.stop = bstack1ll11llll_opy_
            webdriver.Remote.__init__ = bstack1l11111ll_opy_
            webdriver.Remote.get = bstack111l11lll_opy_
            if not isinstance(os.getenv(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫᨧ")), str):
                return
            WebDriver.close = bstack1l11lll1l1_opy_
            WebDriver.quit = bstack11l111ll1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack1llllll11l1_opy_() and bstack1ll1llllll_opy_.on():
            webdriver.Remote.__init__ = bstack1l11l1l1l1_opy_
        bstack11l11ll11_opy_ = True
    except Exception as e:
        pass
    bstack1111l11l_opy_()
    if os.environ.get(bstack11l1_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᨨ")):
        bstack11l11ll11_opy_ = eval(os.environ.get(bstack11l1_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪᨩ")))
    if not bstack11l11ll11_opy_:
        bstack111l1111_opy_(bstack11l1_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣᨪ"), bstack1l111l1l1_opy_)
    if bstack11llll111_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._1ll1111ll1_opy_ = bstack11l11l111_opy_
        except Exception as e:
            logger.error(bstack11ll11llll_opy_.format(str(e)))
    if bstack11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᨫ") in str(framework_name).lower():
        if not bstack1llllll11l1_opy_():
            return
        try:
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
@measure(event_name=EVENTS.bstack1llllllll1_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack11l111ll1_opy_(self):
    global bstack1llll11l1l_opy_
    global bstack1l1l1ll1l_opy_
    global bstack1ll1l111l1_opy_
    try:
        if bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᨬ") in bstack1llll11l1l_opy_ and self.session_id != None and bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᨭ"), bstack11l1_opy_ (u"ࠪࠫᨮ")) != bstack11l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᨯ"):
            bstack1lll1l111l_opy_ = bstack11l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᨰ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᨱ")
            bstack11lll1ll1_opy_(logger, True)
            if self != None:
                bstack11l1111ll_opy_(self, bstack1lll1l111l_opy_, bstack11l1_opy_ (u"ࠧ࠭ࠢࠪᨲ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᨳ"), None)
        if item is not None and bstack1l1lll1lll_opy_(threading.current_thread(), bstack11l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᨴ"), None):
            bstack11ll111ll1_opy_.bstack1lll1llll1_opy_(self, bstack1l111ll1l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11l1_opy_ (u"ࠪࠫᨵ")
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧᨶ") + str(e))
    bstack1ll1l111l1_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack11l1l1l1l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack1l11111ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l1l1ll1l_opy_
    global bstack1l111l111_opy_
    global bstack1l1ll11l11_opy_
    global bstack1llll11l1l_opy_
    global bstack1lll1111l_opy_
    global bstack1ll111l111_opy_
    global bstack1l11l1l1l_opy_
    global bstack1ll1lllll_opy_
    global bstack1l111ll1l1_opy_
    CONFIG[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᨷ")] = str(bstack1llll11l1l_opy_) + str(__version__)
    command_executor = bstack1llll1ll1l_opy_(bstack1l11l1l1l_opy_, CONFIG)
    logger.debug(bstack1l1l1ll11_opy_.format(command_executor))
    proxy = bstack1ll1ll11ll_opy_(CONFIG, proxy)
    bstack1ll1111l_opy_ = 0
    try:
        if bstack1l1ll11l11_opy_ is True:
            bstack1ll1111l_opy_ = int(os.environ.get(bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᨸ")))
    except:
        bstack1ll1111l_opy_ = 0
    bstack111ll11ll_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1ll1111l_opy_)
    logger.debug(bstack1lll1l1lll_opy_.format(str(bstack111ll11ll_opy_)))
    bstack1l111ll1l1_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᨹ"))[bstack1ll1111l_opy_]
    if bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᨺ") in CONFIG and CONFIG[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᨻ")]:
        bstack1l1l111l1_opy_(bstack111ll11ll_opy_, bstack1ll1lllll_opy_)
    if bstack1lll11ll1_opy_.bstack111l1ll1l_opy_(CONFIG, bstack1ll1111l_opy_) and bstack1lll11ll1_opy_.bstack1lll1l11_opy_(bstack111ll11ll_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        bstack1lll11ll1_opy_.set_capabilities(bstack111ll11ll_opy_, CONFIG)
    if desired_capabilities:
        bstack11ll11l1l1_opy_ = bstack1ll1llll1_opy_(desired_capabilities)
        bstack11ll11l1l1_opy_[bstack11l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᨼ")] = bstack1l11l1l1_opy_(CONFIG)
        bstack1ll1l1l1ll_opy_ = bstack11ll1l11l_opy_(bstack11ll11l1l1_opy_)
        if bstack1ll1l1l1ll_opy_:
            bstack111ll11ll_opy_ = update(bstack1ll1l1l1ll_opy_, bstack111ll11ll_opy_)
        desired_capabilities = None
    if options:
        bstack11l111lll_opy_(options, bstack111ll11ll_opy_)
    if not options:
        options = bstack1lll11llll_opy_(bstack111ll11ll_opy_)
    if proxy and bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᨽ")):
        options.proxy(proxy)
    if options and bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᨾ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1lll11ll_opy_() < version.parse(bstack11l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᨿ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack111ll11ll_opy_)
    logger.info(bstack1lll1lll1_opy_)
    bstack1ll111l1_opy_.end(EVENTS.bstack1ll1111l1_opy_.value, EVENTS.bstack1ll1111l1_opy_.value + bstack11l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᩀ"),
                               EVENTS.bstack1ll1111l1_opy_.value + bstack11l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᩁ"), True, None)
    if bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩᩂ")):
        bstack1lll1111l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᩃ")):
        bstack1lll1111l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫᩄ")):
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
        bstack1l111ll11l_opy_ = bstack11l1_opy_ (u"ࠬ࠭ᩅ")
        if bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧᩆ")):
            bstack1l111ll11l_opy_ = self.caps.get(bstack11l1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢᩇ"))
        else:
            bstack1l111ll11l_opy_ = self.capabilities.get(bstack11l1_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣᩈ"))
        if bstack1l111ll11l_opy_:
            bstack1lll1ll111_opy_(bstack1l111ll11l_opy_)
            if bstack1l1lll11ll_opy_() <= version.parse(bstack11l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᩉ")):
                self.command_executor._url = bstack11l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᩊ") + bstack1l11l1l1l_opy_ + bstack11l1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᩋ")
            else:
                self.command_executor._url = bstack11l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᩌ") + bstack1l111ll11l_opy_ + bstack11l1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᩍ")
            logger.debug(bstack11ll1l11l1_opy_.format(bstack1l111ll11l_opy_))
        else:
            logger.debug(bstack1lll1l1ll1_opy_.format(bstack11l1_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣᩎ")))
    except Exception as e:
        logger.debug(bstack1lll1l1ll1_opy_.format(e))
    bstack1l1l1ll1l_opy_ = self.session_id
    if bstack11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᩏ") in bstack1llll11l1l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11l1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᩐ"), None)
        if item:
            bstack1l1ll1l1ll1_opy_ = getattr(item, bstack11l1_opy_ (u"ࠪࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨᩑ"), False)
            if not getattr(item, bstack11l1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᩒ"), None) and bstack1l1ll1l1ll1_opy_:
                setattr(store[bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᩓ")], bstack11l1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᩔ"), self)
        bstack1l1lll111_opy_ = getattr(threading.current_thread(), bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨᩕ"), None)
        if bstack1l1lll111_opy_ and bstack1l1lll111_opy_.get(bstack11l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᩖ"), bstack11l1_opy_ (u"ࠩࠪᩗ")) == bstack11l1_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᩘ"):
            bstack1ll1llllll_opy_.bstack11ll1l1ll_opy_(self)
    bstack1ll111l111_opy_.append(self)
    if bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᩙ") in CONFIG and bstack11l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᩚ") in CONFIG[bstack11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᩛ")][bstack1ll1111l_opy_]:
        bstack1l111l111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᩜ")][bstack1ll1111l_opy_][bstack11l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᩝ")]
    logger.debug(bstack1111ll1ll_opy_.format(bstack1l1l1ll1l_opy_))
@measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.SINGLE, bstack1lll11l11l_opy_=bstack1l111l111_opy_)
def bstack111l11lll_opy_(self, url):
    global bstack11llll1ll1_opy_
    global CONFIG
    try:
        bstack1lll1lll11_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11l1l1ll1_opy_.format(str(err)))
    try:
        bstack11llll1ll1_opy_(self, url)
    except Exception as e:
        try:
            bstack11ll111ll_opy_ = str(e)
            if any(err_msg in bstack11ll111ll_opy_ for err_msg in bstack1l11ll11ll_opy_):
                bstack1lll1lll11_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11l1l1ll1_opy_.format(str(err)))
        raise e
def bstack11lll1111_opy_(item, when):
    global bstack1ll1111l11_opy_
    try:
        bstack1ll1111l11_opy_(item, when)
    except Exception as e:
        pass
def bstack11ll11lll_opy_(item, call, rep):
    global bstack1lllll11_opy_
    global bstack1ll111l111_opy_
    name = bstack11l1_opy_ (u"ࠩࠪᩞ")
    try:
        if rep.when == bstack11l1_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ᩟"):
            bstack1l1l1ll1l_opy_ = threading.current_thread().bstackSessionId
            bstack1l1ll1ll111_opy_ = item.config.getoption(bstack11l1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ᩠࠭"))
            try:
                if (str(bstack1l1ll1ll111_opy_).lower() != bstack11l1_opy_ (u"ࠬࡺࡲࡶࡧࠪᩡ")):
                    name = str(rep.nodeid)
                    bstack1l1ll11lll_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᩢ"), name, bstack11l1_opy_ (u"ࠧࠨᩣ"), bstack11l1_opy_ (u"ࠨࠩᩤ"), bstack11l1_opy_ (u"ࠩࠪᩥ"), bstack11l1_opy_ (u"ࠪࠫᩦ"))
                    os.environ[bstack11l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᩧ")] = name
                    for driver in bstack1ll111l111_opy_:
                        if bstack1l1l1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll11lll_opy_)
            except Exception as e:
                logger.debug(bstack11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬᩨ").format(str(e)))
            try:
                bstack1ll1l11l11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᩩ"):
                    status = bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᩪ") if rep.outcome.lower() == bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᩫ") else bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᩬ")
                    reason = bstack11l1_opy_ (u"ࠪࠫᩭ")
                    if status == bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᩮ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪᩯ") if status == bstack11l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᩰ") else bstack11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᩱ")
                    data = name + bstack11l1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪᩲ") if status == bstack11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᩳ") else name + bstack11l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭ᩴ") + reason
                    bstack1l11lll11_opy_ = bstack1llll1l1l1_opy_(bstack11l1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭᩵"), bstack11l1_opy_ (u"ࠬ࠭᩶"), bstack11l1_opy_ (u"࠭ࠧ᩷"), bstack11l1_opy_ (u"ࠧࠨ᩸"), level, data)
                    for driver in bstack1ll111l111_opy_:
                        if bstack1l1l1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11lll11_opy_)
            except Exception as e:
                logger.debug(bstack11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ᩹").format(str(e)))
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭᩺").format(str(e)))
    bstack1lllll11_opy_(item, call, rep)
notset = Notset()
def bstack1111llll1_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11ll111l_opy_
    if str(name).lower() == bstack11l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪ᩻"):
        return bstack11l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ᩼")
    else:
        return bstack11ll111l_opy_(self, name, default, skip)
def bstack11l11l111_opy_(self):
    global CONFIG
    global bstack111ll1lll_opy_
    try:
        proxy = bstack1ll11ll111_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11l1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ᩽")):
                proxies = bstack1l1111l1ll_opy_(proxy, bstack1llll1ll1l_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll1ll1l11_opy_ = proxies.popitem()
                    if bstack11l1_opy_ (u"ࠨ࠺࠰࠱ࠥ᩾") in bstack1ll1ll1l11_opy_:
                        return bstack1ll1ll1l11_opy_
                    else:
                        return bstack11l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯᩿ࠣ") + bstack1ll1ll1l11_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧ᪀").format(str(e)))
    return bstack111ll1lll_opy_(self)
def bstack11llll111_opy_():
    return (bstack11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᪁") in CONFIG or bstack11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᪂") in CONFIG) and bstack1llll1lll1_opy_() and bstack1l1lll11ll_opy_() >= version.parse(
        bstack1l1ll11ll_opy_)
def bstack11l1ll11_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l111l111_opy_
    global bstack1l1ll11l11_opy_
    global bstack1llll11l1l_opy_
    CONFIG[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭᪃")] = str(bstack1llll11l1l_opy_) + str(__version__)
    bstack1ll1111l_opy_ = 0
    try:
        if bstack1l1ll11l11_opy_ is True:
            bstack1ll1111l_opy_ = int(os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ᪄")))
    except:
        bstack1ll1111l_opy_ = 0
    CONFIG[bstack11l1_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ᪅")] = True
    bstack111ll11ll_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1ll1111l_opy_)
    logger.debug(bstack1lll1l1lll_opy_.format(str(bstack111ll11ll_opy_)))
    if CONFIG.get(bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᪆")):
        bstack1l1l111l1_opy_(bstack111ll11ll_opy_, bstack1ll1lllll_opy_)
    if bstack11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᪇") in CONFIG and bstack11l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᪈") in CONFIG[bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᪉")][bstack1ll1111l_opy_]:
        bstack1l111l111_opy_ = CONFIG[bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ᪊")][bstack1ll1111l_opy_][bstack11l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᪋")]
    import urllib
    import json
    if bstack11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ᪌") in CONFIG and str(CONFIG[bstack11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ᪍")]).lower() != bstack11l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ᪎"):
        bstack1l11ll111_opy_ = bstack1lll11l1_opy_()
        bstack111lll11_opy_ = bstack1l11ll111_opy_ + urllib.parse.quote(json.dumps(bstack111ll11ll_opy_))
    else:
        bstack111lll11_opy_ = bstack11l1_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ᪏") + urllib.parse.quote(json.dumps(bstack111ll11ll_opy_))
    browser = self.connect(bstack111lll11_opy_)
    return browser
def bstack1111l11l_opy_():
    global bstack11l11ll11_opy_
    global bstack1llll11l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l1lll_opy_
        if not bstack1llllll11l1_opy_():
            global bstack1ll1ll111l_opy_
            if not bstack1ll1ll111l_opy_:
                from bstack_utils.helper import bstack111l1ll11_opy_, bstack1llll1ll1_opy_
                bstack1ll1ll111l_opy_ = bstack111l1ll11_opy_()
                bstack1llll1ll1_opy_(bstack1llll11l1l_opy_)
            BrowserType.connect = bstack1111l1lll_opy_
            return
        BrowserType.launch = bstack11l1ll11_opy_
        bstack11l11ll11_opy_ = True
    except Exception as e:
        pass
def bstack1l1ll1ll1l1_opy_():
    global CONFIG
    global bstack11llll1l1l_opy_
    global bstack1l11l1l1l_opy_
    global bstack1ll1lllll_opy_
    global bstack1l1ll11l11_opy_
    global bstack1ll1ll1ll_opy_
    CONFIG = json.loads(os.environ.get(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩ᪐")))
    bstack11llll1l1l_opy_ = eval(os.environ.get(bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ᪑")))
    bstack1l11l1l1l_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ᪒"))
    bstack1l1l1l1l1l_opy_(CONFIG, bstack11llll1l1l_opy_)
    bstack1ll1ll1ll_opy_ = bstack11llll11_opy_.bstack1l1lll1111_opy_(CONFIG, bstack1ll1ll1ll_opy_)
    global bstack1lll1111l_opy_
    global bstack1ll1l111l1_opy_
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
    except Exception as e:
        pass
    if (bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᪓") in CONFIG or bstack11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᪔") in CONFIG) and bstack1llll1lll1_opy_():
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
        logger.debug(bstack11l1_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ᪕"))
    bstack1ll1lllll_opy_ = CONFIG.get(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᪖"), {}).get(bstack11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᪗"))
    bstack1l1ll11l11_opy_ = True
    bstack1ll1ll1l_opy_(bstack1l1l1l11l1_opy_)
if (bstack1llll111ll1_opy_()):
    bstack1l1ll1ll1l1_opy_()
@bstack11l11l1l1l_opy_(class_method=False)
def bstack1l1ll111111_opy_(hook_name, event, bstack1l1ll1l1l11_opy_=None):
    if hook_name not in [bstack11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ᪘"), bstack11l1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᪙"), bstack11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᪚"), bstack11l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᪛"), bstack11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭᪜"), bstack11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ᪝"), bstack11l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩ᪞"), bstack11l1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᪟")]:
        return
    node = store[bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ᪠")]
    if hook_name in [bstack11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᪡"), bstack11l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᪢")]:
        node = store[bstack11l1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ᪣")]
    elif hook_name in [bstack11l1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ᪤"), bstack11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ᪥")]:
        node = store[bstack11l1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ᪦")]
    if event == bstack11l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬᪧ"):
        hook_type = bstack1ll11lllll1_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack111lllllll_opy_ = {
            bstack11l1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ᪨"): uuid,
            bstack11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ᪩"): bstack11l1l1lll_opy_(),
            bstack11l1_opy_ (u"ࠨࡶࡼࡴࡪ࠭᪪"): bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ᪫"),
            bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭᪬"): hook_type,
            bstack11l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ᪭"): hook_name
        }
        store[bstack11l1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᪮")].append(uuid)
        bstack1l1ll1l1111_opy_ = node.nodeid
        if hook_type == bstack11l1_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ᪯"):
            if not _11l1111l1l_opy_.get(bstack1l1ll1l1111_opy_, None):
                _11l1111l1l_opy_[bstack1l1ll1l1111_opy_] = {bstack11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᪰"): []}
            _11l1111l1l_opy_[bstack1l1ll1l1111_opy_][bstack11l1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᪱")].append(bstack111lllllll_opy_[bstack11l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ᪲")])
        _11l1111l1l_opy_[bstack1l1ll1l1111_opy_ + bstack11l1_opy_ (u"ࠪ࠱ࠬ᪳") + hook_name] = bstack111lllllll_opy_
        bstack1l1ll1llll1_opy_(node, bstack111lllllll_opy_, bstack11l1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ᪴"))
    elif event == bstack11l1_opy_ (u"ࠬࡧࡦࡵࡧࡵ᪵ࠫ"):
        bstack11l1ll1l1l_opy_ = node.nodeid + bstack11l1_opy_ (u"࠭࠭ࠨ᪶") + hook_name
        _11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸ᪷ࠬ")] = bstack11l1l1lll_opy_()
        bstack1l1ll11l1l1_opy_(_11l1111l1l_opy_[bstack11l1ll1l1l_opy_][bstack11l1_opy_ (u"ࠨࡷࡸ࡭ࡩ᪸࠭")])
        bstack1l1ll1llll1_opy_(node, _11l1111l1l_opy_[bstack11l1ll1l1l_opy_], bstack11l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧ᪹ࠫ"), bstack1l1ll1lll11_opy_=bstack1l1ll1l1l11_opy_)
def bstack1l1ll1l1lll_opy_():
    global bstack1l1ll11l111_opy_
    if bstack1l1lll111l_opy_():
        bstack1l1ll11l111_opy_ = bstack11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪ᪺ࠧ")
    else:
        bstack1l1ll11l111_opy_ = bstack11l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ᪻")
@bstack1ll1llllll_opy_.bstack1l1lllll111_opy_
def bstack1l1ll11l1ll_opy_():
    bstack1l1ll1l1lll_opy_()
    if bstack1llll1lll1_opy_():
        bstack11l1ll1l_opy_(bstack11l111111_opy_)
    try:
        bstack1lll1ll111l_opy_(bstack1l1ll111111_opy_)
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨ᪼").format(e))
bstack1l1ll11l1ll_opy_()