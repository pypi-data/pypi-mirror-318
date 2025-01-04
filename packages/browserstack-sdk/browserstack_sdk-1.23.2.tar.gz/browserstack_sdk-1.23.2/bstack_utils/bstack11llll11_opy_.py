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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11111lll1l_opy_, bstack11111l1lll_opy_
import tempfile
import json
bstack1lll1l111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫᕲ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l1_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨᕳ"),
      datefmt=bstack11l1_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ᕴ"),
      stream=sys.stdout
    )
  return logger
def bstack1lll1l11l1l_opy_():
  global bstack1lll1l111ll_opy_
  if os.path.exists(bstack1lll1l111ll_opy_):
    os.remove(bstack1lll1l111ll_opy_)
def bstack1l1111l11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l1lll1111_opy_(config, log_level):
  bstack1lll11lll1l_opy_ = log_level
  if bstack11l1_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᕵ") in config and config[bstack11l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᕶ")] in bstack11111lll1l_opy_:
    bstack1lll11lll1l_opy_ = bstack11111lll1l_opy_[config[bstack11l1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᕷ")]]
  if config.get(bstack11l1_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪᕸ"), False):
    logging.getLogger().setLevel(bstack1lll11lll1l_opy_)
    return bstack1lll11lll1l_opy_
  global bstack1lll1l111ll_opy_
  bstack1l1111l11_opy_()
  bstack1lll1l1l1l1_opy_ = logging.Formatter(
    fmt=bstack11l1_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᕹ"),
    datefmt=bstack11l1_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬᕺ")
  )
  bstack1lll11lllll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1lll1l111ll_opy_)
  file_handler.setFormatter(bstack1lll1l1l1l1_opy_)
  bstack1lll11lllll_opy_.setFormatter(bstack1lll1l1l1l1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1lll11lllll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭ᕻ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1lll11lllll_opy_.setLevel(bstack1lll11lll1l_opy_)
  logging.getLogger().addHandler(bstack1lll11lllll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1lll11lll1l_opy_
def bstack1lll1l1l111_opy_(config):
  try:
    bstack1lll1l11l11_opy_ = set(bstack11111l1lll_opy_)
    bstack1lll1l11lll_opy_ = bstack11l1_opy_ (u"ࠬ࠭ᕼ")
    with open(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩᕽ")) as bstack1lll1l1l11l_opy_:
      bstack1lll1l11ll1_opy_ = bstack1lll1l1l11l_opy_.read()
      bstack1lll1l11lll_opy_ = re.sub(bstack11l1_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨᕾ"), bstack11l1_opy_ (u"ࠨࠩᕿ"), bstack1lll1l11ll1_opy_, flags=re.M)
      bstack1lll1l11lll_opy_ = re.sub(
        bstack11l1_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬᖀ") + bstack11l1_opy_ (u"ࠪࢀࠬᖁ").join(bstack1lll1l11l11_opy_) + bstack11l1_opy_ (u"ࠫ࠮࠴ࠪࠥࠩᖂ"),
        bstack11l1_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧᖃ"),
        bstack1lll1l11lll_opy_, flags=re.M | re.I
      )
    def bstack1lll1l11111_opy_(dic):
      bstack1lll1l111l1_opy_ = {}
      for key, value in dic.items():
        if key in bstack1lll1l11l11_opy_:
          bstack1lll1l111l1_opy_[key] = bstack11l1_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪᖄ")
        else:
          if isinstance(value, dict):
            bstack1lll1l111l1_opy_[key] = bstack1lll1l11111_opy_(value)
          else:
            bstack1lll1l111l1_opy_[key] = value
      return bstack1lll1l111l1_opy_
    bstack1lll1l111l1_opy_ = bstack1lll1l11111_opy_(config)
    return {
      bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪᖅ"): bstack1lll1l11lll_opy_,
      bstack11l1_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᖆ"): json.dumps(bstack1lll1l111l1_opy_)
    }
  except Exception as e:
    return {}
def bstack1ll11l1ll1_opy_(config):
  global bstack1lll1l111ll_opy_
  try:
    if config.get(bstack11l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᖇ"), False):
      return
    uuid = os.getenv(bstack11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᖈ"))
    if not uuid or uuid == bstack11l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᖉ"):
      return
    bstack1lll11llll1_opy_ = [bstack11l1_opy_ (u"ࠬࡸࡥࡲࡷ࡬ࡶࡪࡳࡥ࡯ࡶࡶ࠲ࡹࡾࡴࠨᖊ"), bstack11l1_opy_ (u"࠭ࡐࡪࡲࡩ࡭ࡱ࡫ࠧᖋ"), bstack11l1_opy_ (u"ࠧࡱࡻࡳࡶࡴࡰࡥࡤࡶ࠱ࡸࡴࡳ࡬ࠨᖌ"), bstack1lll1l111ll_opy_]
    bstack1l1111l11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧᖍ") + uuid + bstack11l1_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪᖎ"))
    with tarfile.open(output_file, bstack11l1_opy_ (u"ࠥࡻ࠿࡭ࡺࠣᖏ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1lll11llll1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1lll1l1l111_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1lll1l1111l_opy_ = data.encode()
        tarinfo.size = len(bstack1lll1l1111l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1lll1l1111l_opy_))
    bstack11ll111lll_opy_ = MultipartEncoder(
      fields= {
        bstack11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩᖐ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l1_opy_ (u"ࠬࡸࡢࠨᖑ")), bstack11l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫᖒ")),
        bstack11l1_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᖓ"): uuid
      }
    )
    response = requests.post(
      bstack11l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡸࡴࡱࡵࡡࡥ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥᖔ"),
      data=bstack11ll111lll_opy_,
      headers={bstack11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᖕ"): bstack11ll111lll_opy_.content_type},
      auth=(config[bstack11l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᖖ")], config[bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᖗ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫᖘ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬᖙ") + str(e))
  finally:
    try:
      bstack1lll1l11l1l_opy_()
    except:
      pass