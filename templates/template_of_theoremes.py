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
"""
