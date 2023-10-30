"""
File: pick_your_starter_pokemon.py
Name:\
--------------------------
This file shows how to use command line 
to launch different functions.
We will be introducing sys module and use it
to do the job
"""
import sys


def main():
	args = sys.argv
	if args[1] == 'charmander':
		draw_charmander()
	elif args[1] == 'bulbasaur':
		draw_bulbasaur()
	elif args[1] == 'squirtle':
		draw_squirtle()
	else:
		print('Illegal Pokemon')


def draw_charmander():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("          N777777777NO")
	print("         N7777777777777N")
	print("        $N877777777D77777M")
	print("       N M77777777ONND777M")
	print("       MN777777777NN  D777")
	print("     N7ZN777777777NN ~M7778")
	print("    N777777777777MMNN88777N")
	print("     N7OONND7777777D77777N")
	print("      8$M++++?N???$77777$")
	print("          DNNM$$$$777777N")
	print("         N$N:=N$777N7777M                         ")
	print("        77Z::::N777777777                          ")
	print("       77N::::::N77777777M                         DZ  ")
	print("     $777:::::::77777777MN                        DNZ ")
	print("    7777M:::::M7777777$777M                      DZZZ")
	print("   M777$:::::N777777$M7777M                      NNZZZ$")
	print("     NN$::::::7777$$M777777N                     M8ZZZ")
	print("       N::::::N:7$O:77777777                     $++IZZ")
	print("       INN===::::::=77777777777N                 I777N")
	print("      ?777N========N7777777777787M               N777")
	print("       M$$$$$$$$M    M$$$$$$$$N=N$$$$7777777$$$ND")
	print("      O77Z$$$$$$$     M$$$$$$$$MNI==$DNNNNM=~N")
	print("   7 :N MNN$$$$M$      $$$777$8      8D8I")
	print("     NMM.:7O           777777778")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def draw_bulbasaur():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("             `;,;.;,;.;.'")
	print("              ..:;:;::;: ")
	print("        ..--''' '' ' ' '''--.  ")
	print("      /' .   .'        '.   .`\\")
	print("     | /    /            \\   '.|")
	print("     | |   :             :    :|")
	print("   .'| |   :             :    :|")
	print(" ,: /\\ \\.._\\ __..===..__/_../ /`.")
	print("|'' |  :.|  `'          `'  |.'  ::.")
	print("|   |  ''|    :'';          | ,  `''\\")
	print("|.:  \\/  | /'-.`'   ':'.-'\\ |  \\,   |")
	print("| '  /  /  | / |...   | \\ |  |  |';'|")
	print(" \\ _ |:.|  |_\\_|`.'   |_/_|  |.:| _ |")
	print("/,.,.|' \\__       . .      __/ '|.,.,\\")
	print("     | ':`.`----._____.---'.'   |")
	print("l42   \\   `:\"\"\"-------'\"\"' |   |")
	print("       ',-,-',             .'-=,=,")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def draw_squirtle():
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('          ___                   ')
	print("     _.-~~   ~~~-.              ")
	print("    /         _   ~.            ")
	print("   |#`       /#`    \\           ")
	print("   |-'|      |-'|    |       ")
	print("   /--        --     |-.        ")
	print("   \\__   .  .        / /\\_      ")
	print("    \\ ~~--___---~~/\\| |   ~-.   ")
	print(".---`~~--____---_)  \\ \\-__  \\  ")
	print(") <    |__    __\\_   \\ \\     | ")
	print("~-.__ /   ~~~~   \\   \\ \\     | ")
	print("      ~-.   |     .~-.-' |    | ")
	print("       | \\___|___/     / /     |")
	print("       | /   |   \\     | |  /  |")
	print("        \\     |   ~-___ \\ \\/  / ")
	print("        /\\__ / `._ /   ~-\\ \\_/  ")
	print("       /    \\_____|      |`~    ")
	print("      |      |    |      |      ")
	print("       \\     |    |      |      ")
	print("       >______)   /_/\\/\\_\\      ")
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


if __name__ == '__main__':
	main()
