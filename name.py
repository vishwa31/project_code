import firebase_admin
from firebase_admin import auth, firestore, storage, credentials

#------------------------------------firebase database---------------------------------------
cred = credentials.Certificate("/content/build-d6b43-firebase-adminsdk-2mh7i-8b5622d29c.json")
firebase_app = firebase_admin.initialize_app(cred)
store = firestore.client()


#---------------------------------Auth's Code-------------------------------------------------
user = auth.create_user(
    email='vish00@gmail.com',
    email_verified=False,
    password='124353')
print('Sucessfully created new user: {0}'.format(user.uid))


#--------------------------------------login------------------------------------------------
def login(emailofuser,passwordofuser):
  uid = ""
  message = ""
  try:
      user = auth.get_user_by_email(emailofuser)
      message = "successfully created new user"
      uid = user.uid
  except:
      message = "user not there in firebase!"
      
  return{"uid":uid, "message":message}
  
  
#-----------------------------------------Sign Up---------------------------------------------

def signUp(emailOfUser,passwordOfUser):
uid = ""
message =""
try:
  user = auth.create_user(email=emailOfUser,
                          email_varified=False,
                          password=passwordOfUser)
                         
   message = "Successfully created new user"
   uid = user.uid
except:
   message = "User Already There"
   
   return {"uid":uid, "message":message}


 #----------------------------------update the user profile-----------------------------------------
 def updateUserData(uid,dit):
 
   dit_user_details = {}
   dit_user_details['name'] = dit["name"]
   dit_user_details['email'] = dit["email"]
   dit_user_details['number'] = dit["number"]
   dit_user_details['image'] = dit["image"]
   dit_user_details['desp'] = dit["desp"]
   dit_user_details['location'] = dit["location"]
   dit_user_details['dob'] = dit["dob"]
   dit_user_details['gender'] = dit["gender"]
   dit_user_details['passion'] = dit["passion"]
   dit_user_details['job'] = dit["job"]
   dit_user_details['company'] = dit["company"]     
  store.collection("users").document(uid).set(dit_user_details)
  
 dit = {}
 dit["name"] = "vish"
 dit["email"] = "vish00@gmail.com"
 dit["number"] = "0101010101"
 dit["image"] = ""
 dit["desp"] = "single"
 dit["location"] = { 
                        "coordinate" : {"lat":22.3071, "lng":73.18100},
                        "city" : "pune",
                        "state" : "maharashtra",
                        "country" : "india"
                    }
 dit["dob"] = "01/09/2000"
 dit["gender"] = "female"
 dit["passion"] = "study"
 dit["job"] = "student"
 dit["company"] = "abcd"
 
 
 #-------------------------------------get the feed--------------------------------------------------
 def getfeed(country, gender):
 docs = store.collection("users").where("gender","==",gender).stream{}
 
 dit = {}
 for doc in docs:
     if doc.to_dict().get("location").get("country") == country:
	    dit[doc.id] = doc.to_dict()
 return dit 
 
 allprofiles = getfeed("male","india")
 
 
 #------------------------------------match-------------------------------------------
 def swipefun(uidA, uidB, isA_yes, isB_yes, firsttime):
 
   dit = {}
   
   dit["uid_A"] = uidA
   dit["uid_B"] = uidB
   dit["isuserA_yes"] = isA_yes
   dit["isuserB_yes"] = isB_yes
   dit["istheotherusershownprofileatleastonce"] = firsttime
   dit["createdAt"] = firestore.SERVER_TIMESTAMP
   
   store.collection("swipes").add(dit)
   
   uidA = "0sOoi8Bacdd4satkzfK3I9pvy5p8"
   uidB = "0sOoi8Bacdd4satkzfK3I9pvy5p9" 
   isA_yes = true
   isB_yes = false
   
   firsttime = false 
   
   swipefun(uidA, uidB, isA_yes, isB_yes, firsttime)
   
   def matchfun(uid):
        docs = store.collection("swipes").stream()
   ditswipes = {}
   for doc in docs:
   
   if doc.to_dict.get("uid_A") == uid or doc.to_dict.get("uid_B") == uid:
       ditswipes[doc.id] = doc.to_dict{}
	   
   return ditswipes 
	
 
 
                         
