# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 12:42:58 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/03 17:09:59 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.io import load_data, save_theta
from utils.plot import plot_data, plot_regression_line, plot_predictions
from utils.normalize import normalize_dataset, denormalize_data
from utils.gradient import gradient_descent
from utils.config import LEARNING_RATE, ITERATIONS, DATA, THETA


def	main():
	data = load_data(DATA)
	km_norm, price_norm = normalize_dataset(data)

	theta0_norm, theta1_norm = gradient_descent(km_norm, price_norm, LEARNING_RATE, ITERATIONS)
	theta_norms = theta0_norm, theta1_norm

	price_bounds = data['price'].min(), data['price'].max()
	mileage_bounds = data['km'].min(), data['km'].max()
	
	theta0, theta1 = denormalize_data(theta_norms, price_bounds, mileage_bounds)
	save_theta(theta0, theta1, THETA)
	
	plot_regression_line(theta0, theta1, mileage_bounds)
	plot_predictions("data/predictions.csv")
	plot_data(data['km'], data['price'])

if __name__ == "__main__":
	main()