from Common.Log import framelog
#对base代码进行优化、增加
class base():
    def __init__(self,driver):
        self.driver = driver
        self.log =framelog().log()

   # 单星号参数代表此处接受任意多个非关键字参数
    def findele(self,*args):
        try:
            print(args)
            self.log.info("通过"+args[0]+"定位,元素是"+args[1])
            return  self.driver.find_element(*args)
        except:
            #找不到元素错误信息你加下
            self.log.error()
    #对元素click
    def click(self,*args):
        self.findele(*args).click()
    #输入值
    def sendkey(self,*args,value):
        self.findelet(*args).send_keys(value)
    #调用js方法
    def js(self,str):
        self.driver.execute_script(str)

    def url(self):
        return  self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()
    #前进
    def forword(self):
        self.driver.forward()
    #退出
    def quit(self):
        self.driver.quit()