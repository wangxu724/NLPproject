Group Member:
	Xu Wang, u0933124
	Kaiqiang Wang, u0931645

==========================================================================
1, How to run our codes?

	1) INSTALL nltk library for python
		Since we import some method from a python's natural language processing library, nltk, it's required to install the library into the python's enivornment. 
		We provide some commands to help you do that as below:
	        1.
	            if you can sudo
	                > sudo pip install nltk
	            else:
	                1. run: 
	                	> pip install --install-option="--prefix=/some/local/path/" nltk
	                2. Add “/some/path/lib/python2.7/site-packages/“ to the PYTHONPATH environment variable
	        2. run: 
	        	> python
	        3. in the python interpreter type:
	            >>> import nltk
	            >>> nltk.download()
	            >>> d all
	            >>> q
	            >>> exit()

	2) Instructions of code files and folders.
		- data/: The folder including all test files for loaded by program, *.story, *.questions. 
		- input.txt: The Input file following the instructions document of project. 
		- output.txt: The Output file to show answers
		- qa.py: The main function of Q/A System. 
		- utility.py: Provide some functions to read / write files, assist others program
		- solver.py: Provide funciton to analysis the background story, question and providing answers.
	3) Configure the information of data files
		- Configure the data path in Input Files:
			1. Open "input.txt", and replace the first line by your data files path. 
			2. And then list names of all testcases files below that. 
			For example:
----------------------------------------------------------------------------------------------
/home/cs5340/project/developset/
1999-W11-2
1999-W22-2
----------------------------------------------------------------------------------------------
	4) Run the code using below command
		> python qa.py <Input Filename>
		For example:
		> python qa.py input.txt

==========================================================================
2, Which CADE machine we tested out program ?
lab2-5



