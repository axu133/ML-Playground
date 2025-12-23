# HYPGEOM.DIST

> Returns the hypergeometric distribution

## Syntax
HYPGEOM.DIST(sample_s,number_sample,population_s,number_pop,cumulative)

The HYPGEOM.DIST function syntax has the following arguments:

Sample_sRequired. The number of successes in the sample.Number_sampleRequired. The size of the sample.Population_sRequired. The number of successes in the population.Number_popRequired. The population size.CumulativeRequired. A logical value that determines the form of the function. If cumulative is TRUE, then HYPGEOM.DIST returns the cumulative distribution function; if FALSE, it returns the probability mass function.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Data | Description | Result
1 | Number of successes in the sample | 
4 | Sample size | 
8 | Number of successes in the population | 
20 | Population size | 
Formula | Description (Result) | 
=HYPGEOM.DIST(A2,A3,A4,A5,TRUE) | Cumulative hypergeometric distribution function, for sample and population in cells A2 through A5. | 0.4654
 |  | 
=HYPGEOM.DIST(A2,A3,A4,A5,FALSE) | Probability hypergeometric distribution function, for sample and in cells A2 through A5. | 0.3633

---

[Original Documentation](https://support.microsoft.com/en-us/office/hypgeom-dist-function-6dbd547f-1d12-4b1f-8ae5-b0d9e3d22fbf)