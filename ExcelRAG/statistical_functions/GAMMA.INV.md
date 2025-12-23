# GAMMA.INV

> Returns the inverse of the gamma cumulative distribution

## Syntax
GAMMA.INV(probability,alpha,beta)

The GAMMA.INV function syntax has the following arguments:

ProbabilityRequired. The probability associated with the gamma distribution.AlphaRequired. A parameter to the distribution.BetaRequired. A parameter to the distribution. If beta = 1, GAMMA.INV returns the standard gamma distribution.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
0.068094 | Probability associated with the gamma distribution | 
9 | Alpha parameter to the distribution | 
2 | Beta parameter to the distribution | 
Formula | Description | Result
=GAMMA.INV(A2,A3,A4) | Inverse of the gamma cumulative distribution for the probability, alpha, and beta arguments in A2, A3, and A4. | 10.0000112

---

[Original Documentation](https://support.microsoft.com/en-us/office/gamma-inv-function-74991443-c2b0-4be5-aaab-1aa4d71fbb18)