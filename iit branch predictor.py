print("*************************")
print("** IIT college pravesh **")
print("*************************")
print("Top 5 IITs With Top 5 Branch")
rank = int(input("ENTER YOUR RANK:"))
preference = input("ENTER ANY TOP 7 IITs AS YOUR PREFERENCE:").upper()
if preference in ["IIT DELHI","IIT BOMBAY","IIT KANPUR","IIT MADRAS","IIT KHARAGPUR"]:
    if preference=="IIT BOMBAY":
          if rank<2782:
            dict2 = {}
            list1 = ["IIT BOMBAY,COMPUTER SCIENCE ENGINEERING","IIT BOMBAY,ELECTRICAL AND ELECTONICS ENGINEERING","IIT BOMBAY,MECHANICAL ENGINEERING","IIT BOMBAY,ENGINEERING PHYSICS","IIT BOMBAY,CHEMICAL ENGINEERING","IIT BOMBAY,CIVIL ENGINEERING","IIT BOMBAY,AEROSPACE ENGINEERING"]
            list2 = [[1,64],[71,293],[196,999],[347,1203],[440,1674],[747,2782],[1071,2025],[2138,3271]]
            for i in range(0,len(list1)):
                value = [list1[i] for j in range(list2[i][0],list2[i][1])]
                dict1 = {}
                for k in range(list2[i][0],list2[i][1]):
                  for x in value:
                    dict1[k]=x
                dest = dict(dict2)
                dict2.update(dict1)
            print(dest)
            print(dest[rank])
          else:
             print("no seats available for this rank at IIT BOMBAY")
             pass
    if preference=="IIT DELHI":
          if rank<2417:
              dict2 = {}
              list1 = ["IIT DELHI,COMPUTER SCIENCE ENGINEERING","IIT DELHI,ELECTRICAL AND ELECTONICS ENGINEERING","IIT DELHI,MECHANICAL ENGINEERING","IIT DELHI,ENGINEERING PHYSICS","IIT DELHI,CHEMICAL ENGINEERING","IIT DELHI,CIVIL ENGINEERING"]
              list2 = [[2,93],[297,468],[498,1281],[1243,1967],[1876,2417],[2381,3193]]
              for i in range(0,len(list1)):
                  value = [list1[i] for j in range(list2[i][0],list2[i][1])]
                  dict1 = {}
                  for k in range(list2[i][0],list2[i][1]):
                    for x in value:
                      dict1[k]=x
                  dest = dict(dict2)
                  dict2.update(dict1)
              
              print(dest[rank])
          else:
              print("no seats available for this rank at IIT DELHI")
              pass

    if preference=="IIT KANPUR":
        if rank<4151:
             dict2 = {}
             list1 = ["IIT KANPUR,COMPUTER SCIENCE ENGINEERING","IIT KANPUR,ELECTRICAL AND ELECTONICS ENGINEERING","IIT KANPUR,MECHANICAL ENGINEERING","IIT KANPUR,CHEMICAL ENGINEERING","IIT KANPUR,CIVIL ENGINEERING","IIT KANPUR,AEROSPACE ENGINEERING"]
             list2 = [[95,216],[431,931],[1254,1990],[2064,3049],[3061,4151],[1854,3333]]
             for i in range(0,len(list1)):
                  value = [list1[i] for j in range(list2[i][0],list2[i][1])]
                  dict1 = {}
                  for k in range(list2[i][0],list2[i][1]):
                    for x in value:
                      dict1[k]=x
                  dest = dict(dict2)
                  dict2.update(dict1)
             
             print(dest[rank])
        else:
             print("no seats available for this rank at IIT KANPUR")
             pass
    if preference=="IIT KHARAGPUR":
        if rank<3608:
            dict2 = {}
            list1 = ["IIT KHARAGPUR,COMPUTER SCIENCE ENGINEERING","IIT KHARAGPUR,ELECTRICAL AND ELECTONICS ENGINEERING","IIT KHARAGPUR,ELECTRICAL AND COMMUNICATION ENGINEERING","IIT KHARAGPUR,MECHANICAL ENGINEERING","IIT KHARAGPUR,CHEMICAL ENGINEERING","IIT KHARAGPUR,AEROSPACE ENGINEERING","IIT KHARAGPUR,CIVIL ENGINEERING"]
            list2 = [[204,283],[560,921],[781,1263],[1518,2072],[2099,3344],[2418,3609],[3601,4503]]
            for i in range(0,len(list1)):
                  value = [list1[i] for j in range(list2[i][0],list2[i][1])]
                  dict1 = {}
                  for k in range(list2[i][0],list2[i][1]):
                    for x in value:
                      dict1[k]=x
                  dest = dict(dict2)
                  dict2.update(dict1)
            
            print(dest[rank])
        else:
            print("no seats available for this rank at IIT KHARAGPUR")
            pass
    if preference=="IIT MADRAS":
        if rank<3036:
            dict2 = {}
            list1 = ["IIT MADRAS,COMPUTER SCIENCE ENGINEERING","IIT MADRAS,ELECTRICAL AND ELECTRONIC ENGINEERING","IIT MADRAS,MECHANICAL ENGINEERING","IIT MADRAS,ENGINEERING PHYSICS","IIT MADRAS,CHEMICAL ENGINEERING","IIT MADRAS,CIVIL ENGINEERING"]
            list2 = [[90,188],[182,777],[722,1891],[1430,2458],[1831,3037],[2220,4346]]
            for i in range(0,len(list1)):
                  value = [list1[i] for j in range(list2[i][0],list2[i][1])]
                  dict1 = {}
                  for k in range(list2[i][0],list2[i][1]):
                    for x in value:
                      dict1[k]=x
                  dest = dict(dict2)
                  dict2.update(dict1)
           
            print(dest[rank])
        else:
             print("no seats available for this rank at IIT MADRAS")
             pass
            
            
