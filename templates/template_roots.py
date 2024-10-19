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
"""
