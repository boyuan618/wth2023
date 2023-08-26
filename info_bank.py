from lib.startup import init_app

URL = "http://127.0.0.1:10000/google_results"

app = init_app(URL)

if app:
    try:
        app.run(host="0.0.0.0", port=10001, debug=True)
    
    except KeyboardInterrupt:
        print('[*] Keyboard Interrupt detected. Terminating application....')
else:
    print('[!] Couldn\'t start Application. For more details, please check logs')