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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1111l1l11l_opy_, bstack11llll1l11_opy_, bstack1llllll11l_opy_, bstack1l1l11l111_opy_,
                                    bstack11111l11ll_opy_, bstack11111ll1l1_opy_, bstack11111l1lll_opy_, bstack11111llll1_opy_)
from bstack_utils.messages import bstack11111llll_opy_, bstack11ll11llll_opy_
from bstack_utils.proxy import bstack1l1l1l1ll_opy_, bstack1ll11ll111_opy_
bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
logger = logging.getLogger(__name__)
def bstack111l1111ll_opy_(config):
    return config[bstack11l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ፭")]
def bstack111l11llll_opy_(config):
    return config[bstack11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ፮")]
def bstack111l111l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1lllll1l1ll_opy_(obj):
    values = []
    bstack1llll11l111_opy_ = re.compile(bstack11l1_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤ፯"), re.I)
    for key in obj.keys():
        if bstack1llll11l111_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1llllll111l_opy_(config):
    tags = []
    tags.extend(bstack1lllll1l1ll_opy_(os.environ))
    tags.extend(bstack1lllll1l1ll_opy_(config))
    return tags
def bstack1llll1l11ll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1lllll1ll1l_opy_(bstack1llll11l1l1_opy_):
    if not bstack1llll11l1l1_opy_:
        return bstack11l1_opy_ (u"࠭ࠧ፰")
    return bstack11l1_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣ፱").format(bstack1llll11l1l1_opy_.name, bstack1llll11l1l1_opy_.email)
def bstack111l1l11ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1llll1111l1_opy_ = repo.common_dir
        info = {
            bstack11l1_opy_ (u"ࠣࡵ࡫ࡥࠧ፲"): repo.head.commit.hexsha,
            bstack11l1_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧ፳"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l1_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥ፴"): repo.active_branch.name,
            bstack11l1_opy_ (u"ࠦࡹࡧࡧࠣ፵"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣ፶"): bstack1lllll1ll1l_opy_(repo.head.commit.committer),
            bstack11l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢ፷"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢ፸"): bstack1lllll1ll1l_opy_(repo.head.commit.author),
            bstack11l1_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨ፹"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l1_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥ፺"): repo.head.commit.message,
            bstack11l1_opy_ (u"ࠥࡶࡴࡵࡴࠣ፻"): repo.git.rev_parse(bstack11l1_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨ፼")),
            bstack11l1_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨ፽"): bstack1llll1111l1_opy_,
            bstack11l1_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤ፾"): subprocess.check_output([bstack11l1_opy_ (u"ࠢࡨ࡫ࡷࠦ፿"), bstack11l1_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦᎀ"), bstack11l1_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧᎁ")]).strip().decode(
                bstack11l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᎂ")),
            bstack11l1_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᎃ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᎄ"): repo.git.rev_list(
                bstack11l1_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᎅ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1llllllll11_opy_ = []
        for remote in remotes:
            bstack1llllll1l1l_opy_ = {
                bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᎆ"): remote.name,
                bstack11l1_opy_ (u"ࠣࡷࡵࡰࠧᎇ"): remote.url,
            }
            bstack1llllllll11_opy_.append(bstack1llllll1l1l_opy_)
        bstack1111111lll_opy_ = {
            bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎈ"): bstack11l1_opy_ (u"ࠥ࡫࡮ࡺࠢᎉ"),
            **info,
            bstack11l1_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᎊ"): bstack1llllllll11_opy_
        }
        bstack1111111lll_opy_ = bstack1llll11llll_opy_(bstack1111111lll_opy_)
        return bstack1111111lll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᎋ").format(err))
        return {}
def bstack1llll11llll_opy_(bstack1111111lll_opy_):
    bstack1llll1lll1l_opy_ = bstack1lllllllll1_opy_(bstack1111111lll_opy_)
    if bstack1llll1lll1l_opy_ and bstack1llll1lll1l_opy_ > bstack11111l11ll_opy_:
        bstack1llll11lll1_opy_ = bstack1llll1lll1l_opy_ - bstack11111l11ll_opy_
        bstack111111ll1l_opy_ = bstack1llll11l11l_opy_(bstack1111111lll_opy_[bstack11l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᎌ")], bstack1llll11lll1_opy_)
        bstack1111111lll_opy_[bstack11l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᎍ")] = bstack111111ll1l_opy_
        logger.info(bstack11l1_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᎎ")
                    .format(bstack1lllllllll1_opy_(bstack1111111lll_opy_) / 1024))
    return bstack1111111lll_opy_
def bstack1lllllllll1_opy_(bstack1ll1l11l1l_opy_):
    try:
        if bstack1ll1l11l1l_opy_:
            bstack1lllll111ll_opy_ = json.dumps(bstack1ll1l11l1l_opy_)
            bstack1llll1l1111_opy_ = sys.getsizeof(bstack1lllll111ll_opy_)
            return bstack1llll1l1111_opy_
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᎏ").format(e))
    return -1
def bstack1llll11l11l_opy_(field, bstack1llll111lll_opy_):
    try:
        bstack1111111l11_opy_ = len(bytes(bstack11111ll1l1_opy_, bstack11l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᎐")))
        bstack1llll1l11l1_opy_ = bytes(field, bstack11l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᎑"))
        bstack11111111l1_opy_ = len(bstack1llll1l11l1_opy_)
        bstack1llllll1111_opy_ = ceil(bstack11111111l1_opy_ - bstack1llll111lll_opy_ - bstack1111111l11_opy_)
        if bstack1llllll1111_opy_ > 0:
            bstack1llll1l111l_opy_ = bstack1llll1l11l1_opy_[:bstack1llllll1111_opy_].decode(bstack11l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᎒"), errors=bstack11l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭᎓")) + bstack11111ll1l1_opy_
            return bstack1llll1l111l_opy_
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧ᎔").format(e))
    return field
def bstack1l11ll1111_opy_():
    env = os.environ
    if (bstack11l1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ᎕") in env and len(env[bstack11l1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᎖")]) > 0) or (
            bstack11l1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᎗") in env and len(env[bstack11l1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᎘")]) > 0):
        return {
            bstack11l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᎙"): bstack11l1_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᎚"),
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᎛"): env.get(bstack11l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᎜")),
            bstack11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᎝"): env.get(bstack11l1_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᎞")),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᎟"): env.get(bstack11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᎠ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠨࡃࡊࠤᎡ")) == bstack11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧᎢ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᎣ"))):
        return {
            bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎤ"): bstack11l1_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᎥ"),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᎦ"): env.get(bstack11l1_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᎧ")),
            bstack11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᎨ"): env.get(bstack11l1_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᎩ")),
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᎪ"): env.get(bstack11l1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᎫ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠥࡇࡎࠨᎬ")) == bstack11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤᎭ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᎮ"))):
        return {
            bstack11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᎯ"): bstack11l1_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᎰ"),
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᎱ"): env.get(bstack11l1_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᎲ")),
            bstack11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᎳ"): env.get(bstack11l1_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᎴ")),
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᎵ"): env.get(bstack11l1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᎶ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠢࡄࡋࠥᎷ")) == bstack11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᎸ") and env.get(bstack11l1_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᎹ")) == bstack11l1_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᎺ"):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᎻ"): bstack11l1_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᎼ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᎽ"): None,
            bstack11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᎾ"): None,
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᎿ"): None
        }
    if env.get(bstack11l1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᏀ")) and env.get(bstack11l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᏁ")):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏂ"): bstack11l1_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᏃ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᏄ"): env.get(bstack11l1_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᏅ")),
            bstack11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᏆ"): None,
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᏇ"): env.get(bstack11l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᏈ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠦࡈࡏࠢᏉ")) == bstack11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᏊ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᏋ"))):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏌ"): bstack11l1_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᏍ"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᏎ"): env.get(bstack11l1_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᏏ")),
            bstack11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᏐ"): None,
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᏑ"): env.get(bstack11l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᏒ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠢࡄࡋࠥᏓ")) == bstack11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᏔ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᏕ"))):
        return {
            bstack11l1_opy_ (u"ࠥࡲࡦࡳࡥࠣᏖ"): bstack11l1_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᏗ"),
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᏘ"): env.get(bstack11l1_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᏙ")),
            bstack11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᏚ"): env.get(bstack11l1_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᏛ")),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᏜ"): env.get(bstack11l1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᏝ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠦࡈࡏࠢᏞ")) == bstack11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᏟ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᏠ"))):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏡ"): bstack11l1_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᏢ"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᏣ"): env.get(bstack11l1_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᏤ")),
            bstack11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᏥ"): env.get(bstack11l1_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᏦ")),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᏧ"): env.get(bstack11l1_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᏨ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠣࡅࡌࠦᏩ")) == bstack11l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᏪ") and bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᏫ"))):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏬ"): bstack11l1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᏭ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᏮ"): env.get(bstack11l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᏯ")),
            bstack11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᏰ"): env.get(bstack11l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᏱ")) or env.get(bstack11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᏲ")),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᏳ"): env.get(bstack11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᏴ"))
        }
    if bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᏵ"))):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᏶"): bstack11l1_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣ᏷"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᏸ"): bstack11l1_opy_ (u"ࠥࡿࢂࢁࡽࠣᏹ").format(env.get(bstack11l1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᏺ")), env.get(bstack11l1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᏻ"))),
            bstack11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᏼ"): env.get(bstack11l1_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᏽ")),
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᏾"): env.get(bstack11l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ᏿"))
        }
    if bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧ᐀"))):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐁ"): bstack11l1_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᐂ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᐃ"): bstack11l1_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᐄ").format(env.get(bstack11l1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᐅ")), env.get(bstack11l1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᐆ")), env.get(bstack11l1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᐇ")), env.get(bstack11l1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᐈ"))),
            bstack11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᐉ"): env.get(bstack11l1_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᐊ")),
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᐋ"): env.get(bstack11l1_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᐌ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᐍ")) and env.get(bstack11l1_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᐎ")):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐏ"): bstack11l1_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢᐐ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᐑ"): bstack11l1_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥᐒ").format(env.get(bstack11l1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᐓ")), env.get(bstack11l1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧᐔ")), env.get(bstack11l1_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪᐕ"))),
            bstack11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᐖ"): env.get(bstack11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᐗ")),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᐘ"): env.get(bstack11l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᐙ"))
        }
    if any([env.get(bstack11l1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᐚ")), env.get(bstack11l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᐛ")), env.get(bstack11l1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᐜ"))]):
        return {
            bstack11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐝ"): bstack11l1_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧᐞ"),
            bstack11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᐟ"): env.get(bstack11l1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᐠ")),
            bstack11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᐡ"): env.get(bstack11l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᐢ")),
            bstack11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᐣ"): env.get(bstack11l1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᐤ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥᐥ")):
        return {
            bstack11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᐦ"): bstack11l1_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢᐧ"),
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᐨ"): env.get(bstack11l1_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦᐩ")),
            bstack11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᐪ"): env.get(bstack11l1_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥᐫ")),
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᐬ"): env.get(bstack11l1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦᐭ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣᐮ")) or env.get(bstack11l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᐯ")):
        return {
            bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᐰ"): bstack11l1_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦᐱ"),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᐲ"): env.get(bstack11l1_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᐳ")),
            bstack11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᐴ"): bstack11l1_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢᐵ") if env.get(bstack11l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᐶ")) else None,
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᐷ"): env.get(bstack11l1_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᐸ"))
        }
    if any([env.get(bstack11l1_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᐹ")), env.get(bstack11l1_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᐺ")), env.get(bstack11l1_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᐻ"))]):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐼ"): bstack11l1_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᐽ"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᐾ"): None,
            bstack11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᐿ"): env.get(bstack11l1_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᑀ")),
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᑁ"): env.get(bstack11l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᑂ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᑃ")):
        return {
            bstack11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᑄ"): bstack11l1_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᑅ"),
            bstack11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᑆ"): env.get(bstack11l1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᑇ")),
            bstack11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᑈ"): bstack11l1_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᑉ").format(env.get(bstack11l1_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᑊ"))) if env.get(bstack11l1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᑋ")) else None,
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᑌ"): env.get(bstack11l1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᑍ"))
        }
    if bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᑎ"))):
        return {
            bstack11l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᑏ"): bstack11l1_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢᑐ"),
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᑑ"): env.get(bstack11l1_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧᑒ")),
            bstack11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᑓ"): env.get(bstack11l1_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᑔ")),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᑕ"): env.get(bstack11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᑖ"))
        }
    if bstack1111ll1l1_opy_(env.get(bstack11l1_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᑗ"))):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᑘ"): bstack11l1_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᑙ"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᑚ"): bstack11l1_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᑛ").format(env.get(bstack11l1_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᑜ")), env.get(bstack11l1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᑝ")), env.get(bstack11l1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᑞ"))),
            bstack11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᑟ"): env.get(bstack11l1_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᑠ")),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᑡ"): env.get(bstack11l1_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᑢ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠦࡈࡏࠢᑣ")) == bstack11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᑤ") and env.get(bstack11l1_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᑥ")) == bstack11l1_opy_ (u"ࠢ࠲ࠤᑦ"):
        return {
            bstack11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᑧ"): bstack11l1_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᑨ"),
            bstack11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᑩ"): bstack11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᑪ").format(env.get(bstack11l1_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᑫ"))),
            bstack11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᑬ"): None,
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᑭ"): None,
        }
    if env.get(bstack11l1_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᑮ")):
        return {
            bstack11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᑯ"): bstack11l1_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᑰ"),
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᑱ"): None,
            bstack11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᑲ"): env.get(bstack11l1_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᑳ")),
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᑴ"): env.get(bstack11l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᑵ"))
        }
    if any([env.get(bstack11l1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᑶ")), env.get(bstack11l1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᑷ")), env.get(bstack11l1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᑸ")), env.get(bstack11l1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᑹ"))]):
        return {
            bstack11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᑺ"): bstack11l1_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᑻ"),
            bstack11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᑼ"): None,
            bstack11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᑽ"): env.get(bstack11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᑾ")) or None,
            bstack11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᑿ"): env.get(bstack11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᒀ"), 0)
        }
    if env.get(bstack11l1_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᒁ")):
        return {
            bstack11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᒂ"): bstack11l1_opy_ (u"ࠣࡉࡲࡇࡉࠨᒃ"),
            bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᒄ"): None,
            bstack11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᒅ"): env.get(bstack11l1_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᒆ")),
            bstack11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᒇ"): env.get(bstack11l1_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᒈ"))
        }
    if env.get(bstack11l1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᒉ")):
        return {
            bstack11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᒊ"): bstack11l1_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᒋ"),
            bstack11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᒌ"): env.get(bstack11l1_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᒍ")),
            bstack11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᒎ"): env.get(bstack11l1_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᒏ")),
            bstack11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᒐ"): env.get(bstack11l1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᒑ"))
        }
    return {bstack11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᒒ"): None}
def get_host_info():
    return {
        bstack11l1_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᒓ"): platform.node(),
        bstack11l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᒔ"): platform.system(),
        bstack11l1_opy_ (u"ࠧࡺࡹࡱࡧࠥᒕ"): platform.machine(),
        bstack11l1_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᒖ"): platform.version(),
        bstack11l1_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᒗ"): platform.architecture()[0]
    }
def bstack1llll1lll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1llll1ll1l1_opy_():
    if bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᒘ")):
        return bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᒙ")
    return bstack11l1_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᒚ")
def bstack1llll1ll11l_opy_(driver):
    info = {
        bstack11l1_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᒛ"): driver.capabilities,
        bstack11l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᒜ"): driver.session_id,
        bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᒝ"): driver.capabilities.get(bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᒞ"), None),
        bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᒟ"): driver.capabilities.get(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᒠ"), None),
        bstack11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᒡ"): driver.capabilities.get(bstack11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᒢ"), None),
    }
    if bstack1llll1ll1l1_opy_() == bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᒣ"):
        if bstack1lll1l1111_opy_():
            info[bstack11l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᒤ")] = bstack11l1_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᒥ")
        elif driver.capabilities.get(bstack11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒦ"), {}).get(bstack11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᒧ"), False):
            info[bstack11l1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᒨ")] = bstack11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᒩ")
        else:
            info[bstack11l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᒪ")] = bstack11l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᒫ")
    return info
def bstack1lll1l1111_opy_():
    if bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᒬ")):
        return True
    if bstack1111ll1l1_opy_(os.environ.get(bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᒭ"), None)):
        return True
    return False
def bstack11ll1l11ll_opy_(bstack1lllllll111_opy_, url, data, config):
    headers = config.get(bstack11l1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᒮ"), None)
    proxies = bstack1l1l1l1ll_opy_(config, url)
    auth = config.get(bstack11l1_opy_ (u"ࠪࡥࡺࡺࡨࠨᒯ"), None)
    response = requests.request(
            bstack1lllllll111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1111ll1_opy_(bstack1llll1l1ll_opy_, size):
    bstack1l1llllll_opy_ = []
    while len(bstack1llll1l1ll_opy_) > size:
        bstack111ll11l_opy_ = bstack1llll1l1ll_opy_[:size]
        bstack1l1llllll_opy_.append(bstack111ll11l_opy_)
        bstack1llll1l1ll_opy_ = bstack1llll1l1ll_opy_[size:]
    bstack1l1llllll_opy_.append(bstack1llll1l1ll_opy_)
    return bstack1l1llllll_opy_
def bstack111111l1ll_opy_(message, bstack1lllll11111_opy_=False):
    os.write(1, bytes(message, bstack11l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᒰ")))
    os.write(1, bytes(bstack11l1_opy_ (u"ࠬࡢ࡮ࠨᒱ"), bstack11l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᒲ")))
    if bstack1lllll11111_opy_:
        with open(bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᒳ") + os.environ[bstack11l1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᒴ")] + bstack11l1_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᒵ"), bstack11l1_opy_ (u"ࠪࡥࠬᒶ")) as f:
            f.write(message + bstack11l1_opy_ (u"ࠫࡡࡴࠧᒷ"))
def bstack1llllll11l1_opy_():
    return os.environ[bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᒸ")].lower() == bstack11l1_opy_ (u"࠭ࡴࡳࡷࡨࠫᒹ")
def bstack1l11l111ll_opy_(bstack111111l111_opy_):
    return bstack11l1_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ᒺ").format(bstack1111l1l11l_opy_, bstack111111l111_opy_)
def bstack11l1l1lll_opy_():
    return bstack11l111l11l_opy_().replace(tzinfo=None).isoformat() + bstack11l1_opy_ (u"ࠨ࡜ࠪᒻ")
def bstack1llllll1lll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l1_opy_ (u"ࠩ࡝ࠫᒼ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l1_opy_ (u"ࠪ࡞ࠬᒽ")))).total_seconds() * 1000
def bstack1llll1lllll_opy_(timestamp):
    return bstack11111l111l_opy_(timestamp).isoformat() + bstack11l1_opy_ (u"ࠫ࡟࠭ᒾ")
def bstack1lllllll1ll_opy_(bstack1lllll1llll_opy_):
    date_format = bstack11l1_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᒿ")
    bstack1111111l1l_opy_ = datetime.datetime.strptime(bstack1lllll1llll_opy_, date_format)
    return bstack1111111l1l_opy_.isoformat() + bstack11l1_opy_ (u"࡚࠭ࠨᓀ")
def bstack1llll1ll1ll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᓁ")
    else:
        return bstack11l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᓂ")
def bstack1111ll1l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᓃ")
def bstack1llll1l1l1l_opy_(val):
    return val.__str__().lower() == bstack11l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᓄ")
def bstack11l11l1l1l_opy_(bstack1llll1ll111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1llll1ll111_opy_ as e:
                print(bstack11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᓅ").format(func.__name__, bstack1llll1ll111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1lllll11l1l_opy_(bstack1lllll1l1l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1lllll1l1l1_opy_(cls, *args, **kwargs)
            except bstack1llll1ll111_opy_ as e:
                print(bstack11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᓆ").format(bstack1lllll1l1l1_opy_.__name__, bstack1llll1ll111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1lllll11l1l_opy_
    else:
        return decorator
def bstack11lll1lll1_opy_(bstack111ll1l111_opy_):
    if bstack11l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᓇ") in bstack111ll1l111_opy_ and bstack1llll1l1l1l_opy_(bstack111ll1l111_opy_[bstack11l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᓈ")]):
        return False
    if bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᓉ") in bstack111ll1l111_opy_ and bstack1llll1l1l1l_opy_(bstack111ll1l111_opy_[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᓊ")]):
        return False
    return True
def bstack1l1lll111l_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111111ll1_opy_ = os.environ.get(bstack11l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥᓋ"), None)
        return bstack1111111ll1_opy_ is None or bstack1111111ll1_opy_ == bstack11l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᓌ")
    except Exception as e:
        return False
def bstack1llll1ll1l_opy_(hub_url, CONFIG):
    if bstack1l1lll11ll_opy_() <= version.parse(bstack11l1_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬᓍ")):
        if hub_url != bstack11l1_opy_ (u"࠭ࠧᓎ"):
            return bstack11l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᓏ") + hub_url + bstack11l1_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᓐ")
        return bstack1llllll11l_opy_
    if hub_url != bstack11l1_opy_ (u"ࠩࠪᓑ"):
        return bstack11l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᓒ") + hub_url + bstack11l1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᓓ")
    return bstack1l1l11l111_opy_
def bstack1llll111ll1_opy_():
    return isinstance(os.getenv(bstack11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫᓔ")), str)
def bstack11l11lll_opy_(url):
    return urlparse(url).hostname
def bstack1l1l11l1_opy_(hostname):
    for bstack1l1l1l1ll1_opy_ in bstack11llll1l11_opy_:
        regex = re.compile(bstack1l1l1l1ll1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111111lll1_opy_(bstack1llll11ll11_opy_, file_name, logger):
    bstack1llllllll_opy_ = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"࠭ࡾࠨᓕ")), bstack1llll11ll11_opy_)
    try:
        if not os.path.exists(bstack1llllllll_opy_):
            os.makedirs(bstack1llllllll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l1_opy_ (u"ࠧࡿࠩᓖ")), bstack1llll11ll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l1_opy_ (u"ࠨࡹࠪᓗ")):
                pass
            with open(file_path, bstack11l1_opy_ (u"ࠤࡺ࠯ࠧᓘ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11111llll_opy_.format(str(e)))
def bstack1lll1lllll1_opy_(file_name, key, value, logger):
    file_path = bstack111111lll1_opy_(bstack11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᓙ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lll1l11l1_opy_ = json.load(open(file_path, bstack11l1_opy_ (u"ࠫࡷࡨࠧᓚ")))
        else:
            bstack1lll1l11l1_opy_ = {}
        bstack1lll1l11l1_opy_[key] = value
        with open(file_path, bstack11l1_opy_ (u"ࠧࡽࠫࠣᓛ")) as outfile:
            json.dump(bstack1lll1l11l1_opy_, outfile)
def bstack11l1llll_opy_(file_name, logger):
    file_path = bstack111111lll1_opy_(bstack11l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᓜ"), file_name, logger)
    bstack1lll1l11l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l1_opy_ (u"ࠧࡳࠩᓝ")) as bstack1ll1l11lll_opy_:
            bstack1lll1l11l1_opy_ = json.load(bstack1ll1l11lll_opy_)
    return bstack1lll1l11l1_opy_
def bstack1ll1lll1ll_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᓞ") + file_path + bstack11l1_opy_ (u"ࠩࠣࠫᓟ") + str(e))
def bstack1l1lll11ll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l1_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᓠ")
def bstack1l11l1l1_opy_(config):
    if bstack11l1_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᓡ") in config:
        del (config[bstack11l1_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᓢ")])
        return False
    if bstack1l1lll11ll_opy_() < version.parse(bstack11l1_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᓣ")):
        return False
    if bstack1l1lll11ll_opy_() >= version.parse(bstack11l1_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᓤ")):
        return True
    if bstack11l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᓥ") in config and config[bstack11l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᓦ")] is False:
        return False
    else:
        return True
def bstack1lll1ll1l_opy_(args_list, bstack1llll111l11_opy_):
    index = -1
    for value in bstack1llll111l11_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11l1lll111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11l1lll111_opy_ = bstack11l1lll111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᓧ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᓨ"), exception=exception)
    def bstack111ll111l1_opy_(self):
        if self.result != bstack11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᓩ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᓪ") in self.exception_type:
            return bstack11l1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᓫ")
        return bstack11l1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᓬ")
    def bstack1lllllll1l1_opy_(self):
        if self.result != bstack11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᓭ"):
            return None
        if self.bstack11l1lll111_opy_:
            return self.bstack11l1lll111_opy_
        return bstack1llllllll1l_opy_(self.exception)
def bstack1llllllll1l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1lll1llll1l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1lll1lll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111l111l1_opy_(config, logger):
    try:
        import playwright
        bstack1llllll1l11_opy_ = playwright.__file__
        bstack1llllllllll_opy_ = os.path.split(bstack1llllll1l11_opy_)
        bstack11111111ll_opy_ = bstack1llllllllll_opy_[0] + bstack11l1_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᓮ")
        os.environ[bstack11l1_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᓯ")] = bstack1ll11ll111_opy_(config)
        with open(bstack11111111ll_opy_, bstack11l1_opy_ (u"ࠬࡸࠧᓰ")) as f:
            bstack1ll1l1llll_opy_ = f.read()
            bstack1llllll1ll1_opy_ = bstack11l1_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᓱ")
            bstack1llll11ll1l_opy_ = bstack1ll1l1llll_opy_.find(bstack1llllll1ll1_opy_)
            if bstack1llll11ll1l_opy_ == -1:
              process = subprocess.Popen(bstack11l1_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᓲ"), shell=True, cwd=bstack1llllllllll_opy_[0])
              process.wait()
              bstack1llll1l1l11_opy_ = bstack11l1_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᓳ")
              bstack1lllll11ll1_opy_ = bstack11l1_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᓴ")
              bstack1lllll1ll11_opy_ = bstack1ll1l1llll_opy_.replace(bstack1llll1l1l11_opy_, bstack1lllll11ll1_opy_)
              with open(bstack11111111ll_opy_, bstack11l1_opy_ (u"ࠪࡻࠬᓵ")) as f:
                f.write(bstack1lllll1ll11_opy_)
    except Exception as e:
        logger.error(bstack11ll11llll_opy_.format(str(e)))
def bstack1llll11l_opy_():
  try:
    bstack1lllll1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᓶ"))
    bstack1lll1llllll_opy_ = []
    if os.path.exists(bstack1lllll1l111_opy_):
      with open(bstack1lllll1l111_opy_) as f:
        bstack1lll1llllll_opy_ = json.load(f)
      os.remove(bstack1lllll1l111_opy_)
    return bstack1lll1llllll_opy_
  except:
    pass
  return []
def bstack1lll1ll111_opy_(bstack1l111ll11l_opy_):
  try:
    bstack1lll1llllll_opy_ = []
    bstack1lllll1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᓷ"))
    if os.path.exists(bstack1lllll1l111_opy_):
      with open(bstack1lllll1l111_opy_) as f:
        bstack1lll1llllll_opy_ = json.load(f)
    bstack1lll1llllll_opy_.append(bstack1l111ll11l_opy_)
    with open(bstack1lllll1l111_opy_, bstack11l1_opy_ (u"࠭ࡷࠨᓸ")) as f:
        json.dump(bstack1lll1llllll_opy_, f)
  except:
    pass
def bstack11lll1ll1_opy_(logger, bstack1llll1111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l1_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᓹ"), bstack11l1_opy_ (u"ࠨࠩᓺ"))
    if test_name == bstack11l1_opy_ (u"ࠩࠪᓻ"):
        test_name = threading.current_thread().__dict__.get(bstack11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᓼ"), bstack11l1_opy_ (u"ࠫࠬᓽ"))
    bstack1lllll1111l_opy_ = bstack11l1_opy_ (u"ࠬ࠲ࠠࠨᓾ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1llll1111ll_opy_:
        bstack1ll1111l_opy_ = os.environ.get(bstack11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᓿ"), bstack11l1_opy_ (u"ࠧ࠱ࠩᔀ"))
        bstack11l1lll1_opy_ = {bstack11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᔁ"): test_name, bstack11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᔂ"): bstack1lllll1111l_opy_, bstack11l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᔃ"): bstack1ll1111l_opy_}
        bstack1llll1llll1_opy_ = []
        bstack1lllllll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᔄ"))
        if os.path.exists(bstack1lllllll11l_opy_):
            with open(bstack1lllllll11l_opy_) as f:
                bstack1llll1llll1_opy_ = json.load(f)
        bstack1llll1llll1_opy_.append(bstack11l1lll1_opy_)
        with open(bstack1lllllll11l_opy_, bstack11l1_opy_ (u"ࠬࡽࠧᔅ")) as f:
            json.dump(bstack1llll1llll1_opy_, f)
    else:
        bstack11l1lll1_opy_ = {bstack11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᔆ"): test_name, bstack11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᔇ"): bstack1lllll1111l_opy_, bstack11l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᔈ"): str(multiprocessing.current_process().name)}
        if bstack11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᔉ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11l1lll1_opy_)
  except Exception as e:
      logger.warn(bstack11l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᔊ").format(e))
def bstack1l111ll11_opy_(error_message, test_name, index, logger):
  try:
    bstack1llll1l1lll_opy_ = []
    bstack11l1lll1_opy_ = {bstack11l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᔋ"): test_name, bstack11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᔌ"): error_message, bstack11l1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᔍ"): index}
    bstack1llll11111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᔎ"))
    if os.path.exists(bstack1llll11111l_opy_):
        with open(bstack1llll11111l_opy_) as f:
            bstack1llll1l1lll_opy_ = json.load(f)
    bstack1llll1l1lll_opy_.append(bstack11l1lll1_opy_)
    with open(bstack1llll11111l_opy_, bstack11l1_opy_ (u"ࠨࡹࠪᔏ")) as f:
        json.dump(bstack1llll1l1lll_opy_, f)
  except Exception as e:
    logger.warn(bstack11l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᔐ").format(e))
def bstack11l1ll1ll_opy_(bstack1l11lllll1_opy_, name, logger):
  try:
    bstack11l1lll1_opy_ = {bstack11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᔑ"): name, bstack11l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᔒ"): bstack1l11lllll1_opy_, bstack11l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᔓ"): str(threading.current_thread()._name)}
    return bstack11l1lll1_opy_
  except Exception as e:
    logger.warn(bstack11l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᔔ").format(e))
  return
def bstack11111l1111_opy_():
    return platform.system() == bstack11l1_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᔕ")
def bstack1l111l1l_opy_(bstack1llllll11ll_opy_, config, logger):
    bstack111111111l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1llllll11ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᔖ").format(e))
    return bstack111111111l_opy_
def bstack111111llll_opy_(bstack1lllll11lll_opy_, bstack111111l1l1_opy_):
    bstack1llll111111_opy_ = version.parse(bstack1lllll11lll_opy_)
    bstack111111l11l_opy_ = version.parse(bstack111111l1l1_opy_)
    if bstack1llll111111_opy_ > bstack111111l11l_opy_:
        return 1
    elif bstack1llll111111_opy_ < bstack111111l11l_opy_:
        return -1
    else:
        return 0
def bstack11l111l11l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11111l111l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111111ll11_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll11111l1_opy_(options, framework, bstack1ll11lll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l1_opy_ (u"ࠩࡪࡩࡹ࠭ᔗ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1l11111_opy_ = caps.get(bstack11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᔘ"))
    bstack1lllll11l11_opy_ = True
    bstack1lll1l1l11_opy_ = os.environ[bstack11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᔙ")]
    if bstack1llll1l1l1l_opy_(caps.get(bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫᔚ"))) or bstack1llll1l1l1l_opy_(caps.get(bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭ᔛ"))):
        bstack1lllll11l11_opy_ = False
    if bstack1l11l1l1_opy_({bstack11l1_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢᔜ"): bstack1lllll11l11_opy_}):
        bstack1ll1l11111_opy_ = bstack1ll1l11111_opy_ or {}
        bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᔝ")] = bstack111111ll11_opy_(framework)
        bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᔞ")] = bstack1llllll11l1_opy_()
        bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᔟ")] = bstack1lll1l1l11_opy_
        bstack1ll1l11111_opy_[bstack11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᔠ")] = bstack1ll11lll_opy_
        if getattr(options, bstack11l1_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᔡ"), None):
            options.set_capability(bstack11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᔢ"), bstack1ll1l11111_opy_)
        else:
            options[bstack11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᔣ")] = bstack1ll1l11111_opy_
    else:
        if getattr(options, bstack11l1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᔤ"), None):
            options.set_capability(bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᔥ"), bstack111111ll11_opy_(framework))
            options.set_capability(bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᔦ"), bstack1llllll11l1_opy_())
            options.set_capability(bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᔧ"), bstack1lll1l1l11_opy_)
            options.set_capability(bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᔨ"), bstack1ll11lll_opy_)
        else:
            options[bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᔩ")] = bstack111111ll11_opy_(framework)
            options[bstack11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᔪ")] = bstack1llllll11l1_opy_()
            options[bstack11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᔫ")] = bstack1lll1l1l11_opy_
            options[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᔬ")] = bstack1ll11lll_opy_
    return options
def bstack1llll111l1l_opy_(bstack1llll1l1ll1_opy_, framework):
    bstack1ll11lll_opy_ = bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᔭ"))
    if bstack1llll1l1ll1_opy_ and len(bstack1llll1l1ll1_opy_.split(bstack11l1_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᔮ"))) > 1:
        ws_url = bstack1llll1l1ll1_opy_.split(bstack11l1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᔯ"))[0]
        if bstack11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩᔰ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1lllll111l1_opy_ = json.loads(urllib.parse.unquote(bstack1llll1l1ll1_opy_.split(bstack11l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᔱ"))[1]))
            bstack1lllll111l1_opy_ = bstack1lllll111l1_opy_ or {}
            bstack1lll1l1l11_opy_ = os.environ[bstack11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᔲ")]
            bstack1lllll111l1_opy_[bstack11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᔳ")] = str(framework) + str(__version__)
            bstack1lllll111l1_opy_[bstack11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᔴ")] = bstack1llllll11l1_opy_()
            bstack1lllll111l1_opy_[bstack11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᔵ")] = bstack1lll1l1l11_opy_
            bstack1lllll111l1_opy_[bstack11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᔶ")] = bstack1ll11lll_opy_
            bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_.split(bstack11l1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᔷ"))[0] + bstack11l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᔸ") + urllib.parse.quote(json.dumps(bstack1lllll111l1_opy_))
    return bstack1llll1l1ll1_opy_
def bstack111l1ll11_opy_():
    global bstack1ll1ll111l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll1ll111l_opy_ = BrowserType.connect
    return bstack1ll1ll111l_opy_
def bstack1llll1ll1_opy_(framework_name):
    global bstack1llll11l1l_opy_
    bstack1llll11l1l_opy_ = framework_name
    return framework_name
def bstack1111l1lll_opy_(self, *args, **kwargs):
    global bstack1ll1ll111l_opy_
    try:
        global bstack1llll11l1l_opy_
        if bstack11l1_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᔹ") in kwargs:
            kwargs[bstack11l1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᔺ")] = bstack1llll111l1l_opy_(
                kwargs.get(bstack11l1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᔻ"), None),
                bstack1llll11l1l_opy_
            )
    except Exception as e:
        logger.error(bstack11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦᔼ").format(str(e)))
    return bstack1ll1ll111l_opy_(self, *args, **kwargs)
def bstack1lllll1l11l_opy_(bstack1llll11l1ll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1l1l1ll_opy_(bstack1llll11l1ll_opy_, bstack11l1_opy_ (u"ࠧࠨᔽ"))
        if proxies and proxies.get(bstack11l1_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᔾ")):
            parsed_url = urlparse(proxies.get(bstack11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᔿ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᕀ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬᕁ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᕂ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᕃ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1ll1llll_opy_(bstack1llll11l1ll_opy_):
    bstack1llll1lll11_opy_ = {
        bstack11111llll1_opy_[bstack1111111111_opy_]: bstack1llll11l1ll_opy_[bstack1111111111_opy_]
        for bstack1111111111_opy_ in bstack1llll11l1ll_opy_
        if bstack1111111111_opy_ in bstack11111llll1_opy_
    }
    bstack1llll1lll11_opy_[bstack11l1_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧᕄ")] = bstack1lllll1l11l_opy_(bstack1llll11l1ll_opy_, bstack1l1l1lll1_opy_.get_property(bstack11l1_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨᕅ")))
    bstack1lll1llll11_opy_ = [element.lower() for element in bstack11111l1lll_opy_]
    bstack1lllll1lll1_opy_(bstack1llll1lll11_opy_, bstack1lll1llll11_opy_)
    return bstack1llll1lll11_opy_
def bstack1lllll1lll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l1_opy_ (u"ࠢࠫࠬ࠭࠮ࠧᕆ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1lllll1lll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1lllll1lll1_opy_(item, keys)