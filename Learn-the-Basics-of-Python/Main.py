from PrintOnScreen import DisplayMsg
from PythonVariables import biodata

dsp = DisplayMsg("CallingClassesFromHere")
dsp.see("Hello World")

data = biodata("Stephan", 1997, 2023)
data.display_data()
data.get_age()

