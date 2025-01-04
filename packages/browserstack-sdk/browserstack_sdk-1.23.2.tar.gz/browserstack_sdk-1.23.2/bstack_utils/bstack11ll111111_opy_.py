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
from uuid import uuid4
from bstack_utils.helper import bstack11l1l1lll_opy_, bstack1llllll1lll_opy_
from bstack_utils.bstack1l1llll1l1_opy_ import bstack1ll11lll1l1_opy_
class bstack11l1l111l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11l1l1l11l_opy_=None, framework=None, tags=[], scope=[], bstack1ll111ll1l1_opy_=None, bstack1ll11l11111_opy_=True, bstack1ll111lllll_opy_=None, bstack1l111l1ll1_opy_=None, result=None, duration=None, bstack11l11l1ll1_opy_=None, meta={}):
        self.bstack11l11l1ll1_opy_ = bstack11l11l1ll1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1ll11l11111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11l1l1l11l_opy_ = bstack11l1l1l11l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1ll111ll1l1_opy_ = bstack1ll111ll1l1_opy_
        self.bstack1ll111lllll_opy_ = bstack1ll111lllll_opy_
        self.bstack1l111l1ll1_opy_ = bstack1l111l1ll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack11l11l11l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l1l1l1_opy_(self, meta):
        self.meta = meta
    def bstack11l1lll1l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack1ll111l1111_opy_(self):
        bstack1ll111lll1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᜌ"): bstack1ll111lll1l_opy_,
            bstack11l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᜍ"): bstack1ll111lll1l_opy_,
            bstack11l1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᜎ"): bstack1ll111lll1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l1_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡸࡱࡪࡴࡴ࠻ࠢࠥᜏ") + key)
            setattr(self, key, val)
    def bstack1ll111llll1_opy_(self):
        return {
            bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᜐ"): self.name,
            bstack11l1_opy_ (u"ࠫࡧࡵࡤࡺࠩᜑ"): {
                bstack11l1_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᜒ"): bstack11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᜓ"),
                bstack11l1_opy_ (u"ࠧࡤࡱࡧࡩ᜔ࠬ"): self.code
            },
            bstack11l1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ᜕"): self.scope,
            bstack11l1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ᜖"): self.tags,
            bstack11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᜗"): self.framework,
            bstack11l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ᜘"): self.bstack11l1l1l11l_opy_
        }
    def bstack1ll111ll11l_opy_(self):
        return {
         bstack11l1_opy_ (u"ࠬࡳࡥࡵࡣࠪ᜙"): self.meta
        }
    def bstack1ll111lll11_opy_(self):
        return {
            bstack11l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩ᜚"): {
                bstack11l1_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫ᜛"): self.bstack1ll111ll1l1_opy_
            }
        }
    def bstack1ll111l11ll_opy_(self, bstack1ll111l111l_opy_, details):
        step = next(filter(lambda st: st[bstack11l1_opy_ (u"ࠨ࡫ࡧࠫ᜜")] == bstack1ll111l111l_opy_, self.meta[bstack11l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ᜝")]), None)
        step.update(details)
    def bstack1ll111ll1_opy_(self, bstack1ll111l111l_opy_):
        step = next(filter(lambda st: st[bstack11l1_opy_ (u"ࠪ࡭ࡩ࠭᜞")] == bstack1ll111l111l_opy_, self.meta[bstack11l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᜟ")]), None)
        step.update({
            bstack11l1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᜠ"): bstack11l1l1lll_opy_()
        })
    def bstack11l1l1llll_opy_(self, bstack1ll111l111l_opy_, result, duration=None):
        bstack1ll111lllll_opy_ = bstack11l1l1lll_opy_()
        if bstack1ll111l111l_opy_ is not None and self.meta.get(bstack11l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᜡ")):
            step = next(filter(lambda st: st[bstack11l1_opy_ (u"ࠧࡪࡦࠪᜢ")] == bstack1ll111l111l_opy_, self.meta[bstack11l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᜣ")]), None)
            step.update({
                bstack11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᜤ"): bstack1ll111lllll_opy_,
                bstack11l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᜥ"): duration if duration else bstack1llllll1lll_opy_(step[bstack11l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᜦ")], bstack1ll111lllll_opy_),
                bstack11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᜧ"): result.result,
                bstack11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᜨ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1ll111l11l1_opy_):
        if self.meta.get(bstack11l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᜩ")):
            self.meta[bstack11l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᜪ")].append(bstack1ll111l11l1_opy_)
        else:
            self.meta[bstack11l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᜫ")] = [ bstack1ll111l11l1_opy_ ]
    def bstack1ll111ll1ll_opy_(self):
        return {
            bstack11l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᜬ"): self.bstack11l11l11l1_opy_(),
            **self.bstack1ll111llll1_opy_(),
            **self.bstack1ll111l1111_opy_(),
            **self.bstack1ll111ll11l_opy_()
        }
    def bstack1ll111l1l1l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᜭ"): self.bstack1ll111lllll_opy_,
            bstack11l1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᜮ"): self.duration,
            bstack11l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᜯ"): self.result.result
        }
        if data[bstack11l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᜰ")] == bstack11l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᜱ"):
            data[bstack11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᜲ")] = self.result.bstack111ll111l1_opy_()
            data[bstack11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᜳ")] = [{bstack11l1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫᜴ࠧ"): self.result.bstack1lllllll1l1_opy_()}]
        return data
    def bstack1ll111l1lll_opy_(self):
        return {
            bstack11l1_opy_ (u"ࠬࡻࡵࡪࡦࠪ᜵"): self.bstack11l11l11l1_opy_(),
            **self.bstack1ll111llll1_opy_(),
            **self.bstack1ll111l1111_opy_(),
            **self.bstack1ll111l1l1l_opy_(),
            **self.bstack1ll111ll11l_opy_()
        }
    def bstack11l1l11l11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l1_opy_ (u"࠭ࡓࡵࡣࡵࡸࡪࡪࠧ᜶") in event:
            return self.bstack1ll111ll1ll_opy_()
        elif bstack11l1_opy_ (u"ࠧࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ᜷") in event:
            return self.bstack1ll111l1lll_opy_()
    def bstack11l111l1ll_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll111lllll_opy_ = time if time else bstack11l1l1lll_opy_()
        self.duration = duration if duration else bstack1llllll1lll_opy_(self.bstack11l1l1l11l_opy_, self.bstack1ll111lllll_opy_)
        if result:
            self.result = result
class bstack11l1lll11l_opy_(bstack11l1l111l1_opy_):
    def __init__(self, hooks=[], bstack11l1lllll1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11l1lllll1_opy_ = bstack11l1lllll1_opy_
        super().__init__(*args, **kwargs, bstack1l111l1ll1_opy_=bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹ࠭᜸"))
    @classmethod
    def bstack1ll111l1l11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1_opy_ (u"ࠩ࡬ࡨࠬ᜹"): id(step),
                bstack11l1_opy_ (u"ࠪࡸࡪࡾࡴࠨ᜺"): step.name,
                bstack11l1_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬ᜻"): step.keyword,
            })
        return bstack11l1lll11l_opy_(
            **kwargs,
            meta={
                bstack11l1_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭᜼"): {
                    bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᜽"): feature.name,
                    bstack11l1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ᜾"): feature.filename,
                    bstack11l1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭᜿"): feature.description
                },
                bstack11l1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫᝀ"): {
                    bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᝁ"): scenario.name
                },
                bstack11l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᝂ"): steps,
                bstack11l1_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧᝃ"): bstack1ll11lll1l1_opy_(test)
            }
        )
    def bstack1ll111l1ll1_opy_(self):
        return {
            bstack11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᝄ"): self.hooks
        }
    def bstack1ll11l1111l_opy_(self):
        if self.bstack11l1lllll1_opy_:
            return {
                bstack11l1_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᝅ"): self.bstack11l1lllll1_opy_
            }
        return {}
    def bstack1ll111l1lll_opy_(self):
        return {
            **super().bstack1ll111l1lll_opy_(),
            **self.bstack1ll111l1ll1_opy_()
        }
    def bstack1ll111ll1ll_opy_(self):
        return {
            **super().bstack1ll111ll1ll_opy_(),
            **self.bstack1ll11l1111l_opy_()
        }
    def bstack11l111l1ll_opy_(self):
        return bstack11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᝆ")
class bstack11l1ll1111_opy_(bstack11l1l111l1_opy_):
    def __init__(self, hook_type, *args,bstack11l1lllll1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1ll11l111l1_opy_ = None
        self.bstack11l1lllll1_opy_ = bstack11l1lllll1_opy_
        super().__init__(*args, **kwargs, bstack1l111l1ll1_opy_=bstack11l1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᝇ"))
    def bstack11l111l1l1_opy_(self):
        return self.hook_type
    def bstack1ll111ll111_opy_(self):
        return {
            bstack11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᝈ"): self.hook_type
        }
    def bstack1ll111l1lll_opy_(self):
        return {
            **super().bstack1ll111l1lll_opy_(),
            **self.bstack1ll111ll111_opy_()
        }
    def bstack1ll111ll1ll_opy_(self):
        return {
            **super().bstack1ll111ll1ll_opy_(),
            bstack11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩᝉ"): self.bstack1ll11l111l1_opy_,
            **self.bstack1ll111ll111_opy_()
        }
    def bstack11l111l1ll_opy_(self):
        return bstack11l1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᝊ")
    def bstack11l1ll11l1_opy_(self, bstack1ll11l111l1_opy_):
        self.bstack1ll11l111l1_opy_ = bstack1ll11l111l1_opy_