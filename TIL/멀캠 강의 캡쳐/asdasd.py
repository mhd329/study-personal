import requests
from pprint import pprint

def ranking():

    url = f'https://api.themoviedb.org/3/movie/popular?api_key=f4dd99962cc7bdf87852d77531969501&language=ko'    
    respon = requests.get(url)
    data = respon.json()    
    avg5 = [] # 최정 리턴될 평점 리스트
    n = [] # 가공되지 않은 평점 리스트

    for i in (data.get('results')): 
        n.append(i.get('vote_average')) # 평점을 리스트(n)에 모음
    n_list = sorted(n) # 순차 정렬 
    n_list.reverse()  # 리버스
    
    # print(n_list)
    
    # n5 = n_list[4:5] # 리버스로 높은 수부터 슬라이싱 4:5으로 5번째 높은 점수값 얻음
    n5 = n_list[4]
    
    # print(n5, type(n5))
    
    for i in (data.get('results')):             # 다시 반복문 돌면서
        if i.get('vote_average') >= n5: # n5[0]: # 평점을  리스트 n5[0]값과 비교하여 리스트 추가
            avg5.append(i)
        
    return avg5

if __name__ == '__main__':
    
    pprint(ranking())