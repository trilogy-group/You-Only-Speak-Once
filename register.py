from pydub import AudioSegment
from pydub.utils import make_chunks
import requests



users = [
    "uchokshi",
    "kushalchordiya",
    "sahil.marwaha",
    "mdave",
    "yogeshkumar",
    "vinayak.sachdeva",
    "shivamgupta",
    "sbanga",
    "samyaksamdariya",
    "rohit.kumar1",
    "quintuslamar",
    "omkardeshpande",
    "manrajkotiya",
    "jenishmonpara",
    "dhanrajabhishek",
    "bhoomil.gohel",
    "ayodejiodesile",
    "ashwanth.r",
    "arumullasriram",
    "archanaghei",
    "aprusty",
    "andreikharytonenka",
    "amandal",
    "aman.jain",
    "agaba",
    "abraganza",
    "abedi",
    "adityapurohit",
    "vicky.biswas",
    "siddhanthirve",
    "shubhankaramitabh",
    "sahilbajaj",
    "rakshitbhatt",
]




for i in users:
    url = "https://5000-aqua-locust-p0lj31r8.ws.legacy.devspaces.com/register/"+i

    payload={'username': i}

    files=[
        ('file',('arpit3.wav',open("audio_sample/"+i+".wav",'rb'),'audio/wav'))
    ]

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        response_Json = response.json()
        print(response_Json["result"])

