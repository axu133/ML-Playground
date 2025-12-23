# VARA

> Estimates variance based on a sample, including numbers, text, and logical values

## Syntax
VARA(value1, [value2], ...)

The VARA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 value arguments corresponding to a sample of a population.

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
=VARA(A2:A11) | Estimates the variance for the breaking strength of the tools being tested. VARA assumes a population sample. | 754.26667

---

[Original Documentation](https://support.microsoft.com/en-us/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07)