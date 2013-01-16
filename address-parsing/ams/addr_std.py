from ctypes import *
from zip_types import *
import addr_conf

zop = Z4OPEN_PARM()
zop.config.address1 = addr_conf.ac
zop.config.addrindex = addr_conf.ac
zop.config.citystate = addr_conf.ac
zop.config.crossref = addr_conf.ac
zop.config.fnsnpath = addr_conf.ac
zop.config.elot = addr_conf.ae
zop.config.elotindex = addr_conf.ae
zop.config.llkpath = addr_conf.ll
zop.config.dpvpath = addr_conf.ad
zop.config.stelnkpath = addr_conf.sl
zop.config.abrstpath = addr_conf.ac
zop.config.system = './'

zop.dpvflag = addr_conf.dpvflag
zop.llkflag = addr_conf.llkflag
zop.stelnkflag = addr_conf.stelnkflag
zop.ewsflag = addr_conf.ewsflag
zop.abrstflag = addr_conf.abrstflag
zop.elotflag = addr_conf.elotflag

ziplib = CDLL(addr_conf.libz_loc)

print 'conf response %s' % ziplib.z4opencfg(byref(zop))

response_map = {10:'Invalid Input Address',11:'Invalid Input 5-Digit ZIP Code',12:'Invalid Input State Abbreviation Code',13:'Invalid Input City Name',21:'No Match Found Using Input Address',22:'Multiple Responses',31:'Single Address Found',32:'Could Find More Specific Address'}

def get_std(addr, cty, add2='',state='', zzip=''):
    zp = ZIP4_PARM()
    zp.iadl1 = addr
    zp.iadl2 = add2
    zp.ictyi = cty
    zp.istai = state
    zp.izipc = zzip
    ziplib.z4adrinq(byref(zp))
    ret = int(zp.retcc.encode('hex'), 16)
    if ret == 22:
        ziplib.z4adrstd(byref(zp), 0)
    footsignals = []
    for foo in [chr(i) for i in range(ord('a'),ord('z'))]:
        if zp.foot.__getattribute__(foo) != '\x00':
            footsignals.append(zp.foot.__getattribute__(foo))
    parsed = {
            'primary number':zp.ppnum,
            'secondary number':zp.psnum,
            'second or right secondary number':zp.psnum2,
            'rural route number':zp.prote,
            'secondary number unit':zp.punit,
            'secondary or right secondary number unit':zp.punit2,
            'first or left pre-direction':zp.ppre1,
            'second or right pre-direction':zp.ppre2,
            'first or left suffix':zp.psuf1,
            'second or right suffix':zp.psuf2,
            'first or left post-direction':zp.ppst1,
            'second or right post-direction':zp.ppst2,
            'primary name':zp.ppnam,
            'matched primary number':zp.mpnum,
            'matched secondary number':zp.msnum,
            'pmb unit designator':zp.pmb,
            'pmb number':zp.pmbnum,
            }
    return ret, response_map[ret], '{ad1} {ad2} {city}, {state} {zip}'.format(ad1=zp.dadl1, ad2=zp.dadl3, city=zp.dctya, state=zp.dstaa, zip=zp.zipc), parsed, footsignals, zp.dadl1, zp.dadl3, zp.dctya, zp.dstaa, zp.zipc ,zp.county
