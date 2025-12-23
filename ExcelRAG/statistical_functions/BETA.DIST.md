# BETA.DIST

> Returns the beta cumulative distribution function

## Syntax
BETA.DIST(x,alpha,beta,cumulative,[A],[B])

The BETA.DIST function syntax has the following arguments:

XRequired. The value between A and B at which to evaluate the functionAlphaRequired. A parameter of the distribution.BetaRequired. A parameter of the distribution.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, BETA.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.AOptional. A lower bound to the interval of x.BOptional. An upper bound to the interval of x.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
2 | Value at which to evaluate the function | 
8 | Parameter of the distribution | 
10 | Parameter of the distribution | 
1 | Lower bound | 
3 | Upper bound | 
Formula | Description | Result
=BETA.DIST(A2,A3,A4,TRUE,A5,A6) | Cumulative beta probability density function, for the above parameters | 0.6854706
=BETA.DIST(A2,A3,A4,FALSE,A5,A6) | Beta probability density function, for the above parameters | 1.4837646

---

[Original Documentation](https://support.microsoft.com/en-us/office/beta-dist-function-11188c9c-780a-42c7-ba43-9ecb5a878d31)