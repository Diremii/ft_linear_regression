# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    callbacks.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/10 16:34:27 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/10 16:43:02 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from tkinter import messagebox

from train import main as train
from utils.config import THETA, PREDICTIONS, DATA
from utils.predictor import predict
from utils.reset import reset_files
from utils.metrics import calculate_r2


def	update_r2(r2_label):
	if os.path.exists(THETA):
		r2 = calculate_r2(DATA, THETA)
		r2_label.configure(text=f"Model precision (R²): {r2 * 100:.2f}%")
	else:
		r2_label.configure(text="R² score: Model not trained")


def	on_predict(mileage_entry, success_label, set_warning, refresh_history):
	mileage_str = mileage_entry.get()

	try:
		mileage = float(mileage_str)
	except ValueError:
		messagebox.showerror("Error", "put a valid value.")
		return

	price, theta0, theta1 = predict(mileage, THETA, PREDICTIONS)

	if theta0 == 0 and theta1 == 0:
		set_warning("Warning: model not trained yet, prediction will be 0.")
	else:
		set_warning("")

	success_label.configure(text=f"Estimated price: {price:.2f}")
	refresh_history()


def	on_train(set_warning, update_r2):
	train()
	set_warning("")
	update_r2()


def	on_reset(set_warning, success_label, update_r2, refresh_history):
	confirm = messagebox.askyesno("Reset", "This will delete your trained model and prediction history.")

	if not confirm:
		return

	reset_files(THETA, PREDICTIONS)
	set_warning("Warning: model not trained yet, prediction will be 0.")
	success_label.configure(text="")
	update_r2()
	refresh_history()