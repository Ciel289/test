from tkinter import *
from tkinter import ttk, messagebox # messagebox คือpop up ที่จะเด้งขึ้นมา
import csv
from datetime import datetime


GUI = Tk()
GUI.title('test byHIN v.1.0')
GUI.geometry('900x600+50+0')


############### MENU #########################


menubar=Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0) # tearoff=0 เป็นการปิดระบบที่สามาถดึงเมนูมาไว้ส่วนนไหนของจอก็ได้
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export CSV')

# help
HP1 = 'How to use'
def About():
	messagebox.showinfo('About','วิธีใช้งานนั้นไม่ยากเลย เพียงแค่ท่าน....')

Hepp = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=Hepp)
Hepp.add_command(label=HP1,command=About)


# donate
def DNTW():
	messagebox.showinfo('TrueWallet','เบอร์ 098-3477-461')
def DNSCB():
	messagebox.showinfo('SCB','เลขบัญชี 123-456-789')

Donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donat',menu=Donatemenu)
Donatemenu.add_command(label='TrueWallet',command=DNTW)
Donatemenu.add_command(label='SCB',command=DNSCB)


#########################################


Tab = ttk.Notebook(GUI) # notebook มาจาก ttk อยู่แล้ว
T1 = Frame(Tab)
T2 = Frame(Tab) # width=400 เป็นการ
Tab.pack(fill=BOTH, expand=1) # pack คืออการเรียงจากด้านบนลงมาด้านล่าง # fill เป็นการขยายให้ติดขอบจอ
# expand มักคู่กับ fill





Tab.add(T1, text=f'{"เพิ่ม":^{30}}') 
Tab.add(T2, text=f'{"ค่าใช้จ่าย":^{30}}')


days = {'Mon':'จันทร์',              
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัส',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}


F1 = Frame(T1)
F1.pack()

Riom = " รวม"


def Save(event=None):
	expense = V_expense.get() # .get() คือดึงมาจาก V_expense = StringVar()
	price = V_price.get()
	numberx = V_numberx.get() # แสดงราคารวมที่จ่ายไป

	
 
	if expense == '':   # ถ้าไม่ใส่ข้อมูลจะไม่โชว์อะไรเลย
		print('No Data')
		messagebox.showwarning('ERROR','กรอกข้อมูลค่าใช้จ่าย')
		return          # เมื่อไม่ใส่แล้วจะไม่มีการเซฟ หรือทำงานต่อไป คือจะไม่ทำในบรรทัดต่อๆไป

	elif price == '':
		messagebox.showwarning('ERROR','กรอกข้อมูลราคา')
		return
	
	elif numberx == '':
		numberx = 1 # เป็นการบอกว่าช่องว่างอันนี้มีค่าเป็น 1 ไม่ใส้่ก็ไม่เป็นไร
	

	total = int(price)*int(numberx)



	try:
		total = int(price)*int(numberx)
		
		
		
		print('expense:{} price:{} number:{}, all:{}'.format(expense,price,numberx,total))
		
		text = 'รายการ:{} ราคา:{} จำนวน:{} '.format(expense,price,numberx,)
		text = text + '\nรวมทั้งสิ้น:{}'.format(total)
		v_result.set(text)
		
		

		#clear ข้อมูลเก่าโดยใช้ .set('')
		V_expense.set('') 
		V_price.set('')
		V_numberx.set('')
		
		today = datetime.now().strftime('%a')
		print(today)
		stamp = datetime.now()
		dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
		transactionid = stamp.strftime('%Y%m%d%H%M%f')
		dt = days[today]+'-'+ dt

		# บันทึกข้อมูลลง csv อย่าลืม import csv
		with open('TestExGUI.csv','a', encoding='utf-8', newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# *? 'a' คือการบันทึกเรื่อยๆ/เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# 'w' คือการเขียนใหม่ทั้งหมด
			# newline='' ทำให้ข้อมูลที่บันทึกไม่มีบรรทัดว่างเมื่อเปิดดูไฟล์ของมัน
			# 'utf-8' คือการทำให้เซฟเป็นภาษาไทยได้
			fw = csv.writer(f) # สร้างฟังก์ชั่นสำหรับการเขียนข้อมูล
			data = [transactionid,dt,expense, price, numberx,total,] 
			fw.writerow(data)
			

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1 ก็คือเมื่อ Saveแล้ว พิมพ์ต่อได้เลย ไม่ต้องกดที่ช่องแรกเพื่อกรอกใหม่
		E1.focus()
		update_table()
	except Exception as e: 
		print('ERROR:',e) # Exception as e เป็นการแสดงให้เห็นความผิดพลาดโดยนำมาใส่ในตัวแปร e แล้ว print ออกมาเพื่อให้รู้ว่าผิดตรงไหน
		print('ERROR')
		# messagebox.showerror('Error','กรอกใหม่ครับ')
		messagebox.showwarning('Error','กรอกใหม่ครับ')
		# messagebox.showinfo('Error','กรอกใหม่ครับ')
		# error/warning/info จะเลือกใช้อันไหนก็ได้ตามแต่จะเลือก
		# ข้อความแรกเป้นหัวข้อ, ข้อความที่สองเป็นข้อความภายในลก่อง
			
		V_expense.set('') 
		V_price.set('')
		V_numberx.set('')
		# เมื่อกรอกผิดจะทำการเคลียร์ข้อมูลภายในช่องกรอก
		# ถ้านำไปใส่ไว้ก่อน massege ข้อความที่กรอกจะหายก่อนการแจ้งเตือน


# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน () ของ def save() ด้วย

FONT1 = (None,16) # None คือการเลือกใช้ font เปลี่ยนได้ถ้ามีที่ต้องการ

#--------text1-------------------------

L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack() # ถ้าชื่อไม่มีการเปลี่ยนแปลงใช้แค่L ก็ได้
V_expense = StringVar() # StringVar() คือตัวแปรชนิดพิเศษสำหรับเก็บข้อมุลใน GUI
E1 = ttk.Entry(F1, textvariable=V_expense, font=FONT1) # เป็นการทำกรอบช่องรับ 
E1.pack() # หรือจะใส่ .pack() ต่อหลังประโยคก็ได้
#--------------------------------------

#--------text2-------------------------

L = ttk.Label(F1,text='ราคา(บาท)',font=FONT1).pack()
V_price = StringVar()
E2 = ttk.Entry(F1, textvariable=V_price, font=FONT1) #Entry คือช่องรับinput
E2.pack()
#--------------------------------------

#

L = ttk.Label(F1, text='จำนวน', font=FONT1).pack()
V_numberx = StringVar()
E3 = ttk.Entry(F1, textvariable=V_numberx, font=FONT1).pack()
#


B1 = ttk.Button(F1,text='Save',command=Save)
B1.pack(ipadx=50, ipady=20)
 

 # label แสดงผลลัพธ์
v_result = StringVar()
v_result.set('-----ผลลัพธ์-----')
result = ttk.Label(F1, textvariable=v_result, font=FONT1, foreground='green') # foreground เป็นการเปลี่ยนสี
result.pack()


#####################TAB2################################################################

def read_csv(): # with มีไว้กันลืม close 
	# global rs # เป็นการบอกว่าให้ rs
	with open('TestExGUI.csv', newline='', encoding='utf-8') as f: # เปิดไฟล์ csv และตั้งชื่อว่า f
		fr = csv.reader(f)
		data = list(fr)  # แปลงfrเป็น data ให้ไฟล์มันอ่านออก
	return data  # เป็นการส่งต่อข้อมูล ว่าจะให้ไปโชว์ในtab ไหน
	#	print(data)
	#	print('------------')
	#	print(data[0][0]) # 0 ตัวแรกคือรายการอันแรก 0 ตัวหลังคือรายการ ในที่นี้คือเวลา ถ้าเป็น1 ก็จะเป็นชื่อรายการ
	# for a,b,c,d,e in data: # a,b,... เป็นการซ้อนlist
	#	print(a) # เป็นการปริ้นข้อมูลตัวแรก ก็คือวันเวลา
	# ถ้าทำตาม #ข้างบน ต้องลงท้ายเหลือแค่ read_csv()
	
# rs = read_csv()
# print(rs) เกี่ยวกบัพวกช้อความคำสั่งต่างๆที่อยู่ใน #ข้างบน


L = ttk.Label(T2,text='ตารางแสดงข้อมูล',font=FONT1).pack(pady=20)

# table # treeviwe เป็นการโชว์ข้อความ สำคัญมากๆ ต้องเรียนรู้ไว้
header = ['รหัสรายการ','วันเวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม','หมายเหตุ']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10) 
# ใส่ใน t2, ทำเป็นช่องๆบนหัว, โชว์ไว้, สูง10บรรทัด
resulttable.pack()

for h in header:   # วิธีนี้ดีที่สุด
	resulttable.heading(h,text=h) 

headerwidth = [120,150,170,80,80,80,80]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)


# วิธีโชว์ชื่อบนหัวของตาราง 1
# for i in range(len(header)):
#	resulttable.heading(header[i],text=header[i])


# 2 
# resulttable.heading(header[0],text=header[0])
# resulttable.heading(header[1],text=header[1]) และพิมพ์แบบนี้ยาวไป


# resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])
# resulttable.insert('','0',value=['อังคาร','น้ำดื่ม',30,5,150])


alltransection = {}


def UpdateCSV():
	with open('TestExGUI.csv','w', newline='', encoding='utf-8') as f: # เปิดไฟล์ csv และตั้งชื่อว่า f
		# *? 'w' เป็นการเขียนทับลงไปเลย
		fw = csv.writer(f)
		# เตรียมข้อมูลจาก alltransection ให้กลายเป็น list
		data = list(alltransection.values())
		fw.writerows(data) # เมื่อเติม 's' ต่อท้าย เป็นการเขียนได้หลายบรรทัด (ต่อบรรทัดล่าง)
		# *! multiple line from nested list [[],[],[]] เป็น list ซ้อน list
		print('Table was updated')
		

def DeleteRecord(event=None):
	check = messagebox.askyesno('Confirm','คุณต้งการลบข้อมูลใช่หรือไม่')
	print('YES/NO:', check)

	if check == True:
		print('Delete')
		select = resulttable.selection()
		#print(select)
		data = resulttable.item(select)
		data = data['values'] # *! อย่าลืมตัว 's' ท้าย value
		transectionid = data[0]
		#print(transectionid) 
		#print(type(transectionid))
		del alltransection[str(transectionid)] # delete data in dict.
		#print(alltransection)
		UpdateCSV()
		update_table()

	else:
		print('Cancel')


BDelete = ttk.Button(T2,text='Delete',command=DeleteRecord)
BDelete.place(x=50,y=450)

resulttable.bind('<Delete>', DeleteRecord)





def update_table(): # funtion อ่านข้อมูล
	resulttable.delete(*resulttable.get_children()) # get_childern เป็นเสมือนรหัสของโปรแกรมที่าร้างขึ้นสำหรับข้อความนั้นๆ
	# '*' ทำหน้าที่เหมือน for loop ซึ่งข้อความเต็มๆนั้นก็คือ....
	#  for c in resulttable.get_childern():
	#      resulttle.delete(c)
	# 
	try:
		data = read_csv()
		for d in data:
			# creat transection data
			alltransection[d[0]] = d # d[0] = transectionid
			resulttable.insert('',0,value=d)
		print(alltransection)
	except:
		print('No Flie')











update_table()
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
