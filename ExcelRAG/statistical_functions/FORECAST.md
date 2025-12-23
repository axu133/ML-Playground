# FORECAST

> Returns a value along a linear trendNote:In Excel 2016, this function is replaced withFORECAST.LINEARas part of the newForecasting functions, but it's still available for compatibility with earlier versions.

## Syntax
FORECAST.LINEAR(x, known_y's, known_x's)

- or -

FORECAST(x, known_y's, known_x's)

The FORECAST/FORECAST.LINEAR function syntax has the following arguments:

Argument | Required | Refers to
x | yes | The data point for which you want to predict a value.
known_y's | yes | The dependent array or range of data.
known_x's | yes | The independent array or range of data.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Known Y | Known X | 
6 | 20 | 
7 | 28 | 
9 | 31 | 
15 | 38 | 
21 | 40 | 
Formula | Description | Result
=FORECAST.LINEAR(30,A2:A6,B2:B6) | Predicts a value for y given an x value of 30 | 10.607253

---

[Original Documentation](https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99)