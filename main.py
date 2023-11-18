import io
from math import cos, sin, log
import sys
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QFileDialog

# UI для приложения
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>SmartStudy</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>10</y>
      <width>461</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;</string>
    </property>
    <property name="text">
     <string>Приветствую в моём первом приложении!</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>490</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Что оно может?</string>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>Icons/1x/outline_help_outline_white_24dp.png</normaloff>Icons/1x/outline_help_outline_white_24dp.png</iconset>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>210</y>
      <width>171</width>
      <height>121</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Начать</string>
    </property>
    <property name="icon">
     <iconset>
      <normaloff>Icons/1x/outline_play_arrow_white_24dp.png</normaloff>Icons/1x/outline_play_arrow_white_24dp.png</iconset>
    </property>
    <property name="iconSize">
     <size>
      <width>25</width>
      <height>25</height>
     </size>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Главное окно SchoolHelper
template2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>widget</class>
 <widget class="QWidget" name="widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>300</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>300</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>300</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Что оно может?</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>0</y>
     <width>502</width>
     <height>302</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label">
      <property name="minimumSize">
       <size>
        <width>450</width>
        <height>200</height>
       </size>
      </property>
      <property name="maximumSize">
       <size>
        <width>490</width>
        <height>200</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>12</pointsize>
        <kerning>false</kerning>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;</string>
      </property>
      <property name="text">
       <string>    Моё приложение &quot;SmartStudy&quot; - идеальное решение для всех, кто хочет учиться более эффективно и организованно. Это удобное и легкое в использовании приложение, созданное специально для студентов и школьников всех возрастов и уровней образования. Основная цель приложения - помочь пользователям в достижении своих учебных целей. Для этого я предлагаю широкий спектр полезных функций и возможностей. Не получается построить график функции y=x или забыл теорему Пифагора? Тебе сюда!</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <connections/>
</ui>
"""  # Что может SchoolHelper
template3 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>widget</class>
 <widget class="QMainWindow" name="widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>470</width>
    <height>250</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>470</width>
    <height>250</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>470</width>
    <height>250</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Меню</string>
  </property>
  <property name="windowIcon">
   <iconset resource="../../SmartStudy/Icons.qrc">
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Калькулятор</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>20</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Калькулятор 
 оценок</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>20</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Теоремы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Построение 
 графиков</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>120</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Формулы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>120</y>
      <width>130</width>
      <height>80</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>130</width>
      <height>80</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Oxanium</family>
      <pointsize>8</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
    </property>
    <property name="text">
     <string>Вычислить 
 корни квадратного 
 уравнения</string>
    </property>
    <property name="checkable">
     <bool>false</bool>
    </property>
    <property name="checked">
     <bool>false</bool>
    </property>
    <property name="autoRepeat">
     <bool>false</bool>
    </property>
    <property name="autoExclusive">
     <bool>false</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>470</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Меню SchoolHelper
template_calculator = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>290</width>
    <height>395</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>290</width>
    <height>395</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777215</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Калькулятор</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="0">
     <widget class="QPushButton" name="btn_4">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>4</string>
      </property>
     </widget>
    </item>
    <item row="2" column="2">
     <widget class="QPushButton" name="btn_6">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>6</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QPushButton" name="btn_5">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>5</string>
      </property>
     </widget>
    </item>
    <item row="1" column="2">
     <widget class="QPushButton" name="btn_3">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>3</string>
      </property>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QPushButton" name="btn_1">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>1</string>
      </property>
      <property name="flat">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QPushButton" name="btn_7">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>7</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QPushButton" name="btn_8">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>8</string>
      </property>
     </widget>
    </item>
    <item row="3" column="2">
     <widget class="QPushButton" name="btn_9">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>9</string>
      </property>
     </widget>
    </item>
    <item row="3" column="3">
     <widget class="QPushButton" name="btn_minus">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="tabletTracking">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>-</string>
      </property>
      <property name="autoDefault">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="4" column="0">
     <widget class="QPushButton" name="btn_clear">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: #1D2024;
color: #0FFB7E;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>C</string>
      </property>
      <property name="autoDefault">
       <bool>false</bool>
      </property>
      <property name="default">
       <bool>false</bool>
      </property>
      <property name="flat">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="4" column="3">
     <widget class="QPushButton" name="btn_plus">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="tabletTracking">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>+</string>
      </property>
      <property name="autoDefault">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="2" column="3">
     <widget class="QPushButton" name="btn_mul">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="tabletTracking">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>×</string>
      </property>
      <property name="autoDefault">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="1" column="3">
     <widget class="QPushButton" name="btn_div">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="tabletTracking">
       <bool>false</bool>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>÷</string>
      </property>
      <property name="autoDefault">
       <bool>false</bool>
      </property>
     </widget>
    </item>
    <item row="4" column="1">
     <widget class="QPushButton" name="btn_0">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>0</string>
      </property>
     </widget>
    </item>
    <item row="4" column="2">
     <widget class="QPushButton" name="btn_eq">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: #1D2024;
color: #0FFB7E;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>=</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QPushButton" name="btn_2">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>64</width>
        <height>64</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>2</string>
      </property>
     </widget>
    </item>
    <item row="0" column="0" colspan="4">
     <widget class="QLineEdit" name="table">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>75</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">border: none;
color: #F1F1F1;
font-size: 50px</string>
      </property>
      <property name="text">
       <string>0</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
      </property>
      <property name="readOnly">
       <bool>true</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Калькулятор
template_calc_of_marks = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>270</width>
    <height>270</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>270</width>
    <height>270</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>270</width>
    <height>270</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Калькулятор оценок</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0" colspan="3">
     <widget class="QLineEdit" name="lineEdit">
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">border: none;
color: #F1F1F1;</string>
      </property>
      <property name="readOnly">
       <bool>true</bool>
      </property>
      <property name="placeholderText">
       <string>Оценочки</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QPushButton" name="btn_2">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>2</string>
      </property>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QPushButton" name="btn_4">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>4</string>
      </property>
     </widget>
    </item>
    <item row="2" column="2">
     <widget class="QPushButton" name="btn_3">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>3</string>
      </property>
     </widget>
    </item>
    <item row="3" column="2">
     <widget class="QPushButton" name="btn_res">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>Результат</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_done_white_24dp.png</normaloff>Icons/1x/outline_done_white_24dp.png</iconset>
      </property>
      <property name="iconSize">
       <size>
        <width>12</width>
        <height>12</height>
       </size>
      </property>
     </widget>
    </item>
    <item row="4" column="0" colspan="3">
     <widget class="QPushButton" name="btn_clear">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>Очистить всё</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_backspace_white_24dp.png</normaloff>Icons/1x/outline_backspace_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QPushButton" name="btn_5">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>5</string>
      </property>
     </widget>
    </item>
    <item row="2" column="0">
     <widget class="QPushButton" name="btn_1">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>1</string>
      </property>
     </widget>
    </item>
    <item row="1" column="0" colspan="3">
     <widget class="QLineEdit" name="table">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>75</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
        <pointsize>40</pointsize>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">border: none;
color: #F1F1F1;</string>
      </property>
      <property name="text">
       <string>0</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
      </property>
      <property name="readOnly">
       <bool>true</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>270</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Калькулятор оценок
template_roots = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="windowModality">
   <enum>Qt::WindowModal</enum>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>460</width>
    <height>270</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>460</width>
    <height>270</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>460</width>
    <height>270</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Вычислить корни квадратного уравнения</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0" colspan="3">
     <layout class="QVBoxLayout" name="verticalLayout_4">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <layout class="QVBoxLayout" name="verticalLayout">
          <item>
           <widget class="QLineEdit" name="line_a">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Введите коэффициент &quot;a&quot;</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_2">
          <item>
           <widget class="QLineEdit" name="line_b">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Введите коэффициент &quot;b&quot;</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_3">
          <item>
           <widget class="QLineEdit" name="line_c">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Введите коэффициент &quot;c&quot;</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label_D">
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;</string>
      </property>
      <property name="text">
       <string>Дискриминант равен:</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QLineEdit" name="line_D">
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
      </property>
      <property name="readOnly">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="1" column="2">
     <widget class="QPushButton" name="btn_roots">
      <property name="minimumSize">
       <size>
        <width>200</width>
        <height>20</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
      </property>
      <property name="text">
       <string>Вычислить корни и дискриминант</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_done_white_24dp.png</normaloff>Icons/1x/outline_done_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
    <item row="2" column="0" colspan="3">
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QLabel" name="label_r1">
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;</string>
        </property>
        <property name="text">
         <string>Корень 1:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="line_r1">
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
        <property name="placeholderText">
         <string/>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_r2">
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;</string>
        </property>
        <property name="text">
         <string>Корень 2:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="line_r2">
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item row="3" column="0" colspan="3">
     <widget class="QPushButton" name="btn_clear">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>26</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Oxanium</family>
       </font>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>Очистить всё</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_backspace_white_24dp.png</normaloff>Icons/1x/outline_backspace_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Вычислитель корней
template_of_theoremes = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>792</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>790</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777215</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Теоремы</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

QMessageBox QLabel {
    color: #F1F1F1;
}

QMessageBox QPushButton{
height: 20px;
width: 40px;
color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
}
</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="1">
     <layout class="QVBoxLayout" name="verticalLayout_5">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_5">
        <item>
         <widget class="QLabel" name="label_2">
          <property name="font">
           <font>
            <family>Oxanium</family>
           </font>
          </property>
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;</string>
          </property>
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Добавить теорему&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_6">
          <item>
           <widget class="QLineEdit" name="line_name">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Название</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_7">
          <item>
           <widget class="QLineEdit" name="line_theorem">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Теорема</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_11">
          <item>
           <widget class="QLineEdit" name="line_subj">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Предмет</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QPushButton" name="btn_add">
          <property name="minimumSize">
           <size>
            <width>75</width>
            <height>20</height>
           </size>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
          </property>
          <property name="text">
           <string>Добавить</string>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>Icons/1x/outline_add_white_24dp.png</normaloff>Icons/1x/outline_add_white_24dp.png</iconset>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item row="5" column="1">
     <widget class="QTableWidget" name="tableWidget">
      <property name="styleSheet">
       <string notr="true">background-color: #3a3d41;
color: #F1F1F1;
border: none;
border-radius: 3px</string>
      </property>
      <property name="rowCount">
       <number>0</number>
      </property>
      <property name="columnCount">
       <number>0</number>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QLineEdit" name="line_search">
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
          </property>
          <property name="placeholderText">
           <string>Введите название</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QPushButton" name="btn_search">
        <property name="minimumSize">
         <size>
          <width>60</width>
          <height>20</height>
         </size>
        </property>
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
        </property>
        <property name="text">
         <string>Поиск</string>
        </property>
        <property name="icon">
         <iconset>
          <normaloff>Icons/1x/outline_search_white_24dp.png</normaloff>Icons/1x/outline_search_white_24dp.png</iconset>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_5">
        <property name="font">
         <font>
          <family>Oxanium</family>
          <weight>50</weight>
          <bold>false</bold>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;</string>
        </property>
        <property name="text">
         <string>Фильтр по предмету</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QComboBox" name="combo_filtr">
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">background-color: #3a3d41;
border-radius: 3px;
color: #F1F1F1;</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item row="4" column="1">
     <widget class="QPushButton" name="btn_save">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>20</height>
       </size>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border-color: #1F2F34;
border-radius: 3px;
</string>
      </property>
      <property name="text">
       <string>Сохранить результат добавления или изменения</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_save_white_24dp.png</normaloff>Icons/1x/outline_save_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLineEdit" name="line_del">
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>16777215</height>
         </size>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
        </property>
        <property name="placeholderText">
         <string>Введите id</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="btn_del">
        <property name="minimumSize">
         <size>
          <width>143</width>
          <height>20</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>16777215</height>
         </size>
        </property>
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
        </property>
        <property name="text">
         <string>Удалить теорему по id</string>
        </property>
        <property name="icon">
         <iconset>
          <normaloff>Icons/1x/outline_delete_white_24dp.png</normaloff>Icons/1x/outline_delete_white_24dp.png</iconset>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""  # БД с теоремами
template_of_formuls = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>792</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>790</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777215</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Формулы</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

QMessageBox QLabel {
    color: #F1F1F1;
}

QMessageBox QPushButton{
height: 20px;
width: 40px;
color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
}
</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="1">
     <layout class="QVBoxLayout" name="verticalLayout_5">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_5">
        <item>
         <widget class="QLabel" name="label_2">
          <property name="font">
           <font>
            <family>Oxanium</family>
           </font>
          </property>
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;</string>
          </property>
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Добавить формулу&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_6">
          <item>
           <widget class="QLineEdit" name="line_name">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Название</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_7">
          <item>
           <widget class="QLineEdit" name="line_theorem">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Формула</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_11">
          <item>
           <widget class="QLineEdit" name="line_subj">
            <property name="styleSheet">
             <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
            </property>
            <property name="placeholderText">
             <string>Предмет</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QPushButton" name="btn_add">
          <property name="minimumSize">
           <size>
            <width>75</width>
            <height>20</height>
           </size>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
          </property>
          <property name="text">
           <string>Добавить</string>
          </property>
          <property name="icon">
           <iconset>
            <normaloff>Icons/1x/outline_add_white_24dp.png</normaloff>Icons/1x/outline_add_white_24dp.png</iconset>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item row="5" column="1">
     <widget class="QTableWidget" name="tableWidget">
      <property name="styleSheet">
       <string notr="true">background-color: #3a3d41;
color: #F1F1F1;
border: none;
border-radius: 3px</string>
      </property>
      <property name="rowCount">
       <number>0</number>
      </property>
      <property name="columnCount">
       <number>0</number>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QLineEdit" name="line_search">
          <property name="styleSheet">
           <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
          </property>
          <property name="placeholderText">
           <string>Введите название</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QPushButton" name="btn_search">
        <property name="minimumSize">
         <size>
          <width>60</width>
          <height>20</height>
         </size>
        </property>
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
        </property>
        <property name="text">
         <string>Поиск</string>
        </property>
        <property name="icon">
         <iconset>
          <normaloff>Icons/1x/outline_search_white_24dp.png</normaloff>Icons/1x/outline_search_white_24dp.png</iconset>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_5">
        <property name="font">
         <font>
          <family>Oxanium</family>
          <weight>50</weight>
          <bold>false</bold>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;</string>
        </property>
        <property name="text">
         <string>Фильтр по предмету</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QComboBox" name="combo_filtr">
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">background-color: #3a3d41;
border-radius: 3px;
color: #F1F1F1;</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item row="4" column="1">
     <widget class="QPushButton" name="btn_save">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>20</height>
       </size>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border-color: #1F2F34;
border-radius: 3px;
</string>
      </property>
      <property name="text">
       <string>Сохранить результат добавления или изменения</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_save_white_24dp.png</normaloff>Icons/1x/outline_save_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLineEdit" name="line_del">
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>16777215</height>
         </size>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
        </property>
        <property name="placeholderText">
         <string>Введите id</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="btn_del">
        <property name="minimumSize">
         <size>
          <width>143</width>
          <height>20</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>16777215</height>
         </size>
        </property>
        <property name="cursor">
         <cursorShape>PointingHandCursor</cursorShape>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #F1F1F1;
background-color: #3a3d41;
border-color: #1F2F34;
border-radius: 3px;
</string>
        </property>
        <property name="text">
         <string>Удалить формулу по id</string>
        </property>
        <property name="icon">
         <iconset>
          <normaloff>Icons/1x/outline_delete_white_24dp.png</normaloff>Icons/1x/outline_delete_white_24dp.png</iconset>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""  # БД с формулами
template_of_graphs = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>417</width>
    <height>240</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>0</width>
    <height>0</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Построение графиков</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>Icons/1x/outline_import_contacts_black_24dp.png</normaloff>Icons/1x/outline_import_contacts_black_24dp.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
    background-color: #171A1E;
	font-family: Oxanium;
}

</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="3">
     <widget class="QPushButton" name="pushButton">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>20</height>
       </size>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1D2024;
border: none;
border-radius: 5px;</string>
      </property>
      <property name="text">
       <string>Построить</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_architecture_white_24dp.png</normaloff>Icons/1x/outline_architecture_white_24dp.png</iconset>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLineEdit" name="lineEdit">
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
border: 2px solid #3a3d41;
border-radius: 3px</string>
      </property>
      <property name="placeholderText">
       <string>Введите функцию типа y=x</string>
      </property>
     </widget>
    </item>
    <item row="1" column="3">
     <widget class="QPushButton" name="btn_open">
      <property name="minimumSize">
       <size>
        <width>170</width>
        <height>30</height>
       </size>
      </property>
      <property name="cursor">
       <cursorShape>PointingHandCursor</cursorShape>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #F1F1F1;
background-color: #1F2F34;
border: none;
border-radius: 5px;
display: flex;
align-items: center;
text-align: center;
</string>
      </property>
      <property name="text">
       <string>    Открыть прошлую 
 сохранённую функцию</string>
      </property>
      <property name="icon">
       <iconset>
        <normaloff>Icons/1x/outline_folder_open_white_24dp.png</normaloff>Icons/1x/outline_folder_open_white_24dp.png</iconset>
      </property>
      <property name="iconSize">
       <size>
        <width>20</width>
        <height>20</height>
       </size>
      </property>
     </widget>
    </item>
    <item row="1" column="0" colspan="2">
     <widget class="QLabel" name="label_img">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="../../SmartStudy/Icons.qrc"/>
 </resources>
 <connections/>
</ui>
"""  # Построение графиков


# Backend для приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template)
        uic.loadUi(f, self)

    def init(self):
        self.pushButton.clicked.connect(self.run_btn)
        self.pushButton_2.clicked.connect(self.run_btn2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.run_btn2()

    def run_btn(self):
        self.w = AboutUs()
        self.w.show()

    def run_btn2(self):
        self.w = MenuWindow()
        self.w.show()
        self.hide()


class AboutUs(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f2 = io.StringIO(template2)
        uic.loadUi(f2, self)


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f3 = io.StringIO(template3)
        uic.loadUi(f3, self)

    def init(self):
        self.pushButton.clicked.connect(self.run_btn1)
        self.pushButton_2.clicked.connect(self.run_btn2)
        self.pushButton_3.clicked.connect(self.run_btn3)
        self.pushButton_4.clicked.connect(self.run_btn4)
        self.pushButton_5.clicked.connect(self.run_btn5)
        self.pushButton_6.clicked.connect(self.run_btn6)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.run_btn1()
        elif event.key() == Qt.Key_2:
            self.run_btn2()
        elif event.key() == Qt.Key_3:
            self.run_btn3()
        elif event.key() == Qt.Key_4:
            self.run_btn4()
        elif event.key() == Qt.Key_5:
            self.run_btn5()
        elif event.key() == Qt.Key_6:
            self.run_btn6()

    def run_btn1(self):
        self.w = Calculator()
        self.w.show()

    def run_btn2(self):
        self.w = CalculatorOfMarks()
        self.w.show()

    def run_btn3(self):
        self.w = Theoremes()
        self.w.show()

    def run_btn4(self):
        self.w = Graphs()
        self.w.show()

    def run_btn5(self):
        self.w = Formuls()
        self.w.show()

    def run_btn6(self):
        self.w = Roots()
        self.w.show()


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_calculator)
        uic.loadUi(f, self)

    def init(self):
        self.doing = ''
        self.num1 = ''
        self.num2 = ''
        self.is_num2 = False
        self.btn_0.clicked.connect(lambda: self.psh_btn_num('0'))
        self.btn_1.clicked.connect(lambda: self.psh_btn_num('1'))
        self.btn_2.clicked.connect(lambda: self.psh_btn_num('2'))
        self.btn_3.clicked.connect(lambda: self.psh_btn_num('3'))
        self.btn_4.clicked.connect(lambda: self.psh_btn_num('4'))
        self.btn_5.clicked.connect(lambda: self.psh_btn_num('5'))
        self.btn_6.clicked.connect(lambda: self.psh_btn_num('6'))
        self.btn_7.clicked.connect(lambda: self.psh_btn_num('7'))
        self.btn_8.clicked.connect(lambda: self.psh_btn_num('8'))
        self.btn_9.clicked.connect(lambda: self.psh_btn_num('9'))
        self.btn_plus.clicked.connect(lambda: self.psh_doing('+'))
        self.btn_minus.clicked.connect(lambda: self.psh_doing('-'))
        self.btn_div.clicked.connect(lambda: self.psh_doing('/'))
        self.btn_mul.clicked.connect(lambda: self.psh_doing('*'))
        self.btn_eq.clicked.connect(self.psh_eq)
        self.btn_clear.clicked.connect(self.psh_clear)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.btn_0.click()
        elif event.key() == Qt.Key_1:
            self.btn_1.click()
        elif event.key() == Qt.Key_2:
            self.btn_2.click()
        elif event.key() == Qt.Key_3:
            self.btn_3.click()
        elif event.key() == Qt.Key_4:
            self.btn_4.click()
        elif event.key() == Qt.Key_5:
            self.btn_5.click()
        elif event.key() == Qt.Key_6:
            self.btn_6.click()
        elif event.key() == Qt.Key_7:
            self.btn_7.click()
        elif event.key() == Qt.Key_8:
            self.btn_8.click()
        elif event.key() == Qt.Key_9:
            self.btn_9.click()
        elif event.key() == Qt.Key_Minus:
            self.btn_minus.click()
        elif event.key() == Qt.Key_Plus:
            self.btn_plus.click()
        elif event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_eq.click()
        elif event.key() == Qt.Key_C or event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def psh_btn_num(self, btn_text):
        global is_num2
        if not self.is_num2:
            if self.table.text() == '0' or self.table.text() == 'Error' or self.table.text() == 'None':
                self.table.setText(btn_text)
            else:
                self.table.setText(self.table.text() + btn_text)
        else:
            self.is_num2 = False
            self.table.setText('' + btn_text)

    def psh_doing(self, btn_text):
        global doing
        global num1
        global is_num2
        self.doing = ''
        self.num1 = self.table.text()
        self.is_num2 = True
        self.doing += btn_text

    def psh_eq(self):
        global is_num2
        global doing
        global num1
        global num2
        self.num2 += self.table.text()
        if self.num2 == '0' and self.doing == '/':
            self.table.setText('Error')
        else:
            self.table.setText(str(eval(f'{self.num1} {self.doing} {self.num2}')))
        self.num2 = ''
        self.num1 = ''
        self.doing = ''
        self.is_num2 = False

    def psh_clear(self):
        global is_num2
        global doing
        global num1
        global num2
        self.num2 = ''
        self.num1 = ''
        self.doing = ''
        self.is_num2 = False
        self.table.setText('0')


class CalculatorOfMarks(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_calc_of_marks)
        uic.loadUi(f, self)

    def init(self):
        self.marks = []
        self.btn_1.clicked.connect(lambda: self.add_mark('1'))
        self.btn_2.clicked.connect(lambda: self.add_mark('2'))
        self.btn_3.clicked.connect(lambda: self.add_mark('3'))
        self.btn_4.clicked.connect(lambda: self.add_mark('4'))
        self.btn_5.clicked.connect(lambda: self.add_mark('5'))
        self.btn_res.clicked.connect(self.psh_res)
        self.btn_clear.clicked.connect(self.psh_clear)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.btn_1.click()
        elif event.key() == Qt.Key_2:
            self.btn_2.click()
        elif event.key() == Qt.Key_3:
            self.btn_3.click()
        elif event.key() == Qt.Key_4:
            self.btn_4.click()
        elif event.key() == Qt.Key_5:
            self.btn_5.click()
        elif event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_res.click()
        elif event.key() == Qt.Key_C:
            self.btn_clear.click()
        elif event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def add_mark(self, mark):
        global marks
        self.marks.append(int(mark))
        if not self.lineEdit.text():
            self.lineEdit.setText(mark)
        else:
            self.lineEdit.setText(self.lineEdit.text() + ',' + ' ' + mark)

    def psh_res(self):
        global marks
        if not self.lineEdit.text():
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Введите хотя бы одну оценку!")
            msg_box.exec()
        else:
            self.table.setText(str(round((sum(self.marks) / len(self.marks)), ndigits=2)))

    def psh_clear(self):
        global marks
        self.marks = []
        self.table.setText('0')
        self.lineEdit.setText('')


class Roots(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_roots)
        uic.loadUi(f, self)

    def init(self):
        self.btn_roots.clicked.connect(self.psh_res)
        self.btn_clear.clicked.connect(self.btn_clean)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_roots.click()
        elif event.key() == Qt.Key_C or event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def btn_clean(self):
        self.set_text()

    def psh_res(self):
        self.zeros()
        self.a, self.b, self.c = self.checking_float()
        self.num_a, self.num_b, self.num_c = self.line_a.text(), self.line_b.text(), self.line_c.text()
        if not self.num_a or not self.num_b or not self.num_c:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Введите все значения!")
            msg_box.exec()
        elif self.checking_alphas():
            self.set_text()
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Программа принимает только числа!")
            msg_box.exec()
        elif self.a == True or self.b == True or self.c == True:
            self.set_text()
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Программа принимает только целые числа!")
            msg_box.exec()
        else:
            if self.num_a == '0' or self.num_b == '0' or self.num_c == '0':
                if self.num_a == '0' and self.num_b == '0' and int(self.num_c) != 0:
                    self.set_text()
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle('Ошибка')
                    msg_box.setText(f"К сожалению {self.num_c} не равно 0")
                    msg_box.exec()
                elif (self.num_a[0] == '0' and self.num_b[0] == '0' and self.num_c[0] == '0'):
                    self.set_text()
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle('Ошибка')
                    msg_box.setText("Не делай так больше!")
                    msg_box.exec()
                elif self.num_b == '0' and self.num_c == '0':
                    self.line_D.setText('Один корень')
                    self.line_r1.setText('0')
                    self.line_r2.setText('0')
                elif self.num_a == '0':
                    self.line_D.setText('Один корень')
                    if self.num_c == '0':
                        self.line_r1.setText('0')
                        self.line_r2.setText('0')
                    else:
                        self.line_r1.setText(str((int(self.num_c) / int(self.num_b)) * -1))
                        self.line_r2.setText(str((int(self.num_c) / int(self.num_b)) * -1))
                elif self.num_b == '0':
                    self.line_D.setText('2 корня')
                    self.line_r1.setText(str((((int(self.num_c) / int(self.num_a)) * -1) ** 0.5) * -1))
                    self.line_r2.setText(str(((int(self.num_c) / int(self.num_a)) * -1) ** 0.5))
                elif self.num_c == '0':
                    self.line_D.setText('2 корня')
                    self.line_r1.setText(str((int(self.num_b) / int(self.num_a)) * -1))
                    self.line_r2.setText('0')
            else:
                self.line_D.setText(
                    str(int(self.num_b) ** 2 + (-4 * int(self.num_a) * int(self.num_c))))
                if int(self.line_D.text()) < 0:
                    self.line_r1.setText('Нет корней')
                    self.line_r2.setText('Нет корней')
                elif int(self.line_D.text()) == 0:
                    self.line_r1.setText(
                        str(round((((-1 * int(self.num_b)) - int(self.line_D.text())) / (
                                2 * int(self.num_a))), ndigits=4)))
                    self.line_r2.setText(
                        str(round((((-1 * int(self.num_b)) - int(self.line_D.text())) / (
                                2 * int(self.num_a))), ndigits=4)))
                else:
                    self.line_r1.setText(
                        str(round((((-1 * int(self.num_b)) - int(self.line_D.text())) / (
                                2 * int(self.num_a))), ndigits=4)))
                    self.line_r2.setText(
                        str(round((((-1 * int(self.num_b)) + int(self.line_D.text())) / (
                                2 * int(self.num_a))), ndigits=4)))

    def set_text(self):
        self.line_a.setText('')
        self.line_b.setText('')
        self.line_c.setText('')
        self.line_D.setText('')
        self.line_r1.setText('')
        self.line_r2.setText('')

    def zeros(self):
        for i, data in enumerate([self.line_a.text(), self.line_b.text(), self.line_c.text()]):
            if data and data.isdigit():
                if float(data) == 0.0:
                    if i == 0:
                        self.line_a.setText('0')
                    elif i == 1:
                        self.line_b.setText('0')
                    elif i == 2:
                        self.line_c.setText('0')
                elif data == '-0':
                    if i == 0:
                        self.line_a.setText('0')
                    elif i == 1:
                        self.line_b.setText('0')
                    elif i == 2:
                        self.line_c.setText('0')
                elif len(set(data)) == 1:
                    if list(set(data))[0] == '0':
                        if i == 0:
                            self.line_a.setText('0')
                        elif i == 1:
                            self.line_b.setText('0')
                        elif i == 2:
                            self.line_c.setText('0')

    def checking_alphas(self):
        for i in self.line_a.text(), self.line_b.text(), self.line_c.text():
            for j in i:
                if not j.isdigit():
                    return True

    def checking_float(self):
        self.a_is_float = False
        self.b_is_float = False
        self.c_is_float = False
        for i, data in enumerate([self.line_a.text(), self.line_b.text(), self.line_c.text()]):
            if '.' in data:
                if data[1] == '.':
                    if i == 0:
                        self.a_is_float = True
                    elif i == 1:
                        self.b_is_float = True
                    elif i == 2:
                        self.c_is_float = True
        return self.a_is_float, self.b_is_float, self.c_is_float


class Theoremes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_theoremes)
        uic.loadUi(f, self)

    def init(self):
        self.con = sqlite3.connect('DataBaseOfApp.db')
        cur = self.con.cursor()
        self.combo_filtr.addItems(
            [i[0] for i in cur.execute("SELECT DISTINCT Предмет FROM Теоремы").fetchall() if i[0] != 'Нет'])
        self.combo_filtr.addItem('Нет')
        self.btn_search.clicked.connect(self.psh_search)
        self.btn_add.clicked.connect(
            lambda: self.psh_add(self.line_name.text(), self.line_theorem.text(), self.line_subj.text()))
        self.btn_save.clicked.connect(self.psh_save)
        self.btn_del.clicked.connect(self.psh_del)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.btn_search.click()

    def psh_search(self):
        cur = self.con.cursor()
        if self.combo_filtr.currentText() == 'Нет':
            if self.line_search.text():
                res = cur.execute(
                    f'''SELECT id, Название, Теорема FROM Теоремы WHERE Название = '{self.line_search.text()}' ''').fetchall()
            else:
                res = cur.execute(
                    f'''SELECT id, Название, Теорема FROM Теоремы''').fetchall()
        else:
            if self.line_search.text():
                res = cur.execute(
                    f'''SELECT id, Название, Теорема FROM Теоремы WHERE Название = '{self.line_search.text()}' AND Предмет = '{str(self.combo_filtr.currentText())}' ''').fetchall()
            else:
                res = cur.execute(
                    f'''SELECT id, Название, Теорема FROM Теоремы WHERE Предмет = '{str(self.combo_filtr.currentText())}' ''').fetchall()
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            for i, elem in enumerate(res):
                for j, vol in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(vol)))
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Ничего не найдено! Попробуйте снова.")
            msg_box.exec()

    def psh_add(self, name, theorem, subject):
        if not self.line_name.text():
            name = 'Теорема'
        if not self.line_theorem.text():
            theorem = 'Не добавлено'
        if not self.line_subj.text():
            subject = 'Нет'
        valid = QMessageBox.question(
            self, '', f"Действительно добавить элемент {str(name)}?",
            QMessageBox.Yes, QMessageBox.No)
        cur = self.con.cursor()
        if valid == QMessageBox.Yes:
            cur.execute(
                f'''INSERT INTO Теоремы (Название, Теорема, Предмет) VALUES ('{str(name)}', '{str(theorem)}', '{str(subject)}')''')

    def psh_save(self):
        cur = self.con.cursor()
        self.con.commit()

    def psh_del(self):
        cur = self.con.cursor()
        ids = cur.execute(f"""SELECT id FROM Теоремы""").fetchall()
        ids = [str(i)[1:-2] for i in ids]
        if not self.line_del.text().isdigit():
            self.line_del.setText('')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("id это число")
            msg_box.exec()
        elif self.line_del.text() not in ids:
            self.line_del.setText('')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Такого id нет!")
            msg_box.exec()
        elif self.line_del.text():
            name = cur.execute(
                f"""SELECT DISTINCT Название FROM Теоремы WHERE id={int(self.line_del.text())}""").fetchall()
            valid = QMessageBox.question(
                self, '', f"Действительно удалить элемент {name[:][0][0][:]}?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur.execute(
                    f'''DELETE FROM Теоремы WHERE id = {int(self.line_del.text())}''')


class Formuls(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_formuls)
        uic.loadUi(f, self)

    def init(self):
        self.con = sqlite3.connect('DataBaseOfApp.db')
        cur = self.con.cursor()
        self.combo_filtr.addItems(
            [i[0] for i in cur.execute("SELECT DISTINCT Предмет FROM Формулы").fetchall() if i[0] != 'Нет'])
        self.combo_filtr.addItem('Нет')
        self.btn_search.clicked.connect(self.psh_search)
        self.btn_add.clicked.connect(
            lambda: self.psh_add(self.line_name.text(), self.line_theorem.text(), self.line_subj.text()))
        self.btn_save.clicked.connect(self.psh_save)
        self.btn_del.clicked.connect(self.psh_del)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.btn_search.click()

    def psh_search(self):
        cur = self.con.cursor()
        if self.combo_filtr.currentText() == 'Нет':
            if self.line_search.text():
                res = cur.execute(
                    f'''SELECT id, Название, Формула FROM Формулы WHERE Название = '{self.line_search.text()}' ''').fetchall()
            else:
                res = cur.execute(
                    f'''SELECT id, Название, Формула FROM Формулы''').fetchall()
        else:
            if self.line_search.text():
                res = cur.execute(
                    f'''SELECT id, Название, Формула FROM Формулы WHERE Название = '{self.line_search.text()}' AND Предмет = '{str(self.combo_filtr.currentText())}' ''').fetchall()
            else:
                res = cur.execute(
                    f'''SELECT id, Название, Формула FROM Формулы WHERE Предмет = '{str(self.combo_filtr.currentText())}' ''').fetchall()
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            for i, elem in enumerate(res):
                for j, vol in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(vol)))
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Ничего не найдено! Попробуйте снова.")
            msg_box.exec()

    def psh_add(self, name, formul, subject):
        if not self.line_name.text():
            name = 'Формула'
        if not self.line_theorem.text():
            formul = 'Не добавлено'
        if not self.line_subj.text():
            subject = 'Нет'
        valid = QMessageBox.question(
            self, '', f"Действительно добавить элемент {str(name)}?",
            QMessageBox.Yes, QMessageBox.No)
        cur = self.con.cursor()
        if valid == QMessageBox.Yes:
            cur.execute(
                f'''INSERT INTO Формулы (Название, Формула, Предмет) VALUES ('{str(name)}', '{str(formul)}', '{str(subject)}')''')

    def psh_save(self):
        cur = self.con.cursor()
        self.con.commit()

    def psh_del(self):
        cur = self.con.cursor()
        ids = cur.execute(f"""SELECT id FROM Формулы""").fetchall()
        ids = [str(i)[1:-2] for i in ids]
        if not self.line_del.text().isdigit():
            self.line_del.setText('')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("id это число")
            msg_box.exec()
        elif self.line_del.text() not in ids:
            self.line_del.setText('')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Такого id нет!")
            msg_box.exec()
        elif self.line_del.text():
            name = cur.execute(
                f"""SELECT DISTINCT Название FROM Формулы WHERE id={int(self.line_del.text())}""").fetchall()
            valid = QMessageBox.question(
                self, '', f"Действительно удалить элемент {name[:][0][0][:]}?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur.execute(
                    f'''DELETE FROM Формулы WHERE id = {int(self.line_del.text())}''')


class Graphs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_graphs)
        uic.loadUi(f, self)

    def init(self):
        self.pushButton.clicked.connect(self.do_graph)
        self.btn_open.clicked.connect(self.btn_op)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.pushButton.click()

    def do_graph(self):
        doing = self.normal_function(self.lineEdit.text())
        if not 'x' in doing:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Ошибка')
            msg_box.setText("Введите функцию типа y = x!")
            msg_box.exec()
        else:
            if self.lineEdit.text():
                fig, ax = plt.subplots()
                ax.set_title(f'График {self.lineEdit.text()}')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.grid()
                x = np.linspace(-100, 100, 1000)
                flag = False
                if doing == 'x':
                    y = x
                else:
                    try:
                        y = eval(doing)
                    except NameError:
                        self.lineEdit.setText('')
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle('Ошибка')
                        msg_box.setText("Введите функцию типа y = x!")
                        msg_box.exec()
                    except SyntaxError:
                        self.lineEdit.setText('')
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle('Ошибка')
                        msg_box.setText(
                            "Вводите только математические действия!")
                        msg_box.exec()
                    except ValueError:
                        self.lineEdit.setText('')
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle('Ошибка')
                        msg_box.setText(
                            "Вводите только математические действия!")
                        msg_box.exec()
                    except TypeError:
                        self.lineEdit.setText('')
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle('Ошибка')
                        msg_box.setText(
                            "Не используй log(), sin(), cos() и т.д., пожалуйста, моя программа так пока что не умеет...")
                        msg_box.exec()
                if not flag:
                    ax.plot(x, y)
                    plt.show()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Ошибка')
                msg_box.setText("Сначала введите функцию!")
                msg_box.exec()

    def btn_op(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.png);;Все файлы (*)')[0]
        self.pixmap = QPixmap(fname)
        self.label_img.setPixmap(self.pixmap)

    def normal_function(self, function: str):
        flag = False
        li = []
        for i in function:
            if flag:
                li.append(i)
            if i == '=':
                flag = True
        doing = ''.join(li)
        return doing


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
