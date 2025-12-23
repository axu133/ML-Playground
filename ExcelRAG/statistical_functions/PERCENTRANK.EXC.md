# PERCENTRANK.EXC

> Returns the rank of a value in a data set as a percentage (0 to 1, exclusive) of the data set

## Syntax
PERCENTRANK.EXC(array,x,[significance])

The PERCENTRANK.EXC function syntax has the following arguments:

ArrayRequired. The array or range of data with numeric values that defines relative standingXRequired. The value for which you want to know the rank.SignificanceOptional. A value that identifies the number of significant digits for the returned percentage value. If omitted, PERCENTRANK.EXC uses three digits (0.xxx).

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
1 |  | 
2 |  | 
3 |  | 
6 |  | 
6 |  | 
6 |  | 
7 |  | 
8 |  | 
9 |  | 
Formula | Description | Result
=PERCENTRANK.EXC(A2:A10, 7) | Returns the rank of the value 7 from the array contained in A2:A10. | 0.7
=PERCENTRANK.EXC(A2:A10,5.43) | Returns the rank of the value 5.43 in the same array. | 0.381
=PERCENTRANK.EXC(A2:A10,5.43,1) | Returns the rank of the value 5.43 in the same array, displaying only 1 significant digit in the result (the default is 3). | 0.3

---

[Original Documentation](https://support.microsoft.com/en-us/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314)