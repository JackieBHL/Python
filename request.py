# 引入requests库
import requests

#text
def webget_text(website,saveToTxtFile = False,wordlimit=False,endcoding = 'utf-8',):
    # requests.get是在调用requests库中的get()方法，它向服务器发送了一个请求，括号里的参数是你需要的数据所在的网址，然后服务器对请求作出了响应。
    # 我们把这个响应返回的结果赋值给变量res
    res = requests.get(website)
    #input the choosen URL
    # res saved the information get from the URL
    # print(res.status_code)
    # the number return give the user the status of the request
    # code 200 == Approval Check on res.status_code.png
    novel = res.text
    # print the novel
    #enocding
    res.encoding= endcoding

    if wordlimit == True:
        #limit the printed word[start:end]
        wordlimitmin = input("Starting word poistion: ")
        wordlimitMax = input("Ending word poistion: ")
        print(novel[wordlimitmin:wordlimitMax])
    else:
        print(novel)

    if saveToTxtFile == True:
        #stored the text file in to local 
        # 创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
        txtFileName = input('Name your txt File:')
        fulltxtFileName = txtFileName+'.txt'
        k = open(fulltxtFileName,'a+')
        # 写进文件中 
        k.write(novel)
        # 关闭文档    
        k.close()
def webget_photo(Website,filename='picture'):
    #photos
    # 发出请求，并把返回的结果放在变量res中
    res = requests.get(Website)
    # 把Reponse对象的内容以二进制数据的形式返回
    pic = res.content
    # 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
    # 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
    photofile = filename + '.jpg'
    photo = open(photofile,'wb')
    # 获取pic的二进制内容
    photo.write(pic) 
    # 关闭文件
    photo.close()
