# EXPON.DIST

> Returns the exponential distribution

## Syntax
EXPON.DIST(x,lambda,cumulative)

The EXPON.DIST function syntax has the following arguments:

XRequired. The value of the function.LambdaRequired. The parameter value.CumulativeRequired. A logical value that indicates which form of the exponential function to provide. If cumulative is TRUE, EXPON.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
0.2 | Value of the function | 
10 | Parameter value | 
Formula | Description | Result
=EXPON.DIST(A2,A3,TRUE) | Cumulative exponential distribution function | 0.86466472
=EXPON.DIST(0.2,10,FALSE) | Probability exponential distribution function | 1.35335283

---

[Original Documentation](https://support.microsoft.com/en-us/office/expon-dist-function-4c12ae24-e563-4155-bf3e-8b78b6ae140e)