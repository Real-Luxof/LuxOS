from ..utilityfolder.blocks import *
import api

plr = api.entity(varname="plr",image="#FFC000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[108, 267],replace=Air,inventory=api.inventory(slotnum=25,slotdata={"slot0": Grass,"slot1": Dirt,"slot2": None,"slot3": None,"slot4": None,"slot5": None,"slot6": None,"slot7": None,"slot8": None,"slot9": None,"slot10": None,"slot11": None,"slot12": None,"slot13": None,"slot14": None,"slot15": None,"slot16": None,"slot17": None,"slot18": None,"slot19": None,"slot20": None,"slot21": None,"slot22": None,"slot23": None},selectedindex="slot1"),dead=False,deffactor=0.5,atkfactor=0.5,reach=1,handvalue=2)
worldtype = [500, api.Limit(25, 495)]