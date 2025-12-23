# PERCENTILE.INC

> Returns the k-th percentile of values in a range

## Syntax
PERCENTILE.INC(array,k)

The PERCENTILE.INC function syntax has the following arguments:

ArrayRequired. The array or range of data that defines relative standing.KRequired. The percentile value in the range 0 to 1, inclusive.

## Examples
- Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
1 |  | 
3 |  | 
2 |  | 
4 |  | 
Formula | Description | Result
=PERCENTILE.INC(A2:A5,0.3) | 30th percentile of the list in the range A2:A5. | 1.9

---

[Original Documentation](https://support.microsoft.com/en-us/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed)