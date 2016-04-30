title: Scatter Matrix
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
    seaborn.pairplot(sample_dataframe) # Option 1, PREFERED
![scatter matrix option 1](/static/img/scatter_matrix_1.png)

    :::python
    pandas.tools.plotting.scatter_matrix(sample_dataframe) # Option 2
![scatter matrix option 2](/static/img/scatter_matrix_2.png)


### Clean Shaven

    :::python
    ax_scatter_matrix = seaborn.pairplot(
      data=sample_dataframe,
      x_vars=[
          'int_field_1',
          'int_field_2',
          'float_field_1'],
      y_vars=[
          'int_field_1',
          'int_field_2',
          'float_field_1'],
      diag_kind = 'kde', # kde vs hist
      hue='string_field_1', # color base on categories
      palette = 'Spectral')
![scatter matrix option 3](/static/img/scatter_matrix_3.png)


### Random Thoughts
