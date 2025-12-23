# COUNTIFS

> Counts the number of cells within a range that meet multiple criteria

## Syntax
COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2]…)

The COUNTIFS function syntax has the following arguments:

criteria_range1Required. The first range in which to evaluate the associated criteria.criteria1Required. The criteria in the form of a number, expression, cell reference, or text that define which cells will be counted. For example, criteria can be expressed as 32, ">32", B4, "apples", or "32".criteria_range2, criteria2, ...Optional. Additional ranges and their associated criteria. Up to 127 range/criteria pairs are allowed.

Important:Each additional range must have the same number of rows and columns as thecriteria_range1argument. The ranges do not have to be adjacent to each other.

## Examples
- Copy the example data in the following tables, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Salesperson | Exceeded Q1 quota | Exceeded Q2 quota | Exceeded Q3 quota
Davidoski | Yes | No | No
Burke | Yes | Yes | No
Sundaram | Yes | Yes | Yes
Levitan | No | Yes | Yes
Formula | Description | Result | 
=COUNTIFS(B2:D2,"=Yes") | Counts how many times Davidoski exceeded a sales quota for periods Q1, Q2, and Q3 (only in Q1). | 1 | 
=COUNTIFS(B2:B5,"=Yes",C2:C5,"=Yes") | Counts how many salespeople exceeded both their Q1 and Q2 quotas (Burke and Sundaram). | 2 | 
=COUNTIFS(B5:D5,"=Yes",B3:D3,"=Yes") | Counts how many times Levitan and Burke exceeded the same quota for periods Q1, Q2, and Q3 (only in Q2). | 1 | 

---

[Original Documentation](https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)