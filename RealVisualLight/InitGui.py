import FreeCADGui
import FreeCAD

# ============================================================
#  RealVisualLight - Workbench Integration
# ============================================================

class RealVisualLightWorkbench(FreeCADGui.Workbench):

    MenuText = "RealVisualLight"
    ToolTip = "Ottimizzazione automatica della visualizzazione"
    Icon = """
    /* SVG ICON */
    """

    def Initialize(self):
        FreeCAD.Console.PrintMessage("[RealVisualLight] Workbench attivato.\n")

    def Activated(self):
        FreeCAD.Console.PrintMessage("[RealVisualLight] Analisi automatica attiva.\n")

    def Deactivated(self):
        pass

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(RealVisualLightWorkbench())
