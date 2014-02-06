from random import choice
from os import chdir, getcwd, listdir
from os.path import isfile, isdir
from sys import exit


def change_dir():
	""" Changes current working directory. """

	print("Enter desired directory path:")
	path = input("> ")
	if isdir(path) == True:
		chdir(path)
		print("Directory changed to {}".format(getcwd()))
	else:
		print("Directory not found. Exiting...")
		exit(0)


def prompt():
	""" Prompts user for options """

	print("-- Quiz generator --")
	print("")
	print("Current working directory: {}".format(getcwd()))
	print("Use this directory (Y/N)?")
	option = input("> ")
	if option.upper() == "Y":
		pass
	elif option.upper() == "N":
		change_dir()
	else:
		print("Invalid option. Exiting...")
		exit(0)


def show_files():
	""" Displays files in current working directory """

	dir_list = listdir()
	print("")
	print("Files in this directory:")
	for i in dir_list:
		if isfile(i) == True:
			print(i)
	print("")
	return dir_list

def choose_file(dir_list):
	name = input("Enter filename: ")
	while name not in dir_list:
		print("File not found. Try again.")
		name = input("Enter filename: ")
	return name


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
			try:
				quiz_dict[t] = lines[index + 1]   # answer index
			except IndexError:
				quiz_dict[t] = " "
	return quiz_dict


def display_question(question,quiz):
	""" Displays question to user """
	answer = quiz[question]
	go = input("{}".format(question))
	print("Answer:",answer,end="")
	print("")


def main():
	prompt()
	dir_list = show_files()
	filename = choose_file(dir_list)
	print("Using {}".format(filename))
	print("Press enter to view answers.")
	print("")
	quiz = make_quiz(filename)
	used_list = []
	option = ""
	while option.lower() != "q":
		keys = list(quiz.keys())
		question = choice(keys)
		if question not in used_list:
			display_question(question,quiz)
			used_list.append(question)
			option = input("Enter 'q' to quit or press Enter to continue ")
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