# PERMUTATIONA

> Returns the number of permutations for a given number of objects (with repetitions) that can be selected from the total objects

## Syntax
PERMUTATIONA(number, number-chosen)

The PERMUTATIONA function syntax has the following arguments:

NumberRequired. An integer that describes the total number of objects.Number_chosenRequired. An integer that describes the number of objects in each permutation.

PERMUTATIONA uses the following equation:

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=PERMUTATIONA(3,2) | Suppose there are 3 objects in the group, [4,5,6]. Using PERMUTATIONA with 2 of the 3 objects, there are 9 ways the numbers can be arranged with repetition: | 9
 | 4,4 | 
 | 4,5 | 
 | 4,6 | 
 | 5,4 | 
 | 5,5 | 
 | 5,6 | 
 | 6,4 | 
 | 6,5 | 
 | 6,6 | 
 |  | 
=PERMUTATIONA(2,2) | Suppose there are 2 objects in the group, [3,5]. Using PERMUTATIONA with both of the objects, there are 4 ways the numbers can be arranged with repetition: | 4
 | 3,3 | 
 | 3,5 | 
 | 5,3 | 
 | 5,5 | 

- Top of Page

---

[Original Documentation](https://support.microsoft.com/en-us/office/permutationa-function-6c7d7fdc-d657-44e6-aa19-2857b25cae4e)