# TRIMMEAN

> Returns the mean of the interior of a data set

## Syntax
TRIMMEAN(array, percent)

The TRIMMEAN function syntax has the following arguments:

ArrayRequired. The array or range of values to trim and average.PercentRequired. The fractional number of data points to exclude from the calculation. For example, if percent = 0.2, 4 points are trimmed from a data set of 20 points (20 x 0.2): 2 from the top and 2 from the bottom of the set.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
4 |  | 
5 |  | 
6 |  | 
7 |  | 
2 |  | 
3 |  | 
4 |  | 
5 |  | 
1 |  | 
2 |  | 
3 |  | 
Formula | Description | Result
=TRIMMEAN(A2:A12,0.2) | Mean of the interior of the data set contained in A2:A12, with 20 percent excluded from calculation. | 3.778

---

[Original Documentation](https://support.microsoft.com/en-us/office/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3)