# NORM.S.DIST

> Returns the standard normal cumulative distribution

## Syntax
For a standard normal distribution, this is the syntax:

NORM.S.DIST(z,cumulative)

This function syntax uses the following arguments:

zRequired. This is the value for which you want the distribution.cumulativeRequired. Thecumulativeargument can be eitherTRUEorFALSE. This logical value determines the form of the function. If cumulative is TRUE then NORM.S.DIST returns thecumulativedistributionfunction. If it is FALSE, it returns theprobability massfunction.

## Examples
- Copy the following entire table. Paste it into cell A1 (and adjacent cells) in a new Excel worksheet. If you do not automatically see results, select the formula, press F2 and press Enter. Adjust column widths if needed to see everything.

- Table:
Formula | Description | Result
=NORM.S.DIST(1.333333,TRUE) | Normal cumulative distribution function at 1.333333 | 0.908788726
=NORM.S.DIST(1.333333,FALSE) | Normal probability distribution function at 1.333333 | 0.164010148

---

[Original Documentation](https://support.microsoft.com/en-us/office/norm-s-dist-function-1e787282-3832-4520-a9ae-bd2a8d99ba88)