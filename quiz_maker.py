from random import choice


def prompt():
	""" Prompts user for file name """

	print("Enter a file name")
	filename = input("> ")
	return filename


def make_quiz(filename):
	""" Reads from file to create dictionary with questions and answers """
	with open(filename,"r") as file_obj:
		lines = file_obj.readlines()
	for i in lines:
		if i == "\n":
			lines.remove(i)  # remove blank lines

	quiz_dict = {}
	for t in lines:
		index = lines.index(t)
		if index % 2 == 0:                    # question index
			quiz_dict[t] = lines[index + 1]   # answer index
	return quiz_dict


def display_question(question,quiz):
	""" Displays question to user """
	answer = quiz[question]
	print(question,end="")
	go = input("Press enter to view answer.")
	print("Answer:",answer,end="")
	print("")


def main():
	filename = prompt()
	quiz = make_quiz(filename)
	used_list = []
	option = ""
	while option.lower() != "q":
		keys = list(quiz.keys())
		question = choice(keys)
		if question not in used_list:
			display_question(question,quiz)
			used_list.append(question)
			option = input("Enter 'q' to quit or press Enter to continue")
			print("")
		elif len(used_list) == len(quiz):
			print("All questions used. Restart?")
			restart = input("> ")
			if restart.lower() == "y":
				used_list = []
				continue
			elif restart.lower() == "n":
				break
	print("Goodbye!")


if __name__ == "__main__":
	main()