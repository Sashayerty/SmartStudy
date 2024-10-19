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
"""
