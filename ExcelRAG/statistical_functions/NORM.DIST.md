# NORM.DIST

> Returns the normal cumulative distribution

## Syntax
NORM.DIST(x,mean,standard_dev,cumulative)

The NORM.DIST function syntax has the following arguments:

XRequired. The value for which you want the distribution.MeanRequired. The arithmetic mean of the distribution.Standard_devRequired. The standard deviation of the distribution.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, NORM.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
42 | Value for which you want the distribution
40 | Arithmetic mean of the distribution
1.5 | Standard deviation of the distribution
Formula | Description | Result
=NORM.DIST(A2,A3,A4,TRUE) | Cumulative distribution function for the terms above | 0.9087888
=NORM.DIST(A2,A3,A4,FALSE) | Probability mass function for the terms above | 0.10934

---

[Original Documentation](https://support.microsoft.com/en-us/office/norm-dist-function-edb1cc14-a21c-4e53-839d-8082074c9f8d)