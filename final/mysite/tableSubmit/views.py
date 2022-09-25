from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


import re
import requests
import json
def findstr(pattern, string):
    # 正则表达式匹配字符串
    ans = re.search(pattern, string)
    if ans:
        span = ans.span()
        return string[span[0] : span[1]]
    return None

class Student: 
    def __init__(self, username, password):
        # 请求头
        import re
        import requests
        import json
        self.head = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        # 个人工作台登陆接口
        login_url = "http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn"
        # 实例化持久化线程
        self.ssion = requests.session()
        # 获取随机表单数据
        page = self.ssion.get(login_url, headers=self.head).text
        # 去掉所有空格
        page = re.sub(r'\s', '', page)
        # 模式匹配
        lt = findstr(r'(?<=lt"value=")(.*?)(?=")', page)
        execution = findstr(r'(?<=execution"value=")(.*?)(?=")', page)
        _eventId = findstr(r'(?<=_eventId"value=")(.*?)(?=")', page)
        # 参数
        data = {
            'username' : username,
            'password' : password,
            'lt' : lt,
            'execution' : execution,
            '_eventId' : _eventId
        }
        # 按post方法，获得cookie
        self.ssion.post(login_url, params=data, headers=self.head, allow_redirects=False)

        
   

def currentSubmit(request):
    try:
        project = request.GET.get('Project')
        Dorm = request.GET.get('dorm')
        phoneNumber = request.GET.get('phonenumber')
        teacherName = request.GET.get('teacherName')
        teacherPhonenumber = request.GET.get('teacherPhonenumber')
        reason = request.GET.get('reason')
        current = request.GET.get('howMuch')
        from email import header
        import re
        import requests
        import json
        
        # 账号和密码
        #pwd = ["320220941831","Yanhe521"]
        pwd = ["32022093656","Wly20031125"]
        # 实例化Student类
        student = Student(pwd[0], pwd[1])


        applicationUrl = 'http://oa.lzu.edu.cn/jsoa/WorkflowButtonAction.do?flag=save&resubmitWorkId='


        headersapp = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Length': '3806',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'JSESSIONID=B13D38FCE82A634D89AC2298A35C6BC4; iPlanetDirectoryPro=TGT-628310-ZcKnimtZkXYUD5neKwbm0jxhjecboluxknjpFiJlH5qs2PPZmm-cas01.example.org; jsoaUserName=320220941831; MarkPwd=0',
        'Host': 'oa.lzu.edu.cn',
        'Origin': 'http://oa.lzu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://oa.lzu.edu.cn/jsoa/JsFlowAddAction.do?action=add&processId=27642667&tableId=27642326&processName=%25u5b66%25u751f%25u514d%25u8d39%25u6d41%25u91cf%25u4f7f%25u7528%25u7533%25u8bf7%25u8868&processType=1&remindField=null&moduleId=1&formType=0&jspFile=null&layParent=MainDesktop',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        applicationData ={
        'fromFlagFlow':'null',     #null              
        'wfWorkId':'null',        #null
        'collectId':'null',       #null一下等等·
        'workId':'null',  
        'workType':'null',
        'curActivityId':'null',
        'submitPerson':'null',
        'submitPersonId':'null',
        'stepCount':'null',
        'isStandForWork':'null',
        'standForUserId':'null',
        'standForUserName':'null',
        'initActivity':'null',
        'haierFileId':'null',
        'FileId':'null',
        'myAction':'',
        'remindField':'null',
        'user_Id':'68998463',    #id之前爬虫
        'user_Name':'',#姓名
        'user_Account':'',#学号 must
        'org_Name':'',#本科生，学院
        'org_ID':'962190',       #爬虫获取
        'group_ID':'null',       #NULL
        'Hide_Field':'1012523,1012524,1012525,1012526,1012527,1012523,1012524,1012525,1012526,1012527',
        'Page_Id':'27642326',   #爬虫
        'Info_Id':'null',       #null
        'work_Status':'null',   #固定
        'parent_fromDraft':'0', #固定
        'resubmit':'0',         #固定
        'totalValueSet':'',     #空 
        'dateCompare':'',       #空
        'sendSMS':'1',          #短信提醒1为勾选 0为不选
        'needCheckField':'jst_3455_f8859',#固定
        'jst_3455_f8859_type':'jsdate',   #固定
        'jst_3455_f8859':'2022-09-19',    #申请时间
        'mustWrite':'jst_3455_f8859',     #本科生，学院
        'jst_3455_f8860_type':'varchar',   
        'jst_3455_f8860_size':'255',
        'jst_3455_f8860':'', #must
        'wf_ua':'jst_3455_f8860',
        'jst_3455_f8861_type':'varchar',
        'jst_3455_f8861_size':'255',
        'jst_3455_f8861':'', #must
        'mustWrite':'jst_3455_f8861',
        'jst_3455_f8862_type':'varchar',
        'jst_3455_f8862_size':'255',
        'jst_3455_f8862':'',#name 
        'mustWrite':'jst_3455_f8862',
        'jst_3455_f8863_type':'varchar',
        'jst_3455_f8863_size':'255',
        'jst_3455_f8863':'0',         #0为男，1为女
        'mustWrite':'jst_3455_f8863',
        'jst_3455_f8864_type':'varchar',
        'jst_3455_f8864_size':'255',
        'jst_3455_f8864':'',#本科生，学院
        'jst_3455_f8865_type':'varchar',
        'jst_3455_f8865_size':'255',
        'jst_3455_f8865':project,#专业 must
        'mustWrite':'jst_3455_f8865',
        'jst_3455_f8866_type':'varchar',
        'jst_3455_f8866_size':'255',
        'jst_3455_f8866':Dorm,#宿舍地址 must
        'mustWrite':'jst_3455_f8866',
        'jst_3455_f8867_type':'varchar',
        'jst_3455_f8867_size':'255',
        'jst_3455_f8867':phoneNumber,      #电话号码 must
        'mustWrite':'jst_3455_f8867',
        'jst_3455_f8868_type':'varchar',
        'jst_3455_f8868_size':'255',
        'jst_3455_f8868': teacherName,#辅导员姓名
        'mustWrite':'jst_3455_f8868',
        'jst_3455_f8869_type':'varchar',
        'jst_3455_f8869_size':'255',
        'jst_3455_f8869': teacherPhonenumber,             #辅导员电话号码
        'mustWrite':'jst_3455_f8869',
        'jst_3455_f8870_type':'varchar',
        'jst_3455_f8870_size':'255',
        'jst_3455_f8870':'2',                      #0：10g,1: 20g,2:50g
        'mustWrite':'jst_3455_f8870',
        'jst_3455_f8871_type':'varchar',
        'jst_3455_f8871_size':'500',
        'jst_3455_f8871':reason,                   #申请原因 must
        'mustWrite':'jst_3455_f8871',
        'jst_3455_f8872_type':'file',             #附件
        'jst_3455_f8872_fileName':'',
        'jst_3455_f8872_saveName':'',
        'addDivContent':'',
        'signatureIds':'A',
        'relproject':'-1',
        'tableId':'27642326',
        'recordId':'null',
        'editId':'',
        'processType':'1',
        'processName':'%D1%A7%C9%FA%C3%E2%B7%D1%C1%F7%C1%BF%CA%B9%D3%C3%C9%EA%C7%EB%B1%ED',
        'processId':'27642667',
        'remindField':'null',
        'moduleId':'1',
        'isSending2':'1',
        'mainLinkFile':'/jsoa/WorkFlowProcAction.do?flowpara=1',
        'titleFieldName':'',
        'msgFrom':'工作流程',
        'cancelHref':"JSMainWinOpen(\"/jsoa/jsflow/workflow_cancelReason.jsp?workStatus=1&workId=workIdValue&tableId=tableIdValue&processName=processNameValue&recordId=recordIdValue&processId=processIdValue&remindValue=remindValueValue&moduleId=1&remindField=null','','TOP=0,LEFT=0,scrollbars=no,resizable=no,width=480,height=250\")",
        'userType':'100', 
        'operName':'张玉',                #辅导员姓名
        'operId':'$35258585$',               #辅导员id
        'allowStandFor':'1',                #未知
        'allowCancel':'0',                 
        'activityId':'27642687',           #未知随机(发现为固定)
        'activityName':'虚拟节点',
        'branchActInfo':'',
        'pressType':'0',
        'deadLineTime':'0',
        'pressMotionTime':'0',
        'emergence':'0',
        'needSendMsg':'',
        'smsContent':'',
        'dealTips':'',
        'processDeadlineDate':'0',
        'approveMode':'2',                     #审批方式默认为单人：2
        'saveCheckFn':'beforeSubmit()',        
        'formName':'WorkFlowFormActionForm',
        'sendMsgToInitiator':'0',              #提醒流程发起人
        'sendMsgToDealDone':'0',               #是否给已办人员发送
        'sendContinue':'0',                    #是否继续发送
        'sendContinueUrl':'http://oa.lzu.edu.cn/jsoa/JsFlowAddAction.do?action=add&processId=27642667&tableId=27642326&processName=%25u5b66%25u751f%25u514d%25u8d39%25u6d41%25u91cf%25u4f7f%25u7528%25u7533%25u8bf7%25u8868&processType=1&remindField=null&moduleId=1&formType=0&jspFile=null&layParent=MainDesktop',
        'subProcess':'0',
        'changeDeadLineTime':'-1',
        'mainNeedPassRound':'1',
        'mainPassRoundUserType':'100',
        'passRoundId':'',
        'passRoundName':'',
        'jybd':''}

        user_data = student.ssion.get("http://my.lzu.edu.cn/getUser?t=", headers=student.head).text
        user_data = json.loads(user_data)['data']
        applicationData['org_name'] = '本科生，' + user_data['dwmc']
        applicationData['jst_3455_f8864'] = '本科生，' + user_data['dwmc']
        applicationData['jst_3455_f8867'] = phoneNumber #phone
        applicationData['jst_3455_f8865'] = project #major
        applicationData['jst_3455_f8862'] = user_data['xm']
        applicationData['user_Name'] = user_data['xm'] # 名字
        applicationData['jst_3455_f8866'] = Dorm # 宿舍
        applicationData['jst_3455_f8863'] = str(int(user_data['xb'] != '男性'))
        applicationData['jst_3455_f8860'] = user_data['rybh'] #以下三个是学号
        applicationData['jst_3455_f8861'] = user_data['rybh']
        applicationData['user_Account'] = user_data['rybh']
        applicationData['jst_3455_f8868'] = teacherName
        applicationData['jst_3455_f8869'] = teacherPhonenumber
        applicationData['jst_3455_f8871'] = reason
        for each in applicationData:
            if re.search(r'[\u4e00-\u9fa5]', applicationData[each]):
                applicationData[each] = applicationData[each].encode('gbk')

        student.ssion.get("http://oa.lzu.edu.cn/jsoa/LDCheckUser.do")
        appanswer = student.ssion.post(applicationUrl,data = applicationData,headers=headersapp)
        ans = {
            "status_code" : 100
        }
        return(HttpResponse(json.dumps(ans)))
    except Exception as e:
        ans={
            'status_code': -1,
            'ans': Dorm
        }
        return(HttpResponse(json.dumps(ans)))


def dayoffSubmit(request):
    import re
    from email import header
    import requests
    import json

    startTime=request.GET.get('startTime')
    endTime=request.GET.get('endTime')
    destination=request.GET.get('destination')
    carNumber=request.GET.get('number')
    onTheWay=request.GET.get('onTheWay')
    carStartTime=request.GET.get('carStartTime')
    carEndTime=request.GET.get('carEndTime')
    urgencyMan=request.GET.get('uegencyMan')
    relevant=request.GET.get('relevant')
    urgencyManPhoneNumber=request.GET.get('urgencyManPhoneNumber')
    qq=request.GET.get('qq')
    phoneNumber=request.GET.get('phoneNumber')
    wx=request.GET.get('wx')
    happen=request.GET.get('happen')
    goout=request.GET.get('goout')
    outLan = request.GET.get('outLan')
    vehicle=request.GET.get('vehicle')
    Type=request.GET.get('Type')
    if outLan == '0':
        vehicle = ''
        destination = ''
    if goout == '0':
        carNumber = ''
        carStartTime = ''
        carEndTime = ''
        urgencyMan = ''
        urgencyManPhoneNumber=''
        relevant=''
        onTheWay =''

        
    try:
        

        # 账号和密码
        pwd = ["320220941831","Yanhe521"]
        # 实例化Student类
        student = Student(pwd[0], pwd[1])


        submitUrl = 'http://zhxg.lzu.edu.cn/lzuyz/qxj/rcqj/savestu'

        formdata = {
        'rcqjKey':'', #hidden为空
        'xykh':'',    #hidden为空
        'qjlx': Type, #请假类型
        'startDate': '2022-09-19 12:15:04', #开始时间
        'endDate': '2022-09-19 18:15:06',   #结束时间
        'sfwc': goout,  # 1为是 0为否 是否外出
        'sfcl': outLan,  # 同上  是否离开兰州
        'mdsf': '',   #省份选择
        'mdsq': '',   #市选择
        'mdqx': '',   #区选择
        'jtgj': vehicle,   #出行方式
        'cjxx': carNumber,   #输入车次/航班号车牌号
        'tjd': onTheWay,    #途径地
        'tjsj': carStartTime,   #乘车开始时间
        'tjsj': carEndTime,   #乘车结束时间
        'wcmdd': destination,      #外出目的地
        'jjlxr': urgencyMan,          #紧急联系人
        'lxrgx': relevant,          #与请假人关系
        'jjdh': urgencyManPhoneNumber,  #紧急联系人电话号码
        'qq': qq,      #qq
        'dh': phoneNumber,    #自己电话
        'wx': wx,        #微信
        'qjsy': happen,         #请假理由
        }
        #出行方式 火车：0 飞机：1 其它：2
        #

        headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '219',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': 'JSESSIONID=1287C76419BB3A08E28266F3723C1F89; route=1663476347.319.6520.269011; Hm_lvt_d214947968792b839fd669a4decaaffc=1662087972,1663303570,1663476335; iPlanetDirectoryPro=TGT-230356-orJSEtzmrBdvIuu1wBqAfwgUGkT9f9ofcBe60Sde6LFQkFaNub-cas01.example.org; Hm_lpvt_d214947968792b839fd669a4decaaffc=1663477913',
        'Host': 'zhxg.lzu.edu.cn',
        'Origin': 'http://zhxg.lzu.edu.cn',
        'Referer': 'http://zhxg.lzu.edu.cn/lzuyz/qxj/wdqjEdit.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
        'X-Requested-With': 'XMLHttpRequest',
        }

        for each in formdata:
            if re.search(r'[\u4e00-\u9fa5]', formdata[each]):
                formdata[each] = formdata[each].encode('gbk')

        url = "http://zhxg.lzu.edu.cn/lzuyz/sys/sysuser/loginPortal"
        tmp = student.ssion.get(url, headers=student.head)
        tmp = student.ssion.get("http://zhxg.lzu.edu.cn/lzuyz/sys/sysindex/toIndex")
        dayoffSave =student.ssion.post(submitUrl, headers = headers,data = formdata)
        ans={
            'status_code':100
        }
        return(HttpResponse(json.dumps(ans)))
    except Exception as e:
        ans={
            'status_code':-1,
                    }
        return(HttpResponse(json.dumps(ans)))



def fixedInfo(request):
    try:
        import re
        from email import header
        import requests
        import json
        
        # 账号和密码
        #pwd = ["320220941831","Yanhe521"]
        pwd = ["320220936560","Wly20031125"]
        # 实例化Student类
        student = Student(pwd[0], pwd[1])
        user_data = student.ssion.get("http://my.lzu.edu.cn/getUser?t=", headers=student.head).text
        user_data = json.loads(user_data)['data']
        ans ={
            'status_code':100,
            'id': user_data['rybh'],
            'name':user_data['xm'],
            'department':user_data['dwmc'],
            'gender':user_data['xb']
        }
        return(HttpResponse(json.dumps(ans)))
    except Exception as e:
        ans={
            'status_code':-1,
            'id':'failed'
        }
        return(HttpResponse(json.dumps(ans)))
