import re
import timeit

# read file
BlastnFile = open("blastn.subset.txt", "r")

def Hits_find():
    blast_of_read = {}

    chrom_list = [str(i) for i in range(1, 22)]
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

#           print(s_start)
#           print(s_end)
            try:
                chr_dict[chr_num].append((s_start, s_end))
            except:
                pass    
#print(chr_dict)
#print(chr_dict)
          
#반복문 빠져나옴
    combined_dict = chr_dict

#   print(chr_dict)

    for c in combined_dict:
        i = list(set(combined_dict[c]))         # i는 리스트임    

        for seq1 in i:
            try:
                if remove_flag == 1:
                    i.remove(before_value)
                else:
                    pass 
            except:
                pass

            s_1 = min(seq1)
            e_1 = max(seq1)
            remove_flag = 0
            before_value = seq1
    
            for seq2 in i:
                s_2 = min(seq2)
                e_2 = max(seq2)

                if i.count(seq1) > 1:
                    remove_flag = 1

                if s_1 < s_2 and e_2 < e_1:             # 특정 seq이 다른 하나의 seq의 내부에 존재하는 경우(동일한 경우) (●)
                    i.remove(seq2)
                                                        #   [s_1               e_1]
                                                        #   [s_2 [s_2          e_2]

                elif s_2 < s_1 and e_1 < e_2:
                    remove_flag = 1


                elif s_1 <= s_2 < e_1 < e_2 :          # 특정 seq이 다른 seq에 포함되지 않고 겹치는 경우 (○)
                    i.append((s_1, e_2))
                    i.remove(seq2)                                # [s_1            e_1] 
                    remove_flag = 1                               # [s_2     [s_2      ○-->     e_2]
                

                elif s_2 < s_1 < e_2 <= e_1 :
                    i.append((s_2,e_1))                           #          [s_1              e_1]
                    i.remove(seq2)                                # [s_2  <--○           e_2]  e_2]
                    remove_flag = 1   
                

                elif 0 < (int(e_1 - s_2) or int(e_2 - s_1)) <= 1000:  
                    i.append((s_1, e_2))               # [s_1      e_1] <--1000이하--> [s_2    e_2]
                    i.remove(seq2)
                    remove_flag = 1

                else:
                    remove_flag = 1    

#==============[중복되는 hit 자체출력]==================
#count_dup = 0
#dup_list = []
#for c in integral_dict:
#    i = integral_dict[c]
#    for seq1 in i:
#        s_1 = seq1[0]
#        e_1 = seq1[1]
#        for seq2 in i:
#            s_2 = seq2[0]
#            e_2 = seq2[1]
#
#        if 0 < int(e_1-s_2) < 1000:
#            count_dup =+ 1
#            dup_list.append((c,seq1, seq2))
#if count_dup > 0:    
#    print(dup_list)
#else:
#    print("No seqs in 1kb nearby")
#======================================================



#=================[중복되는 hit 출력]================
    # for c in combined_dict:
    #     i = combined_dict[c]

    #     for seq in i:
    #         dup = i.count(seq)

    #         print(dup, end='')    # 중복되는 hit는 2로 표현

            # if dup == 2:          # 중복되는 hit만 프린트
            #     print(c,seq,(seq[1]-seq[0]))
#===================================================


#===========[합성 query 전체 불러오기]===============
    # for i in combined_dict:
    #     print(i,combined_dict[i])
#===================================================

Hits_find()
# print(timeit.timeit(stmt=Hits_find,number = 1))
