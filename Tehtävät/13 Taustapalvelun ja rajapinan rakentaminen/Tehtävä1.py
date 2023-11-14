from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/alkuluku/<luku>')

def alkuluku():
    args = request.args
    luku = float(args.get("luku"))

    if luku % 2 == 0 or luku % 3 == 0:
        vastaus = {"number": luku,
                   "isPrime": False
                   }
        return str(vastaus)
    else:
        vastaus = {"number": luku,
                   "isPrime": True
                   }
        return str(vastaus)

if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


