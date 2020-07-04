
    # To determine the Unique list and make duplicates
    # converting stop words to unk
    # Stemming and spelling correction
import sys, os, re, argparse
def tam_preprocess(ifile,ifile1,ifile2,ofile):
    b = 0
    a =[]
    d = 0
    e = 0
    stop = {}
    remove_stop = []
    stem = {}
    stem_convert = []

    #ofile1 = open('/Users/faith/Downloads/co/malayalam_dev1.tsv', 'w')
    for line in ifile:

        columns = line.strip().split('\t')

        mal_clean = re.sub('[^A-z \n]', ' ',re.sub(r'(.)\1+', r'\1\1',re.sub(r'[_\\]', r' ',  re.sub(' +', ' ', columns[0]) )))
        mal_clean2 =  re.sub(' +',' ', re.sub(' +\n', '\n',mal_clean))
        cleaned = mal_clean2.lower()+'\t'
        cleaned1 = re.sub(' \t', '\t', re.sub('\t{2}', '\t', cleaned))
        if len(cleaned1) < 2:
            continue
        for sentence in cleaned1.strip().split('\n'):
            sentence_tag = sentence + '\t' + columns[1]+'\n'

            intent = sentence_tag.split('\n')


            for i in intent:

                if i not in a:
                    b = b+1
                    a.append(i)

    for line in ifile1:
        columns = line.strip().split('\t')
        if len(columns[0]) < 1:
            continue
        stop[columns[0]] = columns[1]

    for line in ifile2:
        columns = line.strip().split('\t')
        if len(columns[0]) < 1:
            continue
        stem[columns[0]] = columns[1]
    print(b)
    intents = '\n'.join(a)
    negatives =[]
    Mixed_feelings = []
    not_malayalams = []
    positives = []
    unknown_states = []
    category = []
    combined = intents.strip().split('\n')
    for line in combined:
        columns = line.split('\t')
        if len(columns) < 2:
            continue
        words = columns[0].split(' ')
        #print(words)
        for i in range(len(words)):
            word = words[i]
            #print(word)

            if word in stop:
                word_map = re.sub(word, stop[word], word)

                words[i] = word_map
        new_sentence = ' '.join(words)
        removed = new_sentence +'\t' + columns[1] +'\n'
        removed_s = removed.strip().split('\n')

        for sentence in removed_s:
            if sentence not in remove_stop:
                d = d+1
                remove_stop.append(sentence)
    print(d)
    stops_removed = '\n'.join(remove_stop)
    new_combined = stops_removed.strip().split('\n')

    for line in new_combined:
        columns = line.split('\t')
        if len(columns) < 2:
            continue
        words = columns[0].split(' ')
        #print(words)
        for i in range(len(words)):
            word = words[i]
            #print(word)
            if word in stem:
                word_map = re.sub(word, stem[word], word)

                words[i] = word_map
        new_sentence = ' '.join(words)
        convert = new_sentence +'\t' + columns[1] +'\n'
        converted = convert.strip().split('\n')

        for sentence in converted:
            if sentence not in stem_convert:
                e = e+1
                stem_convert.append(sentence)
    print(e)
    stem_converted = '\n'.join(stem_convert)
    new_clean = stem_converted.strip().split('\n')
    #ofile1.write(stem_converted)
    for line in new_clean:
        comments = line.split('\t')
        if len(comments) < 2:
            continue
        comments = line.split('\t')

        if comments[1].lower() == 'positive':
            positive = '\t'.join(comments[0:2])
            positives.append(positive)

        if comments[1].lower() == 'negative':
            negative = '\t'.join(comments[0:2])

            negatives.append(negative)

        if comments[1].lower() == 'mixed_feelings':
            mixed_feeling = '\t'.join(comments[0:2])

            Mixed_feelings.append(mixed_feeling)

        if 'not' in comments[1].lower():

            not_malayalam = '\t'.join(comments[0:2])

            not_malayalams.append(not_malayalam)

        if comments[1].lower() == 'unknown_state':
            unknown_state = '\t'.join(comments[0:2])

            unknown_states.append(unknown_state)

        if comments[1].lower() == 'category':
            header = '\t'.join(comments[0:2])

            category.append(header)

    new_comments = '\n'.join(category)+'\n'+'\n'.join(positives*2)+'\n' +'\n'.join(negatives*7)+'\n' + '\n'.join(Mixed_feelings*13) +'\n'+ '\n'.join(unknown_states*3) +'\n'+ '\n'.join(not_malayalams*6)
    #new_comments = '\n'.join(category)+'\n'+'\n'.join(positives)+'\n' +'\n'.join(negatives*3)+'\n' + '\n'.join(Mixed_feelings*6) +'\n'+ '\n'.join(unknown_states) +'\n'+ '\n'.join(not_malayalams*2)
    new_comments_tam = '\n'.join(category)+'\n'+'\n'.join(positives)+'\n' +'\n'.join(negatives*5)+'\n' + '\n'.join(Mixed_feelings*4) +'\n'+ '\n'.join(unknown_states*12) +'\n'+ '\n'.join(not_malayalams*20)

    ofile.write(new_comments_tam)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tam_preprocess')
    parser.add_argument('-it', '--input_train', help='Input train file')
    parser.add_argument('-s', '--input_mal_stop', help='Input stop file')
    parser.add_argument('-ms', '--input_mal_stem', help='Input stem file')
    parser.add_argument('-o', '--output', help='Output file after preprocessing')
    args = parser.parse_args()
    ifile = open(args.input_train,'r')
    ifile1 = open(args.input_mal_stop,'r')
    ifile2 = open(args.input_mal_stem,'r')
    ofile = open(args.output, "w")
    tam_preprocess(ifile,ifile1,ifile2,ofile)
