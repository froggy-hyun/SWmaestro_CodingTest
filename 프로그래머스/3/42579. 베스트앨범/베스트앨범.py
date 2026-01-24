def solution(genres, plays):
    answer = []
    musics = {}
    for i in range(len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = {i:plays[i]}
        else:
            musics[genres[i]][i] = plays[i]
            
    # print(musics)
    musics = dict(sorted(musics.items(), key = lambda x : sum(x[1].values()), reverse = True))
    # print(musics)
    
    for g in musics:
        musics[g] = dict(sorted(musics[g].items(), key = lambda x: x[1], reverse = True))
        
        
    for g in musics:
        if len(list(musics[g].keys())) == 1:
            answer.append(list(musics[g].keys())[0])
        else:
            answer.append(list(musics[g].keys())[0])
            answer.append(list(musics[g].keys())[1])
    return answer
            
#장르 play 순 최다 2개씩. 1개면 1개