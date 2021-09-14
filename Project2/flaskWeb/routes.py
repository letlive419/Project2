from flaskWeb import app,forms , api_methods
from flask import request, render_template

@app.route('/')
@app.route('/home')
def index():
    form1 = forms.studentForm(request.form)
    return render_template('index.html', form = form1)

@app.route('/booktitle', methods=['GET','POST'])
def booktitle():
     form2 = forms.studentForm(request.form)
     if request.method == 'POST':
         selected_title = request.form['title']
         top_titles = api_methods.request_title(selected_title)
         lst_bookTitles = []
         for i in top_titles["results"]:
            book_title = (i["book_author"], i["summary"], i["publication_dt"])
            lst_bookTitles.append(book_title)
         return render_template("BookTitleResponse.html", response=lst_bookTitles)

     return render_template('BookTitle.html', form = form2)

@app.route('/bookauthor',methods=['GET','POST'])
def bookauthor():
     form3 = forms.studentForm(request.form)
     if request.method == 'POST':
         author_name = request.form['author']
         books_byauthor = api_methods.request_author(author_name)
         lst_titles= []
         for i in books_byauthor["results"]:
             title = (i["book_title"],i["publication_dt"])
             lst_titles.append(title)
         return render_template("BookAuthorResponse.html",response=lst_titles)
     return render_template('BookAuthor.html', form = form3)

@app.route('/booklist',methods=['GET','POST'])
def booklist():
     form4 = forms.studentForm(request.form)
     if request.method == 'POST':
         selected_genre = request.form['list_title']
         selected_date = request.form['date']
         top_bydate = api_methods.request_date(selected_date,selected_genre)
         lst_bookList = []
         for i in top_bydate["results"]:
             titles = (i["books"]["title"], i["books"]["author"], i["books"]["rank"])
             lst_bookList.append(titles)
         return render_template("BookTitleResponse.html", response=lst_bookList)
         return top_bydate
     return render_template('BookList.html', form = form4)
