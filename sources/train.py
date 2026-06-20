# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 12:42:58 by humontas@st       #+#    #+#              #
#    Updated: 2026/06/20 18:43:53 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.io import load_data, save_theta, load_theta
from utils.plot import plot_data, plot_regression_line
from utils.normalize import normalize_dataset, denormalize_data
from utils.gradient import gradient_descent


def	main():
	data = load_data("data/data.csv")
	km_norm, price_norm = normalize_dataset(data)

	learning_rate = 0.1
	iterations = 1000

	theta0_norm, theta1_norm = gradient_descent(km_norm, price_norm, learning_rate, iterations)
	theta_norms = theta0_norm, theta1_norm

	price_bounds = data['price'].min(), data['price'].max()
	mileage_bounds = data['km'].min(), data['km'].max()
	
	theta0, theta1 = denormalize_data(theta_norms, price_bounds, mileage_bounds)
	save_theta(theta0, theta1, "data/theta.csv")
	
	plot_regression_line(theta0, theta1, mileage_bounds)
	plot_data(data['km'], data['price'])

if __name__ == "__main__":
	main()