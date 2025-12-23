# LOGNORM.DIST

> Returns the cumulative lognormal distribution

## Syntax
LOGNORM.DIST(x,mean,standard_dev,cumulative)

The LOGNORM.DIST function syntax has the following arguments:

XRequired. The value at which to evaluate the function.MeanRequired. The mean of ln(x).Standard_devRequired. The standard deviation of ln(x).CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, LOGNORM.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
4 | Value at which to evaluate the function (x)
3.5 | Mean of ln(x) | 
1.2 | Standard deviation of ln(x) | 
Formula | Description | Result
=LOGNORM.DIST(A2,A3,A4,TRUE) | Cumulative lognormal distribution at 4, using the arguments in A2:A4. | 0.0390836
=LOGNORM.DIST(A2,A3,A4,FALSE) | Probability lognormal distribution at 4, using the same arguments. | 0.0176176

---

[Original Documentation](https://support.microsoft.com/en-us/office/lognorm-dist-function-eb60d00b-48a9-4217-be2b-6074aee6b070)