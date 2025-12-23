# CONFIDENCE.T

> Returns the confidence interval for a population mean, using a Student's t distribution

## Syntax
CONFIDENCE.T(alpha,standard_dev,size)

The CONFIDENCE.T function syntax has the following arguments:

AlphaRequired. The significance level used to compute the confidence level. The confidence level equals 100*(1 - alpha)%, or in other words, an alpha of 0.05 indicates a 95 percent confidence level.Standard_devRequired. The population standard deviation for the data range and is assumed to be known.SizeRequired. The sample size.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=CONFIDENCE.T(0.05,1,50) | Confidence interval for the mean of a population based on a sample size of 50, with a 5% significance level and a standard deviation of 1. This is based on a Student's t-distribution. | 0.284196855

---

[Original Documentation](https://support.microsoft.com/en-us/office/confidence-t-function-e8eca395-6c3a-4ba9-9003-79ccc61d3c53)