# random_oracle
Just a small thought towards the problem

In this exercise, you will create and populate a table, fetch rows from the table using a python client. 

In cryptography, a random oracle is an oracle (a theoretical black box) that responds to every unique query with a random response chosen uniformly from its output domain. If a query is repeated, it responds the same way every time that query is submitted.

In this exercise, you have to create a table named oracle (in the lab4db database) with two columns, one for the query parameters (integer) and the other for the output (256-bit hex string) using python (including table creation). The query parameter’s range is  [0, 216) and the output must be a 256-bit hexadecimal string. Your python code should print the output for every parameter value requested. You can use the same config.py file from Exercise 1 to connect to the database. Your program should be in a file oracle.py. Here are some sample runs of the program. 

~$  python3 oracle.py
Query:
10
1c04fb12c0f5074cb8261b83686b02d9f0db99fa1ff3144671ca2f6446c9a2e9
Query:
3
6d61009c7f585fee977a5a7ff04776cc5368a26c17af9e96ced3bb59869011c1
Query:	
10
1c04fb12c0f5074cb8261b83686b02d9f0db99fa1ff3144671ca2f6446c9a2e9
.
.
.
Query:
-1
exiting...
~$  


So my solution works on this basis: I use a random (can be any number, even 1111...) 16 digit number. Then everytime I get a (new) query number, I generate bitwise equal to operation's result between the query num and the original num. Now the thing is that every number will have a different result (by contradiction). And at the place where they differ, the range of possible hex digits is different! So this ensures a different hash for every query number. (Note that existing ones are stored in the SQL table)
