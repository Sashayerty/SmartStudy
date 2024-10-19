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
"""
