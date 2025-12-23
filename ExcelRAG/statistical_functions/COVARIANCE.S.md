# COVARIANCE.S

> Returns the sample covariance, the average of the products deviations for each data point pair in two data sets

## Syntax
COVARIANCE.S(array1,array2)

The COVARIANCE.S function syntax has the following arguments:

Array1Required. The first cell range of integers.Array2Required. The second cell range of integers.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=COVARIANCE.S({2,4,8},{5,11,12}) | Sample covariance for the data points entered as an array in the function. | 9.666666667
2 | 5 | 
4 | 11 | 
8 | 12 | 
Formula | Description | Result
=COVARIANCE.S(A3:A5,B3:B5) | Sample covariance for the identical data points, but entered as cell ranges in the function. | 9.666666667

- Top of Page

---

[Original Documentation](https://support.microsoft.com/en-us/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977)