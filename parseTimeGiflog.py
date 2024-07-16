"""
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/t.gif  200 
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/a.gif  200 
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/d.gif  200 
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/p.gif  200 
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/c.gif  304 304
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/p.gif  200 - duplicate
abc def rtrtg "00:00:0030T:200" GET /home/r/bs/       200 
abc def rtrtg "00:00:0030T:200" PUT /home/r/ss/t.gif  200 
abc def rtrtg "00:00:0030T:200" GET /home/r/bns/s.gif  400 - 400
abc def rtrtg "00:00:0030T:200" PUT /home/r/bcs/t.gif  200 -duplicate
abc def rtrtg "00:00:0030T:200" PUT /home/r/bvs/t.gif  200 PUT and Duplicate
abc def rtrtg "00:00:0030T:200" PUT /home/r/bbs/t.gif  200 


"""
filename = "/workspaces/my-tool-set/logfile.txt"
outfileSet = set()
fileN = filename.rsplit("/", 1)
outfile = "gif_"+fileN[1]
with open(filename, "r") as f , open(outfile,"w") as out:
    for line in f:
        _, _, _, _, verb, filepath, statusCode = line.split()
        if statusCode!="200":
            continue 
        elif "GET" != verb:
            continue
        else:
            fname = filepath.rsplit("/", 1)
            if fname[1] not in outfileSet:
                outfileSet.add(fname[1])
                out.write(fname[1])
                out.write("\n")


 

