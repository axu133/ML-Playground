# BETA.INV

> Returns the inverse of the cumulative distribution function for a specified beta distribution

## Syntax
BETA.INV(probability,alpha,beta,[A],[B])

The BETA.INV function syntax has the following arguments:

ProbabilityRequired. A probability associated with the beta distribution.AlphaRequired. A parameter of the distribution.BetaRequired. A parameter the distribution.AOptional. A lower bound to the interval of x.BOptional. An upper bound to the interval of x.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | 
0.685470581 | Probability associated with the beta distribution | 
8 | Parameter of the distribution | 
10 | Parameter of the distribution | 
1 | Lower bound | 
3 | Upper bound | 
Formula | Description | Result
=BETA.INV(A2,A3,A4,A5,A6) | Inverse of the cumulative beta probability density function for the parameters above. | 2

---

[Original Documentation](https://support.microsoft.com/en-us/office/beta-inv-function-e84cb8aa-8df0-4cf6-9892-83a341d252eb)