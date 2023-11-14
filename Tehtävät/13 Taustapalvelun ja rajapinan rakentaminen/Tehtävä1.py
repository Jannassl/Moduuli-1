from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/alkuluku')

def alkuluku():
    args = request.args
    luku = int(args.get("luku"))

    if luku % 2 == 0 or luku % 3 == 0:
        vastaus = {"number": luku,
                   "isPrime": False
                   }
        print(vastaus)
    else:
        vastaus = {"number": luku,
                   "isPrime": True
                   }
        print(vastaus)

if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


