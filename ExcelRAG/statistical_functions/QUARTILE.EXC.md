# QUARTILE.EXC

> Returns the quartile of the data set, based on percentile values from 0 to 1, exclusive

## Syntax
QUARTILE.EXC(array, quart)

The QUARTILE.EXC function syntax has the following arguments:

ArrayRequired. The array or cell range of numeric values for which you want the quartile value.QuartRequired. Indicates which value to return.

## Examples
- Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
6 |  | 
7 |  | 
15 |  | 
36 |  | 
39 |  | 
40 |  | 
41 |  | 
42 |  | 
43 |  | 
47 |  | 
49 |  | 
Formula | Description | Result
=QUARTILE.EXC(A2:A12,1) | Locates the position of the first quartile (15). | 15
=QUARTILE.EXC(A2:A12,3) | Locates the position of the third quartile (43). | 43

---

[Original Documentation](https://support.microsoft.com/en-us/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad)