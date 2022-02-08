# This file describes the datasets from the Google drive associated with the paper

## File formats

### train.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = Number of types of events
- devtest = Empty list
- args = Empty
- dev = Empty list
- train = List of lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event
- test = Empty list

### dev.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = Number of types of events
- devtest = Empty list
- args = Empty
- dev = List of lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event
- train = Empty list
- test = Empty list

### test.pkl

Dictionary with 6 keys: dim_process, devtest, args, dev, train, test

- dim_process = Number of types of events
- devtest = Empty list
- args = Empty
- dev = Empty list
- train = Empty list
- test = List of lists. Each one of them is a list of dictionaries. Each dictionary represents one event, and has keys time_since_start, time_since_last_event, type_event

## data_bookorder

There are 2 types of events (taking values 0 or 1).

The train set contains 90 lists. The length of a list of events is 3319.

The dev set contains 10 lists. The length of a list of events is 3319.

The test set contains 100 lists. The length of a list of events is 829.

## data_conttime

There are 5 types of events (taking values from 0 to 4).

No devtest in dictionary.

The train sets contains 5 lists. The length of a list of events is between 20 and 100, with average length 59.9 events.

The train sets contains 1000 lists. The length of a list of events is between 20 and 100, with average length 61.7 events.

args is a dictionary containing keys:
{'NumSeqs': 12000,
 'DimStates': 32,
 'MinLen': 20,
 'PID': 81233,
 'MaxLen': 100,
 'DimLSTM': 32,
 'FilePretrain': None,
 'DimProcess': 5,
 'ModelGen': 'conttime',
 'TIME': '2017-09-27T13:46:44.282072',
 'FileModel': '/Users/hongyuan/Documents/GitJHU/NeuralHawkesProcess/gen_models/model_ModelGen=conttime_PID=81233_TIME=2017-09-27T13:46:44.282072.pkl',
 'FileSave': '/Users/hongyuan/Documents/GitJHU/NeuralHawkesProcess/data/data_ModelGen=conttime_PID=81233_TIME=2017-09-27T13:46:44.282072.pkl',
 'SetParams': False,
 'Seed': 12345}
## data_mimic / fold1

There are 75 types of events (taking values from 0 to 72).

The train set contains 527 lists. The length of a list of events is between 2 and 24, with average length 3.7 events.

The dev set contains 58 lists. The length of a list of events is between 2 and 33, with average length 4.3 events.

The test set contains 66 lists. The length of a list of events is between 2 and 11, with average length 3.6 events.

