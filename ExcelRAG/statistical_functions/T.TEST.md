# T.TEST

> Returns the probability associated with a Student's t-test

## Syntax
T.TEST(array1,array2,tails,type)

The T.TEST function syntax has the following arguments:

Array1Required. The first data set.Array2Required. The second data set.TailsRequired. Specifies the number of distribution tails. If tails = 1, T.TEST uses the one-tailed distribution. If tails = 2, T.TEST uses the two-tailed distribution.TypeRequired. The kind of t-Test to perform.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data 1 | Data 2 | 
3 | 6 | 
4 | 19 | 
5 | 3 | 
8 | 2 | 
9 | 14 | 
1 | 4 | 
2 | 5 | 
4 | 17 | 
5 | 1 | 
Formula | Description | Result
=T.TEST(A2:A10,B2:B10,2,1) | Probability associated with a Student's paired t-Test, with a two-tailed distribution. | 0.196016

---

[Original Documentation](https://support.microsoft.com/en-us/office/t-test-function-d4e08ec3-c545-485f-962e-276f7cbed055)