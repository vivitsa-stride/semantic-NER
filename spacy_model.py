import spacy

nlp = spacy.load('en_core_web_sm')

sentence = "Apple is looking at buying U.K. startup for $1 billion"

doc = nlp(sentence)

for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)

def get_spacy_entities():
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(sentence)
	for ent in doc.ents:
		return (ent.text, ent.start_char, ent.end_char, ent.label_)


