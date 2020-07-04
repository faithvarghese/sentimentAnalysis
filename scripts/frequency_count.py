
    # frequncy count
import sys, os, re, argparse
def frequncy(ifile,ofile):

    word_tag_count ={}

    for line in ifile:

        columns = line.strip().split('\t')

        words = columns[0].split(' ')

        for i in range(len(words)):

            if words[i] =="":
                continue

            if words[i] in word_tag_count:

                value = word_tag_count[words[i]]

                word_tag_count[words[i]] = value+1
            else:

                word_tag_count[words[i]] = 1


    for item in sorted(word_tag_count.keys(),reverse = True):

        ofile.write(item+'\t'+str(word_tag_count[item])+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='to do frequency_count')
    parser.add_argument('-i', '--input_train', help='Input file after preprocessing')
    parser.add_argument('-o', '--output', help='output frequncy count of words')
    args = parser.parse_args()
    ifile = open(args.input_train,'r')
    ofile = open(args.output, "w")
    frequncy(ifile,ofile)
