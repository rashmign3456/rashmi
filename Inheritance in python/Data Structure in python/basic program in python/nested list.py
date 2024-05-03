if __name__ == '__main__':
    
    records = []
    scores = set()
    sec_low_names = []
    
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.add(score)
        
    second_lowest_score = sorted(scores)[1]
    
    for name,score in records:
        if score == second_lowest_score:
            sec_low_names.append(name)
            
    for name  in  sorted(sec_low_names):
      print(name)                  
        
