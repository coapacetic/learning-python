# Input and Output Redirection 
There are two ways you can override how python uses input() and print()

## Input redirection
The line below will use inputs from a list of inputs stored in the text file _rather_ than prompting the user to enter the values

`python telemarketers.py < telemarketers_input.txt`


## Output Redirection
The line below will write outputs to a file _rather_ than directly to the terminal

`python telemarketers.py > telemarketers_output.txt`

You can try both of these with the files that are currently in this directory