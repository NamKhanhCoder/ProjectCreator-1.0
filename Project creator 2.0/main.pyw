import os
import tkinter as tk
from tkinter import *


root=tk.Tk()
root.title("Project creator 2")
root.geometry('600x400')
root.resizable(0,0)
#root.withdraw()#hide console
#commands
def select_lang(selected):
    global lang
    lang=selected
    pass
def check_new_tag_available(selected):
    global Uchoice
    Uchoice=selected
    
    if selected == taglist[0]:
        tag_create_entry.config(state='normal')
    else:
        tag_create_entry.config(state='disabled')
def create_project():
    global index_file,tag_file,project_create_directory_file
    tag_to_append=''
    #get final name
    newtag=False
    if Uchoice!=taglist[0]:
        project_tmp_tag=Uchoice
    elif tag_create_entry.get()!='':
        project_tmp_tag=tag_create_entry.get()
        newtag=True
    else:
        project_tmp_tag=''
    #print(project_tmp_tag,"|",Uchoice)
    project_tag=''
    if project_tmp_tag!='':
        project_tag=' ('+project_tmp_tag+')'    
    #print(project_tag,"|",Uchoice)
    project_name=name_entry.get()
    project_index=str(index_entry.get())
    if len(project_index)==1:
        project_index='0'+project_index
    
    Project_final_name=project_index+'. '+project_name+project_tag
    Project_final_name_main=project_name
    Project_final_name_inp=project_name
    des=path_entry.get()
    print("Final name:",Project_final_name)
    print("Destination: ", des)
    project_directory=des+'/'+Project_final_name
    print('Folder created ',project_directory+'|')
    index_entry.delete(0,tk.END)
    index_entry.insert(0,str(int(project_index)+1))
    os.mkdir(des+'/'+Project_final_name)#create folder
    #create main and inp file
    if lang==lang_list[0]:#if c++
        #create main
        Main=open(project_directory+'/'+project_name+'.cpp','w')
        Inp=open(project_directory+'/'+project_name+'.INP','w')

        #import library
        if import_selected.get()=='default':
            Main.write("#include<bits/stdc++.h>\n")
        elif import_selected.get()=="codeforces":
            Main.write("#include<iostream>\n#include <algorithm>\n#include <iostream>\n#include <vector>\n#include <cmath>\n")
        elif import_selected.get()=='no':
            Main.write("#include<iostream>\n")
        #write initial code
        Main.close()
        Main=open(project_directory+'/'+project_name+'.cpp','a')
        Main.write('#define fastInp cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);\n#define print_array void cout_array(lli A[69420],lli n){for(int i=0;i<n;i++)cout<<A[i]<<\':\';}\n#define lli long long int \nusing namespace std;\n\nint main()\n{\n    freopen("'+project_name+'.INP","r",stdin);\n    cout<<"Hello World!";\n    return 0;\n}')
    elif lang==lang_list[1]:#if python
        #create main
        Main=open(project_directory+'/'+project_name+'.py','w')
        Inp=open(project_directory+'/'+project_name+'.INP','w')

        #write initial code
        Main.write('import os\nfile_directory=os.path.dirname(os.path.abspath(__file__))\ninp_file=open(file_directory+"/'+project_name+'.INP")')

        pass
    index_file.close()
    tag_file.close()
    project_create_directory_file.close()
    
    
    
    if newtag:
        tag_file=open(file_directory+'/Tag list.txt','a')
        tag_file.write(project_tmp_tag+"\n")
    index_file=open(file_directory+'/index.txt','w')
    index_file.write(str(int(project_index)+1))
    project_create_directory_file=open(file_directory+'/directory.txt','r')
    
    
    
    
def import_selection():
    print(import_selected.get())
#files
file_directory=os.path.dirname(os.path.abspath(__file__))
tag_file=open(file_directory+'/Tag list.txt','r')
index_file=open(file_directory+'/index.txt','r')
project_create_directory_file=open(file_directory+'/directory.txt','r')

#required vars
taglist=tag_file.read().splitlines()
print(taglist)
path=project_create_directory_file.read()
print(path)
index=int(index_file.read())
print(index)
lang_list=['C++',"Python"]

#General 
general_frame=tk.LabelFrame(root,text="General",fg='orange')
general_frame.place(x=10,y=10)

#Name
name_labelframe=tk.LabelFrame(general_frame, text="Enter project name",fg='blue')
name_entry=tk.Entry(name_labelframe,width=25)
name_entry.pack()
name_labelframe.pack()

#tag choice
Uchoice='No tag'
tag_choice_frame=tk.LabelFrame(general_frame,text='Select a tag',fg='blue')
tag_choice_datatype=tk.StringVar(root)
tag_choice_datatype.set(taglist[0])
tag_choice_menu=tk.OptionMenu(tag_choice_frame,tag_choice_datatype,*taglist,command=check_new_tag_available)
tag_choice_menu.config(width=18)
tag_choice_menu.pack()
tag_choice_frame.pack()

#tag creation
tag_create_frame=tk.LabelFrame(general_frame,text="Or create a new tag",fg="blue")
tag_create_entry=tk.Entry(tag_create_frame,width=25)
tag_create_entry.pack()
tag_create_frame.pack()

#directory entry
path_frame=tk.LabelFrame(general_frame,text='Destination',fg='blue')
path_entry=tk.Entry(path_frame,width=25)
path_entry.insert(0,path)
path_entry.pack()
path_frame.pack()

#button
p_create_button=tk.Button(root,text='Create',command=create_project)
p_create_button.pack(side='bottom')

#file choice
lang=lang_list[0]
lang_frame=tk.LabelFrame(general_frame,text='Select language',fg='blue')
lang_choice_datatype=tk.StringVar()
lang_choice_datatype.set(lang_list[0])
lang_choice_menu=tk.OptionMenu(lang_frame,lang_choice_datatype,*lang_list,command=select_lang)
lang_choice_menu.config(width=18)
lang_choice_menu.pack()
lang_frame.pack()

#Advance(should be pre-written)
advance_frame=tk.LabelFrame(root,text="Advance",fg='orange')
advance_frame.place(x=180,y=10)

#index entry (pre-written)
index_frame=tk.LabelFrame(advance_frame, text='No:',fg='blue')
index_entry=tk.Entry(index_frame,width=25)
index_entry.insert(0,index)
index_entry.pack()
index_frame.pack()

#Library list
import_libraries_frame=LabelFrame(advance_frame,text="Import libraries",fg='blue')
import_libraries_frame.pack(side='left')
#Options for importing
import_selected=StringVar()
StringVar.set(import_selected,"default")
import_default_pack=Radiobutton(
    import_libraries_frame,
    text="Default pack",
    variable=import_selected,
    value="default",
    command=import_selection)
import_codeforces_pack=Radiobutton(
    import_libraries_frame,
    text="Codeforces pack             ",
    variable=import_selected,
    value="codeforces",
    command=import_selection)
import_none=Radiobutton(
    import_libraries_frame,
    text="Don't import",
    variable=import_selected,
    value="no",
    command=import_selection)
import_default_pack.pack(anchor=W)
import_codeforces_pack.pack(anchor=W)
import_none.pack(anchor=W)
root.mainloop()
