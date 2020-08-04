# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
time.sleep(5)
x,y,z=mc.player.getTilePos()

mc.setBlocks(x+11,y-1,z+11,x-11,y-1,z-11,57)

