# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 18:22:24 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/03 17:06:43 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from utils.io import load_theta, save_prediction
from utils.model import estimate_price
from utils.config import THETA, PREDICTIONS


def	main():
	if os.path.exists(THETA):
		theta0, theta1 = load_theta(THETA)
	else:
		theta0, theta1 = 0, 0

	mileage_str = input("Enter the mileage: ")
	try:
		mileage = float(mileage_str)
	except ValueError:
		print("Error: put a valid value.")
		return
	if theta0 == 0 and theta1 == 0:
		print("Warning: model not trained yet, prediction will be 0.")
	price = estimate_price(mileage, theta0, theta1)
	print(f"Estimated price: {price:.2f}")
	save_prediction(mileage, price, PREDICTIONS)

if __name__ == "__main__":
	main()