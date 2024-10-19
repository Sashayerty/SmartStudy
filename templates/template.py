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
"""
