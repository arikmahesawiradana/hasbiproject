# Import required modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import *

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("hasbi.json", scope)
client = gspread.authorize(creds)
sheet = client.open("ESP32 Data").sheet1
def index():
    return "Sukses"

def send_data():
    try:
        data0 = request.args.get('nama')
        data1 = request.args.get('volume')
        data3 = request.args.get('tanggal')
        data4 = request.args.get('jam')
        insertRow = [data0, data3, data4, data1]
        sheet.insert_row(insertRow, 2)
        return "sukses"
    except:
        return "gagal"

app = Flask(__name__)
app.add_url_rule("/", "index", index)
app.add_url_rule("/send", "send", send_data)

if __name__ == "__main__":
    app.run(debug=True)
