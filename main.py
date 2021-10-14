# create interface with buttons to wakeup computer on LAN

from wakeonlan import send_magic_packet
from tkinter import *

# systems

dadpc1 = {'name':'PC 1','mac_address':'74:27:ea:01:cb:69'}
dadpc2 = {'name':'PC 2','mac_address':'3c:1e:04:ea:a2:2e'}

# tkinter interface
root = Tk()
root.title('WOL - Multicon')
title_row = Label( root,width=40,text='Multicon WOL' )
title_row.grid( row=0,column=0 )
console_row = Label( root,width=40,text='Select system' )
console_row.grid( row=2,column=1 )

def wake_up(system):
    send_magic_packet(system['mac_address'])
    # tkinter interface
    console_row = Label(root,width=40, text='Waking up \'{}\' at \'{}\' \n'.format(system['name'], system['mac_address']))
    console_row.grid(row=2,column=1,rowspan=2)

# make buttons
button_1 = Button(root,text=' pc 1', padx=60,pady=20,border=10,command=lambda: wake_up(dadpc1))
button_2 = Button(root,text=' pc 2', padx=60,pady=20,border=10,command=lambda: wake_up(dadpc2))

# position objects
button_1.grid(row=2,column=0)
button_2.grid(row=3,column=0)

root.mainloop()
