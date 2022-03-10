import sys
import heapq
import pandas as pd

try:
  in_file = sys.argv[1]
  df = pd.read_csv(in_file)
  grouped = df.groupby('player_id').mean()
  rank = grouped['score'].rank(ascending=False, method='min') 

  rank = rank.to_numpy().tolist()
  player_ID = grouped.index.to_numpy().tolist()
  mean_score = grouped.to_numpy().tolist()
  
  print('rank,player_id,mean_score')
  
  ans = [[int(rank[i]),player_ID[i],mean_score[i][0]]  for i in range(len(player_ID))] 

  for _ in range(len(player_ID)):
    i = heapq.heappop(ans)
    print(f'{i[0]},{i[1]},{i[2]}')
except Exception as e:
  print(e)



