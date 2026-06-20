# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    model.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas@student.42.fr <humontas>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 13:09:30 by humontas@st       #+#    #+#              #
#    Updated: 2026/06/20 13:14:50 by humontas@st      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	estimate_price(mileage: float, theta0: float, theta1: float) -> float:
	return theta0 + theta1 * mileage