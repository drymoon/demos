import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
     
class MainHandler(tornado.web.RequestHandler):
	def get(self):
	#	self.render("index.html")
		self.write("Tornado") 
def main():
    	application = tornado.web.Application([
    	(r"/", MainHandler),
    	])
    	http_server = tornado.httpserver.HTTPServer(application)
    	port = int(os.environ.get("PORT", 5002))
    	http_server.listen(port)
    	tornado.ioloop.IOLoop.instance().start()
     
if __name__ == "__main__":
    main()
