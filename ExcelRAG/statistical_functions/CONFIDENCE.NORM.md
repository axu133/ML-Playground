# CONFIDENCE.NORM

> Returns the confidence interval for a population mean

## Syntax
CONFIDENCE.NORM(alpha,standard_dev,size)

The CONFIDENCE.NORM function syntax has the following arguments:

AlphaRequired. The significance level used to compute the confidence level. The confidence level equals 100*(1 - alpha)%, or in other words, an alpha of 0.05 indicates a 95 percent confidence level.Standard_devRequired. The population standard deviation for the data range and is assumed to be known.SizeRequired. The sample size.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
0.05 | Significance level | 
2.5 | Standard deviation of the population | 
50 | Sample size | 
Formula | Description | Result
=CONFIDENCE.NORM(A2,A3,A4) | Confidence interval for a population mean. In other words, the confidence interval for the underlying population mean for travel to work equals 30 ± 0.692952 minutes, or 29.3 to 30.7 minutes. | 0.692952

---

[Original Documentation](https://support.microsoft.com/en-us/office/confidence-norm-function-7cec58a6-85bb-488d-91c3-63828d4fbfd4)