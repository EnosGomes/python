import requests
import json

url = "https://portal.cfm.org.br/api_rest_php/api/v1/medicos/buscar_medicos"

payload = "[{\"useCaptchav2\":true,\"captcha\":\"03AFcWeA4r6Ov4VLMSE2cEgXX5A6Rw2yxVfArJp3OXeg7CZJL2iHGPTdWgTnbkrR-hvMadLXxhBdVTcldASHObAWiigMRBqCs0DRQusJyAz_NwCitvFZja0EAZya4NerGbH9sct8vSZ_BsunO9COg7hByooHgOg_Mb9Z_NeLptvP8rcBLjPM4lzntu08tc9ylnd_kTZfSyVIC7M6Pe6aYxoDC815aTw-bnpVabnQwC13PoJzYNqP55Hm5clxrNcX-9nAvHhp7otXO__EDcJ_3LMl8xfZsZdmfVBGZ4bEbZknnzrAcJvwWv3YeptyK6JrMxOd5TLYD6Lj1hj9P4L4GMnRbZW1jGAnm_nOhJ7031BhdUbJQ_Gag1_wcHdD4J8R53bdfp24-utnLp-vt4gzpeN80YGYC7OpedlFArE8G9DTMSI4kzOPpGtk5_QPMFM220OGmS2b22sjO80REwmC55PuFGow3xsoTWG4IrBtdSZwfD48tWN8Qwb16KBb4FwaSB3-5InFHkkefAuIHARhbIme4BukMXOFnjpFvT46GjvP6SWzE80eO5dJzMdojZoPLk4WkNCYBtfMm9GXFYIpqZ9riQDMUp30ST5tT4AQZrH1aNUJmHC33gVflGkDyJWcIKMp3wNzPh3sVxB6IazqxNVjXuXsZQWuo_1OgFZcSq6GPaJXJeX1uQ2RFkiHD1GroD0YV4qHPkE9AsPzijE_AkVLC1DSigKMOjzyhIu2LbkiHB1Esq5l-VNSg\",\"medico\":{\"nome\":\"\",\"ufMedico\":\"SP\",\"crmMedico\":\"4189\",\"municipioMedico\":\"\",\"tipoInscricaoMedico\":\"\",\"situacaoMedico\":\"\",\"detalheSituacaoMedico\":\"\",\"especialidadeMedico\":\"\",\"areaAtuacaoMedico\":\"\"},\"page\":1,\"pageNumber\":1,\"pageSize\":10}]"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,it;q=0.6,la;q=0.5',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': '_gid=GA1.3.1240153155.1716170581; __utmpk=0; _fbp=fb.2.1716170584875.723985151; PHPSESSID=6ce3e2a6cc45452b3da30dad290370d2; _ga_4R9TTHD8FZ=GS1.1.1716236227.3.1.1716236269.0.0.0; _ga_P7Y8CBXPB2=GS1.1.1716236150.6.1.1716236271.0.0.0; _ga=GA1.1.543811647.1716170581; __utmpk=0',
  'Origin': 'https://portal.cfm.org.br',
  'Referer': 'https://portal.cfm.org.br/busca-medicos/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

values = json.loads(response.text)
print(values['dados'][0]['NM_MEDICO'])