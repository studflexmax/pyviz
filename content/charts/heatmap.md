title: Heatmap
author: studflexmax
date: 2016-04

# Heatmap


[TOC]


## Quick Dirty

    :::python
	sample_dataframe.boxplot() # Option 1, PREFERED
![boxplot option 1](/static/img/boxplot_1.png)

    :::python
	seaborn.boxplot(sample_dataframe) # Option 2
![boxplot option 2](/static/img/boxplot_2.png)


## Clean Shaven

    :::python
    # Option 1
    ax_box = sample_dataframe.boxplot(
        column=['int_field_1'],
        by=['string_field_1']) # grouping by a categorical var
![boxplot option 3](/static/img/boxplot_3.png)


    :::python
    # Option 2
    ax_box = seaborn.boxplot(
        data=sample_dataframe,
        x='int_field_2',
        y='string_field_1', # grouping by a categorical var
        orient='h')
![boxplot option 4](/static/img/boxplot_4.png)


## Random Thoughts
