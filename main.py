import time,os,sys,traceback

def write_file(f_location,f_name,w_string=''):  #写文件函数 一般用来写日志
    if w_string=='':
        return
    log_file = open(str(f_name),"a+")
    log_file.write(w_string+"\n") #print successful
    log_file.close()

    #文件写状态返回
    if log_file.closed==True:
        write_status=0
        return
    else:
        write_status=-1
        return Exception(str(f_name),"a+").write("can't close log file"+time.strftime('%Y-%m-%d,%H:%M:%S')+"\n") #返回异常无法关闭文件



def main():

    try:
        #......your_program........

        #frame test funcation:
        print("Hello World")
        print(the_running_program_file_location)
        write_file(the_running_program_file_location,'file_location.txt',str(the_running_program_file_location))
        for i in the_program_launch_parameters:
            print(i)
        
        #.........xxx...........

    except Exception as the_program_error:  #捕获错误并写如日志  
        if the_program_error == "<INSERT GRACEFUL INTERRUPT HERE>": #由于中断退出
            write_file(the_running_program_file_location,'user.log',traceback.format_exc()+time.strftime('%Y-%m-%d,%H:%M:%S')+'\n'+'由于触发中断导致退出')#在脚本文件路径下记录异常信息字符串
        else:#由于异常导致程序崩溃
            write_file(the_running_program_file_location,'error.log',traceback.format_exc()+time.strftime('%Y-%m-%d,%H:%M:%S'))#记录异常信息字符串

if __name__=="__main__":
    #全局变量区
    print('检测到启动附带参数为 '+str(len(sys.argv)-1)+' 个')#sys.argv中元素个数永远大于1，因为sys.argv[0]是文件名称
    if len(sys.argv)>1:#若检测到脚本启动时带参数
        the_program_launch_parameters=(sys.argv)
        the_program_launch_parameters.pop(0)#去掉序列0元素，从1开始是为了避免得到sys.argv[0]这一文件名称
        '''#低效的遍历.....
        for i in range(1,len(sys.argv)):
            the_program_launch_parameters.append(sys.argv[i])#获取启动脚本指定参数,例如python3 main.py 12 ac 中的 12和ac
        '''
    if sys.version_info.major < 3:#检查用户python大版本
        print('! warning:your python version <3 !')
    the_running_program_file_location=os.path.split(os.path.realpath(__file__))[0]#获取当前脚本绝对路径，linux/windows通用


    main()
