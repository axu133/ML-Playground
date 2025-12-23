# PROB

> Returns the probability that values in a range are between two limits

## Syntax
PROB(x_range, prob_range, [lower_limit], [upper_limit])

The PROB function syntax has the following arguments:

X_rangeRequired. The range of numeric values of x with which there are associated probabilities.Prob_rangeRequired. A set of probabilities associated with values in x_range.Lower_limitOptional. The lower bound on the value for which you want a probability.Upper_limitOptional. The optional upper bound on the value for which you want a probability.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
Value of x | Probability | 
0 | 0.2 | 
1 | 0.3 | 
2 | 0.1 | 
3 | 0.4 | 
Formula | Description | Result
=PROB(A3:A6,B3:B6,2) | Probability that x is 2. | 0.1
=PROB(A3:A6,B3:B6,1,3) | Probability that x is between 1 and 3. | 0.8

---

[Original Documentation](https://support.microsoft.com/en-us/office/prob-function-9ac30561-c81c-4259-8253-34f0a238fc49)