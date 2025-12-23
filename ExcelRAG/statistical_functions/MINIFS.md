# MINIFS

> Returns the minimum value among cells specified by a given set of conditions or criteria.

## Syntax
MINIFS(min_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)

Argument | Description
min_range(required) | The actual range of cells in which the minimum value will be determined.
criteria_range1(required) | Is the set of cells to evaluate with the criteria.
criteria1(required) | Is the criteria in the form of a number, expression, or text that defines which cells will be evaluated as minimum. The same set of criteria works for theMAXIFS,SUMIFSandAVERAGEIFSfunctions.
criteria_range2,criteria2, ...(optional) | Additional ranges and their associated criteria. You can enter up to 126 range/criteria pairs.

## Examples
- Copy the example data in each of the following tables, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Example 1

- Table:
Grade | Weight
89 | 1
93 | 2
96 | 2
85 | 3
91 | 1
88 | 1
Formula | Result
=MINIFS(A2:A7,B2:B7,1) | 88In criteria_range1 the cell B2, B6, and B7 match the criteria of 1. Of the corresponding cells in min_range, A7 has the minimum value. The result is therefore 88.

- Example 2

- Table:
Weight | Grade
10 | b
11 | a
100 | a
111 | b
1 | a
1 | a
Formula | Result
=MINIFS(A2:A5,B3:B6,"a") | 10Note:The criteria_range and min_range aren't aligned, but they are the same shape and size.In criteria_range1, the 1st, 2nd, and 4th cells match the criteria of "a." Of the corresponding cells in min_range, A2 has the minimum value. The result is therefore 10.

- Example 3

- Table:
Weight | Grade | Class | Level
10 | b | Business | 100
11 | a | Technical | 100
12 | a | Business | 200
13 | b | Technical | 300
14 | b | Technical | 300
15 | b | Business | 400
 |  |  | 
Formula | Result |  | 
=MINIFS(A2:A7,B2:B7,"b",D2:D7,">100") | 13In criteria_range1, B2, B5, B6 and B7 match the criteria of "b." Of the corresponding cells in criteria_range2, D5, D6, and D7 match the criteria of >100. Finally, of the corresponding cells in min_range, D5 has the minimum value. The result is therefore 13. |  | 

- Example 4

- Table:
Weight | Grade | Class | Level
10 | b | Business | 8
1 | a | Technical | 8
100 | a | Business | 8
11 | b | Technical | 0
1 | a | Technical | 8
1 | b | Business | 0
 |  |  | 
Formula | Result |  | 
=MINIFS(A2:A7,B2:B7,"b",D2:D7,A8) | 1The criteria2 argument is A8. However, because A8 is empty, it is treated as 0 (zero). The cells in criteria_range2 that match 0 are D5 and D7. Finally, of the corresponding cells in min_range, A7 has the minimum value. The result is therefore 1. |  | 

- Example 5

- Table:
Weight | Grade
10 | b
1 | a
100 | a
1 | b
1 | a
1 | a
 | 
Formula | Result
=MINIFS(A2:A5,B2:C6,"a") | #VALUE!Because the size and shape of the min_range and criteria_range aren't the same, MINIFS returns the #VALUE! error.

- Example 6

- Table:
Weight | Grade | Class | Level
10 | b | Business | 100
1 | a | Technical | 100
100 | a | Business | 200
1 | b | Technical | 300
1 | a | Technical | 100
1 | a | Business | 400
 |  |  | 
Formula | Result |  | 
=MINIFS(A2:A6,B2:B6,"a",D2:D6,">200") | 0No cells match the criteria. |  | 

---

[Original Documentation](https://support.microsoft.com/en-us/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599)