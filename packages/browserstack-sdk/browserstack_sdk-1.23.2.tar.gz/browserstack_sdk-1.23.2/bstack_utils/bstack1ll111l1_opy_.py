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
import fcntl
import json
import os
import time
import uuid
from typing import Dict, List, Optional
from bstack_utils.constants import bstack11111lllll_opy_, EVENTS
from bstack_utils.helper import bstack11ll1l11ll_opy_, get_host_info, bstack1l1l1lll1_opy_
from datetime import datetime
from bstack_utils.bstack11llll11_opy_ import get_logger
logger = get_logger(__name__)
bstack1ll1l1l11ll_opy_: Dict[str, float] = {}
bstack1ll1l11lll1_opy_: List = []
bstack1ll1l11llll_opy_ = os.path.join(os.getcwd(), bstack11l1_opy_ (u"ࠪࡰࡴ࡭ࠧᙚ"), bstack11l1_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧᙛ"))
class bstack1ll1l1l11l1_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    def __init__(self, duration: float, name: str, start_time: float, bstack1ll1l1l1l11_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack1ll1l1l1l11_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l1_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࠨᙜ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
class bstack111l1l11l1_opy_:
    global bstack1ll1l1l11ll_opy_
    @staticmethod
    def mark(key: str) -> None:
        bstack1ll1l1l11ll_opy_[key] = time.time_ns() / 1000000
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        bstack111l1l11l1_opy_.mark(end)
        bstack111l1l11l1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        if start not in bstack1ll1l1l11ll_opy_ or end not in bstack1ll1l1l11ll_opy_:
            logger.debug(bstack11l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠤࡴࡸࠠࡦࡰࡧࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠣᙝ").format(start,end))
            return
        duration: float = bstack1ll1l1l11ll_opy_[end] - bstack1ll1l1l11ll_opy_[start]
        bstack1ll1l11ll1l_opy_: bstack1ll1l1l11l1_opy_ = bstack1ll1l1l11l1_opy_(duration, label, bstack1ll1l1l11ll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᙞ"), 0), command, test_name, hook_type)
        del bstack1ll1l1l11ll_opy_[start]
        del bstack1ll1l1l11ll_opy_[end]
        bstack111l1l11l1_opy_.bstack1ll1l11ll11_opy_(bstack1ll1l11ll1l_opy_)
        if label == EVENTS.bstack1l111l111l_opy_.value:
            bstack111l1l11l1_opy_.bstack11l111111l_opy_()
    @staticmethod
    def bstack1ll1l11ll11_opy_(bstack1ll1l11ll1l_opy_):
        os.makedirs(os.path.dirname(bstack1ll1l11llll_opy_)) if not os.path.exists(os.path.dirname(bstack1ll1l11llll_opy_)) else None
        try:
            with open(bstack1ll1l11llll_opy_, bstack11l1_opy_ (u"ࠣࡴ࠮ࠦᙟ"), encoding=bstack11l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᙠ")) as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                data.append(bstack1ll1l11ll1l_opy_.__dict__)
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                fcntl.flock(file, fcntl.LOCK_UN)
        except FileNotFoundError:
            with open(bstack1ll1l11llll_opy_, bstack11l1_opy_ (u"ࠥࡻࠧᙡ"), encoding=bstack11l1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᙢ")) as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                data = [bstack1ll1l11ll1l_opy_.__dict__]
                json.dump(data, file, indent=4)
                fcntl.flock(file, fcntl.LOCK_UN)
    @staticmethod
    def bstack11l111111l_opy_():
        try:
            with open(bstack1ll1l11llll_opy_, bstack11l1_opy_ (u"ࠧࡸࠢᙣ"), encoding=bstack11l1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᙤ")) as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                data = json.load(file)
                config = {
                    bstack11l1_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣᙥ"): {
                        bstack11l1_opy_ (u"ࠣࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠢᙦ"): bstack11l1_opy_ (u"ࠤࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠧᙧ"),
                    }
                }
                bstack1ll1l1l1111_opy_ = datetime.utcnow()
                bstack11l1l1lll_opy_ = bstack1ll1l1l1111_opy_.strftime(bstack11l1_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨ࡙࡙ࠣࡉࠢᙨ"))
                bstack1ll1l1l111l_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᙩ")) if os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᙪ")) else bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣᙫ"))
                payload = {
                    bstack11l1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠦᙬ"): bstack11l1_opy_ (u"ࠣࡵࡧ࡯ࡤ࡫ࡶࡦࡰࡷࡷࠧ᙭"),
                    bstack11l1_opy_ (u"ࠤࡧࡥࡹࡧࠢ᙮"): {
                        bstack11l1_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠤᙯ"): bstack1ll1l1l111l_opy_,
                        bstack11l1_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࡤࡪࡡࡺࠤᙰ"): bstack11l1l1lll_opy_,
                        bstack11l1_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࠤᙱ"): bstack11l1_opy_ (u"ࠨࡓࡅࡍࡉࡩࡦࡺࡵࡳࡧࡓࡩࡷ࡬࡯ࡳ࡯ࡤࡲࡨ࡫ࠢᙲ"),
                        bstack11l1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡪࡴࡱࡱࠦᙳ"): {
                            bstack11l1_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࡵࠥᙴ"): data
                        },
                        bstack11l1_opy_ (u"ࠤࡸࡷࡪࡸ࡟ࡥࡣࡷࡥࠧᙵ"): bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧᙶ")),
                        bstack11l1_opy_ (u"ࠦ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠢᙷ"): get_host_info()
                    }
                }
                response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠧࡖࡏࡔࡖࠥᙸ"), bstack11111lllll_opy_, payload, config)
                if(response.status_code >= 200 and response.status_code < 300):
                    logger.debug(bstack11l1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨᙹ").format(bstack11111lllll_opy_, payload))
                else:
                    logger.debug(bstack11l1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢᙺ").format(bstack11111lllll_opy_, payload))
                fcntl.flock(file, fcntl.LOCK_UN)
        except Exception as e:
            logger.debug(bstack11l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧᙻ").format(e))
        os.remove(bstack1ll1l11llll_opy_)
    @staticmethod
    def bstack1111llllll_opy_(label: str) -> str:
        return bstack11l1_opy_ (u"ࠤࡾࢁ࠿ࢁࡽࠣᙼ").format(label,str(uuid.uuid4().hex)[:6])