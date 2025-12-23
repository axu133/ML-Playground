# POISSON.DIST

> Returns the Poisson distribution

## Syntax
POISSON.DIST(x,mean,cumulative)

The POISSON.DIST function syntax has the following arguments:

XRequired. The number of events.MeanRequired. The expected numeric value.CumulativeRequired. A logical value that determines the form of the probability distribution returned. If cumulative is TRUE, POISSON.DIST returns the cumulative Poisson probability that the number of random events occurring will be between zero and x inclusive; if FALSE, it returns the Poisson probability mass function that the number of events occurring will be exactly x.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
2 | Number of events | 
5 | Expected mean | 
Formula | Description | Result
=POISSON.DIST(A2,A3,TRUE) | Cumulative Poisson probability with the arguments specified in A2 and A3. | 0.124652
=POISSON.DIST(A2,A3,FALSE) | Poisson probability mass function with the arguments specified in A2 and A3. | 0.084224

---

[Original Documentation](https://support.microsoft.com/en-us/office/poisson-dist-function-8fe148ff-39a2-46cb-abf3-7772695d9636)