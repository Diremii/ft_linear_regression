# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    io.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 12:10:48 by humontas@st       #+#    #+#              #
#    Updated: 2026/06/20 18:42:10 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


def	load_data(path: str) -> pd.DataFrame:
	data = pd.read_csv(path)
	if 'km' not in data.columns or 'price' not in data.columns:
		raise ValueError("The CSV file must contain 'km' and 'price' columns.")
	return data

def	save_theta(theta0: float, theta1: float, path: str):
	df = pd.DataFrame({'theta0': [theta0], 'theta1': [theta1]})
	df.to_csv(path, index=False)

def	load_theta(path: str) -> tuple:
	data = pd.read_csv(path)
	if 'theta0' not in data.columns or 'theta1' not in data.columns:
		raise ValueError("The CSV file must contain 'theta0' and 'theta1' columns.")
	theta0 = data['theta0'].iloc[0]
	theta1 = data['theta1'].iloc[0]
	return theta0, theta1