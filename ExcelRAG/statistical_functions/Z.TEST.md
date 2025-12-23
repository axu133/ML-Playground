# Z.TEST

> Returns the one-tailed probability-value of a z-test

## Syntax
Z.TEST(array,x,[sigma])

The Z.TEST function syntax has the following arguments:

ArrayRequired. The array or range of data against which to test x.xRequired. The value to test.SigmaOptional. The population (known) standard deviation. If omitted, the sample standard deviation is used.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
3 |  | 
6 |  | 
7 |  | 
8 |  | 
6 |  | 
5 |  | 
4 |  | 
2 |  | 
1 |  | 
9 |  | 
Formula | Description (Result) | Result
=Z.TEST(A2:A11,4) | One-tailed probability-value of a z-test for the data set above, at the hypothesized population mean of 4 (0.090574) | 0.090574
=2 * MIN(Z.TEST(A2:A11,4), 1 - Z.TEST(A2:A11,4)) | Two-tailed probability-value of a z-test for the data set above, at the hypothesized population mean of 4 (0.181148) | 0.181148
=Z.TEST(A2:A11,6) | One-tailed probability-value of a z-test for the data set above, at the hypothesized population mean of 6 (0.863043) | 0.863043
=2 * MIN(Z.TEST(A2:A11,6), 1 - Z.TEST(A2:A11,6)) | Two-tailed probability-value of a z-test for the data set above, at the hypothesized population mean of 6 (0.273913) | 0.273913

---

[Original Documentation](https://support.microsoft.com/en-us/office/z-test-function-d633d5a3-2031-4614-a016-92180ad82bee)