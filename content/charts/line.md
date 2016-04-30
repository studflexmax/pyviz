title: Line Plot
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
    sample_dataframe.plot.line() # Option 1
![line option 1](/static/img/line_1.png)


### Clean Shaven

    :::python
    # Extract the row index values, range(0, n, 1), into a field.
    # This is required to use the index as the x-axis.
    sample_dataframe['index_value'] = sample_dataframe.index

    seaborn.pointplot(
        data=sample_dataframe,
        estimator=numpy.mean,
        x='index_value',
        y='int_field_1',
        join=True)

    seaborn.pointplot(
        data=sample_dataframe,
        estimator=numpy.mean,
        x='index_value',
        y='int_field_1',
        hue='string_field_1',
        join=False)
![line option 2](/static/img/line_2.png)


### Random Thoughts

