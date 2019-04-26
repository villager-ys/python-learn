
# coding: utf-8

# In[50]:


import requests
import xlrd


# In[51]:


from bs4 import BeautifulSoup


# In[52]:


def app_login(appUrl,account,pwd,mdid,csrf):
    postUrl = appUrl
    postData = {
        "_csrf":csrf,
        "_csrf_header":"X-CSRF-TOKEN",
        "username": account,
        "password": pwd,
        "mdid":mdid
    }
    return requests.post(postUrl, data = postData)
#     responseRes = requests.post(postUrl, data = postData)
#     print(postUrl)
#     print(postData)
#     print(f"statusCode = {responseRes.status_code}")


# In[62]:


def get_csrf(wauth2Url):
    try:
        page = requests.get(wauth2Url)
    except:
        return ''
    soup = BeautifulSoup(page.content, "html.parser")
    csrf = soup.find('input', attrs={"name": "_csrf"}).get("value")
    return csrf


# In[54]:


def get_mdid(appUrl):
    try:
        headers = requests.head(appUrl+'/login').headers
        location = headers['Location']
    except:
        return ''
    data = location.split('&')
    for i in data:
        if 'mdid' in i:
            return i.split('=')[1]
# In[214]:


def get_env_arr(file):
    workbook = xlrd.open_workbook(file)
    # 读取第一个env sheet
    sheet = workbook.sheets()[0] 
    return get_excel_data(sheet)


# In[219]:


def get_domain_arr(file):
    workbook = xlrd.open_workbook(file)
    # 读取第一个domain sheet
    sheet = workbook.sheets()[1] 
    return get_excel_data(sheet)


# In[220]:


def get_excel_data(sheet):
    # 行数,列数
    rows = sheet.nrows  
    cols =sheet.ncols
    list = []
    for i in range(rows):
        for j in range(cols):
            ctype = sheet.cell(i, j).ctype  # 表格的数据类型
            cell = sheet.cell_value(i, j)
            if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                cell = int(cell)  # 强转
            list.append(cell)
    return list


# In[ ]:


def app_login_test():
    file = 'C://Users\yuanshuai/Desktop/env.xlsx'
    # envs=get_env_arr(file)
    # envs = ['041839f72']
    #envs = ['01f8ffecd']
    envs = ['0647ceb80']
    domains=get_domain_arr(file)
    username ='00001'
    pwd='123456'
    for env in envs:
        wauth2Url = 'https://'+env+'-woauth2.app.wowjoycloud.com'
        for domain in domains:
            appUrl = 'https://'+env+'-'+domain+'.app.wowjoycloud.com'
            try:
                result = app_login(appUrl,username,pwd,get_mdid(appUrl),get_csrf(wauth2Url))
            except:
                code = 500
            else:
                code = result.status_code
            finally:
                if(code>200):
                  print(str(code)+',该应用的url：' + appUrl)

app_login_test()