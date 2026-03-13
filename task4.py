def analyze_words(text):
    words=text.split()
    word_dict={}
    for w in words:
        if w in word_dict:
            word_dict[w]= word_dict[w] + 1
        else:
            word_dict[w]=1
    total_words= len(words)
    all_counts=[]
    for key in word_dict:
        all_counts.append(word_dict[key])
    all_counts.sort(reverse=True)
    top_5_sum= 0
    for i in range(5):
        if i<len(all_counts):
            top_5_sum=top_5_sum+ all_counts[i]
    proportion =(top_5_sum/total_words)* 100
    print("Total words:", total_words)
    print("Proportion of 5 most common words:",str(top_5_sum)+"/"+ str(total_words)+"="+str(proportion)+"%")
text_input="the world is mine the the the world is is out out out out out out out"
analyze_words(text_input)