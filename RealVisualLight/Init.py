import FreeCAD
import FreeCADGui
import RVL_Settings

# ============================================================
#  RealVisualLight - Automatic Visual Optimization Engine
# ============================================================

def apply_visual_settings():
    """Applica le impostazioni grafiche in base alla complessità del modello."""
    mode = RVL_Settings.detect_complexity()

    # Modalità Alta Qualità
    if mode == "HighQuality":
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshDeviation", 0.1)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshAngularDeflection", 10)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseShadow", True)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseTransparency", True)

    # Modalità Bilanciata
    elif mode == "Balanced":
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshDeviation", 0.25)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshAngularDeflection", 20)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseShadow", False)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseTransparency", True)

    # Modalità Ultra Leggera (per file pesanti)
    elif mode == "UltraLight":
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshDeviation", 0.5)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part").SetFloat("MeshAngularDeflection", 30)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseShadow", False)
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetBool("UseTransparency", False)

    FreeCAD.Console.PrintMessage(f"[RealVisualLight] Modalità attiva: {mode}\n")


# Applica le impostazioni quando FreeCAD carica un documento
def on_document_open(doc):
    FreeCAD.Console.PrintMessage("[RealVisualLight] Analisi complessità modello in corso...\n")
    apply_visual_settings()


# Collega l’evento di apertura documento
FreeCAD.addDocumentObserver(type("RVL_DocObserver", (), {"slotCreatedDocument": on_document_open})())
