# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gui.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 22:40:21 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 00:34:07 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

import customtkinter as ctk
from tkinter import messagebox

from utils.model import estimate_price
from utils.io import save_prediction, load_theta
from utils.config import THETA, PREDICTIONS
from train import main as train

def	get_theta():
	if os.path.exists(THETA):
		return load_theta(THETA)
	return 0, 0

def	main():
	app = ctk.CTk()
	app.title("ft_linear_regression")
	app.geometry("400x300")

	mileage_label = ctk.CTkLabel(app, text="Mileage", anchor="w")
	mileage_label.pack(fill="x", padx=20, pady=(20, 0))

	mileage_entry = ctk.CTkEntry(app, placeholder_text="Enter mileage")
	mileage_entry.pack(fill="x", padx=20, pady=10)

	warning_label = ctk.CTkLabel(app, text="")
	warning_label.pack(pady=10)

	success_label = ctk.CTkLabel(app, text="")
	success_label.pack(pady=10)

	theta0, theta1 = get_theta()
	if theta0 == 0 and theta1 == 0:
		warning_label.configure(text="Model not trained yet")

	def	on_predict():
		mileage_str = mileage_entry.get()
		try:
			mileage = float(mileage_str)
		except ValueError:
			messagebox.showerror("Error", "put a valid value.")
			return
		theta0, theta1 = get_theta()
		if theta0 == 0 and theta1 == 0:
			warning_label.configure(text="Model not trained yet")
		else:
			warning_label.configure(text="")
		price = estimate_price(mileage, theta0, theta1)
		success_label.configure(text=f"Estimated price: {price:.2f}")
		save_prediction(mileage, price, PREDICTIONS)

	predict_button = ctk.CTkButton(app, text="Predict", command=on_predict)
	predict_button.pack(fill="x", padx=20, pady=10)

	train_button = ctk.CTkButton(app, text="Train", command=train)
	train_button.pack(fill="x", padx=20, pady=10)

	app.mainloop()

if __name__ == "__main__":
	main()