#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("done")

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "plucky-vision-156618",
  "private_key_id": "269e31418b41ae567b240bdc55d1bb5bd4e324ca",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDta3/8RdRYApa6\nK0VbkAsZ/Xi+S7VYrR1zB601BBWea3C2QPstJSsPwKXxFTZ9Olud35JZlfcB9QCF\nx4wi2h1Lx2WA2xaMiHgz2d7su7xJiCut2hIK4Gh2gjg1t7e0D7WZsFKeqqGdIBk5\nAgk+EJPanRZ4F8BnzcR20V+jamHnA9RzTkumvqdpQfAeURwWDPww9XEz04mLcLek\nL0Kg6rfR/lw4s7uz0Z1lgvQnFh5K+3D3R39eNB6iMocfErBTDQiYHjCpbeaPJ0Ka\nWv/XY55Up4KUy/pytw0sK1fH4HjLT3RCPKk0ew+1qcVolxCY9yVSqE1mCnA4jlB2\nkk0Luv0jAgMBAAECggEBAJxTfCIPmJGaosRSWYjAf47NZwNltjJ9SjbDhzixR8rX\n048tmjVPk9r7bkgfP5GVK134J9T0+X9AYuezTIJmO4P59suxdldyRDNf8XjO5FtG\nXfxK6jZfLGlbtMcqALt+3IQlpUDz+RYMXI881/kV0UTQykqo2PeAdSwHEIH5Oh1x\nE2W+ue8c3IlD97cTB7XV1OZRG43En6639MZoxgpC2lIVq9pKxdEN6jR1UEdU0iti\ngnRHqEyEAkYGG5bXheOK1tG1r9KhAWxOqQTcMBJLlYepP1xSWhTAEOGRWdPWkcGD\nxaoLSU+tYSKio7QiXD85zLCXVY4iRPsdBHkg/XBkqwECgYEA++XPciG/N3ZtuZaN\nRwCjy/9majBJKUAc3KmEmLBfu8Z4+xoFdxXMEYDAQDw8byesGtx4a6jzoTO6F6/E\n2Cq/Zzi1TEs4XjkGY7MYmQMnCazR5ZnOw5p5GHXmNh0jweEga7Jaq9nh4m72CnBk\n5JZEGqsOABsDauZ1OWZNPvRmp3sCgYEA8UlUhGOLqQ3g1OMDuI4Rs/c99FI6d+jZ\nk8x0fEPUhUU7iyt0ppmJzGzhDJfDy815Zhsg6yb9AkKpmCx2NHMATcS13QKC3lmj\n1EBbz6FKTDZRKGKhxJ0L5kZAORTbDknUoHKL+NPd5PJj9a9bLNr8oQqs9vpkyJZV\ndjttEotPPHkCgYEAtCU8/119F9gdTo2Jyc5+VcT4ZFbV66dLPNAK4Pu561tcaA/K\n+she4eGXHBk4CzJvFeK4SB5S5eVNX+U3PHUN328h0Uc2L8ROeny5yawEfhnXHoGp\n6h+OHN0sX2TljqFHA15RE/fFYJ+EXCDXNtb0K7JLV+35urjH+t3bvnsg8wMCgYAd\n8XC4oTXiu+Mr6CQ9EfxmbgdVO6Mf4Fin+9Z02WIVS9sw0Sq/xgwQv25KRsc4kn4/\nSpySMhtx3V34kYP1zFO8Uu4SyE3/U/Z9z6LVKHn07USzE1Jp+OdSI2Oy8cChjE4D\nv1NZhMljsSTwh1t0PJTfU1jVqYs6TVW7v3Iwu/MQWQKBgAc18oFQrqbKbz2Ug6Sf\nKipE0KzVTBsq08mWNZsot+TfCEaupcr8prAdOvamtkCShedb0tZkt803F5ah9ieN\nfgrt3nW2mvt9+Vew7IpYh3z048DDvUGZuGuIu1F+i2qWMONmt1f8U9aLl+6ehE3B\nwOauMzc+aHRz6hdGgIUM3Bo0\n-----END PRIVATE KEY-----\n",
  "client_email": "personal@plucky-vision-156618.iam.gserviceaccount.com",
  "client_id": "117766175886450184086",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/personal%40plucky-vision-156618.iam.gserviceaccount.com"
}"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
