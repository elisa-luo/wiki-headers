# wiki-headers

A Python script that determines the most common words used in headers of wikipedia articles. Note that the headers are assumed to be surrounded by two equals signs, i.e. ==New York==

__Use:__
Simply change the following line of code on line `12`: `SOURCE = "wiki_data.txt" #filename of dataset` to contain the filename (filepath if file is not in the same directory) of the dataset to be used. i.e. `SOURCE = "<your_file_path>"`

__Additional Settings:__
Settings are currently from lines `12` through `16`
- `OCCURENCES`: adjust the _n_ most common words to display. [Default = `10`]
- `RUNTIME`: toggle program runtime display on/off. [Default = `True`]
- `SUBHEADERS`: toggle including/ignorning subheaders in the final ranking. [Default = `False`]
- `CASE_SENSITIVE`: toggle if the words should be case-senstive. [Default = `False`]

__Sample Output:__
```
10 most common words in headers:
CASE_SENSITIVE = False
INCLUDE SUBHEADERS = False

RANK WORD           COUNT
-------------------------
1.   references     3527
2.   external       2506
3.   links          2503
4.   also           1113
5.   see            1112
6.   and            858
7.   history        766
8.   licensing      636
9.   summary        588
10.  career         548

--- runtime: 0.311229944229126 seconds ---
```
