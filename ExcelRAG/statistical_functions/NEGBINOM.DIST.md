# NEGBINOM.DIST

> Returns the negative binomial distribution

## Syntax
NEGBINOM.DIST(number_f,number_s,probability_s,cumulative)

The NEGBINOM.DIST function syntax has the following arguments:

Number_fRequired. The number of failures.Number_sRequired. The threshold number of successes.Probability_sRequired. The probability of a success.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, NEGBINOM.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
10 | Number of failures | 
5 | Threshold number of successes
0.25 | Probability of a success | 
Formula | Description | Result
=NEGBINOM.DIST(A2,A3,A4,TRUE) | Cumulative negative binomial distribution for the terms above | 0.3135141
=NEGBINOM.DIST(A2,A3,A4,FALSE) | Probability negative binomial distribution for the terms above | 0.0550487

---

[Original Documentation](https://support.microsoft.com/en-us/office/negbinom-dist-function-c8239f89-c2d0-45bd-b6af-172e570f8599)