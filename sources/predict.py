# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 18:22:24 by humontas@st       #+#    #+#              #
#    Updated: 2026/06/20 18:51:52 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.io import load_theta
import os

def	main():
	if os.path.exists("data/theta.csv"):
		theta0, theta1 = load_theta("data/theta.csv")
	else:
		theta0, theta1 = 0, 0

# Récuperer l'input et le paser


if __name__ == "__main__":
	main()