# COUNTIF

> Counts the number of cells within a range that meet the given criteria

## Syntax
COUNTIF(range, criteria)Argument nameDescriptionrange(required)The group of cells you want to count.Rangecan contain numbers, arrays, a named range, or references that contain numbers. Blank and text values are ignored.Learn how toselect ranges in a worksheet.criteria(required)A number, expression, cell reference, or text string that determines which cells will be counted.For example, you can use a number like 32, a comparison like ">32", a cell like B4, or a word like "apples".COUNTIF uses only a single criteria. UseCOUNTIFSif you want to use multiple criteria.

## Examples
- To use these examples in Excel, copy the data in the table below, and paste it in cell A1 of a new worksheet.

- Table:
Data | Data
apples | 32
oranges | 54
peaches | 75
apples | 86
Formula | Description
=COUNTIF(A2:A5,"apples") | Counts the number of cells with apples in cells A2 through A5. The result is 2.
=COUNTIF(A2:A5,A4) | Counts the number of cells with peaches (the value in A4) in cells A2 through A5. The result is 1.
=COUNTIF(A2:A5,A2)+COUNTIF(A2:A5,A3) | Counts the number of apples (the value in A2), and oranges (the value in A3) in cells A2 through A5. The result is 3. This formula uses COUNTIF twice to specify multiple criteria, one criteria per expression. You could also use theCOUNTIFSfunction.
=COUNTIF(B2:B5,">55") | Counts the number of cells with a value greater than 55 in cells B2 through B5. The result is 2.
=COUNTIF(B2:B5,"<>"&B4) | Counts the number of cells with a value not equal to 75 in cells B2 through B5. The ampersand (&) merges the comparison operator for not equal to (<>) and the value in B4 to read =COUNTIF(B2:B5,"<>75"). The result is 3.
=COUNTIF(B2:B5,">=32")-COUNTIF(B2:B5,"<=85") | Counts the number of cells with a value greater than (>) or equal to (=) 32 and less than (<) or equal to (=) 85 in cells B2 through B5. The result is 1.
=COUNTIF(A2:A5,"*") | Counts the number of cells containing any text in cells A2 through A5. The asterisk (*) is used as the wildcard character to match any character. The result is 4.
=COUNTIF(A2:A5,"?????es") | Counts the number of cells that have exactly 7 characters, and end with the letters "es" in cells A2 through A5. The question mark (?) is used as the wildcard character to match individual characters. The result is 2.

---

[Original Documentation](https://support.microsoft.com/en-us/office/use-the-countif-function-in-microsoft-excel-e0de10c6-f885-4e71-abb4-1f464816df34)