title: Heatmap
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
    two_dimentional_dataframe = sample_dataframe.pivot_table(
        index="string_field_1", columns="string_field_2", values="float_field_1")

    seabor.heatmap(two_dimentional_dataframe)
![heatmap option 1](/static/img/heatmap_1.png)


### Random Thoughts
