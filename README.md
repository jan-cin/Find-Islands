# Find islands

This mini project was done as take-home assignment, which was part of interview process. 
Description of recruitment task is the bottom of this README

In order to test solution:
* Run python script locally, e.g.: `python solution.py tests/sample_valid_inputs/islands1.txt`
* or Run docker container and then run shell script that is wrapper for python script (recommended) 

In order to run docker image:
* Navigate to project directory
* Build docker image `docker build --tag python:find-islands .`
* Run image `docker run -v //path_to_project/find_island:/usr/app/src/find_islands --name find-islands-container -t -d python:find-islands`
* Connect to shell of running image `docker exec -it find-islands-container /bin/bash`


## Recruitment task description
At the beginning of this task, you are given a path to the file that denotes a
two-dimensional array which visualizes a map. Each element of this array will take
one of the following values:
* 0 (which represents water),
* 1 (which represents land).

These values will form islands on water.

For example:<br />
`0 0 0 0 0 0 0 0 0`<br />
`0 1 0 0 0 0 0 0 0`<br />
`1 1 1 0 0 0 1 0 0`<br />
`1 1 0 0 0 1 1 1 0`<br />
`0 0 0 0 0 1 1 0 0`<br />
`0 0 1 0 0 0 0 0 0`<br />
`1 1 0 0 0 0 0 0 0`<br />
`0 0 0 0 0 1 1 0 0`

This example illustrates 4 islands. Counting from left upper corner:
* First Island is made of six land elements,
* Second Island is also made of six land elements.
* Third island consists of 3 elements,
* The last one is made of two elements.

The invocation of your bash script will look like:<br />
`./your_script.sh <path_to_the_file>`<br />
where the file denoted by the path will be a text file with only zeros (ASCII character 48) and ones (ASCII character 49) 
and end-of-line, i.e.:<br />
000000000<br />
010000000<br />
111000100<br />
110001110<br />
000001100<br />
001000000<br />
110000000<br />
000001100<br />
Write a short program, which will count the number of islands. The following data structure could be varying in size. 
The only output of the program written to STDOUT should be the number (all additional diagnostics information, if needed, 
should be written to STDERR).

Example invocation (and output):<br />
`$ ./your_script.sh islands.txt`<br />
`4`