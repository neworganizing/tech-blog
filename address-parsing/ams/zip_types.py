from ctypes import *
class ADDR_REC(Structure):
	_fields_ = [("detail_code",c_char),("zip_code",c_char * 6),("update_key",c_char * 11),("action_code",c_char),("rec_type",c_char),("carr_rt",c_char * 5),("pre_dir",c_char * 3),("str_name",c_char * 29),("suffix",c_char * 5),("post_dir",c_char * 3),("prim_low",c_char * 11),("prim_high",c_char * 11),("prim_code",c_char),("sec_name",c_char * 41),("unit",c_char * 5),("sec_low",c_char * 9),("sec_high",c_char * 9),("sec_code",c_char),("addon_low",c_char * 5),("addon_high",c_char * 5),("base_alt_code",c_char),("lacs_status",c_char),("finance",c_char * 7),("state_abbrev",c_char * 3),("county_no",c_char * 4),("congress_dist",c_char * 3),("municipality",c_char * 7),("urbanization",c_char * 7),("last_line",c_char * 7)]

class CITY_REC(Structure):
	_fields_ = [("detail_code",c_char),("zip_code",c_char * 6),("city_key",c_char * 7),("zip_class_code",c_char),("city_name",c_char * 29),("city_abbrev",c_char * 14),("facility_cd",c_char),("mailing_name_ind",c_char),("last_line_num",c_char * 7),("last_line_name",c_char * 29),("city_delv_ind",c_char),("auto_zone_ind",c_char),("unique_zip_ind",c_char),("finance",c_char * 7),("state_abbrev",c_char * 3),("county_no",c_char * 4),("county_name",c_char * 26)]
class foot(Structure):
    _fields_ = [("a",c_char),("b",c_char),("c",c_char),("d",c_char),("e",c_char),("f",c_char),("g",c_char),("h",c_char),("i",c_char),("j",c_char),("k",c_char),("l",c_char),("m",c_char),("n",c_char),("o",c_char),("p",c_char),("q",c_char),("r",c_char),("s",c_char),("t",c_char),("u",c_char),("v",c_char),("w",c_char),("x",c_char),("y",c_char),("z",c_char),("f0",c_char),("f1",c_char),("f2",c_char),("f3",c_char),("f4",c_char),("f5",c_char)]

class ZIP4_PARM(Structure):
	_fields_ = [("rsvd0",c_char * 4),("iadl1",c_char * 51),("iadl2",c_char * 51),("ictyi",c_char * 51),("istai",c_char * 3),("izipc",c_char * 11),("iprurb",c_char * 29),("iadl3",c_char * 51),("iddpv11",c_char * 13),("rsvd1",c_char * 85),("dadl3",c_char * 51),("dadl1",c_char * 51),("dadl2",c_char * 51),("dlast",c_char * 51),("dprurb",c_char * 29),("dctys",c_char * 29),("dstas",c_char * 3),("dctya",c_char * 29),("abcty",c_char * 14),("dstaa",c_char * 3),("zipc",c_char * 6),("addon",c_char * 5),("dpbc",c_char * 4),("cris",c_char * 5),("county",c_char * 4),("respn",c_short),("retcc",c_char),("adrkey",c_char * 12),("auto_zone_ind",c_char),("elot_num",c_char * 5),("elot_code",c_char),("llk_rc",c_char * 3),("llk_ind",c_char),("misc",c_char * 129),("rsvd2",c_char * 20),("ppnum",c_char * 11),("psnum",c_char * 9),("prote",c_char * 4),("punit",c_char * 5),("ppre1",c_char * 3),("ppre2",c_char * 3),("psuf1",c_char * 5),("psuf2",c_char * 5),("ppst1",c_char * 3),("ppst2",c_char * 3),("ppnam",c_char * 29),("mpnum",c_char * 11),("msnum",c_char * 9),("pmb",c_char * 4),("pmbnum",c_char * 9),("mlevl",c_char),("footnotes",c_char * 33),("stelnkfoot",c_char * 4),("punit2",c_char * 5),("psnum2",c_char * 9),("rsvd3",c_char * 10),("foot", foot), ("stack",ADDR_REC * 10), ('rsvd4', c_char * 194)]

class GET_ZIPCODE_STRUCT(Structure):
	_fields_ = [("input_cityst",c_char * 51),("output_cityst",c_char * 51),("low_zipcode",c_char * 6),("high_zipcode",c_char * 6),("finance_num",c_char * 7)]

class TAbbrSt(Structure):
	_fields_ = [("psDetailCode",c_char * 1),("szZipcode",c_char * 6),("szUpdateKey",c_char * 11),("psActionCode",c_char * 1),("psRecordType",c_char * 1),("szCarrierRt",c_char * 5),("szPreDir",c_char * 3),("szStreetName",c_char * 29),("szSuffix",c_char * 5),("szPostDir",c_char * 3),("szPrimaryL",c_char * 11),("szPrimaryH",c_char * 11),("psPrimarCode",c_char * 1),("szFirm",c_char * 41),("szUnit",c_char * 5),("szSecondaryL",c_char * 9),("szSecondaryH",c_char * 9),("psSecondaryCode",c_char * 1),("szAddonL",c_char * 5),("szAddonH",c_char * 5),("psBaseAltCode",c_char * 1),("psLACS",c_char * 1),("szFinance",c_char * 7),("szState",c_char * 3),("szCountyNumber",c_char * 4),("szCongressDist",c_char * 3),("szMunicipality",c_char * 7),("szUrbanization",c_char * 7),("szLastLineKey",c_char * 7),("szAddress",c_char * 51)]

class Z4_ERROR(Structure):
	_fields_ = [("iErrorCode",c_int),("strErrorMessage",c_char * 101),("iFileCode",c_int),("strFileName",c_char * 27),("strDiagnostics",c_char * 301)]

class Z4_ENV(Structure):
	_fields_ = [("strConfigFile",c_char * 301),("address1",c_char * 301),("addrindex",c_char * 301),("cdrom",c_char * 301),("citystate",c_char * 301),("crossref",c_char * 301),("system",c_char * 301),("elot",c_char * 301),("elotindex",c_char * 301),("llkpath",c_char * 301),("ewspath",c_char * 301),("fnsnpath",c_char * 301),("stelnkpath",c_char * 301),("abrstpath",c_char * 301),("rsvd1",c_char * 1208),("stelnkflag",c_char),("abrstflag",c_char),("ewsflag",c_char),("elotflag",c_char),("llkflag",c_char),("dpvflag",c_char)]

class CONFIG_PARM(Structure):
	_fields_ = [("address1",c_char_p),("addrindex",c_char_p),("cdrom",c_char_p),("citystate",c_char_p),("crossref",c_char_p),("system",c_char_p),("elot",c_char_p),("elotindex",c_char_p),("llkpath",c_char_p),("ewspath",c_char_p),("dpvpath",c_char_p),("fnsnpath",c_char_p),("stelnkpath",c_char_p),("abrstpath",c_char_p),("rsvd",c_char * 116)]

class Z4OPEN_PARM(Structure):
	_fields_ = [("rsvd1",c_char * 50),("status",c_short),("fname",c_char_p),("config",CONFIG_PARM),("ewsflag",c_char),("elotflag",c_char),("llkflag",c_char),("dpvflag",c_char),("systemflag",c_char),("rtsw",c_char * 16),("dpvtypeflag",c_char),("stelnkflag",c_char),("abrstflag",c_char),("rsvd2",c_char * 492)]

