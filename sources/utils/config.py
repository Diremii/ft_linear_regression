# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 15:16:25 by humontas@st       #+#    #+#              #
#    Updated: 2026/07/12 21:00:11 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import sys
import os


if getattr(sys, 'frozen', False):
	_root = os.path.dirname(sys.executable)
else:
	_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(_root, "config.json")) as file:
	_config = json.load(file)

CONFIG = os.path.join(_root, "config.json")
DATA = os.path.join(_root, _config["paths"]["data"])
THETA = os.path.join(_root, _config["paths"]["theta"])
PREDICTIONS = os.path.join(_root, _config["paths"]["predictions"])

LEARNING_RATE = _config["training"]["learning_rate"]
ITERATIONS = _config["training"]["iterations"]
VERBOSE = _config["training"]["verbose"]

POINT_COLOR = _config["plot"]["point_color"]
POINT_MARKER = _config["plot"]["point_marker"]
SHOW_POINTS = _config["plot"]["show_points"]

LINE_COLOR = _config["plot"]["line_color"]
SHOW_LINE = _config["plot"]["show_line"]

SHOW_PREDICTIONS = _config["plot"]["show_predictions"]
PREDICTION_COLOR = _config["plot"]["prediction_color"]
PREDICTION_MARKER = _config["plot"]["prediction_marker"]
