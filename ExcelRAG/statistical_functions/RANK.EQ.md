# RANK.EQ

> Returns the rank of a number in a list of numbers

## Syntax
RANK.EQ(number,ref,[order])

The RANK.EQ function syntax has the following arguments:

NumberRequired. The number whose rank you want to find.RefRequired. An array of, or a reference to, a list of numbers. Non-numeric values in Ref are ignored.OrderOptional. A number specifying how to rank number.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data |  | 
7 |  | 
3.5 |  | 
3.5 |  | 
1 |  | 
2 |  | 
Formula | Description | Result
=RANK.EQ(A2,A2:A6,1) | Rank of 7 in the list contained in the range A2:A6. Because the Order argument (1) is a non-zero value, the list is sorted lowest to highest. | 5
=RANK.EQ(A6,A2:A6) | Rank of 2 in the same list. Because the Order argument is omitted, the list is sorted, by default, highest to lowest. | 4
=RANK.EQ(A3,A2:A6,1) | Rank of 3.5 in the same list. | 3

---

[Original Documentation](https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40)