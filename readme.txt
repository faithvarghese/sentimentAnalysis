
To run =>	mal-preprocessing.py or tam-preprocessing.py
	----

python3 mal-preprocessing.py -it malayalam_train.tsv -s mal_stop.tsv -ms mal_stem.tsv -o mal_train_out.tsv


		{lang} = tamil or malayalam

			{lang}_stop.tsv

			Find malayalam or tamil functional words and tag it as 'unk' (to replace functional wordds to unk)

			E.g. 'oru' -> 'unk'


			{lang}_stem.tsv

			Find the opinion carrying words and map to stem, correct spellings

			E.g 'likee'	-> 'like', 'liked' -> 'like'




{lang}_stop.tsv and {lang}_stem.tsv can be build by taking frequency count of unique words.

To generate frequency file for the language

	First
		
		run the mal-preprocessing.py or tam-preprocessing.py.

		here {lang}_stop.tsv and {lang}_stem.tsv can be empty.

	Second

		The output file of mal-preprocessing.py or tam-preprocessing.py will be the desired input for frequency_count.py

	Third

		run the command

python3 frequency_count.py -i mal_train_out.tsv -o mal_freq.tsv


Simple rule


	{lang}train.tsv, {lang}dev.tsv , {lang}_stem.tsv and {lang}_stop.tsv will be in two column format.

	for help check mal_stem.tsv and mal_stop.tsv (For implementation, I just added a few)




