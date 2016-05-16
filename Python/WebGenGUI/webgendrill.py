import webbrowser




def write(text):
    f = open('summersale.html', 'w')


    message = """<html>
    <head></head>
    <body><p>%s</p></body> 
    </html>"""%text

    f.write(message)
    f.close()

    
