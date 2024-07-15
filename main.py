def convert(dictionary):
	return [{"letter": key, "num": value} for key, value in dictionary.items()]

def word_count(book_string):
	return len(book_string.split())

def character_count(book_string):
	lowered_string = book_string.lower()
	my_dict = {}
	for character in lowered_string:
		if character.isalpha():
			my_dict[character] = my_dict.get(character, 0) + 1
	return my_dict

def sort_on(dict):
	return dict["num"]



def report(book_string):
	report_text = "--- Begin report of books/frankenstein.txt ---\n" + str(word_count(book_string)) + " words found in the document\n\n"
	dict_list = convert(character_count(book_string))
	dict_list.sort(reverse=True, key=sort_on)
	for dictionary in dict_list:
		report_text = report_text + "The " + dictionary["letter"] + " character was found " + str(dictionary["num"]) + " times\n"
	report_text = report_text + "--- End report ---"
	return report_text

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	print(report(file_contents))
	
	

main()


