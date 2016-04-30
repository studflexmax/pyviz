title: Bar
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
    # Option 1, PREFERED
    seaborn.barplot(sample_dataframe.string_field_1, sample_dataframe.int_field_1)
![bar option 1](/static/img/bar_1.png)

    :::python
    # Option 2
    sample_dataframe.groupby("string_field_1").sum()['int_field_1'].plot.bar()
![bar option 2](/static/img/bar_2.png)


### Clean Shaven

    :::python
    seaborn.barplot(
        data=sample_dataframe,
        orient='h',
        estimator=numpy.median,
        x='float_field_1',
        y='string_field_1',
        order=['baz', 'bar', 'qux', 'foo'],
        hue_order=['b', 'g', 'r', 'p'])
![bar option 3](/static/img/bar_3.png)


### Random Thoughts
