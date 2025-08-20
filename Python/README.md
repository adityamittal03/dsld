# DSLD: Data Science Looks at Discrimination (Python Interfaces)

The **dsld** package includes working Python interfaces for all R functions.  
Using `rpy2`, users can directly call the R functions from Python and easily replicate results.

Ideally, users should have an understanding of how the functions are supposed to be used in R to make the 
the usage intuitive --- at least until I add more documentation and checks.

## Installation
To install the necessary dependencies [Docker instructions to be added].

## Examples
Examples of how the functions are structured and run can be found in the Jupyter notebooks under the `examples/` subfolder:

- **machine_learning.ipynb**: demonstrates the `dsldFairML` and `dsldQeFairML` wrappers and shows how to train/test models with cross-validation.  
- **graphical.ipynb**: provides examples of graphical methods for sensitive data analysis available in dsld.  
- **tabular.ipynb**: covers tabular and analytical methods for sensitive data analysis available in dsld.  

> Before running, please check the example notebooks for how to prepare the data — a few simple steps are required before making function calls.

---

**To Do:**  
- Add OS shell functionality to allow calling dsld directly from the command line.  
- Add reproducible docker file
- Clean arguments
- Documentation?

