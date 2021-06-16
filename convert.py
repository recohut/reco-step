import os
import re
import glob
import shutil
from pathlib import Path
from zipfile import ZipFile
from urllib.parse import quote

def replacer(p, tgt=False):
  if tgt:
    _x = "img/"+p.name
  else:
    _x = quote(p.parent.name)+"/"+quote(p.name)
  return _x

source_path = './_markdowns/raw'
target_path = './_markdowns'


list_of_files = glob.glob(os.path.join(source_path,'*.zip'))
latest_file = max(list_of_files, key=os.path.getctime)

with ZipFile(latest_file, 'r') as zipobj:
    zipobj.extractall(source_path)
    
image_paths = []
for path in Path(source_path).rglob('*.png'):
    image_paths.append(path)
    
def clean_path(x):
    x = ' '.join([re.sub(r'\b\w{20,40}\b', ' ', _x) for _x in x.split('/')])
    x = '-'.join(x.lower().split())
    return x

renamed_image_paths = []
for p in image_paths:
    newname = clean_path(str(p))
    newpath = Path(os.path.join(p.parent,newname))
    os.rename(p, newpath)
    renamed_image_paths.append(newpath)
    try:
      shutil.move(str(newpath), os.path.join(target_path,'img'))
    except:
      print('{} already exists! please rename the new file if this is different one otherwise ignore this message!'.format(newpath.name))
      continue

sourcestr = [replacer(x) for x in image_paths]
targetstr = [replacer(x, True) for x in renamed_image_paths]

for p in Path(source_path).rglob('*.md'):
  with open(p, 'r') as fin:
    data = fin.read()
    for check, rep in zip(sourcestr, targetstr):
      data = data.replace(check, rep)
    data = data.splitlines(True)
  with open(p, 'w') as fout:
    fout.writelines(data[2:])
  newname = clean_path(p.name)
  newpath = Path(os.path.join(p.parent,newname))
  os.rename(p, newpath)
  try:
    shutil.move(str(newpath), target_path)
  except:
    print('{} already exists! please rename the new file if this is different one otherwise ignore this message!'.format(newname))
    continue

print('Done!')
