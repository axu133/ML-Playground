# WEIBULL.DIST

> Returns the Weibull distribution

## Syntax
WEIBULL.DIST(x,alpha,beta,cumulative)

The WEIBULL.DIST function syntax has the following arguments:

XRequired. The value at which to evaluate the function.AlphaRequired. A parameter to the distribution.BetaRequired. A parameter to the distribution.CumulativeRequired. Determines the form of the function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
105 | Value at which to evaluate the function | 
20 | Alpha parameter to the distribution | 
100 | Beta parameter to the distribution | 
Formula | Description (Result) | Result
=WEIBULL.DIST(A2,A3,A4,TRUE) | Weibull cumulative distribution function for the terms above (0.929581) | 0.929581
=WEIBULL.DIST(A2,A3,A4,FALSE) | Weibull probability density function for the terms above (0.035589) | 0.035589

---

[Original Documentation](https://support.microsoft.com/en-us/office/weibull-dist-function-4e783c39-9325-49be-bbc9-a83ef82b45db)