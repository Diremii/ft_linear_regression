# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    window.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/10 16:34:52 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/12 21:09:51 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import customtkinter as ctk

from gui.components import (
	build_mileage_section,
	build_predict_button,
	build_result_section,
	build_buttons_section,
	build_history_section
)

from gui.callbacks import (
	on_predict,
	on_train,
	on_reset,
	update_r2
)


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

	set_warning, success_label, r2_label = build_result_section(left_frame)

	update_r2(r2_label)

	build_predict_button(
		left_frame,
		lambda: on_predict(
			mileage_entry,
			success_label,
			set_warning,
			refresh_history
		)
	)

	build_buttons_section(
		left_frame,
		lambda: on_train(set_warning, lambda: update_r2(r2_label)),
		lambda: on_reset(
			set_warning,
			success_label,
			lambda: update_r2(r2_label),
			refresh_history
		)
	)

	app.mainloop()