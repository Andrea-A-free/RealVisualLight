import FreeCAD as App
import FreeCADGui as Gui
import RVL_Settings as S

def applyRealVisualLight():
    """Applica la visualizzazione ottimizzata usando i parametri personalizzabili"""
    try:
        view = Gui.ActiveDocument.ActiveView
    except:
        return

    # Impostazioni di visualizzazione
    view.setCameraType(S.CAMERA)
    view.setAxisCross(S.AXIS)
    view.setGrid(S.GRID)
    view.setBackgroundColor(S.BACKGROUND)
    view.setHighlightColor(S.HIGHLIGHT)
    view.setSelectionColor(S.SELECTION)

    print("RealVisualLight: visualizzazione applicata")

# --- Observer per apertura file ---
class RVL_DocObserver:
    def slotCreatedDocument(self, doc):
        applyRealVisualLight()

    def slotRestoredDocument(self, doc):
        applyRealVisualLight()

docObserver = RVL_DocObserver()
App.addDocumentObserver(docObserver)

# --- Observer per cambio Workbench ---
def onWorkbenchActivated():
    applyRealVisualLight()

Gui.getMainWindow().workbenchActivated.connect(onWorkbenchActivated)

# --- Registrazione Workbench ---
class RealVisualLightWorkbench(Gui.Workbench):
    MenuText = "Real Visual Light"
    ToolTip = "Motore di visualizzazione ottimizzato"
    Icon = "resources/icons/rvl_icon.svg"

    def Initialize(self):
        pass

    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui.addWorkbench(RealVisualLightWorkbench())




