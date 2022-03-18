# 2018 Midterms: Did anti-establishment Republicans perform better?

> [Democrats here!](anti-establishment-democrats)

## There was *no* overall outperformance by anti-establishment Republicans compared to establishment Republicans.

**There was *no* overall outperformance by anti-establishment Republicans relative to their districts' partisan leans in the 2018 U.S. House general elections.**

* As with the Democrats, **a lot depends on how one defines "anti-establishment".** Several fields in the dataset were used to categorize a candidate as "anti-establishment" or not:

    * `Yes` on any of the following fields indicated the candidate was anti-establishment: `Trump Endorsed?`, `Great America Endorsed?`, `Bannon Endorsed?`, `House Freedom Support?`, `Tea Party Endorsed?`
    * The following fields were *not* considered indicative of establishment/anti-establishment status:
      * `Rep Party Support?` - Political parties often throw their support behind viable candidates in competitive races (in general elections), even if the candidates don't line up completely with the party establishment.

* Using these criteria, I found n = 15 anti-establishment candidates and n = 174 establishment candidates. At p = 0.651, there was no significant difference in performance between the two groups.

### What if?

I tried several combinations of fields to look for a possible significant result, to no avail.

* `No` on any of the following fields indicated the candidate was anti-establishment: `Main Street Endorsed?`, `Chamber Endorsed?`, `Club for Growth Endorsed?`, `Koch Support?`, `No Labels Support?` - At p = 0.471, there was still no significant difference in performance between the two groups.
* `Yes` on *only* `Trump Endorsed?` - p >> 0.05
* `Yes` on `Trump Endorsed?`, `Great America Endorsed?`, *or* `Bannon Endorsed?`  - p >> 0.05
* `Yes` on `House Freedom Support?` *or* `Tea Party Endorsed?` - p >> 0.05
* [There are other organizations in the dataset](women-candidates-emily-susan), but they endorse both establishment and anti-establishment candidates.

***

## Did candidates' professional background, characteristics, etc. affect performance?

Surprisingly, candidates with party support (`Rep Party Support?`) didn't perform better (or worse) than candidates without party support. (38 candidates were explicitly identified as having party support; 151 were not. p = 0.482)

Some fields were not available in the Republican dataset: `Veteran?`, `Elected Official?`, `Race`, `LGBTQ?` So these variables couldn't be analyzed.

***

## Notes

I used [FiveThirtyEight's dataset on 2018 Republican primary candidates](https://github.com/fivethirtyeight/data/blob/master/primary-candidates-2018/rep_candidates.csv). This dataset includes only candidates who had primary challengers, so incumbent U.S. Representatives who did not face a primary challenge were excluded from this analysis.

***

## [Data Sources](data-sources)

***

# 2018 Midterms

### [2018 Midterms: Did anti-establishment candidates really perform better?](anti-establishment-democrats)

### ["The Year of the Woman": Did candidate gender impact electoral performance?](women-candidates-emily-susan)

### [2018 Midterms: Did candidates' professional background, characteristics, and/or identities affect performance?](characteristics-democrats)

### [U.S. House: Do moderates come from swing districts? Relationship between caucus/coalition membership and district partisan lean](index)

***

**Last Updated:** Feb 15, 2019