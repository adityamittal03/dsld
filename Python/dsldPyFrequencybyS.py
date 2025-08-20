import os, tempfile
import rpy2.robjects as ro
from rpy2.robjects.vectors import StrVector, IntVector, BoolVector
from IPython.display import Image, display
from Utils import dsld_Rpy2_IsRDataframe, dsld_Rpy2_RDataframeToPandas
from rpy2.robjects.packages import importr

R_NULL = ro.NULL

dsld = importr("dsld")
qeML = importr("qeML")
grdevices = importr("grDevices")

def dsldPyFrequencybyS(data, cName, sName):

    r_data = dsld_Rpy2_IsRDataframe(data)
    cName_r = StrVector([cName])
    sName_r = StrVector([sName])

    res = dsld.dsldFrequencyByS(r_data, cName_r, sName_r)
    return dsld_Rpy2_RDataframeToPandas(res)

