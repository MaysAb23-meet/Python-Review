def create_youtube_video(title,descriotion):
	uvid={"title": title,"description": descriotion,"likes":0,"dislikes":0,"comments":{}}
	return uvid

def like (uvid):
	if "likes" in uvid:
		uvid["likes"]=uvid["likes"] + 1
	
	return uvid

def dislike(uvid):
	if "dislikes" in uvid:
		uvid["dislikes"]=uvid["dislikes"] + 1

def add_comment(uvid,username,comment_text):
	uvid["comments"][username]= comment_text
	return uvid



video= create_youtube_video("vid2","its a vid")
like(video)
dislike(video)
add_comment(video,"mays","meh")
for i in range(495):
 	like (video)
print(video)
	
	
