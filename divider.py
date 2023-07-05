import os
import random
import shutil

root = os.path.dirname(os.path.realpath(__file__))
in_data = root+'\Input'
out_data = root+'\Output'
teste = os.path.join(root,'Output')
pastas = ['Train','Valid','Test']

list_dir = os.listdir(in_data)
data=[]

#separate de images
for classe in list_dir:
    data.append(os.listdir(in_data+'\\'+classe))
#
for classe in range(len(list_dir)):
    random.shuffle(data[classe])
new_data = []

for classe in range(len(data)):
    new_data.append([])
    a = int(0.7*len(data[classe]))
    b = int(round(0.1*len(data[classe])))
    c = a+b
    x = data[classe]
    new_data[classe].append(x[:a])
    new_data[classe].append(x[a:c])
    new_data[classe].append(x[c:])

if len(os.listdir(out_data))!=0:
    for item in os.listdir(out_data):
        shutil.rmtree(out_data+"\\"+item)

os.chdir(out_data)
for i in range(len(new_data)):
    os.mkdir(str(i))

for i in os.listdir(out_data):
    os.chdir(out_data+'\\'+i)
    for pasta in range(len(pastas)):
        os.mkdir(pastas[pasta])

classes_out = os.listdir(out_data)
classes_in = os.listdir(in_data)
#train

#train
for clas in range(len(new_data)):
    for image in new_data[clas][0]:
        shutil.copyfile(in_data+'\\'+classes_in[clas]+'\\' + image,
                        out_data+'\\'+classes_out[clas]+'\\Train'+'\\' + image)
#Valid
for clas in range(len(new_data)):
    for image in new_data[clas][1]:
        shutil.copyfile(in_data + '\\' + classes_in[clas] + '\\' + image,
                        out_data + '\\' + classes_out[clas] + '\\Valid' + '\\' + image)
#Test
for clas in range(len(new_data)):
    for image in new_data[clas][2]:
        shutil.copyfile(in_data + '\\' + classes_in[clas] + '\\' + image,
                        out_data + '\\' + classes_out[clas] + '\\Test' + '\\' + image)

os.chdir(root)

a = open("classes.txt",'w')
lista_in = os.listdir(in_data)
for name in range(len(lista_in)):
    a.writelines(str(name)+' - '+lista_in[name]+'\n')
a.close()