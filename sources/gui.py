# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gui.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 22:40:21 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 14:51:36 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import subprocess
import platform

import customtkinter as ctk
from tkinter import messagebox

from train import main as train
from utils.config import THETA, PREDICTIONS, CONFIG
from utils.predictor import predict
from utils.reset import reset_files
from utils.io import load_predictions


# -----------------------------------------------------------------#
#  Left column sections (mileage / predict / result / train-reset) #
# -----------------------------------------------------------------#

def	build_mileage_section(app):
	label = ctk.CTkLabel(app, text="Mileage", anchor="w")
	label.pack(fill="x", padx=20, pady=(20, 5))
	entry = ctk.CTkEntry(app, placeholder_text="Enter mileage", height=36)
	entry.pack(fill="x", padx=20, pady=(0, 15))
	return entry

def	build_predict_button(app, on_predict):
	predict_button = ctk.CTkButton(app, text="Predict", command=on_predict, height=36)
	predict_button.pack(fill="x", padx=20, pady=(0, 15))

def	build_result_section(app):
	warning_label = ctk.CTkLabel(app, text="", text_color="orange")
	frame = ctk.CTkFrame(app, corner_radius=8)
	frame.pack(fill="x", padx=20, pady=(0, 15))
	success_label = ctk.CTkLabel(frame, text="", anchor="w")
	success_label.pack(fill="x", padx=15, pady=6)
	def	set_warning(text):
		if text:
			warning_label.configure(text=text)
			warning_label.pack(fill="x", padx=20, pady=(0, 10), before=frame)
		else:
			warning_label.pack_forget()
	return set_warning, success_label

def	build_buttons_section(app, on_train, on_reset):
	bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
	bottom_frame.pack(fill="x", padx=20, pady=(0, 20))
	train_button = ctk.CTkButton(bottom_frame, text="Train/Show Graph", command=on_train, height=36)
	train_button.pack(side="left", expand=True, fill="x", padx=(0, 5))
	reset_button = ctk.CTkButton(bottom_frame, text="Reset", command=on_reset, fg_color="darkred", height=36)
	reset_button.pack(side="left", expand=True, fill="x", padx=(5, 0))

	file_frame = ctk.CTkFrame(app, fg_color="transparent")
	file_frame.pack(fill="x", padx=20, pady=(0, 20))
	def	open_file(path):
		system = platform.system()
		if system == "Windows":
			os.startfile(path)
		elif system == "Darwin":
			subprocess.run(["open", path])
		else:
			subprocess.run(["xdg-open", path])
	config_button = ctk.CTkButton(file_frame, text="Config file", command=lambda: open_file(CONFIG), fg_color="gray20", height=36)
	config_button.pack(side="left", expand=True, fill="x", padx=(0, 5))
	predictions_button = ctk.CTkButton(file_frame, text="Prediction file", command=lambda: open_file(PREDICTIONS), fg_color="gray20", height=36)
	predictions_button.pack(side="left", expand=True, fill="x", padx=(5, 0))


# -------------------------------------------#
#  Right column section (prediction history) #
# -------------------------------------------#

def	build_history_section(app):
	title = ctk.CTkLabel(app, text="Prediction history", anchor="center", font=ctk.CTkFont(weight="bold"))
	title.pack(fill="x", padx=15, pady=(15, 5))
	scroll_frame = ctk.CTkScrollableFrame(app, fg_color="transparent")
	scroll_frame.pack(fill="both", expand=True, padx=10, pady=(0, 15))
	def	refresh():
		for widget in scroll_frame.winfo_children():
			widget.destroy()
		data = load_predictions(PREDICTIONS)
		for _, row in data[::-1].iterrows():
			text = f"{row['km']:.0f} km -> {row['price']:.2f}"
			ctk.CTkLabel(scroll_frame, text=text, anchor="w").pack(fill="x", padx=5, pady=2)
	return refresh


# ---------------------#
# Main window assembly
# ---------------------#

def	main():
	app = ctk.CTk()
	app.title("ft_linear_regression")
	app.geometry("550x360")
	app.resizable(False, False)

	left_frame = ctk.CTkFrame(app, fg_color="transparent")
	left_frame.pack(side="left", fill="y")
	right_frame = ctk.CTkFrame(app, corner_radius=8, fg_color="gray17")
	right_frame.pack(side="right", fill="y")

	mileage_entry = build_mileage_section(left_frame)
	refresh_history = build_history_section(right_frame)
	refresh_history()

	def	on_predict():
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

	def	on_reset():
		confirm = messagebox.askyesno("Reset", "This will delete your trained model and prediction history.")
		if not confirm:
			return
		reset_files(THETA, PREDICTIONS)
		set_warning("Warning: model not trained yet, prediction will be 0.")
		success_label.configure(text="")
		refresh_history()

	build_predict_button(left_frame, on_predict)
	set_warning, success_label = build_result_section(left_frame)
	build_buttons_section(left_frame, train, on_reset)

	app.mainloop()


if __name__ == "__main__":
	main()