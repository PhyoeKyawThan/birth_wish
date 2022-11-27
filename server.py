from flask import Flask, render_template, redirect, request, url_for
import pymongo
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception


#create flask app
app = Flask(__name__)

#create db
client = pymongo.MongoClient("mongodb+srv://kyawthanphyoe9:domakpassword@cluster0.ye12rer.mongodb.net/?retryWrites=true&w=majority")
db = client.message

#index
@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    forme = request.form['tome']
    db.messages.insert_one({'message': forme})
    return render_template('index.html')
  else:
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()
