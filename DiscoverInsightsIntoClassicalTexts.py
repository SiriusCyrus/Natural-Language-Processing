from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text of choice here
text = open("dorian_gray.txt",encoding='utf-8').read().lower()
text2 = open("the_iliad.txt",encoding='utf-8').read().lower()

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)
word_tokenized_text2 = word_sentence_tokenize(text2)

# store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[100]
print(single_word_tokenized_sentence)

single_word_tokenized_sentence2 = word_tokenized_text2[100]
print(single_word_tokenized_sentence2)

# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = []
pos_tagged_text2 = []

# create a for loop through each word tokenized sentence here
for i in word_tokenized_text:
  pos_tagged_text.append(pos_tag(i))
for j in word_tokenized_text2:
  pos_tagged_text2.append(pos_tag(j))

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[100]
print(single_pos_sentence)
single_pos_sentence2 = pos_tagged_text2[100]
print(single_pos_sentence2)

# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = "VP :{<VB.*><DT>?<JJ>*<NN><RB.?>?}"

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = []
vp_chunked_text = []

np_chunked_text2 = []
vp_chunked_text2 = []

# create a for loop through each pos-tagged sentence here
for i in pos_tagged_text:
  np_chunked_text.append(np_chunk_parser.parse(i))
  vp_chunked_text.append(vp_chunk_parser.parse(i))

for j in pos_tagged_text2:
  np_chunked_text2.append(np_chunk_parser.parse(j))
  vp_chunked_text2.append(vp_chunk_parser.parse(j))

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)

most_common_np_chunks2 = np_chunk_counter(np_chunked_text2)
print(most_common_np_chunks2)

# store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)

most_common_vp_chunks2 = vp_chunk_counter(vp_chunked_text2)
print(most_common_vp_chunks2)