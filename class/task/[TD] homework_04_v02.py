# homework_04
import os

shot_dict = {
  "sq0010": {
    "sh0010": 3,
    "sh0030": 1,
    "sh0025": 3
  },
  "sq0030": {
    "sh0010": 3,
    "sh0030": 2,
    "sh0040": 1,
    "sh0025": 2
  },
  "sq0020": {
    "sh0010": 3,
    "sh0020": 2,
    "sh0025": 2
  },
  "sq0040": {
    "sh0050": 2,
    "sh0030": 1,
    "sh0020": 3,
    "sh0045": 1
  },
  "sq0070": {
    "sh0010": 2,
    "sh0030": 3,
    "sh0020": 3,
    "sh0050": 3,
    "sh0040": 2,
    "sh0070": 1
  }
}

# get path function 
def get_task_path_list(proj_dict):
    
    task_dict    = {} 
    task_dict[3] = ['animation', 'lighting', 'fx', 'comp']
    task_dict[2] = ['animation', 'lighting', 'comp']
    task_dict[1] = ['comp']

    path_list = []
    #for迴圈太多層的缺點是不好維護
    for squence_name, shot_name in sorted(shot_dict.items()): 
        for shot_name, level in sorted(shot_dict[squence_name].items()): 
            for num in task_dict.keys(): 
                if num == shot_dict[squence_name][shot_name]: 
                    for task in task_dict[num]: 
                        path_list.append('D:/twr/%s/%s/%s' % (squence_name, shot_name, task)) 
    
    return path_list

# create folder function 
def make_dir(input_path): 
    folder_path = '' 
    folder_list = input_path.split('/') 
         
    for folder in folder_list: 
        folder_path = folder_path + '/' + folder 
        if os.path.isdir(folder_path[1:]) != True: 
            os.mkdir(folder_path[1:]) 

# call the function
def main():
    file_list = get_task_path_list(shot_dict)
    #這樣用就很單純直覺
    for item in file_list:
        make_dir(item)

main()