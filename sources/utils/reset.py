# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reset.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 10:58:07 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/04 14:58:50 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os


def	reset_files(theta_path, predictions_path):
	for path in [theta_path, predictions_path]:
		if os.path.exists(path):
			os.remove(path)