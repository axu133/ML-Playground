# LOGEST

> Returns the parameters of an exponential trend

## Syntax
LOGEST(known_y's, [known_x's], [const], [stats])The LOGEST function syntax has the following arguments:known_y'sRequired. The set of y-values you already know in the relationship y = b*m^x.If the array known_y's is in a single column, then each column of known_x's is interpreted as a separate variable.If the array known_y's is in a single row, then each row of known_x's is interpreted as a separate variable.known_x'sOptional. An optional set of x-values that you may already know in the relationship y = b*m^x.The array known_x's can include one or more sets of variables. If only one variable is used, known_y's and known_x's can be ranges of any shape, as long as they have equal dimensions. If more than one variable is used, known_y's must be a range of cells with a height of one row or a width of one column (which is also known as a vector).If known_x's is omitted, it is assumed to be the array {1,2,3,...} that is the same size as known_y's.constOptional. A logical value specifying whether to force the constant b to equal 1.If const is TRUE or omitted, b is calculated normally.If const is FALSE, b is set equal to 1, and the m-values are fitted to y = m^x.statsOptional. A logical value specifying whether to return additional regression statistics.If stats is TRUE, LOGEST returns the additional regression statistics, so the returned array is {mn,mn-1,...,m1,b;sen,sen-1,...,se1,seb;r 2,sey; F,df;ssreg,ssresid}.If stats is FALSE or omitted, LOGEST returns only the m-coefficients and the constant b.For more information about additional regression statistics, see theLINEST function.

## Examples
- You must enter the above formula as an array formula in Excel for it to work correctly. After you enter the formula, pressEnterif you have a current Microsoft 365 subscription; otherwise pressCtrl+Shift+Enter. If the formula is not entered as an array formula, the single result is 1.4633.

---

[Original Documentation](https://support.microsoft.com/en-us/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b)