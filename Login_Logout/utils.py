import uuid
from django.conf import settings




def generate_ref_code():
    return str(uuid.uuid4()).replace('-', '')[:12]


    

def generate_refferal_link(request):
    base_url = settings.BASE_URL
    if request.user.is_authenticated:
        try:
            user_sponsor = request.user.sponsor
            refferal_code = user_sponsor.code
            
            refferal_link = f"{base_url}/Login_Logout/Register/?ref_code={refferal_code}"
            # print(refferal_link)
            return refferal_link
        except Sponsor.DoesNotExist:
            return f"{base_url}/Login_Logout/Register/"
    else:
        return f"{base_url}/Login_Logout/Register/"