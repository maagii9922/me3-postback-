jokes = {
    u'холбоо барих': [u"""холбоо барих-1.""", u"""холбоо барих-2."""],
    u'түгээмэл асуулт хариулт': [u"""түгээмэл асуулт хариулт-1.""", u"""түгээмэл асуулт хариулт-2"""],
    u'эхлэх': [u"""эхлэх-1""", u"""эхлэх-2."""]
}


cont = []
for cc in jokes['холбоо барих']:
    cont.append({
                                "title": "Холбоо барих sajdfksadj f;lsadjf s;djfaslkj flsadj f;lsadjf s;j;lsadjfl ksjlsj sf;lslf jsldjf sdjfsldjfsajfowijfoiarj wp8uf wrjfa98 wru0waug 9p8aeur adsf 9a8s0r9p8saud g0sa uf9f8a rf9a8sru f09airf8a90i",
                                "subtitle":"Бид компанийн бүтээгдэхүүн үйлчилгээтэй холбоотой санал хүсэлтийг ажлын өдрүүдэд 8:30-18:00 цагт хүлээн авч шуурхай шийдвэрлэнэ.",
                                "image_url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/174405334_259070492629794_2304217932548921388_n.png?_nc_cat=110&ccb=1-3&_nc_sid=58c789&_nc_ohc=vE2j43xB3AYAX-ezABC&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=8a1b1ee5319c0a5443b52c0146247d09&oe=609EE59D",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": cc,
                                    "payload": cc
                                }
                                
                                ]
                            }
                        )
print(cont)