# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

width=10
height=50
length=5

block=57
air=0

mc.setBlocks(x,y,z,x+length,y+height,z+width,block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,air)
