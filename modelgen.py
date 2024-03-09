from tkinter import filedialog
 
file_path = filedialog.askopenfilename(title="select dvcfg")

with open(file_path, 'r', encoding='utf-8') as f:
    __dvcfg = f.readlines()[1:-2]
   
_dvcfg = [line for line in __dvcfg if line.find('->') != -1]
dvcfg = [line.split(':')[0].split('->')[1].strip().rstrip('"') for line in _dvcfg]

save_path = filedialog.asksaveasfilename(title="save models.txt as...")

with open(save_path, 'w', encoding='utf-8') as f:
    f.write(','.join(dvcfg))