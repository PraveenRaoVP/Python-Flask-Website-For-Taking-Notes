from website import create_app


app = create_app()
app.route('/')

if __name__=="__main__":
     app.run(debug=True)
     

