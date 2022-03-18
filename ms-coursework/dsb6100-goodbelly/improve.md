---
layout: nosidebar
---

# Things to Improve

## Things I would have done if I had more time:

* Coded Region and Store to include them in the model too
* Looked at possible cyclical trends with month of year, day of week, and day of month (although the dates do not span a large range so this likely wouldn't have yielded much)

## Things I would have done in hindsight:

* Scaled Natural and Fitness, which span range 1-5 and are not binary (0-1) like some of the other variables
* Scaled ARP, which has a range from 2-ish to just under 7, again not binary like some of the other variables
* Alternatively, could have scaled the binary variables to the extremes of the non-binary variables
* Probably would have kept pre-log-transformation adjustment at x+1 not x+0.001 (but having run it both ways, it does not change the findings and it only minimally changes the R-squared of each of our models). Also should have scaled the log-transformed values.

***

[Back to MS in Data Science Coursework](/ms)