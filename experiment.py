import sys
from pydub import AudioSegment
from pydub.utils import make_chunks
import requests


filename = None

if len(sys.argv) < 2:
    print("pls enter file name as argument in cmd")
    exit()

filename = sys.argv[1]
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


myaudio = AudioSegment.from_file("video_sample/"+filename+".wav" , "wav")
chunk_length_ms = 10000
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 10 seconds
newHeaders = {'Content-type': 'multipart/form-data',"Connection": "keep-alive","Accept-Encoding": "gzip, deflate, br"}

#
for i, chunk in enumerate(chunks):
    flag = 0
    chunk_name ="audio_sample/"+filename+"-chunk-"+str(i)+".wav"
    from pydub import AudioSegment
    chunk.export(chunk_name, format="wav")
    for j in users:

        url = "https://5000-aqua-locust-p0lj31r8.ws.legacy.devspaces.com/login/"+j
        payload={'username': j}
        files=[('file',(chunk_name+'.wav',open(chunk_name,'rb'),'audio/wav'))]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        if response.status_code == 200:
            response_Json = response.json()
            if response_Json["result"] == "true":
                print("in chunk "+chunk_name+"speaker found is "+response_Json["username"])
                flag = 1
                break
    if(flag == 0):
        print("no user is found in chunk "+chunk_name)

