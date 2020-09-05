from flask import Flask,render_template,redirect,flash,url_for,request
import requests
import datetime
import pandas as pd
import os
from bokeh.io import output_file, show, save
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.models.widgets import Button
from bokeh.embed import components
#import numpy as np
import matplotlib.pyplot as plt
from goodreads import client

books = pd.read_csv('books.csv', sep=',', error_bad_lines=False, encoding="latin-1")
books.columns = ['bookID','ISBN', 'bookTitle','imageUrlM']
#users = pd.read_csv('users.csv', sep=',', error_bad_lines=False, encoding="latin-1")
#users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']
user_recom = pd.read_csv('user_recom.csv', sep=',', error_bad_lines=False, encoding="latin-1")
user_recom.columns = ['userID','book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'book7', 'book8','book9','book10']

book_recom = pd.read_csv('book_recom.csv', sep=',', error_bad_lines=False, encoding="latin-1")
book_recom.columns = ['bookID','book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'book7', 'book8','book9','book10','book11']

#book_sim = pd.read_csv('book_similar.csv', sep=',', error_bad_lines=False, encoding="latin-1")
#book_sim.columns = ['bookISBN','similar']

book_A = pd.read_csv('bookname_A.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookA_list = book_A.values.tolist()
book_B = pd.read_csv('bookname_B.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookB_list = book_B.values.tolist()
book_C = pd.read_csv('bookname_C.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookC_list = book_C.values.tolist()
book_D = pd.read_csv('bookname_D.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookD_list = book_D.values.tolist()
book_E = pd.read_csv('bookname_E.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookE_list = book_E.values.tolist()
book_F = pd.read_csv('bookname_F.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookF_list = book_F.values.tolist()
book_G = pd.read_csv('bookname_G.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookG_list = book_G.values.tolist()
book_H = pd.read_csv('bookname_H.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookH_list = book_H.values.tolist()
book_I = pd.read_csv('bookname_I.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookI_list = book_I.values.tolist()
book_J = pd.read_csv('bookname_J.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookJ_list = book_J.values.tolist()
book_K = pd.read_csv('bookname_K.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookK_list = book_K.values.tolist()
book_L = pd.read_csv('bookname_L.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookL_list = book_L.values.tolist()
book_M = pd.read_csv('bookname_M.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookM_list = book_M.values.tolist()
book_N = pd.read_csv('bookname_N.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookN_list = book_N.values.tolist()
book_O = pd.read_csv('bookname_O.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookO_list = book_O.values.tolist()
book_P = pd.read_csv('bookname_P.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookP_list = book_P.values.tolist()
book_Q = pd.read_csv('bookname_Q.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookQ_list = book_Q.values.tolist()
book_R = pd.read_csv('bookname_R.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookR_list = book_R.values.tolist()
book_S = pd.read_csv('bookname_S.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookS_list = book_S.values.tolist()
book_T = pd.read_csv('bookname_T.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookT_list = book_T.values.tolist()
book_U = pd.read_csv('bookname_U.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookU_list = book_U.values.tolist()
book_V = pd.read_csv('bookname_V.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookV_list = book_V.values.tolist()
book_W = pd.read_csv('bookname_W.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookW_list = book_W.values.tolist()
book_X = pd.read_csv('bookname_X.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookX_list = book_X.values.tolist()
book_Y = pd.read_csv('bookname_Y.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookY_list = book_Y.values.tolist()
book_Z = pd.read_csv('bookname_Z.csv', sep=',', error_bad_lines=False, encoding="latin-1")
bookZ_list = book_Z.values.tolist()

uid=user_recom['userID']
uid=list(uid.values)

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/index1')
def index1():
  return render_template('index1.html')

@app.route('/index2')
def index2():
  return render_template('index2.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/A')
def A():
  return render_template('A.html')

@app.route('/listA')
def listA():
  return render_template('list.html',data=bookA_list,chr='A')  

@app.route('/B')
def B():
  return render_template('B.html')

@app.route('/listB')
def listB():
  return render_template('list.html',data=bookB_list,chr='B')  

@app.route('/C')
def C():
  return render_template('C.html')

@app.route('/listC')
def listC():
  return render_template('list.html',data=bookC_list,chr='C')  

@app.route('/D')
def D():
  return render_template('D.html')

@app.route('/listD')
def listD():
  return render_template('list.html',data=bookD_list,chr='D')  

@app.route('/E')
def E():
  return render_template('E.html')

@app.route('/listE')
def listE():
  return render_template('list.html',data=bookE_list,chr='E')  

@app.route('/F')
def F():
  return render_template('F.html')

@app.route('/listF')
def listF():
  return render_template('list.html',data=bookF_list,chr='F')  

@app.route('/G')
def G():
  return render_template('G.html')

@app.route('/listG')
def listG():
  return render_template('list.html',data=bookG_list,chr='G')  

@app.route('/H')
def H():
  return render_template('H.html')

@app.route('/listH')
def listH():
  return render_template('list.html',data=bookH_list,chr='H') 

@app.route('/I')
def I():
  return render_template('I.html')

@app.route('/listI')
def listI():
  return render_template('list.html',data=bookI_list,chr='I')

@app.route('/J')
def J():
  return render_template('J.html')

@app.route('/listJ')
def listJ():
  return render_template('list.html',data=bookJ_list,chr='J')

@app.route('/K')
def K():
  return render_template('K.html')

@app.route('/listK')
def listK():
  return render_template('list.html',data=bookK_list,chr='K')

@app.route('/L')
def L():
  return render_template('L.html')

@app.route('/listL')
def listL():
  return render_template('list.html',data=bookL_list,chr='L')

@app.route('/M')
def M():
  return render_template('M.html')

@app.route('/listM')
def listM():
  return render_template('list.html',data=bookM_list,chr='M')

@app.route('/N')
def N():
  return render_template('N.html')

@app.route('/listN')
def listN():
  return render_template('list.html',data=bookN_list,chr='N')

@app.route('/O')
def O():
  return render_template('O.html')

@app.route('/listO')
def listO():
  return render_template('list.html',data=bookO_list,chr='O')

@app.route('/P')
def P():
  return render_template('P.html')

@app.route('/listP')
def listP():
  return render_template('list.html',data=bookP_list,chr='P')

@app.route('/Q')
def Q():
  return render_template('Q.html')

@app.route('/listQ')
def listQ():
  return render_template('list.html',data=bookQ_list,chr='Q')

@app.route('/R')
def R():
  return render_template('R.html')

@app.route('/listR')
def listR():
  return render_template('list.html',data=bookR_list,chr='R')

@app.route('/S')
def S():
  return render_template('S.html')

@app.route('/listS')
def listS():
  return render_template('list.html',data=bookS_list,chr='S')

@app.route('/T')
def T():
  return render_template('T.html')

@app.route('/listT')
def listT():
  return render_template('list.html',data=bookT_list,chr='T')

@app.route('/U')
def U():
  return render_template('U.html')

@app.route('/listU')
def listU():
  return render_template('list.html',data=bookU_list,chr='U')

@app.route('/V')
def V():
  return render_template('V.html')

@app.route('/listV')
def listV():
  return render_template('list.html',data=bookV_list,chr='V')

@app.route('/W')
def W():
  return render_template('W.html')

@app.route('/listW')
def listW():
  return render_template('list.html',data=bookW_list,chr='W')

@app.route('/X')
def X():
  return render_template('X.html')

@app.route('/listX')
def listX():
  return render_template('list.html',data=bookX_list,chr='X')

@app.route('/Y')
def Y():
  return render_template('Y.html')

@app.route('/listY')
def listY():
  return render_template('list.html',data=bookY_list,chr='Y')

@app.route('/Z')
def Z():
  return render_template('Z.html')

@app.route('/listZ')
def listZ():
  return render_template('list.html',data=bookZ_list,chr='Z')

@app.route('/book',methods=['GET','POST'])
def book():
  try:
    default_name=53202
    if (request.method == 'POST'):
        B = int(request.values.get("book",default_name))
        #print(book_recom.loc[book_recom['bookID']==B])
        #bookdes = "ISBN : "+books.loc[books['bookID']==B]['ISBN'].values[0]+" Title : "+books.loc[books['bookID']==B]['bookTitle'].values[0]
        Bimg=books.loc[books['bookID']==B]['imageUrlM'].values[0]
        Btitle=books.loc[books['bookID']==B]['bookTitle'].values[0]
        BISBN=books.loc[books['bookID']==B]['ISBN'].values[0]

        #print(Bimg,Btitle,BISBN,len(BISBN))
        if len(BISBN)<10:
            l=10-len(BISBN)
            BISBN='0'*l+BISBN
        Blist=[Bimg, Btitle]
        try:
            gc = client.GoodreadsClient('jz7ZTvCqb3eUPgtYhXvZ0Q', 'CoZb0wPah3A8iDIYCg0HjEkxKuHIcWjN8vkCBrr8Vk')
            book=gc.book(isbn=BISBN)
            bookdes='ISBN-10: '+str(book.isbn)+', ISBN-13: '+str(book.isbn13)+', Title: '+str(book.title)+', Authors: '+str(book.authors)+', Rating Average: '+str(book.average_rating)
            bookdes1=book.description
            booksim=book.similar_books
            bookisbn='http://covers.openlibrary.org/b/isbn/'+str(book.isbn).strip()+'-M.jpg'
        except Exception as e:
            bookdes=Btitle+','+BISBN
            bookdes1='N/A'
            booksim=[]
            bookisbn=Bimg     
            print('Not Found in Good Reads')
        
        '''
        sim_list=book_sim.loc[book_sim['bookISBN']==BISBN]['similar'].values
        sim_list=sim_list.tolist()
        print(len(sim_list))
        for i in sim_list:
          print(i,len(i))
        '''

        #book_recom

        book1=book_recom.loc[book_recom['bookID']==B]['book2'].values
        book2=book_recom.loc[book_recom['bookID']==B]['book3'].values
        book3=book_recom.loc[book_recom['bookID']==B]['book4'].values
        book4=book_recom.loc[book_recom['bookID']==B]['book5'].values
        book5=book_recom.loc[book_recom['bookID']==B]['book6'].values
        book6=book_recom.loc[book_recom['bookID']==B]['book7'].values
        book7=book_recom.loc[book_recom['bookID']==B]['book8'].values
        book8=book_recom.loc[book_recom['bookID']==B]['book9'].values
        book9=book_recom.loc[book_recom['bookID']==B]['book10'].values
        book10=book_recom.loc[book_recom['bookID']==B]['book11'].values
        
        bisbn1=books.loc[books['bookID']==book1[0]]['ISBN'].values[0]
        bisbn2=books.loc[books['bookID']==book2[0]]['ISBN'].values[0]
        bisbn3=books.loc[books['bookID']==book3[0]]['ISBN'].values[0]
        bisbn4=books.loc[books['bookID']==book4[0]]['ISBN'].values[0]
        bisbn5=books.loc[books['bookID']==book5[0]]['ISBN'].values[0]
        bisbn6=books.loc[books['bookID']==book6[0]]['ISBN'].values[0]
        bisbn7=books.loc[books['bookID']==book7[0]]['ISBN'].values[0]
        bisbn8=books.loc[books['bookID']==book8[0]]['ISBN'].values[0]
        bisbn9=books.loc[books['bookID']==book9[0]]['ISBN'].values[0]
        bisbn10=books.loc[books['bookID']==book10[0]]['ISBN'].values[0]

        bimg1=books.loc[books['bookID']==book1[0]]['imageUrlM'].values[0]
        bimg2=books.loc[books['bookID']==book2[0]]['imageUrlM'].values[0]
        bimg3=books.loc[books['bookID']==book3[0]]['imageUrlM'].values[0]
        bimg4=books.loc[books['bookID']==book4[0]]['imageUrlM'].values[0]
        bimg5=books.loc[books['bookID']==book5[0]]['imageUrlM'].values[0]
        bimg6=books.loc[books['bookID']==book6[0]]['imageUrlM'].values[0]
        bimg7=books.loc[books['bookID']==book7[0]]['imageUrlM'].values[0]
        bimg8=books.loc[books['bookID']==book8[0]]['imageUrlM'].values[0]
        bimg9=books.loc[books['bookID']==book9[0]]['imageUrlM'].values[0]
        bimg10=books.loc[books['bookID']==book10[0]]['imageUrlM'].values[0]
        '''
        bimg1='http://covers.openlibrary.org/b/isbn/'+str(bisbn1).strip()+'-M.jpg'
        bimg2='http://covers.openlibrary.org/b/isbn/'+str(bisbn2).strip()+'-M.jpg'
        bimg3='http://covers.openlibrary.org/b/isbn/'+str(bisbn3).strip()+'-M.jpg'
        bimg4='http://covers.openlibrary.org/b/isbn/'+str(bisbn4).strip()+'-M.jpg'
        bimg5='http://covers.openlibrary.org/b/isbn/'+str(bisbn5).strip()+'-M.jpg'
        bimg6='http://covers.openlibrary.org/b/isbn/'+str(bisbn6).strip()+'-M.jpg'
        bimg7='http://covers.openlibrary.org/b/isbn/'+str(bisbn7).strip()+'-M.jpg'
        bimg8='http://covers.openlibrary.org/b/isbn/'+str(bisbn8).strip()+'-M.jpg'
        bimg9='http://covers.openlibrary.org/b/isbn/'+str(bisbn9).strip()+'-M.jpg'
        bimg10='http://covers.openlibrary.org/b/isbn/'+str(bisbn10).strip()+'-M.jpg'
        '''
        btit1=str(books.loc[books['bookID']==book1[0]]['bookTitle'].values[0])
        btit2=str(books.loc[books['bookID']==book2[0]]['bookTitle'].values[0])
        btit3=str(books.loc[books['bookID']==book3[0]]['bookTitle'].values[0])
        btit4=str(books.loc[books['bookID']==book4[0]]['bookTitle'].values[0])
        btit5=str(books.loc[books['bookID']==book5[0]]['bookTitle'].values[0])
        btit6=str(books.loc[books['bookID']==book6[0]]['bookTitle'].values[0])
        btit7=str(books.loc[books['bookID']==book7[0]]['bookTitle'].values[0])
        btit8=str(books.loc[books['bookID']==book8[0]]['bookTitle'].values[0])
        btit9=str(books.loc[books['bookID']==book9[0]]['bookTitle'].values[0])
        btit10=str(books.loc[books['bookID']==book10[0]]['bookTitle'].values[0])
        

        '''
        sbook=[]
        stitle=[]
        cnt=0
        for i in booksim:
            try:
                r = requests.get('https://www.googleapis.com/books/v1/volumes?q=title:'+str(i).strip())
                if (r.status_code==200):
                    rdict = r.json()
                    try:
                        for j in rdict['items'][0]['volumeInfo']['industryIdentifiers']:
                            if (j['type']=='ISBN_10'):
                                sbook.append(j['identifier'])
                                stitle.append(str(i).strip())
                                cnt+=1
                            if cnt==10: break
                    except Exception as e:
                        print(e)        
            except TypeError as e:
                print(e)
            if cnt==10: break

        bisbn1=sbook[0]
        bisbn2=sbook[1]
        bisbn3=sbook[2]
        bisbn4=sbook[3]
        bisbn5=sbook[4]
        bisbn6=sbook[5]
        bisbn7=sbook[6]
        bisbn8=sbook[7]
        bisbn9=sbook[8]
        bisbn10=sbook[9]

        bimg1='http://covers.openlibrary.org/b/isbn/'+str(bisbn1).strip()+'-M.jpg'
        bimg2='http://covers.openlibrary.org/b/isbn/'+str(bisbn2).strip()+'-M.jpg'
        bimg3='http://covers.openlibrary.org/b/isbn/'+str(bisbn3).strip()+'-M.jpg'
        bimg4='http://covers.openlibrary.org/b/isbn/'+str(bisbn4).strip()+'-M.jpg'
        bimg5='http://covers.openlibrary.org/b/isbn/'+str(bisbn5).strip()+'-M.jpg'
        bimg6='http://covers.openlibrary.org/b/isbn/'+str(bisbn6).strip()+'-M.jpg'
        bimg7='http://covers.openlibrary.org/b/isbn/'+str(bisbn7).strip()+'-M.jpg'
        bimg8='http://covers.openlibrary.org/b/isbn/'+str(bisbn8).strip()+'-M.jpg'
        bimg9='http://covers.openlibrary.org/b/isbn/'+str(bisbn9).strip()+'-M.jpg'
        bimg10='http://covers.openlibrary.org/b/isbn/'+str(bisbn10).strip()+'-M.jpg'


        btit1=stitle[0]
        btit2=stitle[1]
        btit3=stitle[2]
        btit4=stitle[3]
        btit5=stitle[4]
        btit6=stitle[5]
        btit7=stitle[6]
        btit8=stitle[7]
        btit9=stitle[8]
        btit10=stitle[9]
        '''
        bimg = [[bimg1,btit1],[bimg2,btit2],[bimg3,btit3],[bimg4,btit4],[bimg5,btit5],[bimg6,btit6],[bimg7,btit7],[bimg8,btit8],[bimg9,btit9],[bimg10,btit10]]
        
        return render_template('book.html', bookisbn=bookisbn,bookdes=bookdes,bookdes1=bookdes1,booksim=booksim,bimg=bimg,Blist=Blist)

  except Exception as e:
      print(e)
      #flash(e)
      return render_template('index.html')
  
# Route for handling the login page logic
@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        if request.form['username'] in uid and request.form['password'] in uid:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('user',usrid=request.form['username']))
    return render_template('login.html', error=error)  

@app.route('/user/<usrid>')
def user(usrid):
    U=int(usrid)
    
    #rec=users.loc[(users['userID']==U)]
    userdes= 'UserID: '+str(usrid)#+' Location: '+str(rec['Location'].values[0])+', Age :'+str(rec['Age'].values[0])  
    userate10=ratings.loc[(ratings['userID']==U)&(ratings['bookRating']==10)]
    rate10list=[]
    if len(userate10['ISBN'].values)>0:
        for i in userate10['ISBN'].values:
            try:
                bl=books.loc[books['ISBN']==i]['bookTitle'].values[0]
                rate10list.append(bl)
            except IndexError as e:
                print(e)
    
    book1=user_recom.loc[user_recom['userID']==U]['book1'].values
    book2=user_recom.loc[user_recom['userID']==U]['book2'].values
    book3=user_recom.loc[user_recom['userID']==U]['book3'].values
    book4=user_recom.loc[user_recom['userID']==U]['book4'].values
    book5=user_recom.loc[user_recom['userID']==U]['book5'].values
    book6=user_recom.loc[user_recom['userID']==U]['book6'].values
    book7=user_recom.loc[user_recom['userID']==U]['book7'].values
    book8=user_recom.loc[user_recom['userID']==U]['book8'].values
    book9=user_recom.loc[user_recom['userID']==U]['book9'].values
    book10=user_recom.loc[user_recom['userID']==U]['book10'].values
    
    bimg1=books.loc[books['bookID']==book1[0]]['imageUrlM'].values[0]
    bimg2=books.loc[books['bookID']==book2[0]]['imageUrlM'].values[0]
    bimg3=books.loc[books['bookID']==book3[0]]['imageUrlM'].values[0]
    bimg4=books.loc[books['bookID']==book4[0]]['imageUrlM'].values[0]
    bimg5=books.loc[books['bookID']==book5[0]]['imageUrlM'].values[0]
    bimg6=books.loc[books['bookID']==book6[0]]['imageUrlM'].values[0]
    bimg7=books.loc[books['bookID']==book7[0]]['imageUrlM'].values[0]
    bimg8=books.loc[books['bookID']==book8[0]]['imageUrlM'].values[0]
    bimg9=books.loc[books['bookID']==book9[0]]['imageUrlM'].values[0]
    bimg10=books.loc[books['bookID']==book10[0]]['imageUrlM'].values[0]
    
    bisbn1=books.loc[books['bookID']==book1[0]]['ISBN'].values[0]
    bisbn2=books.loc[books['bookID']==book2[0]]['ISBN'].values[0]
    bisbn3=books.loc[books['bookID']==book3[0]]['ISBN'].values[0]
    bisbn4=books.loc[books['bookID']==book4[0]]['ISBN'].values[0]
    bisbn5=books.loc[books['bookID']==book5[0]]['ISBN'].values[0]
    bisbn6=books.loc[books['bookID']==book6[0]]['ISBN'].values[0]
    bisbn7=books.loc[books['bookID']==book7[0]]['ISBN'].values[0]
    bisbn8=books.loc[books['bookID']==book8[0]]['ISBN'].values[0]
    bisbn9=books.loc[books['bookID']==book9[0]]['ISBN'].values[0]
    bisbn10=books.loc[books['bookID']==book10[0]]['ISBN'].values[0]

    '''
    bimg1='http://covers.openlibrary.org/b/isbn/'+str(bisbn1).strip()+'-M.jpg'
    bimg2='http://covers.openlibrary.org/b/isbn/'+str(bisbn2).strip()+'-M.jpg'
    bimg3='http://covers.openlibrary.org/b/isbn/'+str(bisbn3).strip()+'-M.jpg'
    bimg4='http://covers.openlibrary.org/b/isbn/'+str(bisbn4).strip()+'-M.jpg'
    bimg5='http://covers.openlibrary.org/b/isbn/'+str(bisbn5).strip()+'-M.jpg'
    bimg6='http://covers.openlibrary.org/b/isbn/'+str(bisbn6).strip()+'-M.jpg'
    bimg7='http://covers.openlibrary.org/b/isbn/'+str(bisbn7).strip()+'-M.jpg'
    bimg8='http://covers.openlibrary.org/b/isbn/'+str(bisbn8).strip()+'-M.jpg'
    bimg9='http://covers.openlibrary.org/b/isbn/'+str(bisbn9).strip()+'-M.jpg'
    bimg10='http://covers.openlibrary.org/b/isbn/'+str(bisbn10).strip()+'-M.jpg'
    '''

    btit1=str(books.loc[books['bookID']==book1[0]]['bookTitle'].values[0])
    btit2=str(books.loc[books['bookID']==book2[0]]['bookTitle'].values[0])
    btit3=str(books.loc[books['bookID']==book3[0]]['bookTitle'].values[0])
    btit4=str(books.loc[books['bookID']==book4[0]]['bookTitle'].values[0])
    btit5=str(books.loc[books['bookID']==book5[0]]['bookTitle'].values[0])
    btit6=str(books.loc[books['bookID']==book6[0]]['bookTitle'].values[0])
    btit7=str(books.loc[books['bookID']==book7[0]]['bookTitle'].values[0])
    btit8=str(books.loc[books['bookID']==book8[0]]['bookTitle'].values[0])
    btit9=str(books.loc[books['bookID']==book9[0]]['bookTitle'].values[0])
    btit10=str(books.loc[books['bookID']==book10[0]]['bookTitle'].values[0])

    bimg = [[bimg1,btit1],[bimg2,btit2],[bimg3,btit3],[bimg4,btit4],[bimg5,btit5],[bimg6,btit6],[bimg7,btit7],[bimg8,btit8],[bimg9,btit9],[bimg10,btit10]]
    
    title = 'user'
    userate=ratings.loc[(ratings['userID']==U)&(ratings['bookRating']>0)]
    rates=userate.groupby('bookRating').count()
    output_file('./templates/test.html',mode='inline')
    rating = list(rates.index)
    rating = [str(i) for i in rating] 
    p = figure(x_range=rating, plot_height=250, title="Rating Counts",x_axis_label='Ratings',y_axis_label='Number of books')
    p.vbar(x=rating, top=list(rates['ISBN'].values), width=0.9)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    script, div = components(p)
    return render_template('user.html', title = title,userdes = userdes ,script = script, div = div, rate10list=rate10list, bimg=bimg)
if __name__ == '__main__':
  #app.run(port=7000)
  app.run(debug='True')
