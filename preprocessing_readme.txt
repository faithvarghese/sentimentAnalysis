
1.	read the input file (train,dev)
2.	Text cleaning
	removing punctuations, non-latin script,special characters, repeated spequential characters, multi tabs, multi spaces and converting the text into lower case

3.	removing the duplicate sentences and stored in a variable as a list

4.	reading stop file and stem file
	
	stop file and stem file are two column format file.
	1st column -> unique word list of the train data
	2nd column -> the desired substitution (eg: 'a' -> 'unk') ('liked' -> like)

5.	removing the duplicates after substitution

	5.1.	save the output

The above steps are followed for both train and dev data to run the nb model when cross validation is used to evaluate the model.


6. oversampling the data since we have unbalanced class

cross validation may not be a right parameter for model evaluation when we do 6 (oversampling)

The exact sentences and categories in the test fold could be present in the training folds 

There is a high chance of resulting in false higher accuracy