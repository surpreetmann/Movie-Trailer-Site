def sort(a,b,c):
    mylist=[a,b,c]
    mylist=sorted(mylist,key=lambda x: x.name)
    for i in mylist:
        print("Name of film=" + i.name + ", Image Link=" + i.image_url + ",Trailer Link=" + i.trailer_youtube_url)

        
    
    
        
