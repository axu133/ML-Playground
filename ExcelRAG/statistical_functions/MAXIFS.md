# MAXIFS

> Returns the maximum value among cells specified by a given set of conditions or criteria

## Syntax
MAXIFS(max_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)

Argument | Description
max_range(required) | The actual range of cells in which the maximum will be determined.
criteria_range1(required) | Is the set of cells to evaluate with the criteria.
criteria1(required) | Is the criteria in the form of a number, expression, or text that defines which cells will be evaluated as maximum. The same set of criteria works for theMINIFS,SUMIFS, andAVERAGEIFSfunctions.
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
=MAXIFS(A2:A7,B2:B7,1) | 91In criteria_range1 the cells B2, B6, and B7 match the criteria of 1. Of the corresponding cells in max_range, A6 has the maximum value. The result is therefore 91.

- Example 2

- Table:
Weight | Grade
10 | b
1 | a
100 | a
1 | b
1 | a
1 | a
Formula | Result
=MAXIFS(A2:A5,B3:B6,"a") | 10Note:The criteria_range and max_range aren't aligned, but they are the same shape and size.In criteria_range1, the 1st, 2nd, and 4th cells match the criteria of "a." Of the corresponding cells in max_range, A2 has the maximum value. The result is therefore 10.

- Example 3

- Table:
Weight | Grade | Class | Level
10 | b | Business | 100
1 | a | Technical | 100
100 | a | Business | 200
1 | b | Technical | 300
1 | a | Technical | 100
50 | b | Business | 400
 |  |  | 
Formula | Result |  | 
=MAXIFS(A2:A7,B2:B7,"b",D2:D7,">100") | 50In criteria_range1, B2, B5, and B7 match the criteria of "b." Of the corresponding cells in criteria_range2, D5 and D7 match the criteria of >100. Finally, of the corresponding cells in max_range, A7 has the maximum value. The result is therefore 50. |  | 

- Example 4

- Table:
Weight | Grade | Class | Level
10 | b | Business | 8
1 | a | Technical | 8
100 | a | Business | 8
11 | b | Technical | 0
1 | a | Technical | 8
12 | b | Business | 0
 |  |  | 
Formula | Result |  | 
=MAXIFS(A2:A7,B2:B7,"b",D2:D7,A8) | 12The criteria2 argument is A8. However, because A8 is empty, it is treated as 0 (zero). The cells in criteria_range2 that match 0 are D5 and D7. Finally, of the corresponding cells in max_range, A7 has the maximum value. The result is therefore 12. |  | 

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
=MAXIFS(A2:A5,B2:c6,"a") | #VALUE!Because the size and shape of the max_range and criteria_range aren't the same, MAXIFS returns the #VALUE! error.

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
=MAXIFS(A2:A6,B2:B6,"a",D2:D6,">200") | 0No cells match the criteria. |  | 

---

[Original Documentation](https://support.microsoft.com/en-us/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883)