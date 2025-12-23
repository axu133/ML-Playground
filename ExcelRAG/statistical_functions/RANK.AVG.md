# RANK.AVG

> Returns the rank of a number in a list of numbers

## Syntax
RANK.AVG(number,ref,[order])

The RANK.AVG function syntax has the following arguments:

NumberRequired. The number whose rank you want to find.RefRequired. An array of, or a reference to, a list of numbers. Nonnumeric values in Ref are ignored.OrderOptional. A number specifying how to rank number.

## Examples
- Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Day | Temp (F) | 
7/1/2011 | 89 | 
7/2/2011 | 88 | 
7/3/2011 | 92 | 
7/4/2011 | 101 | 
7/5/2011 | 94 | 
7/6/2011 | 97 | 
7/7/2011 | 95 | 
Formula | Description | Result
=RANK.AVG(94,B2:B8) | Finds the rank (the position) of the value 94 in the cell range B2:B8. In this case, 7/5/11, when the temperature reached 94, was the 4th hottest day of the days listed. | 4

---

[Original Documentation](https://support.microsoft.com/en-us/office/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a)