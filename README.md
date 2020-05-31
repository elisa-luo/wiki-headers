# wiki-headers

A Python script that determines the most common words used in headers of wikipedia articles. Note that the headers are assumed to be surrounded by two equals signs, i.e. ==New York==

__Use:__

Simply change the following line of code: `SOURCE = "wiki_data.txt" #filename of dataset` to have the filename of the dataset you're going to use instead. i.e. `SOURCE = "<your_dataset_name>"`

__other settings__

- adjust the _n_ most common words to display by changing the `OCCURENCES` variable (default is `10`)
- turn off program runtime display by changing the `RUNTIME` variable to `False`
- currently ignores subheaders
