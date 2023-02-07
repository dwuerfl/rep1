import sys
from PyQt6.QtWidgets import (
    QApplication,QGridLayout,
    QLabel,QMainWindow,
    QWidget,QLineEdit,
    QPushButton,QMessageBox,)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login-window") #Gibt dem Fenster den Titel "Login-window"
        layout = QGridLayout() #Setzt das Layout des Fensters auf ein Grid Layout
        
        self.input0 = QLineEdit() #Hier werden die 4 Eingabefelder erstellt
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input3 = QLineEdit()
        
        self.input3.setEchoMode(QLineEdit.EchoMode.Password) #Legt den EchoMode für die letzten beiden Zeilen (Passwort Eingabe) fest, sodass nur mehr Punkte Anstelle der Eingabe erscheinen
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        
        layout.addWidget(self.input0,0,1) #Legt die Position der Eingabefelder fest - erste Zahl = Zeile, zweite Zahl = Spalte
        layout.addWidget(self.input1,1,1)
        layout.addWidget(self.input2,2,1)
        layout.addWidget(self.input3,3,1)
        
        layout.addWidget(QLabel("Name"),0,0) #Erstellt die Beschriftungen für die Eingabefelder in Spalte 0, links neben den Eingabefeldern
        layout.addWidget(QLabel("Email"),1,0)
        layout.addWidget(QLabel("Password"),2,0)
        layout.addWidget(QLabel("Password (repeat)"),3,0)
        
        btn1=QPushButton("Login") #Erstellt einen Button mit dem Namen "Login" und weißt diesem die variable btn1 zu
        layout.addWidget(btn1,4,1) #Legt die Position des Buttons fest
        btn1.clicked.connect(self.login) #Legt fest was passiert wenn der Button gedrückt wird. In diesem Fall springt das Programm in die Funktion "login" (Zeile 43)
        btn2=QPushButton("Cancel")  #Erstellt einen Button mit dem Namen "Cancel" und weißt diesem die variable btn2 zu
        layout.addWidget(btn2,4,0) #Legt die Position des Buttons fest
        btn2.clicked.connect(QApplication.instance().quit) #btn.2clicked.connect gibt dem Button eine Funktion, diese steht in der klammer und sorgt dafür, dass das Fenster geschlossen wird
        
        widget = QWidget() #Ein QWidget-Objekt wird erstellt und der Variablen "widget" zugewiesen
        widget.setLayout(layout) #Das als  Argument der Funktion übergebene Layout wird als Layout für das widget-Objekt festgelegt
        self.setCentralWidget(widget) #Das widget-Objekt wird als zentrales Widget für das Hauptfenster festgelegt
        
    def login(self):
           
        if self.input2.text() != self.input3.text(): #Es wird überprüft ob die Eingaben in den beiden Passwortfeldern unterschiedlich sind, ist das der Fall öffnet sich die Messagebox. ".text()" beinhaltet die Eingaben
            dlg = QMessageBox(self) #Erstellt eine Message Box und weißt dieser die Variable dlg zu
            dlg.setIcon(QMessageBox.Icon.Critical) #Legt das Icon in der Messagebox fest
            dlg.setWindowTitle("ERROR") #Gibt der Messagebox einen Titel
            dlg.setText("The Passwords are different") #Bestimmt den Text der in der Messagebox steht
            button = dlg.exec() #startet das Dialogfenster mit einem Button
            button = QMessageBox.StandardButton(button) #legt den Typ des Buttons fest
               
        elif self.input0.text() =='': #Es wird überprüft, ob dieses Feld leer ist, wenn das der Fall ist wird eine MessageBox erzeugt, ansonsten wird in die nächste schleife gesprungen
            dlg = QMessageBox(self) 
            dlg.setWindowTitle("Missing-Input")
            dlg.setText("Please enter a Name")
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()
            button = QMessageBox.StandardButton(button)
                
        elif  self.input1.text() =='': #Es wird überprüft, ob dieses Feld leer ist, wenn das der Fall ist wird eine MessageBox erzeugt, ansonsten wird in die nächste schleife gesprungen
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Missing-Input")
            dlg.setText("Please enter an E-Mail")
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()
            button = QMessageBox.StandardButton(button)
                
        elif  self.input2.text() =='': #Es wird überprüft, ob dieses Feld leer ist, wenn das der Fall ist wird eine MessageBox erzeugt, ansonsten wird in die nächste schleife gesprungen
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Missing-Input")
            dlg.setText("Please enter a password")
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()
            button = QMessageBox.StandardButton(button)
                
        else:
            dlg = QMessageBox(self) #Dieses else wird ausgeführt, wenn keine der Oberen Schleifen zutreffen, hier wird ebenfalls eine Messagebox erzeugt
            dlg.setWindowTitle("Success")
            dlg.setText("You are logged in!")
            dlg.setIcon(QMessageBox.Icon.Information)
            button = dlg.exec()
            button = QMessageBox.StandardButton(button)
                
app = QApplication(sys.argv) #Hier wird eine Instanz von QApplication erzeugt, wo sys.argv übergeben wird
window = MainWindow() #Führt MainWindow aus 
window.show() #Sorgt dafür dass das MainWindow angezeigt wird
app.exec() #Startet die event loop mit allen Inhalten der GUI