import os
from xlsxwriter import Workbook
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QMessageBox
import sys
from PyQt5 import uic
import pandas as pd
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import ctypes
from openpyxl.workbook import Workbook
from datetime import date
#import images_rc
from ui_windows.ui_newVersion import*
import ui_windows.bcg_image_rc as bcg_image_rc
import ui_windows.icons_rc as icons_rc
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from mpl_point_clicker import clicker
from docxtpl import DocxTemplate
from openpyxl.styles import PatternFill, Border, Side
import time
import Main_Program_PyQt5 as mp 
from Main_Program_PyQt5 import *

class Worker(QObject,mp):

    i=0
    for U1 in mp.SpannungListe:
        mp.spannung=U1
        for motor in mp.MotorenListe:
            mp.MotorName=motor
            vv_values = mp.Daten[mp.MotorName][vv_keys]
            vv_values = vv_values[vv_values!=''].astype(int)
            vv_values = vv_values.to_string(header=False,index=False)
            VV_Updats=list(vv_values.split())
            
            for x in laengeListeDrehzahl:
                mp.Laenge=float(x)
                try:
                    TD_Drehzahl=mp.Daten[mp.MotorName][x]
                    if TD_Drehzahl=='':
                        mp.Drehzahl=500
                    else:
                        mp.Drehzahl=TD_Drehzahl
                except KeyError:
                    mp.Drehzahl=500
        
                except ValueError:
                    mp.Drehzahl=500
                    

                selectedLaenge_pulsdauer=LaengeDic.get(x)
                try:
                    if selectedLaenge_pulsdauer in laengeKeys_pulsdauer==False or selectedLaenge_pulsdauer==None :
                        try:
                            mp.pulsDauer=3
                        except KeyError:
                            mp.pulsDauer=3
                    else:
                        try:
                            TD_Pulsdauer=mp.Daten[mp.MotorName][selectedLaenge_pulsdauer]
                            if TD_Pulsdauer=='' :
                                mp.pulsDauer=3
                            else:
                                mp.pulsDauer=TD_Pulsdauer
                        except KeyError:
                            mp.pulsDauer=3
                except ValueError:
                    mp.pulsDauer=3

                for vv in VV_Updats:
                    mp.TM=float(vv)
                    mp.calculation_function(mp.MotorName,mp.WT,mp.KT,mp.spannung,mp.Laenge,mp.Drehzahl,mp.TM,90.0,20.0,mp.pulsDauer,strom_basisDB)
                    i+=1
                    DataToCalculat_values=[mp.M_N,mp.M_n0,mp.n_N,mp.n_MAX,mp.I_N,mp.I_p,mp.I_n0]
                    #print('cycles= ',i)
                    
                    if mp.TM==1:
                        mp.df.loc[(str(int(mp.MotorLaenge)),'S'),(f'{int(mp.spannung)}V',str(mp.MotorName),np.array(DataToCalculat))]=np.array(DataToCalculat_values)
                    else:
                        mp.df.loc[(str(int(mp.MotorLaenge)),f'{int(mp.TM)}TM'),(f'{int(mp.spannung)}V',str(mp.MotorName),np.array(DataToCalculat))]=np.array(DataToCalculat_values)
                    
                    mp.ui.progressBar.setValue(i)
        if i==572:
            mp.ui.exportBasisdaten_btn.setEnabled(True)
            mp.ui.progressBarLabel.setText('Progress successfully completed')