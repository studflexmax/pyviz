title: Preface
author: studflexmax
date: 2016-04


[TOC]


### Mission

Seek out the most practical & efficient data visualization possible.


### About Me

Grew up in Vancouver, studied in Ithaca, currently working with Big Data in Mountain View.


### Python Data Visualization Options

There are many data visualization options available, from mild (Excel) to
wild (writing customized javascript/python/R libraries).  Even within Python,
there are many options. Here, let's examine some of the most popular ones:

#### [Matplotlib](http://matplotlib.org/)
*  a highly-customizable plotting lib for Python, forming the basis for
   many other modules/packages on this list.
*  **CON**: Complexity, requires too much effort to produce charts
   required during an (exploratory) analysis.
*  **SUITABLE**: Fine-tune plots produced by other packages
   that build off matplotlib (e.g. seaborn, pandas).

#### [Pandas](http://pandas.pydata.org/) [chosen for this primer]
*  An absolute godsend, THE data structure/analysis tool for anyone who is
   interested in working with data in Python.
     *  Created by the great [Wes McKinney](https://twitter.com/wesmckinn).
*  Integrated plotting functions into data structures (e.g. Series, DataFrames).
     *  e.g. Allows you to conveniently `sample_dataframe.hist()` to produce a
        histogram.
     *  In most cases these plotting functions call matplotlib.
*  **CON**: Currently lacks the ability produce some less-common plots (e.g.
   heatmap, violin plots).
*  **PRO**: Fast, second only to using matplotlib natively.
     *  This is critically important when the data points gets large (say
        >=50,000 data pt, working on a "high-performance" laptop).
     *  e.g. Its implementation of histogram is likely the fastest
        amongst all the available options, often only require a fifth or a
        tenth of the time it would require other packages to produce a
        comparable histogram.
*  **PRO**: Convenient, in most cases only require 1 line of code (instead of
   the 10-20 lines typically required when using matplotlib, even assuming a
   simple plot).
*  **SUITABLE**: Produce charts/plots required during an analysis to verify
   insights and/or explore shapes/distributions/correlations.
     *  In most cases it's fairly easy to convert these often rough-on-the-edges
        plots into something nice and presentable.

#### [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/) [chosen for this primer]

#### [Bokah](http://bokeh.pydata.org/)
*  A Python interactivite visualization library that targets modern web
   browswers for presentation.
*  **PRO**: Interactivity, all plots are rendered as javascript widgets;
   therefore, you can manipulate the plots after they have been generated
   (pinch, zoom, change resolution, etc.).
*  **CON**: Performance, when working with large number of data points, it may
   take impractically long to produce required plots.
*  **SUITABLE**: Context in which the number of data points is managable (in
   my experience ~5,000 on a laptop) and interactivity is required/prefered
   (e.g. dashboards, webpages).

#### [PyGal](http://www.pygal.org/)

#### [VisPy](http://vispy.org/)

#### [Folium](https://folium.readthedocs.io/)

#### [NetworkX](http://networkx.github.io/)

### Inspirations & Learning Resources
