import tkinter as tk
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
import time
import csv
from tkinter import filedialog

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
def _loopn():
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find('div','news_now2')
    n = 1
    for i in datatag.find_all('li'):
        try:
            lstbox.insert(tk.END, n, i.find('h2','txt').text.strip())
            lstbox.insert(tk.END, 'https://news.tvbs.com.tw/'+i.a['href'])
            lstbox.insert(tk.END, '出版時間：'+i.find('div','time').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue      

def _loopn2():
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find(id='stories-container_2071')
    n = 1
    for i in datatag.find_all(id='infScroll'):
        try:
            lstbox.insert(tk.END, n, i.find('span','headline truncate truncate--3').text.strip())
            lstbox.insert(tk.END, i.a['href'])
            lstbox.insert(tk.END, i.find('div','timestamp').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue
        
def _loopn3(): 
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find('div','column-left')
    n = 1
    for i in datatag.find_all('li'):
        try:
            lstbox.insert(tk.END, n, i.find('h3','title').text.strip())
            lstbox.insert(tk.END, 'https://www.chinatimes.com'+i.a['href'])
            lstbox.insert(tk.END, '出版時間：'+i.find('span','date').text.strip()+' '+i.find('span','hour').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue
        
def _loopn4(): 
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find('div','whitecon boxTitle')
    n = 1
    for i in datatag.find_all('li'):
        try:
            lstbox.insert(tk.END, n, i.find('h3','title').text.strip())
            lstbox.insert(tk.END, i.a['href'])
            lstbox.insert(tk.END, '出版時間：'+i.find('span','time').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue

def _loopn5(): 
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find('div','context-box__content story-list__holder story-list__holder--full')
    n = 1
    for i in datatag.find_all('div','story-list__news'):
        try:
            lstbox.insert(tk.END, n, i.find('h2').text.strip())
            lstbox.insert(tk.END, 'https://udn.com'+i.a['href'])
            lstbox.insert(tk.END, '出版時間：'+i.find('time','story-list__time').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue

def _loopn6(): 
    html = requests.get(url, headers=headers).text
    sp = BeautifulSoup(html, 'lxml')
    datatag = sp.find('div','subcate-list')
    n = 1
    for i in datatag.find_all('div','subcate-list__content-big'):
        try:
            lstbox.insert(tk.END, n, i.find('h3','subcate-list__link__title').text.strip())
            lstbox.insert(tk.END, i.a['href'])
            lstbox.insert(tk.END, '出版時間：'+i.find('span','subcate-list__time').text.strip())
            lstbox.insert(tk.END, '-'*30)
            n += 1
        except:
            continue

def _selectNews():
    global url
    lstbox.delete(0, tk.END)
    if news1.get() == '1':
        if news2.get() == '7':
            url = "https://news.tvbs.com.tw/"
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','breaking_news_other_mo')
            n = 1
            for i in datatag.find_all('li'):
                try:
                    lstbox.insert(tk.END, n, i.find('h2','txt').text)
                    lstbox.insert(tk.END, 'https://news.tvbs.com.tw/'+i.a['href'])
                    lstbox.insert(tk.END, '出版時間：'+i.find('div','time').text)
                    lstbox.insert(tk.END, '-'*30)
                    n += 1                      
                except:
                    continue
                
        elif news2.get() == '8':
            url = 'https://news.tvbs.com.tw/hot'
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','news_list')
            n = 1
            for i in datatag.find_all('li'):
                try:
                    lstbox.insert(tk.END, n, i.find('h2','txt').text)
                    lstbox.insert(tk.END,'https://news.tvbs.com.tw/'+i.a['href'])
                    lstbox.insert(tk.END,'-'*30)
                    n += 1
                except:
                    continue                   
        elif news2.get() == '9':
            url = 'https://news.tvbs.com.tw/politics'
            _loopn()                
        elif news2.get() == '10':
            url = 'https://news.tvbs.com.tw/health'    
            _loopn()            
        elif news2.get() == '11':
            url = 'https://news.tvbs.com.tw/entertainment' 
            _loopn()            
        elif news2.get() == '12':
            url = 'https://news.tvbs.com.tw/world' 
            _loopn()    
        
    if news1.get() == '2':
        if news2.get() == '7':
            url = 'https://www.appledaily.com.tw/realtime/recommend/'
            _loopn2()
        elif news2.get() == '8':
            url = 'https://www.appledaily.com.tw/realtime/hot/'       
            _loopn2()
        elif news2.get() == '9':
            url = 'https://www.appledaily.com.tw/realtime/politics/'
            _loopn2()
        elif news2.get() == '10':
            url = 'https://www.appledaily.com.tw/realtime/life/'
            _loopn2()       
        elif news2.get() == '11':
            url = 'https://www.appledaily.com.tw/realtime/entertainment/'
            _loopn2()
        elif news2.get() == '12':
            url = 'https://www.appledaily.com.tw/realtime/international/'
            _loopn2()

    if news1.get() == '3':
        if news2.get() == '7':
            url = 'https://www.chinatimes.com/realtimenews/?chdtv'
            _loopn3()
        elif news2.get() == '8':
            url = 'https://www.chinatimes.com/hotnews/?chdtv'       
            _loopn3()
        elif news2.get() == '9':
            url = 'https://www.chinatimes.com/realtimenews/260407/?chdtv'
            _loopn3()
        elif news2.get() == '10':
            url = 'https://www.chinatimes.com/realtimenews/260418/?chdtv'
            _loopn3()       
        elif news2.get() == '11':
            url = 'https://www.chinatimes.com/realtimenews/260404/?chdtv'
            _loopn3()
        elif news2.get() == '12':
            url = 'https://www.chinatimes.com/realtimenews/260408/?chdtv'
            _loopn3()
    
    if news1.get() == '4':
        if news2.get() == '7':
            url = 'https://news.ltn.com.tw/list/breakingnews'
            _loopn4()
        elif news2.get() == '8':
            url = 'https://news.ltn.com.tw/list/breakingnews/popular'       
            _loopn4()
        elif news2.get() == '9':
            url = 'https://news.ltn.com.tw/list/breakingnews/politics'
            _loopn4()
        elif news2.get() == '10':
            url = 'https://health.ltn.com.tw/breakingNews/9'
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','whitecon')
            n = 1
            for i in datatag.find_all('li'):
                try:
                    lstbox.insert(tk.END, n, i.find('h3','tit').text.strip())
                    lstbox.insert(tk.END, i.a['href'])
                    lstbox.insert(tk.END, '出版時間：'+i.find('span','time').text.strip())
                    lstbox.insert(tk.END, '-'*30)
                    n += 1
                except:
                    continue     
        elif news2.get() == '11':
            url = 'https://ent.ltn.com.tw/'
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('section','layout_wrap two_col_layout boxTitle boxText')
            n = 1
            for i in datatag.find_all('li'):
                try:
                    lstbox.insert(tk.END, n, i.find('h3').text.strip())
                    lstbox.insert(tk.END, i.a['href'])
                    lstbox.insert(tk.END, '出版時間：'+i.find('time').text.strip())
                    lstbox.insert(tk.END, '-'*30)
                    n += 1
                except:
                    continue
        elif news2.get() == '12':
            url = 'https://news.ltn.com.tw/list/breakingnews/world'
            _loopn4()
            
    if news1.get() == '5':
        if news2.get() == '7':
            url = 'https://udn.com/news/breaknews/1'
            _loopn5()
        elif news2.get() == '8':
            url = 'https://udn.com/news/breaknews/1/1#breaknews'       
            _loopn5()
        elif news2.get() == '9':
            url = 'https://udn.com/news/breaknews/1/4#breaknews'
            _loopn5()
        elif news2.get() == '10':
            url = 'https://health.udn.com/health/cate/5681'
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('ul','lineup__group')
            n = 1
            for i in datatag:
                try:
                    lstbox.insert(tk.END, n, i.find('h3','pic-8to5-item__title').text.strip())
                    lstbox.insert(tk.END, 'https://health.udn.com'+i.a['href'])
                    lstbox.insert(tk.END, '出版時間：'+i.find('p','pic-8to5-item__note').text.strip())
                    lstbox.insert(tk.END, '-'*30)
                    n += 1
                except:
                    continue     
        elif news2.get() == '11':
            url = 'https://udn.com/news/breaknews/1/8#breaknews'
            _loopn5()
        elif news2.get() == '12':
            url = 'https://udn.com/news/breaknews/1/5#breaknews'
            _loopn5()
            
    if news1.get() == '6':
        if news2.get() == '7':
            url = 'https://www.worldjournal.com/wj/cate/breaking'
            _loopn6()
        elif news2.get() == '8':
            url = 'https://www.worldjournal.com/wj/cate/breaking/121005'       
            _loopn6()
        elif news2.get() == '9':
            url = 'https://www.worldjournal.com/wj/cate/breaking/121098'
            _loopn6()
        elif news2.get() == '10':
            url = 'https://www.worldjournal.com/rank/newest/8877/121101'
            _loopn6()       
        elif news2.get() == '11':
            url = 'https://www.worldjournal.com/rank/newest/8877/121007'
            _loopn6()
        elif news2.get() == '12':
            url = 'https://www.worldjournal.com/rank/newest/8877/121099'
            _loopn6()        
        
def _close():
    MBX = tk.messagebox.askyesno('Exit','Are You Sure To Exit?')
    if MBX:
        window.destroy()
    else:
        pass

def _cancel():
    lstbox.delete(0, tk.END)

def _csv():
    global day
    if lstbox.get(0) == '':
        tk.messagebox.showwarning('Warning',"You Haven't Select Something" )
    else:
        csvFile = open(day+".csv", 'w', newline='', encoding='utf-8-sig')
        writeR=csv.writer(csvFile)
        writeR.writerow(["標題","超連結","時間"])
        #--------tvbs--------  
        if news1.get() == '1':
            if news2.get() == '7':
                url = "https://news.tvbs.com.tw/"
                html = requests.get(url, headers=headers).text
                sp = BeautifulSoup(html, 'lxml')
                datatag = sp.find('div','breaking_news_other_mo')
                for i in datatag.find_all('li'):
                    try:
                        writeR.writerow([i.find('h2','txt').text, 'https://news.tvbs.com.tw/'+i.a['href'], '出版時間：'+i.find('div','time').text])                 
                    except:
                        continue
            elif news2.get() == '8':
                url = 'https://news.tvbs.com.tw/hot'
                html = requests.get(url, headers=headers).text
                sp = BeautifulSoup(html, 'lxml')
                datatag = sp.find('div','news_list')
                for i in datatag.find_all('li'):
                    try:
                        writeR.writerow([i.find('h2','txt').text, 'https://news.tvbs.com.tw/'+i.a['href'], ''])
                    except:
                        continue                           
            elif news2.get() == '9':
                url = 'https://news.tvbs.com.tw/politics'               
            elif news2.get() == '10':
                url = 'https://news.tvbs.com.tw/health'               
            elif news2.get() == '11':
                url = 'https://news.tvbs.com.tw/entertainment'            
            elif news2.get() == '12':
                url = 'https://news.tvbs.com.tw/world' 
                
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','news_now2')
    
            for i in datatag.find_all('li'):
                try:
                    writeR.writerow([i.find('h2','txt').text.strip(), 'https://news.tvbs.com.tw/'+i.a['href'], '出版時間：'+i.find('div','time').text.strip()])
                except:
                    continue              
        #-------appledaily-------     
        if news1.get() == '2':
            if news2.get() == '7':
                url = 'https://www.appledaily.com.tw/realtime/recommend/'
            elif news2.get() == '8':
                url = 'https://www.appledaily.com.tw/realtime/hot/'       
            elif news2.get() == '9':
                url = 'https://www.appledaily.com.tw/realtime/politics/'
            elif news2.get() == '10':
                url = 'https://www.appledaily.com.tw/realtime/life/'      
            elif news2.get() == '11':
                url = 'https://www.appledaily.com.tw/realtime/entertainment/'
            elif news2.get() == '12':
                url = 'https://www.appledaily.com.tw/realtime/international/'
                
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find(id='stories-container_2071')
            for i in datatag.find_all(id='infScroll'):
                try:
                    writeR.writerow([i.find('span','headline truncate truncate--3').text.strip(), i.a['href'], i.find('div','timestamp').text.strip()])
                except:
                    continue
        #-------chinatimes------- 
        if news1.get() == '3':
            if news2.get() == '7':
                url = 'https://www.chinatimes.com/realtimenews/?chdtv'
            elif news2.get() == '8':
                url = 'https://www.chinatimes.com/hotnews/?chdtv'       
            elif news2.get() == '9':
                url = 'https://www.chinatimes.com/realtimenews/260407/?chdtv'
            elif news2.get() == '10':
                url = 'https://www.chinatimes.com/realtimenews/260418/?chdtv'     
            elif news2.get() == '11':
                url = 'https://www.chinatimes.com/realtimenews/260404/?chdtv'
            elif news2.get() == '12':
                url = 'https://www.chinatimes.com/realtimenews/260408/?chdtv'
                
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','column-left')
            for i in datatag.find_all('li'):
                try:
                    writeR.writerow([i.find('h3','title').text.strip(), 'https://www.chinatimes.com'+i.a['href'], '出版時間：'+i.find('span','date').text.strip()+' '+i.find('span','hour').text.strip()])
                except:
                    continue
        #-------ltn------- 
        if news1.get() == '4':
            if news2.get() == '10':
                url = 'https://health.ltn.com.tw/breakingNews/9'
                html = requests.get(url, headers=headers).text
                sp = BeautifulSoup(html, 'lxml')
                datatag = sp.find('div','whitecon')
                for i in datatag.find_all('li'):
                    try:
                        writeR.writerow([i.find('h3','tit').text.strip(), i.a['href'], '出版時間：'+i.find('span','time').text.strip()])
                    except:
                        continue     
            elif news2.get() == '11':
                url = 'https://ent.ltn.com.tw/'
                html = requests.get(url, headers=headers).text
                sp = BeautifulSoup(html, 'lxml')
                datatag = sp.find('section','layout_wrap two_col_layout boxTitle boxText')
                for i in datatag.find_all('li'):
                    try:
                        writeR.writerow([i.find('h3').text.strip(), i.a['href'], '出版時間：'+i.find('time').text.strip()])
                    except:
                        continue    
            elif news2.get() == '7':
                url = 'https://news.ltn.com.tw/list/breakingnews'
            elif news2.get() == '8':
                url = 'https://news.ltn.com.tw/list/breakingnews/popular'       
            elif news2.get() == '9':
                url = 'https://news.ltn.com.tw/list/breakingnews/politics'
            elif news2.get() == '12':
                url = 'https://news.ltn.com.tw/list/breakingnews/world'
                
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','whitecon boxTitle')
            
            for i in datatag.find_all('li'):
                try:
                    writeR.writerow([i.find('h3','title').text.strip(), i.a['href'], '出版時間：'+i.find('span','time').text.strip()])
                except:
                    continue  
        #-------udn-------         
        if news1.get() == '5':
            if news2.get() == '10':
                url = 'https://health.udn.com/health/cate/5681'
                html = requests.get(url, headers=headers).text
                sp = BeautifulSoup(html, 'lxml')
                datatag = sp.find('ul','lineup__group')
                for i in datatag:
                    try:
                        writeR.writerow([i.find('h3','pic-8to5-item__title').text.strip(), 'https://health.udn.com'+i.a['href'], '出版時間：'+i.find('p','pic-8to5-item__note').text.strip()])
                    except:
                        continue
            elif news2.get() == '7':
                url = 'https://udn.com/news/breaknews/1'
            elif news2.get() == '8':
                url = 'https://udn.com/news/breaknews/1/1#breaknews'       
            elif news2.get() == '9':
                url = 'https://udn.com/news/breaknews/1/4#breaknews'      
            elif news2.get() == '11':
                url = 'https://udn.com/news/breaknews/1/8#breaknews'
            elif news2.get() == '12':
                url = 'https://udn.com/news/breaknews/1/5#breaknews'
            
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','context-box__content story-list__holder story-list__holder--full')
            for i in datatag.find_all('div','story-list__news'):
                try:
                    writeR.writerow([i.find('h2').text.strip(), 'https://udn.com'+i.a['href'], '出版時間：'+i.find('time','story-list__time').text.strip()])
                except:
                    continue
    
        #-------worldjournal-------         
        if news1.get() == '6':
            if news2.get() == '7':
                url = 'https://www.worldjournal.com/wj/cate/breaking'
            elif news2.get() == '8':
                url = 'https://www.worldjournal.com/wj/cate/breaking/121005'       
            elif news2.get() == '9':
                url = 'https://www.worldjournal.com/wj/cate/breaking/121098'
            elif news2.get() == '10':
                url = 'https://www.worldjournal.com/rank/newest/8877/121101'      
            elif news2.get() == '11':
                url = 'https://www.worldjournal.com/rank/newest/8877/121007'
            elif news2.get() == '12':
                url = 'https://www.worldjournal.com/rank/newest/8877/121099'
                
            html = requests.get(url, headers=headers).text
            sp = BeautifulSoup(html, 'lxml')
            datatag = sp.find('div','subcate-list')
            for i in datatag.find_all('div','subcate-list__content-big'):
                try:
                    writeR.writerow([i.find('h3','subcate-list__link__title').text.strip(), i.a['href'], '出版時間：'+i.find('span','subcate-list__time').text.strip()])
                except:
                    continue
                
        csvFile.close()
        tk.messagebox.showinfo('Text','Save Already!')

def _savefile():
    if lstbox.get(0) == '':
        tk.messagebox.showwarning('Warning',"You Haven't Select Something" )   
    else:
        file = filedialog.asksaveasfile(defaultextension='.*',
                                        filetypes=[
                                            ("All files", ".*"),
                                            ("JSON file", ".json"),
                                            ("Text file",".txt"),])
        
        if file is None:
            return
        filetext = str(lstbox.get(0, tk.END))
    
        file.write(filetext)
        file.close()
        tk.messagebox.showinfo('Text','Save Already!')
#===============================================================
window =  tk.Tk()
window.title('News')
window.geometry('772x577+650+200')
window.resizable(False,False)
window.attributes('-topmost',1)
window.config(bg='SkyBlue3')

tt = time.localtime()
day = str(tt.tm_year) + '-' + str(tt.tm_mon)+ '-' + str(tt.tm_mday)

lb1 = tk.Label(window, text='\tQuit Or Clean\t', bg='SkyBlue3', fg='white', font=('標楷體',15)).place(x=525, y=255)
bnt1 = tk.Button(window, text=' Close ', bd=5, bg='SkyBlue4', fg='white', font=('標楷體',16), command=_close)
bnt1.place(x=630, y=295)
bnt2 = tk.Button(window, text=' Clean ', bd=5, bg='SkyBlue4', fg='white', font=('標楷體',16), command=_cancel)
bnt2.place(x=630, y=340)

lb2 = tk.Label(window, text='\tSave File\t', bg='SkyBlue3', fg='white', font=('標楷體',15)).place(x=550, y=410)
bnt3 = tk.Button(window, text='  CSV  ', bd=5, bg='SkyBlue4', fg='white', font=('標楷體',16), command=_csv)
bnt3.place(x=630, y=450)
bnt4 = tk.Button(window, text=' Other ', bd=5, bg='SkyBlue4', fg='white', font=('標楷體',16), command=_savefile)
bnt4.place(x=630, y=495)

frm1 = tk.Frame(window, bg='SkyBlue3')
frm1.grid(row=0, column=0)
lbfrm1 = tk.LabelFrame(frm1, text=' News Agency ', width=400 , height=250, relief=tk.RIDGE, bd=6, bg='SkyBlue3', fg='white',  font=('標楷體',16)).pack()

news1 = tk.StringVar()
news1.set(' ')

n1 = tk.Radiobutton(frm1, text='TVBS新聞', variable=news1, value='1', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=10, y=55)
n2 = tk.Radiobutton(frm1, text='蘋果新聞', variable=news1, value='2', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=140, y=55)
n3 = tk.Radiobutton(frm1, text='中時新聞', variable=news1, value='3', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=270, y=55)
n4 = tk.Radiobutton(frm1, text='自由時報', variable=news1, value='4', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=10, y=155)
n5 = tk.Radiobutton(frm1, text='聯合新聞', variable=news1, value='5', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=140, y=155)
n6 = tk.Radiobutton(frm1, text='世界新聞', variable=news1, value='6', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=270, y=155)

frm2 = tk.Frame(window, bg='SkyBlue3')
frm2.grid(row=0, column=1)
lbfrm2 = tk.LabelFrame(frm2, text=' Topic ', width=370 , height=250, relief=tk.RIDGE, bd=6, bg='SkyBlue3', fg='white', font=('標楷體',16)).pack()

news2 = tk.StringVar()
news2.set(' ')

n7 = tk.Radiobutton(frm2, text='即時', variable=news2, value='7', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=20, y=55)
n8 = tk.Radiobutton(frm2, text='熱門', variable=news2, value='8', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=150, y=55)
n9 = tk.Radiobutton(frm2, text='政治', variable=news2, value='9', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=280, y=55)
n10 = tk.Radiobutton(frm2, text='健康', variable=news2, value='10', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=20, y=155)
n11 = tk.Radiobutton(frm2, text='娛樂', variable=news2, value='11', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=150, y=155)
n12 = tk.Radiobutton(frm2, text='全球', variable=news2, value='12', bg='SkyBlue3', font=('標楷體',16), command=_selectNews).place(x=280, y=155)

frm3 = tk.Frame(window, bg='SkyBlue3')
frm3.place(x=1,y=255)
lbfrm3 = tk.LabelFrame(frm3, text=' Content ', width=570 , height=320, relief=tk.RIDGE, bd=6, bg='SkyBlue3', fg='white', font=('標楷體',16))
lbfrm3.grid(row=1,column=0)

lstbox=tk.Listbox(frm3, width=58 , height=13,font=("Arial", 13), bg='lightyellow')
lstbox.place(x=15, y=30)

y_scb = tk.Scrollbar(frm3)
y_scb.grid(row=1,sticky= tk.E+tk.N+tk.S)
x_scb = tk.Scrollbar(frm3, orient=tk.HORIZONTAL)
x_scb.grid(row=1,sticky= tk.E+tk.W+tk.S)

y_scb.config(command=lstbox.yview)
lstbox.config(yscrollcommand=y_scb.set)
x_scb.config(command=lstbox.xview)
lstbox.config(xscrollcommand=x_scb.set)

window.mainloop()