# STDEV.S

> Estimates standard deviation based on a sample

## Syntax
STDEV.S(number1,[number2],...)

The STDEV.S function syntax has the following arguments:

Number1Required. The first number argument corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.Number2, ...Optional. Number arguments 2 to 254 corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

## Examples
- Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. (Do not copy the cell containing the word "Data".) For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

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
Formula | Description | Result
=STDEV.S(A2:A11) | Standard deviation of breaking strength. | 27.46391572

---

[Original Documentation](https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23)