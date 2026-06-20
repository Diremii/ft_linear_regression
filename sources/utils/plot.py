# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 13:01:27 by humontas@st       #+#    #+#              #
#    Updated: 2026/06/20 17:33:18 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
from utils.model import estimate_price


def	plot_data(km, price):
	plt.scatter(km, price)
	plt.xlabel("Mileage (km)")
	plt.ylabel("Price")
	plt.title("Car price vs mileage")
	plt.show()

def plot_regression_line(theta0: float, theta1: float, mileage_bounds: tuple):
	mileage_min, mileage_max = mileage_bounds
	price_min_pred = estimate_price(mileage_min, theta0, theta1)
	price_max_pred = estimate_price(mileage_max, theta0, theta1)
	plt.plot([mileage_min, mileage_max], [price_min_pred, price_max_pred], color='red')