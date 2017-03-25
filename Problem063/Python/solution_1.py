#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2017
#
#       @team: DestructHub
#    @project: ProjectEuler
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#


print(len([a ** n
           for a in range(1, 10)
           for n in range(1, 22)
           if len(str(a ** n)) == n]))
