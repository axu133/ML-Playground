# GAMMA.DIST

> Returns the gamma distribution

## Syntax
GAMMA.DIST(x,alpha,beta,cumulative)

The GAMMA.DIST function syntax has the following arguments:

XRequired. The value at which you want to evaluate the distribution.AlphaRequired. A parameter to the distribution.BetaRequired. A parameter to the distribution. If beta = 1, GAMMA.DIST returns the standard gamma distribution.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, GAMMA.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
10.00001131 | Value at which you want to evaluate the distribution | 
9 | Alpha parameter to the distribution | 
2 | Beta parameter to the distribution | 
Formula | Description | Result
=GAMMA.DIST(A2,A3,A4,FALSE) | Probability density using the x, alpha, and beta values in A2, A3, A4, with FALSE cumulative argument. | 0.032639
=GAMMA.DIST(A2,A3,A4,TRUE) | Cumulative distributuion using the x, alpha, and beta values in A2, A3, A4, with TRUE cumulative argument. | 0.068094

---

[Original Documentation](https://support.microsoft.com/en-us/office/gamma-dist-function-9b6f1538-d11c-4d5f-8966-21f6a2201def)