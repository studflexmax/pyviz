title: Histogram
author:
date: 2016-04

# Histogram

### Quick Dirty

    :::python hl_lines="1"

	sample_dataframe.hist() # Option 1 using Pandas, PREFERED

	sample_dataframe.plot(kind='hist') # Option 2 using Pandas

### Clean Shaven

    :::python
    # Customize binning resolution
	bin_boundaries = range(0, 11, 1)

	ax_hist = sample_dataframe.hist(
		column=['int_field_1', 'int_field_2'],
		bins=bin_boundaries,
		layout=(2,1),
		sharex=True,
		sharey=True)


