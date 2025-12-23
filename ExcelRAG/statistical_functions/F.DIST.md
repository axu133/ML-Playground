# F.DIST

> Returns the F probability distribution

## Syntax
F.DIST(x,deg_freedom1,deg_freedom2,cumulative)

The F.DIST function syntax has the following arguments:

XRequired. The value at which to evaluate the function.Deg_freedom1Required. The numerator degrees of freedom.Deg_freedom2Required. The denominator degrees of freedom.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, F.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
15.2069 | Value at which to evaluate the function | 
6 | Numerator degrees of freedom | 
4 | Denominator degrees of freedom | 
Formula | Description | Result
=F.DIST(A2,A3,A4,TRUE) | F probability using the cumulative distribution function (TRUE cumulative argument). | 0.99
=F.DIST(A2,A3,A4,FALSE) | F probability using the probability density function (FALSE cumulative argument). | 0.0012238

- Top of Page

---

[Original Documentation](https://support.microsoft.com/en-us/office/f-dist-function-a887efdc-7c8e-46cb-a74a-f884cd29b25d)