import os, tempfile
import rpy2.robjects as ro
from rpy2.robjects.vectors import StrVector, IntVector, BoolVector
from IPython.display import Image, display
from Utils import dsld_Rpy2_IsRDataframe
from rpy2.robjects.packages import importr

R_NULL = ro.NULL

dsld = importr("dsld")
qeML = importr("qeML")
grdevices = importr("grDevices")

def _maybe_strvec(x):
    if x is None or x is R_NULL: return R_NULL
    return StrVector(list(x) if isinstance(x, (list, tuple)) else [str(x)])

def dsldPyConditDisparity(data, yName, sName, xName, condits = R_NULL, qeFtn="qeKNN", minS=50, useLoess=True):
    r_data   = dsld_Rpy2_IsRDataframe(data)
    yName_r  = StrVector([yName])
    sName_r  = StrVector([sName])
    xName_r  = StrVector([xName])
    condits_r = _maybe_strvec(None if condits is R_NULL else condits)

    if hasattr(qeML, qeFtn) and callable(getattr(qeML, qeFtn)):
        qeFtn_r = getattr(qeML, qeFtn)
    else:
        print(f"ERROR: qeML do not have function name: '{qeFtn}'"); return

    minS_r = IntVector([int(minS)])
    useLoess_r = BoolVector([bool(useLoess)])

    fd, tmpfile = tempfile.mkstemp(suffix=".png"); os.close(fd)
    grdevices.png(file=tmpfile, width=1200, height=800, res=150)
    try:
        res = dsld.dsldConditDisparity(r_data, yName_r, sName_r, xName_r, condits_r, qeFtn_r, minS_r, useLoess_r)
        try: ro.r("print")(res)
        except: pass
    finally:
        grdevices.dev_off()

    if os.path.exists(tmpfile): display(Image(filename=tmpfile))
    return
