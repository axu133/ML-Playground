# CHISQ.DIST

> Returns the cumulative beta probability density function

## Syntax
CHISQ.DIST(x,deg_freedom,cumulative)

The CHISQ.DIST function syntax has the following arguments:

XRequired. The value at which you want to evaluate the distribution.Deg_freedomRequired. The number of degrees of freedom.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, CHISQ.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=CHISQ.DIST(0.5,1,TRUE) | The chi-squared distribution for 0.5, returned as the cumulative distribution function, using 1 degree of freedom. | 0.52049988
=CHISQ.DIST(2,3,FALSE) | The chi-squared distribution for 2, returned as the probability density function, using 3 degrees of freedom. | 0.20755375

---

[Original Documentation](https://support.microsoft.com/en-us/office/chisq-dist-function-8486b05e-5c05-4942-a9ea-f6b341518732)