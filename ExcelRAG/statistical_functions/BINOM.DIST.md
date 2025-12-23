# BINOM.DIST

> Returns the individual term binomial distribution probability

## Syntax
BINOM.DIST(number_s,trials,probability_s,cumulative)

The BINOM.DIST function syntax has the following arguments:

Number_sRequired. The number of successes in trials.TrialsRequired. The number of independent trials.Probability_sRequired. The probability of success on each trial.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, then BINOM.DIST returns the cumulative distribution function, which is the probability that there are at most number_s successes; if FALSE, it returns the probability mass function, which is the probability that there are number_s successes.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
6 | Number of successes in trials | 
10 | Number of independent trials | 
0.5 | Probability of success on each trial | 
Formula | Description | Result
=BINOM.DIST(A2,A3,A4,FALSE) | Probability of exactly 6 of 10 trials being successful. | 0.2050781

---

[Original Documentation](https://support.microsoft.com/en-us/office/binom-dist-function-c5ae37b6-f39c-4be2-94c2-509a1480770c)