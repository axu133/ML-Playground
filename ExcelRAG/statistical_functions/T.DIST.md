# T.DIST

> Returns the Percentage Points (probability) for the Student t-distribution

## Syntax
T.DIST(x,deg_freedom, cumulative)

The T.DIST function syntax has the following arguments:

XRequired. The numeric value at which to evaluate the distributionDeg_freedomRequired. An integer indicating the number of degrees of freedom.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, T.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=T.DIST(60,1,TRUE) | Student's left-tailed t-distribution for 60, returned as the cumulative distribution function, using 1 degree of freedom. | 0.99469533
=T.DIST(8,3,FALSE) | Student's left-tailed t-distribution for 8, returned as the probability density function, using 3 degrees of freedom. | 0.00073691

- Top of Page

---

[Original Documentation](https://support.microsoft.com/en-us/office/t-dist-function-4329459f-ae91-48c2-bba8-1ead1c6c21b2)