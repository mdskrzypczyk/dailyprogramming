from sys import argv
import string

class Substitution_Cryptoanalysis:
	def __init__(self,cfile):
		cdata = open(cfile).read().splitlines()
		self.encrypted = cdata[0]
		del cdata[0]
		del cdata[0]

		self.wordlist = self.create_wordlist()
		self.sentences = []
		self.basemap = {}
		for mapping in cdata:
			self.basemap[mapping[0]] = mapping[1]
			self.encrypted = self.encrypted.replace(mapping[1],mapping[0])

		self.follow_mapping(self.encrypted,self.basemap)
		self.print_sentences

	def follow_mapping(self,sentence,mapping):
		print sentence
		if self.check_sentence(sentence):
			print "ADDING %s" % sentence
			self.sentences.append((sentence,mapping))
			return None

		elif self.check_words(sentence):
			for char in sentence:	
				if char in string.ascii_uppercase:
					sub_chars = [c for c in string.ascii_lowercase if c not in mapping.keys()]
					for schar in sub_chars:
						nmap = dict(mapping)
						nsentence = sentence
						nmap[schar] = char
						nsentence = nsentence.replace(char,schar)
						if self.check_words(nsentence):
							self.follow_mapping(nsentence,nmap)
					return None

	def check_words(self,sentence):
		slist = sentence.split(' ')
		for word in slist:
			matches = []
			for candidate in self.wordlist[len(word)]:
				if self.is_similar(word,candidate):
					matches.append(candidate)

			if len(matches) == 0:
				return False
		return True

	def is_similar(self,word,candidate):
		for c,w in zip(candidate,word):
			if w in string.ascii_uppercase:
				pass
			elif c != w:
				return False

		return True

	def check_sentence(self,sentence):
		slist = sentence.split(' ')
		for word in slist:
			if len(word) in self.wordlist.keys() and word not in self.wordlist[len(word)]:
				return False

		return True
		
	def create_wordlist(self):
		words = open("enable1.txt").read().splitlines()
		wordlist = {}
		for word in words:
			if len(word) not in wordlist.keys():
				wordlist[len(word)] = [word]
			else:
				wordlist[len(word)].append(word)

		return wordlist

	def print_wordlist(self):
		for key in self.wordlist.keys():
			print self.wordlist[key]

	def print_sentences(self):
		for sentence in self.sentences:
			print sentence

cfile = argv[1]
crypto = Substitution_Cryptoanalysis(cfile)
crypto.print_sentences()