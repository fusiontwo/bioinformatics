import re

# read file
BlastnFile = open("blastn.subset.txt", "r")


blast_of_read = {}

chrom_list = [str(i) for i in range(1, 20)]
chrom_list.append('X')
chrom_list.append('Y')
chrom_list.append('MT')

chr_dict = {chrom: [] for chrom in chrom_list}

flag_hits = 0
flag_lines = 0
count = 0

for line in BlastnFile:

    if line == "# BLASTN 2.12.0+\n":
        flag_hits = 0
        flag_lines = 0

    
    if "# Query" in line:
        Query_loc = line[9:]             # Query 추출
        Query_id = Query_loc.replace("\n","")
        blast_of_read[Query_id] = "Add" # 임시 키값으로 Add 부여
        

    if "hits found" in line:
         flag_hits = 1
         flag_lines = 0

         # line의 문자열 패턴에서 BLAST된 횟수의 숫자만 추출
         pattern_hits = "# (\d+) hits found"
         num_hits = re.search(pattern_hits,line)
         hits_value = num_hits.group(1)

        #임시 키값인 Add를 위에서 추출한 BLAST 횟수로 변경
         for key, value in blast_of_read.items():   
            if value == 'Add':
                blast_of_read[key] = hits_value
    
    if "#" not in line:
        count += 1                          #반복횟수

        chr_n_loc = int(line.index("	"))   # chr 번호가 적힌 문자열 위치
        chr_num = line[(chr_n_loc)+1]       # 해당 라인의 chr 번호를 chr num에 입력
        
        cols = line.rstrip().split('\t')
        s_start = int(cols[8])
        s_end = int(cols[9])
        
        query =  line[0:chr_n_loc]

        try:
            chr_dict[chr_num].append((s_start, s_end))
        except:
            pass    

          
#반복문 빠져나옴
c_count = 0
integral_range = []
close_seq = []


for chromosome in chr_dict:
    start_and_end = chr_dict[chromosome]
    
    for tuple_s_and_e in start_and_end:
        start = int(tuple_s_and_e[0])
        end = int(tuple_s_and_e[1])

        for chromosome2 in chr_dict:             #t는 튜플이니 hits_1, hits_2 등으로 나타나고 hits_1 = (s.star, s.end) 형식
            start_and_end2 = chr_dict[chromosome2]
            for tuple_s_and_e2 in start_and_end2:
                start2 = int(tuple_s_and_e2[0])
                end2 = int(tuple_s_and_e2[1])

                END1 = max([start, end])
                START1 = min([start, end])
                END2 = max([start2, end2])
                START2 = min([start2, end2])

                if chromosome == chromosome2:

#case 1: A to B에서 
        # [T      A      TT]
        #      [S        B       SS] 인 경우 >> A[s]<B[s]<A[e]

                    if START1 <= START2 <= END1:
                        if  START1 != START2 or END1 != END2:
                            if END1 <= END2:
                                integral_range.append((chromosome, START1, END2))    #(염색체번호,겹치는 부위 시점, 종점) ,t,s
                            else:
                                integral_range.append((chromosome, START1, END1))
                        else:       
                            pass

#case 2: A to B에서
        #      [T        A       TT]
        # [S     B       SS] 인 경우  >> B[s]<a[s]<B[e]
                    if START2 <= START1 <= END2:
                        if  START1 != START2 or END1 != END2:
                            if END2 <= END1:
                                integral_range.append((chromosome, START2, END1))    #(염색체번호,겹치는 부위 시점, 종점)
                            else:
                                integral_range.append((chromosome, START2, END2))
                        else:
                            pass

                        

# case 3: 
# [s  e] <-- close (<1kb) --> [s e]
                    elif -1000 <= int(START2 - END1) <= 1000:
                        if  START1 != START2 or END1 != END2:
                                close_seq.append((chromosome,tuple_s_and_e,START2-START1,tuple_s_and_e2))  

                        else:
                            pass

                else:
                    pass


for i in integral_range:
    print(i)
print("==============")
for j in close_seq:
    print(j)

# 중복 제거 1
rm_repeat_integral_range = []
for value in integral_range:
    if value not in rm_repeat_integral_range:
        rm_repeat_integral_range.append(value)

print(rm_repeat_integral_range)

# 중복 제거 2
rm_repeat_close_seq = []
for value in close_seq:
    if value not in rm_repeat_close_seq:
        rm_repeat_close_seq.append(value)

print(rm_repeat_close_seq)

for p1, p2 in zip(rm_repeat_integral_range,rm_repeat_integral_range[1:]):
    print(p1, p2)

# case1: 겹치지 않는 경우 (그대로 2개의 region 모두 추가)

# case2: 겹치는 경우 중 첫 번째 region이 두 번째 region보다 앞에 있는 경우 
  # (첫 번째 region의 끝이 두 번째 region의 끝보다 앞이거나 같을 때 or 첫 번째 region의 끝이 두 번째 region의 끝보다 뒤에 있을 때)
  
# case3: 겹치는 경우 중 첫 번째 region이 두 번째 region보다 뒤에 있는 경우 
  # (두 번째 region의 끝이 첫 번째 region의 끝보다 앞이거나 같을 때 or 두 번째 region의 끝이 첫 번째 region의 끝보다 뒤에 있을 때)
  
# case4: 첫 번째 region의 끝과 두 번째 region의 시작이 일치하는 경우 



