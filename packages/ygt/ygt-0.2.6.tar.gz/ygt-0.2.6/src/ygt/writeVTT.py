from lxml import etree

"""
YAnchor
ResYAnchor
[YNoRound, YAnchor]
[YNoRound, ResYAnchor]
ResYAnchor
YInterpolate
YIPAnchor
YDist
ResYDist
[YNoRound, YDist]
[YNoRound, ResYDist]
YLink
ResYLink
[YNoRound, YLink]
[YNoRound, ResYLink]
YShift
smooth
"""

def build_input_output(self):
    pass

def build_defaults(self):
    pass

def build_cvt_settings(self):
    pass

def build_cvt(self):
    pass

def build_cvar_from_masters(self):
    pass

def build_functions(self):
    pass

def build_macros(self):
    pass

def build_glyph_program(g, y_doc[k][g], xgf_doc):
    pass

def ygridfit_parse_obj(y_doc, single_glyph=None, glyph_list=None):
    y_keys = y_doc.keys()


    for k in y_keys:
        if k == "font":
            build_input_output(y_doc[k], xgf_doc)
        elif k == "defaults":
            build_defaults(y_doc[k], xgf_doc)
        elif k == "prep":
            build_cvt_settings(y_doc[k], y_doc["cvt"], xgf_doc)
        elif k == "cvt":
            build_cvt(y_doc[k], xgf_doc)
        elif k == "masters":
            try:
                build_cvar_from_masters(y_doc, xgf_doc)
            except Exception as e:
                pass
        #elif k == "cvar":
        #    if not "masters" in y_doc:
        #        build_cvar(y_doc[k], xgf_doc)
        elif k == "functions":
            build_functions(y_doc[k], xgf_doc)
        elif k == "macros":
            build_macros(y_doc[k], xgf_doc)
        elif k == "glyphs":
            if not single_glyph and not glyph_list:
                g_keys = y_doc[k].keys()
            elif glyph_list and not single_glyph:
                g_keys = glyph_list
            else:
                g_keys = [single_glyph]
            for g in g_keys:
                try:
                    build_glyph_program(g, y_doc[k][g], xgf_doc)
                except KeyError:
                    build_glyph_program(g, {}, xgf_doc)
                except Exception as e:
                    print("Exception in build_glyph_program:")
                    print(type(e))
                    print(e)
    return xgf_doc
