title: Histogram
author: studflexmax
date: 2016-04


[TOC]


### Quick Dirty

    :::python
	sample_dataframe.hist() # Option 1, PREFERED
![histogram option 1](/static/img/histogram_1.png)

    :::python
	sample_dataframe.plot(kind='hist') # Option 2
![histogram option 2](/static/img/histogram_2.png)


### Clean Shaven

    :::python
    # Customize binning resolution
	bin_boundaries = range(0, 11, 1)

	ax_hist = sample_dataframe.hist(
		column=[
            'int_field_1',
            'int_field_2'],
		bins=bin_boundaries,
		layout=(2,1),
		sharex=True,
		sharey=True)
![histogram option 3](/static/img/histogram_3.png)


### Random Thoughts
