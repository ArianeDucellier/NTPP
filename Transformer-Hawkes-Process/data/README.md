# This file describes the datasets from the Google drive associated with the paper

## data_bookorder

There are two types of events (taking values 0 or 1)

dim_process = 2

train = 90 lists of length 

## data_mimic / fold1

There are 66 types of events (taking values from 0 to 72).

The train set contains 527 lists. The length of a list of events is between 2 and 24, with average length 3.7 events.

The dev set contains 58 lists. The length of a list of events is between 2 and 33, with average length 4.3 events.

The test set contains 66 lists. The length of a list of events is between 2 and 11, with average length 3.6 events.

### train.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = 75
- devtest = Empty list
- args = Empty
- dev = Empty list
- train = List of 527 lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event
- test = Empty list

### dev.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = 75
- devtest = Empty list
- args = Empty
- dev = List of 58 lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event
- train = Empty list
- test = Empty list

### test.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = 75
- devtest = Empty list
- args = Empty
- dev = Empty list
- train = Empty list
- test = List of 65 lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event