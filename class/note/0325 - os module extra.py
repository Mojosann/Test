# os module

# 建立資料夾
os.mkdir(input_path)

# 刪除檔案
os.remove(input_path) 

# 刪除資料夾
os.rmdir(input_path) 

# 列出input_path底下所有的項目 type=list
os.listdir(input_path) 

##### os.path module

# 檢查檔案是否存在
os.path.isfile(input_path)

# 是否為folder path
os.path.isdir(input_path)

# 取得file path的路徑(直到最後一個folder)
os.path.dirname(input_path)

# 取得path的檔案名稱
os.path.basename(input_path)

# 分割成檔名與副檔名
name, ext = os.path.splitext(basename)

os.rename()

# 一次創建多層資料夾
os.makedirs()

# 整合路徑內的斜線為'\'
os.path.normpath(input_path)