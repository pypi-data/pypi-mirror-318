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
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lll11lll11_opy_
bstack1l1l1lll1_opy_ = Config.bstack1l1l11lll1_opy_()
def bstack1ll1l111l1l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1ll1l11l111_opy_(bstack1ll1l111ll1_opy_, bstack1ll1l11l11l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1ll1l111ll1_opy_):
        with open(bstack1ll1l111ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1ll1l111l1l_opy_(bstack1ll1l111ll1_opy_):
        pac = get_pac(url=bstack1ll1l111ll1_opy_)
    else:
        raise Exception(bstack11l1_opy_ (u"ࠪࡔࡦࡩࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠪᙽ").format(bstack1ll1l111ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l1_opy_ (u"ࠦ࠽࠴࠸࠯࠺࠱࠼ࠧᙾ"), 80))
        bstack1ll1l11l1ll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1ll1l11l1ll_opy_ = bstack11l1_opy_ (u"ࠬ࠶࠮࠱࠰࠳࠲࠵࠭ᙿ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1ll1l11l11l_opy_, bstack1ll1l11l1ll_opy_)
    return proxy_url
def bstack11ll1lll1l_opy_(config):
    return bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ ") in config or bstack11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᚁ") in config
def bstack1ll11ll111_opy_(config):
    if not bstack11ll1lll1l_opy_(config):
        return
    if config.get(bstack11l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᚂ")):
        return config.get(bstack11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᚃ"))
    if config.get(bstack11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᚄ")):
        return config.get(bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᚅ"))
def bstack1l1l1l1ll_opy_(config, bstack1ll1l11l11l_opy_):
    proxy = bstack1ll11ll111_opy_(config)
    proxies = {}
    if config.get(bstack11l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᚆ")) or config.get(bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᚇ")):
        if proxy.endswith(bstack11l1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬᚈ")):
            proxies = bstack1l1111l1ll_opy_(proxy, bstack1ll1l11l11l_opy_)
        else:
            proxies = {
                bstack11l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᚉ"): proxy
            }
    bstack1l1l1lll1_opy_.bstack1lll1111l1_opy_(bstack11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᚊ"), proxies)
    return proxies
def bstack1l1111l1ll_opy_(bstack1ll1l111ll1_opy_, bstack1ll1l11l11l_opy_):
    proxies = {}
    global bstack1ll1l11l1l1_opy_
    if bstack11l1_opy_ (u"ࠪࡔࡆࡉ࡟ࡑࡔࡒ࡜࡞࠭ᚋ") in globals():
        return bstack1ll1l11l1l1_opy_
    try:
        proxy = bstack1ll1l11l111_opy_(bstack1ll1l111ll1_opy_, bstack1ll1l11l11l_opy_)
        if bstack11l1_opy_ (u"ࠦࡉࡏࡒࡆࡅࡗࠦᚌ") in proxy:
            proxies = {}
        elif bstack11l1_opy_ (u"ࠧࡎࡔࡕࡒࠥᚍ") in proxy or bstack11l1_opy_ (u"ࠨࡈࡕࡖࡓࡗࠧᚎ") in proxy or bstack11l1_opy_ (u"ࠢࡔࡑࡆࡏࡘࠨᚏ") in proxy:
            bstack1ll1l111lll_opy_ = proxy.split(bstack11l1_opy_ (u"ࠣࠢࠥᚐ"))
            if bstack11l1_opy_ (u"ࠤ࠽࠳࠴ࠨᚑ") in bstack11l1_opy_ (u"ࠥࠦᚒ").join(bstack1ll1l111lll_opy_[1:]):
                proxies = {
                    bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᚓ"): bstack11l1_opy_ (u"ࠧࠨᚔ").join(bstack1ll1l111lll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᚕ"): str(bstack1ll1l111lll_opy_[0]).lower() + bstack11l1_opy_ (u"ࠢ࠻࠱࠲ࠦᚖ") + bstack11l1_opy_ (u"ࠣࠤᚗ").join(bstack1ll1l111lll_opy_[1:])
                }
        elif bstack11l1_opy_ (u"ࠤࡓࡖࡔ࡞࡙ࠣᚘ") in proxy:
            bstack1ll1l111lll_opy_ = proxy.split(bstack11l1_opy_ (u"ࠥࠤࠧᚙ"))
            if bstack11l1_opy_ (u"ࠦ࠿࠵࠯ࠣᚚ") in bstack11l1_opy_ (u"ࠧࠨ᚛").join(bstack1ll1l111lll_opy_[1:]):
                proxies = {
                    bstack11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᚜"): bstack11l1_opy_ (u"ࠢࠣ᚝").join(bstack1ll1l111lll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧ᚞"): bstack11l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ᚟") + bstack11l1_opy_ (u"ࠥࠦᚠ").join(bstack1ll1l111lll_opy_[1:])
                }
        else:
            proxies = {
                bstack11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᚡ"): proxy
            }
    except Exception as e:
        print(bstack11l1_opy_ (u"ࠧࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᚢ"), bstack1lll11lll11_opy_.format(bstack1ll1l111ll1_opy_, str(e)))
    bstack1ll1l11l1l1_opy_ = proxies
    return proxies