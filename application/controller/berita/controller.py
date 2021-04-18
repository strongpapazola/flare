from application.config.config import *
from application.helper import *
from application.controller.berita.models import *


berita = Blueprint('berita', __name__, static_folder = 'application/upload/foto_berita', static_url_path="/media")

@berita.route("/get_berita", methods=["GET"])
def get_berita():
    db = MongoHelper()
    if request.args:
        dataload = db.loads('berita', 'args')
    else:
        dataload = db.loads('berita')
        dataload = db.filterfield(dataload, ['_id','judul','foto'], True)
    return json_response(db.json(dataload), 200)

@berita.route("/insert_berita", methods=["POST"])
def insert_berita():
    user = JwtAuth().role("USER")
    schema = SetRules()
    schema.struct('judul','str',"required")
    schema.struct('isi','str',"required")
    schema.struct('waktu_baca','int',"required")
    schema.struct('foto','str','optional')
    schema.struct('sumber_foto','str','optional')
    schema.struct('jumlah_pembaca','int','optional')
    schema.struct('kategori','list')
    schema.struct('komentar','list')
    schema.struct('updated','list')
    schema.struct('is_aktif','int')

    schema.data['updated'] = [
        {
            "id_user": user.data['user_id'],
            "updated_at": Global_var.Time('now')
        }
    ]
    schema.data['is_aktif'] = 2
    data = schema.check_key()
    # insert = MongoHelper().insert('berita', data)
    return json_response(data, 200)

@berita.route("/update_berita", methods=["PUT"])
def update_berita():
    user = JwtAuth().role("USER",show=True)
    schema = SetRules()
    schema.validate('_id',"required")
    schema.validate('judul',"required")
    schema.validate('isi',"required")
    schema.validate('waktu_baca',"required")
    schema.optional(('foto', 'sumber_foto','jumlah_pembaca'))
    schema.data['kategori'] = []
    schema.data['komentar'] = []
    schema.data['is_aktif'] = 1
    schema.set_key(("_id","judul","isi","kategori","foto","sumber_foto","jumlah_baca","waktu_baca","is_aktif","komentar"))
    data = schema.check_key()
    data['_id']
    data = {"$set":data}
    data['$push'] = {
            "updated": {
                "id_user": user.data['user_id'],
                "updated_at": Global_var.Time('now')
            }
        }
    # update = MongoHelper().update('berita', {"_id": ObjectId(schema.check_key()["_id"])}, data)
    return json_response(data, 200)

# {
#     "judul" : "Judul Berita",
#     "isi" : "Isi berita",
#     "kategori": [],
#     "updated" : [
#         {
#             "id_user":"09827349yfg2jd9m8024md34",
#             "updated_at": "82736948763"
#         }
#     ],
#     "foto" : "berita_29830472837.png",
#     "sumber_foto" : "https://example.com/image.png",
#     "jumlah_pembaca" : 12,
#     "waktu_baca" : 5,
#     "is_aktif" : 1,
#     "komentar": [
#         {
#             "id_user": 
#             "komentar" : "comment",
#             "created_at": 82736948762,
#             "id_user": "09827349yh92jd9m8024md34"
#         }
#     ]
# }


# //kategori
# {
#     "_id": "987h0887onas87dn78s",
#     "nama": "AI",
#     "foto" : "berita_29830472837.png",
#     "is_aktif": 1
# }

# // user :
# {
#     "_id": "09827349yh92jd9m8024md34",
#     "email": "strongpapazola@gmai.com", //wajib
#     "password": "o97d2ho3hdpo72no3duwefsd", //wajib
#     "nama": "strongpapazola",
#     "phone": "+62822123123123",
#     "jenis_kelamin": 1, //1 = laki, 2 = pr
#     "foto": "users_29830472837.png",
#     "alamat": "jalan asdasd",
#     "registered_at": 82736948762,
#     "is_register": 1, //1 sudah, 2 belum
#     "is_aktif": 1, //matiin akun
#     "forget_token": "032uyihe2duinoulwjenjd",
#     "token_fcm": null,
#     "roles": [1,2,3], //1 = customer, 2 = penulis, 3 = admin
#     "bookmark": [
#         {
#             "id_berita": "lf7834hof8hsiduhfljkshd",
#             "is_aktif": 1, //matiin akun
#             "created_at": 82736948762
#         }
#     ]
# }

