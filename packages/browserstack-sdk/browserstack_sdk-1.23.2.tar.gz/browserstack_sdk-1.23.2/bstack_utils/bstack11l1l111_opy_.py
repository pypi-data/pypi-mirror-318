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
import json
class bstack1111lll11l_opy_(object):
  bstack1llllllll_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"࠭ࡾࠨံ")), bstack11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ့ࠧ"))
  bstack1111lll1ll_opy_ = os.path.join(bstack1llllllll_opy_, bstack11l1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨး"))
  bstack1111lll111_opy_ = None
  perform_scan = None
  bstack1l1111l1_opy_ = None
  bstack11lll1llll_opy_ = None
  bstack111l1l1111_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l1_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨ္ࠫ")):
      cls.instance = super(bstack1111lll11l_opy_, cls).__new__(cls)
      cls.instance.bstack1111lll1l1_opy_()
    return cls.instance
  def bstack1111lll1l1_opy_(self):
    try:
      with open(self.bstack1111lll1ll_opy_, bstack11l1_opy_ (u"ࠪࡶ်ࠬ")) as bstack1ll1l11lll_opy_:
        bstack1111ll1lll_opy_ = bstack1ll1l11lll_opy_.read()
        data = json.loads(bstack1111ll1lll_opy_)
        if bstack11l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ျ") in data:
          self.bstack111l1ll1ll_opy_(data[bstack11l1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧြ")])
        if bstack11l1_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧွ") in data:
          self.bstack111l1ll11l_opy_(data[bstack11l1_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨှ")])
    except:
      pass
  def bstack111l1ll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11l1_opy_ (u"ࠨࡵࡦࡥࡳ࠭ဿ")]
      self.bstack1l1111l1_opy_ = scripts[bstack11l1_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭၀")]
      self.bstack11lll1llll_opy_ = scripts[bstack11l1_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧ၁")]
      self.bstack111l1l1111_opy_ = scripts[bstack11l1_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩ၂")]
  def bstack111l1ll1ll_opy_(self, bstack1111lll111_opy_):
    if bstack1111lll111_opy_ != None and len(bstack1111lll111_opy_) != 0:
      self.bstack1111lll111_opy_ = bstack1111lll111_opy_
  def store(self):
    try:
      with open(self.bstack1111lll1ll_opy_, bstack11l1_opy_ (u"ࠬࡽࠧ၃")) as file:
        json.dump({
          bstack11l1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣ၄"): self.bstack1111lll111_opy_,
          bstack11l1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣ၅"): {
            bstack11l1_opy_ (u"ࠣࡵࡦࡥࡳࠨ၆"): self.perform_scan,
            bstack11l1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨ၇"): self.bstack1l1111l1_opy_,
            bstack11l1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢ၈"): self.bstack11lll1llll_opy_,
            bstack11l1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤ၉"): self.bstack111l1l1111_opy_
          }
        }, file)
    except:
      pass
  def bstack1lll111lll_opy_(self, bstack1111llll11_opy_):
    try:
      return any(command.get(bstack11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ၊")) == bstack1111llll11_opy_ for command in self.bstack1111lll111_opy_)
    except:
      return False
bstack11l1l111_opy_ = bstack1111lll11l_opy_()