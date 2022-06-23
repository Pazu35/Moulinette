# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:42:44 2022

@author: Hydrograhe
"""
import sys
import os



def get_tree_structure(foldername,dic = {}):    
    
    file_list = os.listdir(foldername)
    file_list = [os.path.join(foldername, file) for file in file_list]
    
    for file in file_list:

        if os.path.isfile(file):
            dic[file] = file
        else:  
            dic.update(get_tree_structure(file,dic))
           
    return dic  
################################################################################
# Main                                                                         #
################################################################################

if __name__ == "__main__":
    
    dic = {}
        
    if len(sys.argv) != 2:
     	sys.stderr.write("Usage: train_model.py Metrics_data_folder  \n")
     	sys.exit(1)
    
    foldername = sys.argv[1]

    if os.path.exists(foldername):
        tree_structure =  list(get_tree_structure(foldername).keys())
            
    else :
        sys.stderr.write("The entry data does not exist\n") 

    for file in tree_structure :
        #sys.stderr.write("{}\n".format(os.path.abspath(file)))
        
        if sys.platform == "linux2":
            file_name = file.split("/")[-1]
            
            
        else:
            file_name = file.split("\\")[-1]
            

        folder_name = file.replace(foldername, "")
        folder_name = folder_name.replace(file_name, "")
        file_name = file_name.split('.')[0] #remove the extension of the file name

        
        with open('{}'.format(file),'r') as f:
            line = f.readline()
            accuracy = line.split(' ')[-1]
            accuracy = float(accuracy.split('\n')[0])
            
        if folder_name in dic.keys():
        
            if dic[folder_name][1] < accuracy :
                dic[folder_name] = (file_name,accuracy)
                
        else :
            dic[folder_name] = (file_name,accuracy)

for key in dic :
    file_name,accuracy = dic[key]
    print("\n {}: \n \t Maximum accuracy: {} in file {} \n".format(key,accuracy,file_name))
