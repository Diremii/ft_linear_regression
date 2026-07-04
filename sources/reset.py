# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reset.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 09:46:51 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 10:59:20 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from utils.config import THETA, PREDICTIONS
from utils.reset import reset_files

def	main():
	confirmation_str = input("Are you sure? This will delete your trained model and prediction history. [y/n]: ")
	if confirmation_str.lower() in ("y", "yes"):
		reset_files(THETA, PREDICTIONS)
		print("Reset complete.")
	else:
		print("Reset cancelled.")

if __name__ == "__main__":
	main()