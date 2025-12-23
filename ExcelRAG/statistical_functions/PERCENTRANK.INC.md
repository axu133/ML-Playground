# PERCENTRANK.INC

> Returns the percentage rank of a value in a data set

## Syntax
PERCENTRANK.INC(array,x,[significance])

The PERCENTRANK.INC function syntax has the following arguments:

ArrayRequired. The array or range of data with numeric values that defines relative standing.XRequired. The value for which you want to know the rank.SignificanceOptional. A value that identifies the number of significant digits for the returned percentage value. If omitted, PERCENTRANK.INC uses three digits (0.xxx).

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
13 |  | 
12 |  | 
11 |  | 
8 |  | 
4 |  | 
3 |  | 
2 |  | 
1 |  | 
1 |  | 
1 |  | 
Formula | Description | Result
=PERCENTRANK.INC(A2:A11,2) | Percent rank of 2 in the range A2:A11 (0.333, because 3 values in the set are smaller than 2, and 6 are larger than 2; 3/(3+6)=0.333). | 0.333
=PERCENTRANK.INC(A2:A11,4) | Percent rank of 4 in the range A2:A11. | 0.555
=PERCENTRANK.INC(A2:A11,8) | Percent rank of 8 in the range A2:A11. | 0.666
=PERCENTRANK.INC(A2:A11,5) | Percent rank of 5 in the range A2:A11 (0.583, one-quarter of the way between the PERCENTRANK.INC of 4 and the PERCENTRANK.INC of 8). | 0.583

---

[Original Documentation](https://support.microsoft.com/en-us/office/percentrank-inc-function-149592c9-00c0-49ba-86c1-c1f45b80463a)