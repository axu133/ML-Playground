# VAR.P

> Calculates variance based on the entire population

## Syntax
VAR.P(number1,[number2],...)

The VAR.P function syntax has the following arguments:

Number1Required. The first number argument corresponding to a population.Number2, ...Optional. Number arguments 2 to 254 corresponding to a population.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Strength |  | 
1,345 |  | 
1,301 |  | 
1,368 |  | 
1,322 |  | 
1,310 |  | 
1,370 |  | 
1,318 |  | 
1,350 |  | 
1,303 |  | 
1,299 |  | 
Formula | Description | Result
=VAR.P(A2:A11) | Variance of breaking strengths for all the tools, assuming that only 10 tools are produced (the entire population is used). | 678.84
=VAR.S(A2:A11) | The variance, using the VAR.S function, which assumes only a sample of the population is tested. The result is different from VAR.P. | 754.27

---

[Original Documentation](https://support.microsoft.com/en-us/office/var-p-function-73d1285c-108c-4843-ba5d-a51f90656f3a)