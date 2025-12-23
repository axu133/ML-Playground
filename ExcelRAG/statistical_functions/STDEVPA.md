# STDEVPA

> Calculates standard deviation based on the entire population, including numbers, text, and logical values

## Syntax
STDEVPA(value1, [value2], ...)

The STDEVPA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 values corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
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
Formula | Description (Result) | Result
=STDEVPA(A3:A12) | Standard deviation of breaking strength, assuming only 10 tools are produced (26.05455814) | 26.05456

---

[Original Documentation](https://support.microsoft.com/en-us/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c)