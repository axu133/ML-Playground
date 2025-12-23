# AVERAGE

> Returns the average of its arguments

## Syntax
AVERAGE(number1, [number2], ...)

The AVERAGE function syntax has the following arguments:

Number1Required. The first number, cell reference, or range for which you want the average.Number2, ...Optional. Additional numbers, cell references or ranges for which you want the average, up to a maximum of 255.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
10 | 15 | 32
7 |  | 
9 |  | 
27 |  | 
2 |  | 
Formula | Description | Result
=AVERAGE(A2:A6) | Average of the numbers in cells A2 through A6. | 11
=AVERAGE(A2:A6, 5) | Average of the numbers in cells A2 through A6 and the number 5. | 10
=AVERAGE(A2:C2) | Average of the numbers in cells A2 through C2. | 19

---

[Original Documentation](https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)