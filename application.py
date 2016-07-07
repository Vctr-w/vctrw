from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

<<<<<<< HEAD
# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))
=======
application.config.from_object('config2')

#s3_client = boto3.client(
#    's3',
#    aws_access_key_id = application.config2['AWS_ACCESS_KEY_ID'],
#    aws_secret_access_key = application.config2['AWS_SECRET_KEY']
#)

s3_resource = boto3.resource(
	's3',
    aws_access_key_id = application.config['AWS_ACCESS']['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key = application.config['AWS_ACCESS']['AWS_SECRET_KEY']
)

@application.route('/', methods = ['GET', 'POST'])
@application.route('/index', methods = ['GET', 'POST'])
def index():
	return render_template('index.html', 
				title='Home')

@application.route('/blog', methods = ['GET', 'POST'])
@application.route('/blog/<int:page>', methods = ['GET', 'POST'])
def blog(page = 1):
	blogs = Blog.select().order_by(Blog.timestamp.desc()).paginate(page, application.config['BLOGS_PER_PAGE'])

	return render_template('blog.html',
				title='Blog',
				blogs = blogs)

@application.route('/blogpost/<urlTitle>', methods = ['GET', 'POST'])
def blogpost(urlTitle):
	blog = Blog.select().where(Blog.urlTitle == urlTitle).first()	
	
	return render_template('blogpost.html',
				title = blog.title,
				blog = blog)

@application.route('/aboutme')
def aboutme():
	return render_template('aboutme.html',
				title='About me')

@application.route('/gallery')
def gallery():
	images = s3_resource.Bucket(application.config['S3_BUCKET']).objects.all()
>>>>>>> db04442... Website ready to go

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
