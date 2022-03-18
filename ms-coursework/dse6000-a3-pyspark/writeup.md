---
layout: nosidebar
---

# [DSE 6000 - Assignment 3](index)

## Write-Up

The most significant difference is that Jupyter Lab runs locally on your machine vs. Apache Spark runs distributed in the cloud. This means Jupyter Lab is best for smaller datasets that can fit within the machine's RAM, and Spark is better for larger datasets that need distributed capacity.

Both datasets I selected for Assignment 1 are very small. Neither comes close to filling the RAM available on my local system (8 GB). It doesn't add value to use Spark for these particular datasets. There is no need for distributed computing in these use cases.

However, had I chosen larger datasets for Assignment 1 originally, then it may have been useful. From a business perspective, enterprise systems often contain billions of records and in these cases distributed computing platforms are required for analysis. At my previous job, we had SQL databases where one table could contain easily 1,000,000 or more records. If several of these tables are required for analysis, they would collectively exceed the local system's available RAM.

For smaller datasets and assignments/class work like this, I personally enjoy using Jupyter Lab for another reason, which is that I can run one cell at a time and immediately see what happens. As I'm still in the learning stages, I like to know immediately if I have made an error or if the output is not what I expected. This makes the learning process simpler and more accessible.

***

**Course:** DSE 6000 Computational Platforms for Data Science, Wayne State University

**Assignment:** 3

**Submitted:** Apr 23, 2018

***

**Last Updated:** Sep 3, 2018

***

[Back](index)