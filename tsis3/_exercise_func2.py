movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}]



#Ex1
def check_score(movie): 
    if(movie['imdb']>5.5):
        return True
    else:
        return False
        
        
i=check_score(movies[3])
if(i):
    print ('True')
else :
    print ('False')



#Ex2
def sublist_score(movies): 
    output_list=[]
    for i in range(0,len(movies)):
        cop_movie=movies[i]
        if cop_movie['imdb']>5.5:
            output_list.append(cop_movie)
    return output_list
    
    
output_list=sublist_score(movies)
print (output_list)



#Ex3
def return_category(movies,cat_name): 
    output_list=[]
    for i in movies:
        cop_cat=i['category']
        if cat_name==cop_cat:
            output_list.append(i)
    return output_list
    
    
output_list=return_category(movies,'Romance')
print (output_list)



#Ex4
def avg_imdb(movies): 
    avg=0
    total=len(movies)
    for i in movies:
        avg += i['imdb']
    avg=avg/total
    return avg

score=avg_imdb(movies)
print (score)



#Ex5
def avg_category(movies,cat_name): 
    output_list=[]
    for i in movies:
        cop_cat=i['category']
        if cat_name==cop_cat:
            output_list.append(i)
    
    avg=0
    total=len(output_list)
    for i in output_list:
        avg += i['imdb']
    avg=avg/total
    return avg


output_list=avg_category(movies,'Thriller')
print (output_list)