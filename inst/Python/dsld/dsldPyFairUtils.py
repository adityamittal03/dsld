### NOT DONE AT ALL

'''
Python interface for dsldFairUtils functions in the dsld R package.
'''

from Utils import dsld_Rpy2_IsRDataframe, R_NULL, dsld_Rpy2_RDataframeToPandas
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

dsld = importr("dsld")

def dsldPyFairUtils(data, yName, sName, dsldFTNname, unfairness = R_NULL, deweightPars = R_NULL, yesYVal = R_NULL, k_folds = 5):
    r_data = dsld_Rpy2_IsRDataframe(data)
    yName_r = robjects.StrVector([yName])
    sName_r = robjects.StrVector([sName])
    dsldFTNname_r = robjects.StrVector([dsldFTNname])
    
    unfairness_r = robjects.FloatVector(unfairness) if unfairness is not R_NULL else R_NULL
    deweightPars_r = robjects.FloatVector(deweightPars) if deweightPars is not R_NULL else R_NULL
    yesYVal_r = robjects.StrVector([yesYVal]) if yesYVal is not R_NULL else R_NULL
    k_folds_r = robjects.IntVector([k_folds]) if k_folds is not R_NULL else R_NULL

    model = dsld.dsldFairUtils(r_data, yName_r, sName_r, dsldFTNname_r, unfairness_r, deweightPars_r, yesYVal_r, k_folds_r, R_NULL)
    
    return dsld_Rpy2_RDataframeToPandas(model)

