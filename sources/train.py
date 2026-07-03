# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 12:42:58 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/03 22:34:54 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.config import DATA, ITERATIONS, LEARNING_RATE, THETA, PREDICTIONS
from utils.gradient import gradient_descent
from utils.io import load_data, save_theta
from utils.normalize import denormalize_data, normalize_dataset
from utils.plot import plot_data, plot_predictions, plot_regression_line


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
	plot_predictions(PREDICTIONS)
	plot_data(data['km'], data['price'])

if __name__ == "__main__":
	main()