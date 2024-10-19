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
"""
