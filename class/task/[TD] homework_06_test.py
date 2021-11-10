# ver.Nuke
from PySide2.QtWidgets import*
from functools import partial
import nuke

def rename_selected_nodes(new_name):
	# update selection
	selected_list = nuke.selectedNodes()
	get_name = lambda node: node.knob('name').getValue()
	sorted_list = sorted(selected_list, key=get_name)
	
	# rename obj
	cont = 1
	for obj in sorted_list:        
	    obj_name = obj.knob('name').getValue()
	    obj.knob('name').setValue(new_name + '_%03d' % cont)
	    cont += 1

def button_command(name_widget):
    get_name = name_widget.text()
    rename_selected_nodes(get_name)

# main window  
window = QWidget()
window.setWindowTitle('Rename object tool')
main_layout = QVBoxLayout(window)

# widget
obj_name = QLineEdit()
obj_name.setPlaceholderText('set new name...')
button = QPushButton('Raname')
button.clicked.connect(partial(button_command, obj_name))

main_layout.addWidget(obj_name)
main_layout.addWidget(button)

window.show()



test_list = [
	{'name':'a', 'num':1},
	{'name':'b', 'num':3},
	{'name':'c', 'num':2}
]
#f = lambda n: n.get['keys']
obj = sorted(test_list, key=lambda n: n.get('num'))
print(obj)