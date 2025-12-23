# MINA

> Returns the smallest value in a list of arguments, including numbers, text, and logical values

## Syntax
MINA(value1, [value2], ...)

The MINA function syntax has the following arguments:

Value1, value2, ...Value1 is required, subsequent values are optional. 1 to 255 values for which you want to find the smallest value.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
FALSE |  | 
0.2 |  | 
0.5 |  | 
0.4 |  | 
0.8 |  | 
Formula | Description | Result
=MINA(A2:A6) | Smallest of the numbers in the range A2:A6. Because a value of FALSE evaluates to 0, it is the smallest. | 0

---

[Original Documentation](https://support.microsoft.com/en-us/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3)