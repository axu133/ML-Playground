# VAR.S

> Estimates variance based on a sample

## Syntax
VAR.S(number1,[number2],...)

The VAR.S function syntax has the following arguments:

Number1Required. The first number argument corresponding to a sample of a population.Number2, ...Optional. Number arguments 2 to 254 corresponding to a sample of a population.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Strength |  | 
1345 |  | 
1301 |  | 
1368 |  | 
1322 |  | 
1310 |  | 
1370 |  | 
1318 |  | 
1350 |  | 
1303 |  | 
1299 |  | 
Formula | Description | Result
=VAR.S(A2:A11) | Variance for the breaking strength of the tools, when the values in A2:A11 represent only a sample of all the data. VAR.S returns a different result than VAR.P, which treats the range of data as the entire population. | 754.27
=VAR.P(A2:A11) | The variance based on the entire population, using the VAR.P function, returns a different result. | 678.84

---

[Original Documentation](https://support.microsoft.com/en-us/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b)