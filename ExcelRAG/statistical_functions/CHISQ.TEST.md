# CHISQ.TEST

> Returns the test for independence

## Syntax
CHISQ.TEST(actual_range,expected_range)

The CHISQ.TEST function syntax has the following arguments:

Actual_rangeRequired. The range of data that contains observations to test against expected values.Expected_rangeRequired. The range of data that contains the ratio of the product of row totals and column totals to the grand total.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Men (Actual) | Women (Actual) | Description
58 | 35 | Agree
11 | 25 | Neutral
10 | 23 | Disagree
Men (Expected) | Women (Expected) | Description
45.35 | 47.65 | Agree
17.56 | 18.44 | Neutral
16.09 | 16.91 | Disagree
Formula | Description | Result
=CHISQ.TEST(A2:B4,A6:B8) | The χ2 statistic for the data above is 16.16957 with 2 degrees of freedom | 0.0003082

---

[Original Documentation](https://support.microsoft.com/en-us/office/chisq-test-function-2e8a7861-b14a-4985-aa93-fb88de3f260f)