import os, tempfile
import rpy2.robjects as ro
from rpy2.robjects.vectors import StrVector, IntVector, BoolVector
from IPython.display import Image, display
from Utils import dsld_Rpy2_IsRDataframe, dsld_Rpy2_RDataframeToPandas
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

R_NULL = ro.NULL

dsld = importr("dsld")
qeML = importr("qeML")
grdevices = importr("grDevices")

def dsldPyMatchedATE(data,yName,sName,yesSVal,yesYVal=R_NULL,propensFtn=R_NULL,k=R_NULL):

    r_data = dsld_Rpy2_IsRDataframe(data)
    yName_r = robjects.StrVector([yName])
    sName_r = robjects.StrVector([sName])
    yesSVal_r = robjects.StrVector([yesSVal])

    if yesYVal != R_NULL:
        yesYVal_r = robjects.StrVector([yesYVal])
    else:
        yesYVal_r = R_NULL

    if propensFtn != R_NULL:
        propensFtn_r = robjects.StrVector([propensFtn])
    else:
        propensFtn_r = R_NULL

    if k != R_NULL:
        k_r = robjects.IntVector([k])
    else:
        k_r = R_NULL

    res = dsld.dsldMatchedATE(r_data,yName_r,sName_r,yesSVal_r,yesYVal_r,propensFtn_r,k_r)

    ro.r("summary")(res)

    return


