import FreeCAD

# ============================================================
#  RealVisualLight - Settings & Automatic Complexity Detection
# ============================================================

def get_auto_mode_enabled():
    """Ritorna True se la modalità automatica è attiva."""
    return FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/RealVisualLight").GetBool("AutoMode", True)

def set_auto_mode_enabled(value):
    """Attiva o disattiva la modalità automatica."""
    FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/RealVisualLight").SetBool("AutoMode", value)

def detect_complexity():
    """Analizza il modello e determina la modalità migliore."""
    doc = FreeCAD.ActiveDocument
    if not doc:
        return "Balanced"

    objs = doc.Objects
    num_objs = len(objs)
    num_solids = len([o for o in objs if hasattr(o, "Shape") and o.Shape.Solids])
    num_booleans = len([o for o in objs if o.TypeId.startswith("Part::Boolean")])
    num_visible = len([o for o in objs if o.ViewObject.Visibility])

    # Punteggio di complessità
    score = num_objs + num_solids * 2 + num_booleans * 3

    if score < 150:
        return "HighQuality"
    elif score < 400:
        return "Balanced"
    else:
        return "UltraLight"
