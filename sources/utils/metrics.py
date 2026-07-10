# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    metrics.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/10 15:57:59 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/10 16:04:02 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.io import load_data, load_theta
from utils.model import estimate_price


def calculate_r2(data_path, theta_path) -> float:
	data = load_data(data_path)
	theta0, theta1 = load_theta(theta_path)

	predictions = estimate_price(data["km"], theta0, theta1)

	ss_res = ((data["price"] - predictions) ** 2).sum()
	ss_tot = ((data["price"] - data["price"].mean()) ** 2).sum()
	if ss_tot == 0:
		return 0.0

	r2 = 1 - ss_res / ss_tot

	return r2
