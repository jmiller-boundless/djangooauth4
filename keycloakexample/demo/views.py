from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import jwt

key=b'-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAksrHKiEzprrTfPLCk9ehdk32eEvP7Xxs73lzdTim9CzYH4PF/j8WfobO3bkpnFDXxDMoazvqyYU3PTioybjnuOV+iGi/OvCn7G165AWK+dvQS9jPkPmDANGb5uZOnVhf2SrrquZLNWQ8yC5zfmKgJZX+jtEeQL5SJGgAM6Z/gELdv6GJf2IKKocTmfvb7NoPz1KXqQoYGhL49dB+npW7/FiTTyVuJjTMjoG0NWameViGZiU92GiAETiCYK7HaTtRZry2MUdCEoTBE4S2sJaIwPs36OjfjgmzQOlYZE3bXewbv509rlc5g+YiPqXvhT5zILrDdMMeunYjBemm2J3nlQIDAQAB-----END PUBLIC KEY-----'

@login_required
def home(request):
    # Old: opresult.mako
    return render_to_response("demo/result.html", 
    {"userinfo": request.session['userinfo'] if 'userinfo' in request.session.keys() else None,
    "id_token": request.session['id_token'],"access_token": request.session['access_token'],
    })

def unprotected(request):
    return render_to_response("demo/unprotected.html")
