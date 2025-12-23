# COUNT

> Counts how many numbers are in the list of arguments

## Syntax
COUNT(value1, [value2], ...)

The COUNT function syntax has the following arguments:

value1Required. The first item, cell reference, or range within which you want to count numbers.value2, ...Optional. Up to 255 additional items, cell references, or ranges within which you want to count numbers.

Note:The arguments can contain or refer to a variety of different types of data, but only numbers are counted.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
12/8/08 |  | 
 |  | 
19 |  | 
22.24 |  | 
TRUE |  | 
#DIV/0! |  | 
Formula | Description | Result
=COUNT(A2:A6) | Counts the number of cells that contain numbers in cells A2 through A7. | 3
=COUNT(A5:A6) | Counts the number of cells that contain numbers in cells A5 through A7. | 1
=COUNT(A2:A6,2) | Counts the number of cells that contain numbers in cells A2 through A7, and the value 2 | 4

---

[Original Documentation](https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c)