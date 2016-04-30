title: Sample Data
author: studflexmax
date: 2016-04


[TOC]


### Generate Sample Data

    :::python
    # Generate some sample data to vizualize.

    numpy.random.seed(49)
    sample_size = 100
    strings = ['foo', 'bar', 'baz', 'qux']

    sample_dataframe = pandas.DataFrame({
        'int_field_1': numpy.random.randint(1, 11, sample_size),
        'int_field_2': numpy.random.randint(1, 11, sample_size),
        'float_field_1': numpy.random.normal(0, 10, sample_size),
        'float_field_2': numpy.random.normal(0, 10, sample_size),
        'string_field_1': numpy.random.choice(strings, sample_size),
        'string_field_2': numpy.random.choice(strings, sample_size)})

    print(sample_dataframe.shape)
    sample_dataframe.head(10)

![sample_data option 1](/static/img/sample_data_1.png)


### Random Thoughts
