from bottle import run, get, static_file, post

COMMAND_PAGE = '''
  <!DOCTYPE html>
  <html>
  <head>
    <title>Commands</title>
  </head>
  <body style='background-size: cover;; background-image: url(\"/static/WebisteBackground.png\");'>
    <center>
      <h1 style='font-family:Cooper Black; font-size: 5em;'>Commands</h1>
      <br>
      </center>
      <h2>
        Commands:
        <br>
        <br>
          '/commands' :
          <br>
          Displays a list of commands.
        <br>
        <br>
          '/youtube/ID_GOES_HERE' :
           <br>
            Displays a youtube video within the window/webpage; all you have to do is enter the id of the video.
          <br>
          <br>
            '/youtube' :
            <br>
            Shows; how to get and insert a youtube videos id into the url for the video to display within the webpage
  <center>
  </center>
</body>
</html>
'''

START_PAGE = '''
  <!DOCTYPE html>
  <html>
  <head>
    <link rel="icon" href="/static/icon.ico">
    <title>TylerR</title>
  </head>
  <body style='background-size: cover;; background-image: url(\"/static/WebisteBackground.png\");'>
  <center>
    <img src='/static/TylerR.png' style="width:300px;height:300px;">
    <h1 style="font-family:Cooper Black; font-size: 7em;"><b>DrummerTyler<b></h1>
    <br>
    <a href='/commands' style='font-size: 5em;' target='_blank'>Commands</a>
  </center>
  </body>
  </html>
  '''

YOUTUBE_PAGE = '''
  <!DOCTYPE html>
  <html>
  <body style='background-size: cover;; background-image: url(\"/static/BlackGrunge.png\");'>
  <center>
  <br>
  <br>
  <br>
  <iframe width="420" height="345" src="https://www.youtube.com/embed/{}">
  </iframe>
  </center>
  </body>
  </html>
  '''


@get('/')
def main():
    return START_PAGE.replace('', '')


@get('/youtube/<id>')
def youtube(id):
    return YOUTUBE_PAGE.replace('{}', id)


@get('/youtube')
def youtube_error():
    return '''Please enter an ID.   e.g https://main.drummertyler.repl.co/youtube/ID_GOES_HERE
  <br>
  https://www.youtube.com/watch?v=YYLw6tyx42U 
  <br>
  This Bit -- YYLw6tyx42U '''


@get('/static/<name>')
def post_image(name):
    image = static_file(name, './static')
    return image


@get('/commands')
def commands():
    return COMMAND_PAGE


@get('/hello')
def hello():
    return '<b>Hello World</b>'


run(debug=True, host='0.0.0.0')
