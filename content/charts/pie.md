title: Pie Plot
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
    # Sum ofint_field_1, by categories string_field_1
    sample_dataframe.groupby("string_field_1").sum()['int_field_1'].plot.pie()
![pie option 1](/static/img/pie_1.png)


### Random Thoughts
