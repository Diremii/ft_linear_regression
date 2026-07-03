# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 15:02:08 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/03 22:35:22 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

from utils.model import estimate_price
from utils.config import VERBOSE


def	gradient_descent(km_norm: pd.Series, price_norm: pd.Series, learning_rate: float, iterations: int) -> tuple:
	theta0 = 0
	theta1 = 0
	m = len(km_norm)
	
	for i in range(iterations):
		predictions = estimate_price(km_norm, theta0, theta1)
		errors = predictions - price_norm
		errors_km = errors * km_norm

		theta0_tmp = learning_rate * (errors.sum() / m)
		theta1_tmp = learning_rate * (errors_km.sum() / m)

		theta0 = theta0 - theta0_tmp
		theta1 = theta1 - theta1_tmp

		if VERBOSE and i % 100 == 0:
			print(i, errors.abs().mean())

	return theta0, theta1