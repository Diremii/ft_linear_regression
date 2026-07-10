# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    file_utils.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/10 16:33:29 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/10 16:33:30 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import subprocess
import platform


def open_file(path):
	system = platform.system()

	if system == "Windows":
		os.startfile(path)
	elif system == "Darwin":
		subprocess.run(["open", path])
	else:
		subprocess.run(["xdg-open", path])