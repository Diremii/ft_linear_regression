# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    normalize.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 13:25:14 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/03 22:15:57 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def	normalize_data(values: pd.Series) -> pd.Series:
	min_val = values.min()
	max_val = values.max()
	return (values - min_val) / (max_val - min_val)

def	normalize_dataset(data: pd.DataFrame) -> tuple:
	km_norm = normalize_data(data['km'])
	price_norm = normalize_data(data['price'])
	return km_norm, price_norm

def	denormalize_data(theta_norms: tuple, price_bounds: tuple, mileage_bounds: tuple) -> tuple:
	price_min, price_max = price_bounds
	mileage_min, mileage_max = mileage_bounds
	theta0_norm, theta1_norm = theta_norms
	
	theta1 = theta1_norm * (price_max - price_min) / (mileage_max - mileage_min)
	theta0 = price_min + theta0_norm * (price_max - price_min) - theta1 * mileage_min
	return theta0, theta1