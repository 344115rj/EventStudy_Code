import re
import glob

print('Big Data Culture Articles for Honeywell Limited. '
      'Below you can find a summary of keywords as well as the importance of each article:' + '\n')

filenames = sorted(glob.glob('article*.txt'))
filenames = filenames[0:71]

i = 0
while i < len(filenames):
    with open((filenames[i]), 'r') as f:
        for line in f:
            line = line.lower()
            print('Word Occurrence', filenames[i]+':' '\n')
            contents = f.read()
            first_word = 'big-data'
            first_count = contents.count(first_word)
            print(first_word, first_count)
            second_word = 'big data'
            second_count = contents.count(second_word)
            print(second_word, second_count)
            extra_word = 'Big Data'
            extra_count = contents.count(extra_word)
            print(extra_word, extra_count)
            third_word = 'culture'
            third_count = contents.count(third_word)
            print(third_word, third_count)
            fourth_word = 'habits'
            fourth_count = contents.count(fourth_word)
            print(fourth_word, fourth_count)
            fifth_word = 'values'
            fifth_count = contents.count(fifth_word)
            print(fifth_word, fifth_count)
            sixth_word = 'norms'
            sixth_count = contents.count(sixth_word)
            print(sixth_word, sixth_count)
            seventh_word = 'proficiency'
            seventh_count = contents.count(seventh_word)
            print(seventh_word, seventh_count)
            eight_word = 'thinking'
            eight_count = contents.count(eight_word)
            print(eight_word, eight_count)
            ninth_word = 'framework'
            ninth_count = contents.count(ninth_word)
            print(ninth_word, ninth_count)
            tenth_word = 'attitude'
            tenth_count = contents.count(tenth_word)
            print(tenth_word, tenth_count)
            eleventh_word = 'belief'
            eleventh_count = contents.count(eleventh_word)
            print(eleventh_word, eleventh_count)
            twelfth_word = 'mindset'
            twelfth_count = contents.count(twelfth_word)
            print(twelfth_word, twelfth_count)
            thirteenth_word = 'intrinsic'
            thirteenth_count = contents.count(thirteenth_word)
            print(thirteenth_word, thirteenth_count)
            fourteenth_word = 'integral'
            fourteenth_count = contents.count(fourteenth_word)
            print(fourteenth_word, fourteenth_count)
            fifteenth_word = 'perception'
            fifteenth_count = contents.count(fifteenth_word)
            print(fifteenth_word, fifteenth_count)
            sixteenth_word = 'enlightenment'
            sixteenth_count = contents.count(sixteenth_word)
            print(sixteenth_word, sixteenth_count)
            seventeenth_word = 'manners'
            seventeenth_count = contents.count(seventeenth_word)
            print(seventeenth_word, seventeenth_count)
            eighteenth_word = 'lifestyle'
            eighteenth_count = contents.count(eighteenth_word)
            print(eighteenth_word, eighteenth_count)
            eighteenth_word = 'mores'
            eighteenth_count = contents.count(eighteenth_word)
            print(eighteenth_word, eighteenth_count)
            print('\n')
            print('Summary Statistics', filenames[i]+':')
            big_data = first_count+second_count+extra_count
            print('Big Data is mentioned', big_data, 'time(s)')
            print('Culture is mentioned', third_count, 'time(s)')
            other_keywords = fourth_count+fifth_count+sixth_count+seventh_count+eight_count\
            +ninth_count+tenth_count+eleventh_count+twelfth_count+thirteenth_count+fourteenth_count+fifteenth_count\
            +sixteenth_count+seventeenth_count+eighteenth_count
            print('Other keywords are mentioned', other_keywords, 'time(s)')
            print('Importance level is', (50*big_data+25*third_count+5*other_keywords))
            print('\n')
    i+=1
