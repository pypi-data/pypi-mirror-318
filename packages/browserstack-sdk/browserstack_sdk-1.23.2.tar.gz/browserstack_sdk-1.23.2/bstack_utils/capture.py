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
import builtins
import logging
class bstack11l1ll11ll_opy_:
    def __init__(self, handler):
        self._1111ll111l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._1111ll1ll1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l1_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ၔ"), bstack11l1_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨၕ"), bstack11l1_opy_ (u"ࠪࡻࡦࡸ࡮ࡪࡰࡪࠫၖ"), bstack11l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪၗ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._1111ll1l11_opy_
        self._1111ll11ll_opy_()
    def _1111ll1l11_opy_(self, *args, **kwargs):
        self._1111ll111l_opy_(*args, **kwargs)
        message = bstack11l1_opy_ (u"ࠬࠦࠧၘ").join(map(str, args)) + bstack11l1_opy_ (u"࠭࡜࡯ࠩၙ")
        self._log_message(bstack11l1_opy_ (u"ࠧࡊࡐࡉࡓࠬၚ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧၛ"): level, bstack11l1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪၜ"): msg})
    def _1111ll11ll_opy_(self):
        for level, bstack1111ll11l1_opy_ in self._1111ll1ll1_opy_.items():
            setattr(logging, level, self._1111ll1l1l_opy_(level, bstack1111ll11l1_opy_))
    def _1111ll1l1l_opy_(self, level, bstack1111ll11l1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack1111ll11l1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._1111ll111l_opy_
        for level, bstack1111ll11l1_opy_ in self._1111ll1ll1_opy_.items():
            setattr(logging, level, bstack1111ll11l1_opy_)