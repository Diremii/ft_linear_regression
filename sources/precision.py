# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    precision.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/10 15:47:11 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/10 16:06:40 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.metrics import calculate_r2
from utils.config import DATA, THETA

def	main():
	r2 = calculate_r2(DATA, THETA)
	print(f"R² score: {r2:.4f}")
	print(f"Explained variance: {r2 * 100:.2f}%")
	

if __name__ == "__main__":
	main()