# BINOM.DIST.RANGE

> Returns the probability of a trial result using a binomial distribution

## Syntax
BINOM.DIST.RANGE(trials,probability_s,number_s,[number_s2])

The BINOM.DIST.RANGE function syntax has the following arguments.

TrialsRequired. The number of independent trials. Must be greater than or equal to 0.Probability_sRequired. The probability of success in each trial. Must be greater than or equal to 0 and less than or equal to 1.Number_sRequired. The number of successes in trials. Must be greater than or equal to 0 and less than or equal to Trials.Number_s2Optional. If provided, returns the probability that the number of successful trials will fall between Number_s and number_s2. Must be greater than or equal to Number_s and less than or equal to Trials.

## Examples
- Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data.

- Table:
Formula | Description | Result
=BINOM.DIST.RANGE(60,0.75,48) | Returns the binomial distribution based on the probability of 48 successes in 60 trials and a 75% probability of success (0.084, or 8.4%). | 0.084
 |  | 
=BINOM.DIST.RANGE(60,0.75,45,50) | Returns the binomial distribution based on the probability of between 45 and 50 successes (inclusive) in 60 trials and a 75% probability of success (0.524, or 52.4%). | 0.524

- Top of Page

---

[Original Documentation](https://support.microsoft.com/en-us/office/binom-dist-range-function-17331329-74c7-4053-bb4c-6653a7421595)