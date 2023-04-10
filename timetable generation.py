#time table generation for senior secondary class[xi,xii]

import random
sub=list(eval(input("enter 5 sub")))
    #sub=['bio','phy','eng','mat','che']#input
days=['mon','tue','wed','thurs','fri',"sat"]
day,cl=[],[]
for i in days:
        i=[]
        day.append(i)
    #mon,tue,wed,thurs,fri=[],[],[],[],[]
    #day=[mon,tue,wed,thurs,fri]
   
classes=list(eval(input("enter the classess in roman")))
    #classes=["xia","xib","xiia","xiib","xiic"]
for i in classes:
        i={}
        cl.append(i)
"""    xia={}
    xib={}
    xic={}
    xid={}
    cl=[xia,xib,xic,xid] """






    #sql connectivity
import sqlite3 as m
txia,txib,txic,txid,txie,txif,txig,txih={},{},{},{},{},{},{},{}
txiia,txiib,txiic,txiid,txiie,txiif,txiig,txiih={},{},{},{},{},{},{},{}
r=[txia,txib,txic,txid,txie,txif,txig,txih,txiia,txiib,txiic,txiid,txiie,txiif,txiig,txiih]
    #rre=[txiia,txiib,txiic,txiid,txiie,txiif,txiig,txiih]
dd=int(input("enter how many classes in xi"))
ff=int(input("enter the how many classes in xii"))
h=[]
h.extend(r[0:dd])
h.extend(r[8:ff+8])
"""if (fc==1):

        for i in range(len(classes)):
              h.append(r[i])
    else:
        for i in range(len(classes)):
            h.append(rre[i])"""
q=0
for i in classes:
          for j in sub:
                a=list(eval(input('enter teacher details as sub,name in the above entered order')))
                h[q][a[0]]=a[1]
          q=q+1
mysql=m.connect('timetable')
cur=mysql.cursor()
cur.execute('create table teachers(class varchar(45))')
for i in sub:
          cur.execute('alter table teachers add {} varchar(40)'.format(i))
qq=0
for i in classes:
          gh=h[qq].values()
          df=list(gh)
          cur.execute("insert into teachers values('{}','{}','{}','{}','{}','{}')".format(i,df[0],df[1],df[2],df[3],df[4]))
          qq=qq+1
cur.execute("select * from teachers")

data=cur.fetchall()

mysql.commit()





    #allocating  7periods for each day for every class
ww=[]
def samp(rr):
           w=random.sample(sub,len(sub))
           if(w==rr):
               ll=samp(rr)
               return(ll)
           else:
                return(w)
for i in cl:
        for j in days:
            w=random.sample(sub,len(sub))
            hh=samp(w)
            ww.append(hh)


def repeat(rr):
        dd=random.choice(sub)
        if(dd==rr):
            l=repeat(rr)
            return(l)
        else:
               return(dd)




def deff(z,yy):
           jj=random.choice(sub)
           if(jj==z or jj==yy):
                  r=deff(z,yy)
                  return(r)
           else:
                  return(jj)



p=0
for i in cl:
        for j in days:
         uu=[]
         for kk in range(2):
            rr=random.choice(sub)

            if(rr in uu):
                pp=repeat(rr)
                uu.append(pp)

            else:
                uu.append(rr)

         if(ww[p][4]==uu[0]):
            uu[0],uu[1]=uu[1],uu[0]
         if(ww[p][0]==uu[1]):
             mm=deff(uu[1],uu[0])
             uu[1]=mm

         s=ww[p]+uu
         i[j]=s
         p=p+1




    #checking for periods clash and swaping in class timetable
'''txia={'bio':'k','phy':'d','eng':'o','mat':'g','che':'a'}
    txib={'bio':'k','phy':'e','eng':'i','mat':'g','che':'b'}
    txic={'bio':'l','phy':'d','eng':'i','mat':'g','che':'c'}
    txid={'bio':'l','phy':'e','eng':'o','mat':'g','che':'a'}
    #codes for generating timetable for 5 periods by swaping using sample function in random module
    h=[txia,txib,txic,txid]'''
def periods(e,h):
        g=random.choice(e)
        if(g==h):
            periods(e,g)
        else:
            return(g)
def rep(w):
        u=[]
        for i in cl:
            if(i!=w):
                u.append(i)
        return(u)
def tea(e):
        g=[]
        for i in h:
            if(i!=e):
                g.append(i)
        return(g)
def seven():
        n=0
        q=0
        while(n<len(cl)):
          for j in range(len(cl)-1):
              p=cl[q]
              m=rep(p)
              v=h[q]
              x=tea(v)

              for i in p.keys():
                for k in p[i]:
                    if(k in m[j][i]):
                        if(p[i].index(k)==m[j][i].index(k)):
                            if(v[k]==x[j][k]):
                               b=p[i].index(k)
                               if(b==len(p[i])-1):
                                   """d=random.choice(xia[i])
                                   if(d==k):
                                       f=periods(xia[i],k)
                                       xia[i][b]=f"""
                                   p[i][b],p[i][0]=p[i][0],p[i][b]

                               else:
                                            c=p[i].index(p[i][b+1])
                                            p[i][b],p[i][c]=p[i][c],p[i][b]
                                            if(p[i][b]==p[i][c]):
                                                yy=repeat(p[i][b])
                                                p[i][b]=yy


          q=q+1

          n=n+1



    #starting  19 09 2019
    # creating a list like li=['a','b','c','d','g','u','o','i','j','k','l']
seven()
seven()
li=[]
for i in h:
        xy=i.values()
        for j in xy:
            if(j not in li):
               li.append(j)

    #a,b,c,d,g,u,o,i,j,k,l={},{},{},{},{},{},{},{},{},{},{}

    #classes=['xia','xib','xic','xid']
    # creating like vr=[a,b,c,d,g,u,o,i,j,k,l]
qw=[]
for i in li:
        i={}
        qw.append(i)


        for j in days:
            l=['-' for w in range(7)]

            i[j]=l


    # picking theperiods and creating teachers timetable
def htea(w,tt):
           for i in h:
                for j,dd in i.items():
                       if(w==dd and (cl.index(tt)==h.index(i)) ):
                             return(j)



ar=gg=t=0
for i in qw:

            for j in days:
                t=0
                for ee in cl:

                        bb=ee[j]
                        cc=htea(li[ar],ee)
                        for z in range(len(bb)):
                            if(bb[z]==cc):

                                y=i[j]
                                y[z]=classes[t]


                        #if (cc in bb):
                            #x=bb.index(cc)

                        t=t+1
            #break
            ar=ar+1





    #writing the teachers timetable in csv file
bv=0
import csv
'''file=open("timetable.csv","w")
    cs=csv.writer(file)
    cs.writerow(["teachersname","teacherstt"])'''


    #x={'mon': ['-', 'xia', '-', 'xid', '-', 'xid', 'xia'], 'tue': ['-', '-', 'xid', 'xia', '-', '-', '-'], 'wed': ['xia', 'xid', '-', '-', '-', 'xid', '-'], 'thurs': ['-', '-', '-', 'xid', 'xia', '-', 'xid'], 'fri': ['xid', '-', '-', '-', 'xia', 'xia', '-']}
aa=['days',1,2,3,4,5,6,7]

j=0
days=['mon','tue','wed','thurs','fri','sat']
for k in li:
      for i in days:

        qw[j][i].insert(0,i)
      j=j+1

z=0
for i in li:
        f=open("{}.csv".format(i),"w",newline='')
        c=csv.writer(f)
        c.writerow(aa)
        for j in qw[z].keys():

            c.writerow(qw[z][j])
        z+=1
        f.close()



    #writing the class timetable in csv file
j=0
for k in classes:
      for i in days:
          cl[j][i].insert(0,i)
      j=j+1

z=0
for i in classes:
        f=open("{}.csv".format(i),"w",newline='')
        c=csv.writer(f)
        c.writerow(aa)
        for j in cl[z].keys():

            c.writerow(cl[z][j])
        z+=1
        f.close()
print("your timetable has been generated for teachers and classes")        
aa=input(' ')

