# AVERAGEIFS

> Returns the average (arithmetic mean) of all cells that meet multiple criteria

## Syntax
AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)

The AVERAGEIFS function syntax has the following arguments:

Average_rangeRequired. One or more cells to average, including numbers or names, arrays, or references that contain numbers.Criteria_range1, criteria_range2, …Criteria_range1 is required, subsequent criteria_ranges are optional. 1 to 127 ranges in which to evaluate the associated criteria.Criteria1, criteria2, ...Criteria1 is required, subsequent criteria are optional. 1 to 127 criteria in the form of a number, expression, cell reference, or text that define which cells will be averaged. For example, criteria can be expressed as 32, "32", ">32", "apples", or B4.

## Examples
- Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Student | First | Second | Final
 | Quiz | Quiz | Exam
 | Grade | Grade | Grade
Emilio | 75 | 85 | 87
Julie | 94 | 80 | 88
Hans | 86 | 93 | Incomplete
Frederique | Incomplete | 75 | 75
Formula | Description | Result | 
=AVERAGEIFS(B2:B5, B2:B5, ">70", B2:B5, "<90") | Average first quiz grade that falls between 70 and 90 for all students (80.5). The score marked "Incomplete" is not included in the calculation because it is not a numerical value. | 75 | 
=AVERAGEIFS(C2:C5, C2:C5, ">95") | Average second quiz grade that is greater than 95 for all students. Because there are no scores greater than 95, #DIV0! is returned. | #DIV/0! | 
=AVERAGEIFS(D2:D5, D2:D5, "<>Incomplete", D2:D5, ">80") | Average final exam grade that is greater than 80 for all students (87.5). The score marked "Incomplete" is not included in the calculation because it is not a numerical value. | 87.5 | 

- Example 2TypePriceTownNumber of BedroomsGarage?Cozy Rambler230000Issaquah3NoSnug Bungalow197000Bellevue2YesCool Cape Codder345678Bellevue4YesSplendid Split Level321900Issaquah2YesExclusive Tudor450000Bellevue5YesClassy Colonial395000Bellevue4NoFormulaDescriptionResult=AVERAGEIFS(B2:B7, C2:C7, "Bellevue", D2:D7, ">2",E2:E7, "Yes")Average price of a home in Bellevue that has at least 3 bedrooms and a garage397839=AVERAGEIFS(B2:B7, C2:C7, "Issaquah", D2:D7, "<=3",E2:E7, "No")Average price of a home in Issaquah that has up to 3 bedrooms and no garage230000

---

[Original Documentation](https://support.microsoft.com/en-us/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690)