# AVERAGEA

> Returns the average of its arguments, including numbers, text, and logical values

## Syntax
AVERAGEA(value1, [value2], ...)

The AVERAGEA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 cells, ranges of cells, or values for which you want the average.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
10 |  | 
7 |  | 
9 |  | 
2 |  | 
Not available |  | 
Formula | Description | Result
=AVERAGEA(A2:A6) | Average of the numbers above, and the text "Not Available". The cell with the text "Not available" is used in the calculation. | 5.6
=AVERAGEA(A2:A5,A7) | Average of the numbers above, and the empty cell. | 5.6

---

[Original Documentation](https://support.microsoft.com/en-us/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091)