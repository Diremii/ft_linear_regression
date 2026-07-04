# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predictor.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 09:53:12 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 14:58:53 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from utils.io import load_theta, save_prediction
from utils.model import estimate_price


def	predict(mileage: float, theta_path: str, predictions_path: str):
	if os.path.exists(theta_path):
		theta0, theta1 = load_theta(theta_path)
	else:
		theta0, theta1 = 0, 0
	price = estimate_price(mileage, theta0, theta1)
	save_prediction(mileage, price, predictions_path)
	return price, theta0, theta1