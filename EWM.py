from MyQR import myqr

#user create website
#print('Create QR code')
#address = 'https://' + input('Enter the website address:')


myqr.run(
    words= 'https://www.google.com',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='',  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='Python.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )