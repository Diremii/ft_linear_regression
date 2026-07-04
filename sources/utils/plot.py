# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 13:01:27 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 14:58:00 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from utils.config import (
	LINE_COLOR, POINT_COLOR, POINT_MARKER, PREDICTION_COLOR,
	PREDICTION_MARKER, SHOW_LINE, SHOW_POINTS, SHOW_PREDICTIONS,
)
from utils.model import estimate_price
from utils.io import load_predictions


def	plot_data(km, price):
	if SHOW_POINTS:
		plt.scatter(km, price, color=POINT_COLOR, marker=POINT_MARKER)
	plt.xlabel("Mileage (km)")
	plt.ylabel("Price")
	plt.title("Car price vs mileage")
	plt.show()

def	plot_regression_line(theta0: float, theta1: float, mileage_bounds: tuple):
	if SHOW_LINE:
		mileage_min, mileage_max = mileage_bounds	
		price_min_pred = estimate_price(mileage_min, theta0, theta1)
		price_max_pred = estimate_price(mileage_max, theta0, theta1)
		plt.plot([mileage_min, mileage_max], [price_min_pred, price_max_pred], color=LINE_COLOR)

def	plot_predictions(path):
	if not SHOW_PREDICTIONS:
		return
	data = load_predictions(path)
	plt.scatter(data['km'], data['price'], color=PREDICTION_COLOR, marker=PREDICTION_MARKER)