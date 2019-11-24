---
layout: nosidebar
---

# Background for: [Popularity of Birth Control Methods on Reddit](index)

### Process

**1)** Extract all user flairs via recent submissions and comments. In order to maximize the number of users scraped, I sorted by `hot`, `top`, and `controversial`, then used search to pull submissions older than the top 1000 in each category. Any future refreshes of the data would only sort by `new` to capture new submissions and users.

**2)** For user flairs analysis:

a) Drop duplicate users (duplicates are to be expected because any given user may have made several submissions or comments) and remove blank/empty/null flairs

b) Search user flairs for each birth control method (via specific search strings using regex) and count frequency with which each birth control method appears in user flairs

**3)** For submission titles analysis:

a) Search submission titles for each birth control method and count frequency with which each birth control method appears in submission titles

b) Then, count submissions flaired `Side Effects` and compare frequencies vs. all submissions

### Notes

* A user's flair reflects her *current* birth control method, while a past submission flaired `Side Effects` may be about a previous method she was using prior to switching to her current method. Thus, I decided to compare all *titles* to *titles* flaired `Side Effects` instead of comparing the *flairs of users* who had posted submissions flaired `Side Effects`.

***

**Last Updated:** Jun 23, 2018