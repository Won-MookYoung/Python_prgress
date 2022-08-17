
### 1단계 모든 대문자를 소문자로
# id=[]
# new=[]
# for i in id:
#     new.append(i.lower())
# print(new)
# new_id=''
# new_id=new_id.lower()

### 2단계 - _ . 를 제외한 모든 특수문자 제거
# a=['!%!@$!@$!asd','!@#!@$!%zxc','#$^$^%^qwe','asdasdasd','zxczxczcasc','qeqweqwe']
# ab=[]
# n=0
# for i in a:
#     i=a[n].replace(',','').replace('<','').replace('>','').replace('~','').replace('`','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('|','').replace('?','').replace('/','').strip()
#     ab.append(i)
#     n+=1
# print(ab)

### 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환함 ... -> . / .. -> .
# a=['asaaaaa','aasqwz','aaacszaa','aaasssssssssccccccxxaaaxaaaxaaaaaaaccccasaaa']
# for i in a:
    
#     result=''
#     result += i[0]
#     for j in range(1,len(i)):
#         if i[j-1]!=i[j] or result[int(len(result))-1]!='a':
#             result+=i[j]
#     print(result)


### 4단계 맨앞이나 맨뒤에 '.' 로 되어있으면 삭제함
# a='..ssasq.qwfqwf.ergwrg.s...'
# for i in range(1,len(a)):
#     if a[0]=='.':
#         a=a[1:]
#     elif a[-1]=='.':
#         a=a[:-1]
# print(a)

### 5단계 new_id가 빈문자열이라면 'a'대입
# new_id=''
# if new_id =='':
#     new_id='a'
# print(new_id)

###6단계 new_id 길이가 16 이상이면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        #만약 제거 후 마침표(.)가 new_id 끝에 위치한다면 끝에 위치한 마침표문자 제거 
# a='qfknqlkfnlqkfn.lqkwnl'
# if len(a) >=16:
#     a=a[:15]
# for i in range(1,len(a)):
#     if a[-1]=='.':
#         a=a[:-1]

# print(a)

###7단계 new_id의 길이가 2자 이하라면 , new_id의 마지막 문자를 new_id의 길이가 3이될때까지 반복해서 끝에붙임
# new_id='ab'
# for i in range(1,len(new_id)+1):
#     if len(new_id)==1:
#         new_id=new_id*3
#     elif len(new_id)==2:
#         new_id=new_id + new_id[0]

# print(new_id)

########### 종합 ############
#1단계 : 모든 대문자를 대응되는 소문자로 치환함
#2단계 : 알파벳 소문자, 숫자, 빼기(-),밑줄(_),마침표(.)를 제외한 모든 문자제거
#3단계 마침표가 두번이상연속된 부분을 하나의 마침표로 치환
#4단계 마침표가 처음이나 끝에위치한다면 제거
#5단계 빈문자열이라면 'a'대입
#6단계 길이가 16자 이상이면 첫 15개문자 제외 나머지모두제거, 제거후 마침표가 끝이라면 마침표제거
#7단계 길이가 2자 이하라면 마지막문자를 길이가 3이 될때까지 반복

'''
def solution(new_id):
    if len(new_id)>=1 or len(new_id)<=1000:
        
    
        new_id=new_id.lower().replace('"','').replace("'",'').replace(',','').replace('<','').replace('>','').replace('~','').replace('`','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('|','').replace('?','').replace('/','').strip()

        result=''
        result += new_id[0]

        for i in range(1,len(new_id)):
            if new_id[i-1]!=new_id[i] or result[len(result)-1]!='.':
                result+=new_id[i]
        new_id=result

        if new_id=='.':
            new_id=''
        elif len(new_id)==1:
            new_id=new_id
        else:

            for i in range(1,len(new_id)):
                if new_id[0]=='.':
                    new_id=new_id[1:]
                elif new_id[-1]=='.':
                    new_id=new_id[:-1]

        if new_id =='':
            new_id='a'

        if len(new_id) >=16:
            new_id=new_id[:15]
            for i in range(1,len(new_id)):
                if new_id[-1]=='.':
                    new_id=new_id[:-1]

        if len(new_id)==1:
            new_id=new_id*3
        elif len(new_id)==2:
            new_id=new_id + new_id[1]

        answer=new_id
        return answer
   

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('!@!@$!%@#%@#%!@#!@....!sdafnAFERGEG..y.aasd'))
print(solution('z-+.^."'))
print(solution('abcdefghijklmn.p'))

'''

#step 1
def solution(new_id):

    
    new_id=new_id.lower()
    
    #step 2
    include=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_','.']
    new_id2=''
    for i in range(len(new_id)):
        if new_id[i] in include:
            new_id2+=new_id[i]

    #step 3
    new_id3=''
    new_id3+= new_id2[0]
    for i in range(1,len(new_id2)):
        if new_id2[i-1]!=new_id2[i] or new_id3[len(new_id3)-1]!='.':
            new_id3+=new_id2[i] 
    
    # #step 4
    if new_id3=='.':
        new_id4=''
    elif len(new_id3)==1:
        new_id4=new_id3
    else:
        
        if new_id3[0]=='.':
            new_id4=new_id3[1:]
        elif new_id3[-1]=='.':
            new_id4=new_id3[:-1]
        else: new_id4=new_id3
    
    # #step 5
    if new_id4 =='':
        new_id5='a'
    else: new_id5=new_id4
    
    # #step 6
    if len(new_id5)>=16:
        new_id6=new_id5[:15]
    else: new_id6=new_id5
    
    if new_id6[-1]=='.':
        new_id7=new_id6[:-1]
    else: new_id7=new_id6

    #step 7
    if len(new_id7)==1:
        answer=new_id7*3
    elif len(new_id7)==2:
        answer=new_id7 + new_id7[1]
    else:

        answer=new_id7
    

    return answer