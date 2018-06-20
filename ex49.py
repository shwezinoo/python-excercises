def peek(word_list):
if word_list:
word = word_list[0]
return word[0]
else:
return None
def match(word_list, expecting):
if word_list:
word = word_list.pop(0)
if word[0] == expecting:
return word
else:
return None
else:
return None
def parse_verb(word_list):
skip(word_list, 'stop')
if peek(word_list) == 'verb':
return match(word_list, 'verb')
else:
raise ParserError("Expected a verb next.")
def parse_object(word_list):
skip(word_list, 'stop')
next_word = peek(word_list)
if next_word == 'noun':
return match(word_list, 'noun')
elif next_word == 'direction':
return match(word_list, 'direction')
else:
   def parse_subject(word_list):
skip(word_list, 'stop')
next_word = peek(word_list)
if next_word == 'noun':
return match(word_list, 'noun')
elif next_word == 'verb':
return ('noun', 'player')
else:
raise ParserError("Expected a verb next.")
def parse_sentence(word_list):
subj = parse_subject(word_list)