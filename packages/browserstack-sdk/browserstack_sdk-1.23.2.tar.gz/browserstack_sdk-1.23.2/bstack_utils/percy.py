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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1l11l111ll_opy_, bstack11ll1l11ll_opy_
from bstack_utils.measure import measure
class bstack1l1l1ll11l_opy_:
  working_dir = os.getcwd()
  bstack1lll1l1111_opy_ = False
  config = {}
  binary_path = bstack11l1_opy_ (u"࠭ࠧᗦ")
  bstack1lll111l1ll_opy_ = bstack11l1_opy_ (u"ࠧࠨᗧ")
  bstack1l1l111l11_opy_ = False
  bstack1lll11l1l11_opy_ = None
  bstack1ll1ll1l1l1_opy_ = {}
  bstack1ll1lllll11_opy_ = 300
  bstack1lll11l1ll1_opy_ = False
  logger = None
  bstack1ll1lll1111_opy_ = False
  bstack11lllll1_opy_ = False
  bstack1l111l1l1l_opy_ = None
  bstack1ll1ll1llll_opy_ = bstack11l1_opy_ (u"ࠨࠩᗨ")
  bstack1lll111111l_opy_ = {
    bstack11l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᗩ") : 1,
    bstack11l1_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫᗪ") : 2,
    bstack11l1_opy_ (u"ࠫࡪࡪࡧࡦࠩᗫ") : 3,
    bstack11l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬᗬ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1ll1llll1l1_opy_(self):
    bstack1lll11111l1_opy_ = bstack11l1_opy_ (u"࠭ࠧᗭ")
    bstack1lll11l11l1_opy_ = sys.platform
    bstack1ll1lll1ll1_opy_ = bstack11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᗮ")
    if re.match(bstack11l1_opy_ (u"ࠣࡦࡤࡶࡼ࡯࡮ࡽ࡯ࡤࡧࠥࡵࡳࠣᗯ"), bstack1lll11l11l1_opy_) != None:
      bstack1lll11111l1_opy_ = bstack11111lll11_opy_ + bstack11l1_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡲࡷࡽ࠴ࡺࡪࡲࠥᗰ")
      self.bstack1ll1ll1llll_opy_ = bstack11l1_opy_ (u"ࠪࡱࡦࡩࠧᗱ")
    elif re.match(bstack11l1_opy_ (u"ࠦࡲࡹࡷࡪࡰࡿࡱࡸࡿࡳࡽ࡯࡬ࡲ࡬ࡽࡼࡤࡻࡪࡻ࡮ࡴࡼࡣࡥࡦࡻ࡮ࡴࡼࡸ࡫ࡱࡧࡪࢂࡥ࡮ࡥࡿࡻ࡮ࡴ࠳࠳ࠤᗲ"), bstack1lll11l11l1_opy_) != None:
      bstack1lll11111l1_opy_ = bstack11111lll11_opy_ + bstack11l1_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡽࡩ࡯࠰ࡽ࡭ࡵࠨᗳ")
      bstack1ll1lll1ll1_opy_ = bstack11l1_opy_ (u"ࠨࡰࡦࡴࡦࡽ࠳࡫ࡸࡦࠤᗴ")
      self.bstack1ll1ll1llll_opy_ = bstack11l1_opy_ (u"ࠧࡸ࡫ࡱࠫᗵ")
    else:
      bstack1lll11111l1_opy_ = bstack11111lll11_opy_ + bstack11l1_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮࡮࡬ࡲࡺࡾ࠮ࡻ࡫ࡳࠦᗶ")
      self.bstack1ll1ll1llll_opy_ = bstack11l1_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨᗷ")
    return bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_
  def bstack1lll111l11l_opy_(self):
    try:
      bstack1lll1111l11_opy_ = [os.path.join(expanduser(bstack11l1_opy_ (u"ࠥࢂࠧᗸ")), bstack11l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᗹ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lll1111l11_opy_:
        if(self.bstack1ll1lll1lll_opy_(path)):
          return path
      raise bstack11l1_opy_ (u"࡛ࠧ࡮ࡢ࡮ࡥࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤᗺ")
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࠱ࠥࢁࡽࠣᗻ").format(e))
  def bstack1ll1lll1lll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  @measure(event_name=EVENTS.bstack11111l1ll1_opy_, stage=STAGE.SINGLE)
  def bstack1ll1llllll1_opy_(self, bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_):
    try:
      bstack1ll1lll1l11_opy_ = self.bstack1lll111l11l_opy_()
      bstack1lll11111ll_opy_ = os.path.join(bstack1ll1lll1l11_opy_, bstack11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴ࡺࡪࡲࠪᗼ"))
      bstack1lll111llll_opy_ = os.path.join(bstack1ll1lll1l11_opy_, bstack1ll1lll1ll1_opy_)
      if os.path.exists(bstack1lll111llll_opy_):
        self.logger.info(bstack11l1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡳ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᗽ").format(bstack1lll111llll_opy_))
        return bstack1lll111llll_opy_
      if os.path.exists(bstack1lll11111ll_opy_):
        self.logger.info(bstack11l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡼ࡬ࡴࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡺࡴࡺࡪࡲࡳ࡭ࡳ࡭ࠢᗾ").format(bstack1lll11111ll_opy_))
        return self.bstack1ll1ll1lll1_opy_(bstack1lll11111ll_opy_, bstack1ll1lll1ll1_opy_)
      self.logger.info(bstack11l1_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱࠥࢁࡽࠣᗿ").format(bstack1lll11111l1_opy_))
      response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠫࡌࡋࡔࠨᘀ"), bstack1lll11111l1_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1lll11111ll_opy_, bstack11l1_opy_ (u"ࠬࡽࡢࠨᘁ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡤࡲࡩࠦࡳࡢࡸࡨࡨࠥࡧࡴࠡࡽࢀࠦᘂ").format(bstack1lll11111ll_opy_))
        return self.bstack1ll1ll1lll1_opy_(bstack1lll11111ll_opy_, bstack1ll1lll1ll1_opy_)
      else:
        raise(bstack11l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡺࡨࡦࠢࡩ࡭ࡱ࡫࠮ࠡࡕࡷࡥࡹࡻࡳࠡࡥࡲࡨࡪࡀࠠࡼࡿࠥᘃ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤᘄ").format(e))
  def bstack1lll1111ll1_opy_(self, bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_):
    try:
      retry = 2
      bstack1lll111llll_opy_ = None
      bstack1ll1ll11ll1_opy_ = False
      while retry > 0:
        bstack1lll111llll_opy_ = self.bstack1ll1llllll1_opy_(bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_)
        bstack1ll1ll11ll1_opy_ = self.bstack1ll1ll11lll_opy_(bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_, bstack1lll111llll_opy_)
        if bstack1ll1ll11ll1_opy_:
          break
        retry -= 1
      return bstack1lll111llll_opy_, bstack1ll1ll11ll1_opy_
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡲࡤࡸ࡭ࠨᘅ").format(e))
    return bstack1lll111llll_opy_, False
  def bstack1ll1ll11lll_opy_(self, bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_, bstack1lll111llll_opy_, bstack1ll1lllll1l_opy_ = 0):
    if bstack1ll1lllll1l_opy_ > 1:
      return False
    if bstack1lll111llll_opy_ == None or os.path.exists(bstack1lll111llll_opy_) == False:
      self.logger.warn(bstack11l1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡷ࡫ࡴࡳࡻ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣᘆ"))
      return False
    bstack1lll11l11ll_opy_ = bstack11l1_opy_ (u"ࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࡜࠰ࡥ࡯࡭ࠥࡢࡤ࠯࡞ࡧ࠯࠳ࡢࡤࠬࠤᘇ")
    command = bstack11l1_opy_ (u"ࠬࢁࡽࠡ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫᘈ").format(bstack1lll111llll_opy_)
    bstack1lll11l1111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lll11l11ll_opy_, bstack1lll11l1111_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡣࡩࡧࡦ࡯ࠥ࡬ࡡࡪ࡮ࡨࡨࠧᘉ"))
      return False
  def bstack1ll1ll1lll1_opy_(self, bstack1lll11111ll_opy_, bstack1ll1lll1ll1_opy_):
    try:
      working_dir = os.path.dirname(bstack1lll11111ll_opy_)
      shutil.unpack_archive(bstack1lll11111ll_opy_, working_dir)
      bstack1lll111llll_opy_ = os.path.join(working_dir, bstack1ll1lll1ll1_opy_)
      os.chmod(bstack1lll111llll_opy_, 0o755)
      return bstack1lll111llll_opy_
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡹࡳࢀࡩࡱࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣᘊ"))
  def bstack1lll111l1l1_opy_(self):
    try:
      bstack1lll111lll1_opy_ = self.config.get(bstack11l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᘋ"))
      bstack1lll111l1l1_opy_ = bstack1lll111lll1_opy_ or (bstack1lll111lll1_opy_ is None and self.bstack1lll1l1111_opy_)
      if not bstack1lll111l1l1_opy_ or self.config.get(bstack11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᘌ"), None) not in bstack1111l1l1ll_opy_:
        return False
      self.bstack1l1l111l11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᘍ").format(e))
  def bstack1ll1llll111_opy_(self):
    try:
      bstack1ll1llll111_opy_ = self.bstack1lll1111lll_opy_
      return bstack1ll1llll111_opy_
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾࠦࡣࡢࡲࡷࡹࡷ࡫ࠠ࡮ࡱࡧࡩ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᘎ").format(e))
  def init(self, bstack1lll1l1111_opy_, config, logger):
    self.bstack1lll1l1111_opy_ = bstack1lll1l1111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lll111l1l1_opy_():
      return
    self.bstack1ll1ll1l1l1_opy_ = config.get(bstack11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫᘏ"), {})
    self.bstack1lll1111lll_opy_ = config.get(bstack11l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᘐ"))
    try:
      bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_ = self.bstack1ll1llll1l1_opy_()
      bstack1lll111llll_opy_, bstack1ll1ll11ll1_opy_ = self.bstack1lll1111ll1_opy_(bstack1lll11111l1_opy_, bstack1ll1lll1ll1_opy_)
      if bstack1ll1ll11ll1_opy_:
        self.binary_path = bstack1lll111llll_opy_
        thread = Thread(target=self.bstack1lll111ll1l_opy_)
        thread.start()
      else:
        self.bstack1ll1lll1111_opy_ = True
        self.logger.error(bstack11l1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾ࠮࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡖࡥࡳࡥࡼࠦᘑ").format(bstack1lll111llll_opy_))
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᘒ").format(e))
  def bstack1ll1ll1l1ll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l1_opy_ (u"ࠩ࡯ࡳ࡬࠭ᘓ"), bstack11l1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰࡯ࡳ࡬࠭ᘔ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l1_opy_ (u"ࠦࡕࡻࡳࡩ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࡴࠢࡤࡸࠥࢁࡽࠣᘕ").format(logfile))
      self.bstack1lll111l1ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࠡࡲࡤࡸ࡭࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᘖ").format(e))
  @measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.SINGLE)
  def bstack1lll111ll1l_opy_(self):
    bstack1ll1ll1ll1l_opy_ = self.bstack1ll1lll11l1_opy_()
    if bstack1ll1ll1ll1l_opy_ == None:
      self.bstack1ll1lll1111_opy_ = True
      self.logger.error(bstack11l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠤᘗ"))
      return False
    command_args = [bstack11l1_opy_ (u"ࠢࡢࡲࡳ࠾ࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠣᘘ") if self.bstack1lll1l1111_opy_ else bstack11l1_opy_ (u"ࠨࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠬᘙ")]
    bstack1ll1ll11l1l_opy_ = self.bstack1ll1ll111ll_opy_()
    if bstack1ll1ll11l1l_opy_ != None:
      command_args.append(bstack11l1_opy_ (u"ࠤ࠰ࡧࠥࢁࡽࠣᘚ").format(bstack1ll1ll11l1l_opy_))
    env = os.environ.copy()
    env[bstack11l1_opy_ (u"ࠥࡔࡊࡘࡃ࡚ࡡࡗࡓࡐࡋࡎࠣᘛ")] = bstack1ll1ll1ll1l_opy_
    env[bstack11l1_opy_ (u"࡙ࠦࡎ࡟ࡃࡗࡌࡐࡉࡥࡕࡖࡋࡇࠦᘜ")] = os.environ.get(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᘝ"), bstack11l1_opy_ (u"࠭ࠧᘞ"))
    bstack1ll1lll111l_opy_ = [self.binary_path]
    self.bstack1ll1ll1l1ll_opy_()
    self.bstack1lll11l1l11_opy_ = self.bstack1lll1111l1l_opy_(bstack1ll1lll111l_opy_ + command_args, env)
    self.logger.debug(bstack11l1_opy_ (u"ࠢࡔࡶࡤࡶࡹ࡯࡮ࡨࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠣᘟ"))
    bstack1ll1lllll1l_opy_ = 0
    while self.bstack1lll11l1l11_opy_.poll() == None:
      bstack1lll11l111l_opy_ = self.bstack1ll1ll11l11_opy_()
      if bstack1lll11l111l_opy_:
        self.logger.debug(bstack11l1_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠦᘠ"))
        self.bstack1lll11l1ll1_opy_ = True
        return True
      bstack1ll1lllll1l_opy_ += 1
      self.logger.debug(bstack11l1_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡔࡨࡸࡷࡿࠠ࠮ࠢࡾࢁࠧᘡ").format(bstack1ll1lllll1l_opy_))
      time.sleep(2)
    self.logger.error(bstack11l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡋࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࠦࡡࡵࡶࡨࡱࡵࡺࡳࠣᘢ").format(bstack1ll1lllll1l_opy_))
    self.bstack1ll1lll1111_opy_ = True
    return False
  def bstack1ll1ll11l11_opy_(self, bstack1ll1lllll1l_opy_ = 0):
    if bstack1ll1lllll1l_opy_ > 10:
      return False
    try:
      bstack1ll1llll1ll_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡗࡊࡘࡖࡆࡔࡢࡅࡉࡊࡒࡆࡕࡖࠫᘣ"), bstack11l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡲ࡯ࡤࡣ࡯࡬ࡴࡹࡴ࠻࠷࠶࠷࠽࠭ᘤ"))
      bstack1ll1ll1l111_opy_ = bstack1ll1llll1ll_opy_ + bstack11111ll11l_opy_
      response = requests.get(bstack1ll1ll1l111_opy_)
      data = response.json()
      self.bstack1l111l1l1l_opy_ = data.get(bstack11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࠬᘥ"), {}).get(bstack11l1_opy_ (u"ࠧࡪࡦࠪᘦ"), None)
      return True
    except:
      self.logger.debug(bstack11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷࡸࡥࡥࠢࡺ࡬࡮ࡲࡥࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢ࡮ࡷ࡬ࠥࡩࡨࡦࡥ࡮ࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨᘧ"))
      return False
  def bstack1ll1lll11l1_opy_(self):
    bstack1ll1lll1l1l_opy_ = bstack11l1_opy_ (u"ࠩࡤࡴࡵ࠭ᘨ") if self.bstack1lll1l1111_opy_ else bstack11l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᘩ")
    bstack1lll11l1l1l_opy_ = bstack11l1_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢᘪ") if self.config.get(bstack11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᘫ")) is None else True
    bstack111111l111_opy_ = bstack11l1_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠫࡶࡥࡳࡥࡼࡁࢀࢃࠢᘬ").format(self.config[bstack11l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᘭ")], bstack1ll1lll1l1l_opy_, bstack1lll11l1l1l_opy_)
    if self.bstack1lll1111lll_opy_:
      bstack111111l111_opy_ += bstack11l1_opy_ (u"ࠣࠨࡳࡩࡷࡩࡹࡠࡥࡤࡴࡹࡻࡲࡦࡡࡰࡳࡩ࡫࠽ࡼࡿࠥᘮ").format(self.bstack1lll1111lll_opy_)
    uri = bstack1l11l111ll_opy_(bstack111111l111_opy_)
    try:
      response = bstack11ll1l11ll_opy_(bstack11l1_opy_ (u"ࠩࡊࡉ࡙࠭ᘯ"), uri, {}, {bstack11l1_opy_ (u"ࠪࡥࡺࡺࡨࠨᘰ"): (self.config[bstack11l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᘱ")], self.config[bstack11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᘲ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1l111l11_opy_ = data.get(bstack11l1_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᘳ"))
        self.bstack1lll1111lll_opy_ = data.get(bstack11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࠬᘴ"))
        os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᘵ")] = str(self.bstack1l1l111l11_opy_)
        os.environ[bstack11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᘶ")] = str(self.bstack1lll1111lll_opy_)
        if bstack1lll11l1l1l_opy_ == bstack11l1_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᘷ") and str(self.bstack1l1l111l11_opy_).lower() == bstack11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᘸ"):
          self.bstack11lllll1_opy_ = True
        if bstack11l1_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᘹ") in data:
          return data[bstack11l1_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᘺ")]
        else:
          raise bstack11l1_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᘻ").format(data)
      else:
        raise bstack11l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᘼ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᘽ").format(e))
  def bstack1ll1ll111ll_opy_(self):
    bstack1ll1lllllll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᘾ"))
    try:
      if bstack11l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᘿ") not in self.bstack1ll1ll1l1l1_opy_:
        self.bstack1ll1ll1l1l1_opy_[bstack11l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᙀ")] = 2
      with open(bstack1ll1lllllll_opy_, bstack11l1_opy_ (u"࠭ࡷࠨᙁ")) as fp:
        json.dump(self.bstack1ll1ll1l1l1_opy_, fp)
      return bstack1ll1lllllll_opy_
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᙂ").format(e))
  def bstack1lll1111l1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1ll1ll1llll_opy_ == bstack11l1_opy_ (u"ࠨࡹ࡬ࡲࠬᙃ"):
        bstack1lll11l1lll_opy_ = [bstack11l1_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᙄ"), bstack11l1_opy_ (u"ࠪ࠳ࡨ࠭ᙅ")]
        cmd = bstack1lll11l1lll_opy_ + cmd
      cmd = bstack11l1_opy_ (u"ࠫࠥ࠭ᙆ").join(cmd)
      self.logger.debug(bstack11l1_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᙇ").format(cmd))
      with open(self.bstack1lll111l1ll_opy_, bstack11l1_opy_ (u"ࠨࡡࠣᙈ")) as bstack1lll1111111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lll1111111_opy_, text=True, stderr=bstack1lll1111111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1ll1lll1111_opy_ = True
      self.logger.error(bstack11l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᙉ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lll11l1ll1_opy_:
        self.logger.info(bstack11l1_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᙊ"))
        cmd = [self.binary_path, bstack11l1_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᙋ")]
        self.bstack1lll1111l1l_opy_(cmd)
        self.bstack1lll11l1ll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᙌ").format(cmd, e))
  def bstack11lllll111_opy_(self):
    if not self.bstack1l1l111l11_opy_:
      return
    try:
      bstack1ll1ll1l11l_opy_ = 0
      while not self.bstack1lll11l1ll1_opy_ and bstack1ll1ll1l11l_opy_ < self.bstack1ll1lllll11_opy_:
        if self.bstack1ll1lll1111_opy_:
          self.logger.info(bstack11l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤᙍ"))
          return
        time.sleep(1)
        bstack1ll1ll1l11l_opy_ += 1
      os.environ[bstack11l1_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᙎ")] = str(self.bstack1lll111l111_opy_())
      self.logger.info(bstack11l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᙏ"))
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᙐ").format(e))
  def bstack1lll111l111_opy_(self):
    if self.bstack1lll1l1111_opy_:
      return
    try:
      bstack1ll1llll11l_opy_ = [platform[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᙑ")].lower() for platform in self.config.get(bstack11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᙒ"), [])]
      bstack1ll1lll11ll_opy_ = sys.maxsize
      bstack1ll1ll1ll11_opy_ = bstack11l1_opy_ (u"ࠪࠫᙓ")
      for browser in bstack1ll1llll11l_opy_:
        if browser in self.bstack1lll111111l_opy_:
          bstack1lll111ll11_opy_ = self.bstack1lll111111l_opy_[browser]
        if bstack1lll111ll11_opy_ < bstack1ll1lll11ll_opy_:
          bstack1ll1lll11ll_opy_ = bstack1lll111ll11_opy_
          bstack1ll1ll1ll11_opy_ = browser
      return bstack1ll1ll1ll11_opy_
    except Exception as e:
      self.logger.error(bstack11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᙔ").format(e))
  @classmethod
  def bstack11ll1l1lll_opy_(self):
    return os.getenv(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᙕ"), bstack11l1_opy_ (u"࠭ࡆࡢ࡮ࡶࡩࠬᙖ")).lower()
  @classmethod
  def bstack11ll11ll1l_opy_(self):
    return os.getenv(bstack11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᙗ"), bstack11l1_opy_ (u"ࠨࠩᙘ"))