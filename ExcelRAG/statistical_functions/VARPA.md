# VARPA

> Calculates variance based on the entire population, including numbers, text, and logical values

## Syntax
VARPA(value1, [value2], ...)

The VARPA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 value arguments corresponding to a population.

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
=VARPA(A2:A11) | Variance of breaking strengths for all the tools, assuming that only 10 tools are produced (entire population). | 678.84
=VAR(A2:A11) | This example uses the VAR function, which assumes a sample of the population, and returns a different result. | 754.27

---

[Original Documentation](https://support.microsoft.com/en-us/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96)