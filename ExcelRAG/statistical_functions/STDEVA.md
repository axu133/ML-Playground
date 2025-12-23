# STDEVA

> Estimates standard deviation based on a sample, including numbers, text, and logical values

## Syntax
STDEVA(value1, [value2], ...)

The STDEVA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 values corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

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
=STDEVA(A3:A12) | Standard deviation of breaking strength for all the tools (27.46391572) | 27.46391572

---

[Original Documentation](https://support.microsoft.com/en-us/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d)