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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11llll11_opy_ import get_logger
from bstack_utils.bstack1ll111l1_opy_ import bstack111l1l11l1_opy_
bstack1ll111l1_opy_ = bstack111l1l11l1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1lll11l11l_opy_: Optional[str] = None):
    bstack11l1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡅࡧࡦࡳࡷࡧࡴࡰࡴࠣࡸࡴࠦ࡬ࡰࡩࠣࡸ࡭࡫ࠠࡴࡶࡤࡶࡹࠦࡴࡪ࡯ࡨࠤࡴ࡬ࠠࡢࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࡦࡲ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺࠠ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡶࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᖚ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1111lllll1_opy_: str = bstack1ll111l1_opy_.bstack1111llllll_opy_(label)
            start_mark: str = label + bstack11l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᖛ")
            end_mark: str = label + bstack11l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᖜ")
            result = None
            try:
                if stage.value == STAGE.bstack1111l1l1l_opy_.value:
                    bstack1ll111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1lll11l11l_opy_)
                elif stage.value == STAGE.SINGLE.value:
                    start_mark: str = bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᖝ")
                    end_mark: str = bstack1111lllll1_opy_ + bstack11l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᖞ")
                    bstack1ll111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1lll11l11l_opy_)
            except Exception as e:
                bstack1ll111l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1lll11l11l_opy_)
            return result
        return wrapper
    return decorator