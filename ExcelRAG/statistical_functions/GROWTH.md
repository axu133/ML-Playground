# GROWTH

> Returns values along an exponential trend

## Syntax
GROWTH(known_y's, [known_x's], [new_x's], [const])

The GROWTH function syntax has the following arguments:

Known_y'sRequired. The set of y-values you already know in the relationship y = b*m^x.If the array known_y's is in a single column, then each column of known_x's is interpreted as a separate variable.If the array known_y's is in a single row, then each row of known_x's is interpreted as a separate variable.If any of the numbers in known_y's is 0 or negative, GROWTH returns the #NUM! error value.Known_x'sOptional. An optional set of x-values that you may already know in the relationship y = b*m^x.The array known_x's can include one or more sets of variables. If only one variable is used, known_y's and known_x's can be ranges of any shape, as long as they have equal dimensions. If more than one variable is used, known_y's must be a vector (that is, a range with a height of one row or a width of one column).If known_x's is omitted, it is assumed to be the array {1,2,3,...} that is the same size as known_y's.New_x'sOptional. Are new x-values for which you want GROWTH to return corresponding y-values.New_x's must include a column (or row) for each independent variable, just as known_x's does. So, if known_y's is in a single column, known_x's and new_x's must have the same number of columns. If known_y's is in a single row, known_x's and new_x's must have the same number of rows.If new_x's is omitted, it is assumed to be the same as known_x's.If both known_x's and new_x's are omitted, they are assumed to be the array {1,2,3,...} that is the same size as known_y's.ConstOptional. A logical value specifying whether to force the constant b to equal 1.If const is TRUE or omitted, b is calculated normally.If const is FALSE, b is set equal to 1 and the m-values are adjusted so that y = m^x.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Month | Units | Formula (Corresponding Units) | 
11 | 33,100 | 32,618 | 
12 | 47,300 | 47,729 | 
13 | 69,000 | 69,841 | 
14 | 102,000 | 102,197 | 
15 | 150,000 | 149,542 | 
16 | 220,000 | 218,822 | 
Month | Formula (Predicted Units) | Formula used in C2:C7 array above | 
17 | 320,197 | =GROWTH(B2:B7,A2:A7)
18 | 468,536 |  | 
 | Formula used in B9:B10 array above |  | 
 | =GROWTH(B2:B7,A2:A7,A9:A10) | 

---

[Original Documentation](https://support.microsoft.com/en-us/office/growth-function-541a91dc-3d5e-437d-b156-21324e68b80d)