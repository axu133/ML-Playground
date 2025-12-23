# AVERAGEIF

> Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria

## Syntax
AVERAGEIF(range, criteria, [average_range])

The AVERAGEIF function syntax has the following arguments:

RangeRequired. One or more cells to average, including numbers or names, arrays, or references that contain numbers.CriteriaRequired. The criteria in the form of a number, expression, cell reference, or text that defines which cells are averaged. For example, criteria can be expressed as 32, "32", ">32", "apples", or B4.Average_rangeOptional. The actual set of cells to average. If omitted, range is used.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Property Value | Commission | 
100000 | 7000 | 
200000 | 14000 | 
300000 | 21000 | 
400000 | 28000 | 
Formula | Description | Result
=AVERAGEIF(B2:B5,"<23000") | Average of all commissions less than 23000. Three of the four commissions meet this condition, and their total is 42000. | 14000
=AVERAGEIF(A2:A5,"<250000") | Average of all property values less than 250000. Two of the four property values meet this condition, and their total is 300000. | 150000
=AVERAGEIF(A2:A5,"<95000") | Average of all property values less than 95000. Because there are 0 property values that meet this condition, the AVERAGEIF function returns the #DIV/0! error because it tries to divide by 0. | #DIV/0!
=AVERAGEIF(A2:A5,">250000",B2:B5) | Average of all commissions with a property value greater than 250000. Two commissions meet this condition, and their total is 49000. | 24500

- Example 2RegionProfits (Thousands)East45678West23789North-4789South (New Office)0MidWest9678FormulaDescriptionResult=AVERAGEIF(A2:A6,"=*West",B2:B6)Average of all profits for the West and MidWest regions.16733.5=AVERAGEIF(A2:A6,"<>*(New Office)",B2:B6)Average of all profits for all regions excluding new offices.18589

---

[Original Documentation](https://support.microsoft.com/en-us/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642)