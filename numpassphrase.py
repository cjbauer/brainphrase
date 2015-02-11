# Functions mapping back and forth between numbers and phrases
# September 19 2014
# Christian Bauer
import hashlib
import names
import nouns
import adjectives
import presverbs
import pastverbs
import adverbs
import preps
import numpassphrase

def addchecksum(n):
   s1=""
   m=n
   for i in range(16):
      s1=chr(m%256)+s1
      m=m>>8
   h=hashlib.sha256(s1)
   s2=h.digest()
   chksum = 256 * (ord(s2[1])%2) + ord(s2[0])
   return ((n<<9) + chksum)

def checksump(n):
   return (n == addchecksum(n>>9))

def num_pnpa():
    return names.ambtitlenum * (names.famnamenum + names.ambfirstnamenum * names.famnamenum) + names.ambfirstnamenum * names.famnamenum

def num_pnpm():
    return names.maletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.malefirstnamenum) + names.ambtitlenum * names.malefirstnamenum * names.famnamenum + names.malefirstnamenum * names.famnamenum

def num_pnpf():
    return names.maletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.malefirstnamenum) + names.ambtitlenum * names.malefirstnamenum * names.famnamenum + names.malefirstnamenum * names.famnamenum

def num_npk(k):
    if k>0:
        return adjectives.num * num_npk(k-1)
    else:
        return nouns.num

def num_np(k):
    return num_pnpa()+num_pnpm()+num_pnpf()+num_npk(k)

def num_pp(k):
    return preps.num * num_np(k)

def num_vp(k):
    if k>0:
       return adverbs.num * num_vp(k-1)
    else:
       return presverbs.num + pastverbs.num

def div(n,m):
    r = n%m
    return ((n-r)/m,r)

def combine(wll):
    rl = []
    for wl in wll:
        rl = rl + wl
    return rl

def tophrase_pnpa(n):
    k = names.ambtitlenum * names.famnamenum
    if n < k:
        (q,r)=div(n,names.ambtitlenum)
        return combine([[names.ambtitle[r]],[names.famname[q]]])
    else:
        n = n - k
        k = names.ambtitlenum * names.ambfirstnamenum * names.famnamenum
        if n < k:
            (q,r)=div(n,names.ambtitlenum)
            (q2,r2)=div(q,names.ambfirstnamenum)
            return combine([[names.ambtitle[r]],[names.ambfirstname[r2]],[names.famname[q2]]])
        else:
            n = n - k
            (q,r)=div(n,names.ambfirstnamenum)
            return combine([[names.ambfirstname[r]],[names.famname[q]]])

def tophrase_pnpm(n):
    k = names.maletitlenum * names.famnamenum
    if n < k:
        (q,r) = div(n,names.maletitlenum)
        return combine([[names.maletitle[r]],[names.famname[q]]])
    else:
        n = n - k
        k = names.maletitlenum * names.ambfirstnamenum * names.famnamenum
        if n < k:
            (q,r) = div(n,names.maletitlenum)
            (q2,r2) = div(q,names.ambfirstnamenum)
            return combine([[names.maletitle[r]],[names.ambfirstname[r2]],[names.famname[q2]]])
        else:
            n = n - k
            k = names.maletitlenum * names.malefirstnamenum * names.famnamenum
            if n < k:
                (q,r) = div(n,names.maletitlenum)
                (q2,r2) = div(q,names.malefirstnamenum)
                return combine([[names.maletitle[r]],[names.malefirstname[r2]],[names.famname[q2]]])
            else:
                n = n - k
                k = names.ambtitlenum * names.malefirstnamenum * names.famnamenum
                if n < k:
                    (q,r) = div(n,names.ambtitlenum)
                    (q2,r2) = div(q,names.malefirstnamenum)
                    return combine([[names.ambtitle[r]],[names.malefirstname[r2]],[names.famname[q2]]])
                else:
                    (q,r) = div(n-k,names.malefirstnamenum)
                    return combine([[names.malefirstname[r]],[names.famname[q]]])

def tophrase_pnpf(n):
    k = names.femaletitlenum * names.famnamenum
    if n < k:
        (q,r) = div(n,names.femaletitlenum)
        return combine([[names.femaletitle[r]],[names.famname[q]]])
    else:
        n = n - k
        k = names.femaletitlenum * names.ambfirstnamenum * names.famnamenum
        if n < k:
            (q,r) = div(n,names.femaletitlenum)
            (q2,r2) = div(q,names.ambfirstnamenum)
            return combine([[names.femaletitle[r]],[names.ambfirstname[r2]],[names.famname[q2]]])
        else:
            n = n - k
            k = names.femaletitlenum * names.femalefirstnamenum * names.famnamenum
            if n < k:
                (q,r) = div(n,names.femaletitlenum)
                (q2,r2) = div(q,names.femalefirstnamenum)
                return combine([[names.femaletitle[r]],[names.femalefirstname[r2]],[names.famname[q2]]])
            else:
                n = n - k
                k = names.ambtitlenum * names.femalefirstnamenum * names.famnamenum
                if n < k:
                    (q,r) = div(n,names.ambtitlenum)
                    (q2,r2) = div(q,names.femalefirstnamenum)
                    return combine([[names.ambtitle[r]],[names.femalefirstname[r2]],[names.famname[q2]]])
                else:
                    (q,r) = div(n-k,names.femalefirstnamenum)
                    return combine([[names.femalefirstname[r]],[names.famname[q]]])

def tophrase_npi(i,n):
    if i>0:
        (q,r)=div(n,adjectives.num)
        return combine([[adjectives.d[r]],tophrase_npi(i-1,q)])
    else:
        return [nouns.d[n]]

def tophrase_np(i,n):
    k = num_pnpa()
    if n < k:
        return tophrase_pnpa(n)
    else:
        n = n - k
        k = num_pnpm()
        if n < k:
            return tophrase_pnpm(n)
        else:
            n = n - k
            k = num_pnpf()
            if n < k:
                return tophrase_pnpf(n)
            else:
                n = n - k
                return ['the'] + tophrase_npi(i,n)

def tophrase_pp(i,n):
    (q,r) = div(n,preps.num)
    return combine([[preps.d[r]],tophrase_np(i,q)])

def tophrase_vp(k,n):
   if k > 0:
      (q,r) = div(n,adverbs.num)
      return [adverbs.d[r]] + tophrase_vp(k-1,q)
   elif n < presverbs.num:
      return [presverbs.d[n]]
   else:
      return [pastverbs.d[n-presverbs.num]]
    
def tophrase_sentence137bit(n):
    (n2,r1) = div(n,num_np(2))
    (n3,r2) = div(n2,num_pp(1))
    (n4,r3) = div(n3,num_vp(1))
    (n5,r4) = div(n4,num_np(2))
    return combine([tophrase_np(2,r1),tophrase_pp(1,r2),tophrase_vp(1,r3),tophrase_np(2,r4),tophrase_pp(1,n5)])

def tophrase_sentence89bit(n):
    (n2,r1) = div(n,num_np(1))
    (n3,r2) = div(n2,num_vp(1))
    (n4,r3) = div(n3,num_np(0))
    return combine([tophrase_np(1,r1),tophrase_vp(1,r2),tophrase_np(0,r3),tophrase_pp(1,n4)])

def appendwords(s,wl,i):
   while i<len(wl):
      s+=" "+wl[i]
      i=i+1
   return s

def posf(wl,i,al,f):
   if i < len(wl) and al.has_key(wl[i]):
      return al[wl[i]]
   else:
      raise ValueError(appendwords(f,wl,i))

def parse_pnpa(wl,i):
   if names.ambtitlerev.has_key(wl[i]):
      r = posf(wl,i,names.ambtitlerev,"Expected title of ambiguous gender:")
      if i+2 < len(wl) and names.famnamerev.has_key(wl[i+2]):
         if names.ambfirstnamerev.has_key(wl[i+1]):
            r2 = posf(wl,i+1,names.ambfirstnamerev,"Expected first name of ambiguous gender:")
            r3 = posf(wl,i+2,names.famnamerev,"Expected family name:")
            return (names.ambtitlenum * names.famnamenum + r + names.ambtitlenum * (r2 + names.ambfirstnamenum * r3),i+3)
         else:
            return None
      elif i+1 < len(wl) and names.famnamerev.has_key(wl[i+1]):
         r2 = posf(wl,i+1,names.famnamerev,"Expected family name:")
         return (r + names.ambtitlenum * r2,i+2)
      else:
         return None
   elif names.ambfirstnamerev.has_key(wl[i]):
      r = posf(wl,i,names.ambfirstnamerev,"Expected first name of ambiguous gender:")
      r2 = posf(wl,i+1,names.famnamerev,"Expected family name:")
      return (names.ambtitlenum * names.famnamenum * (1 + names.ambfirstnamenum) + r + names.ambfirstnamenum * r2,i+2)
   else:
      return None

def parse_pnpm(wl,i):
   if names.maletitlerev.has_key(wl[i]):
      if i+2 < len(wl) and names.famnamerev.has_key(wl[i+2]):
         if names.ambfirstnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.maletitlerev,"Expected male title:")
            r2=posf(wl,i+1,names.ambfirstnamerev,"Expected first name of ambiguous gender:")
            r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
            return (names.maletitlenum * names.famnamenum + r1 + names.maletitlenum * (r2 + names.ambfirstnamenum * r3),i+3)
         elif names.malefirstnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.maletitlerev,"Expected male title:")
            r2=posf(wl,i+1,names.malefirstnamerev,"Expected male first name:")
            r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
            return (names.maletitlenum * (names.famnamenum + names.ambfirstnamenum * names.famnamenum) + r1 + names.maletitlenum * (r2 + names.malefirstnamenum * r3),i+3)
         else:
            return None
      else:
         if i+1 < len(wl) and names.famnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.maletitlerev,"Expected male title:")
            r2=posf(wl,i+1,names.famnamerev,"Expected family name:")
            return (r1 + names.maletitlenum * r2,i+2)
         else:
            return None
   elif names.ambtitlerev.has_key(wl[i]):
      if i+1 < len(wl) and names.malefirstnamerev.has_key(wl[i+1]):
         r1=posf(wl,i,names.ambtitlerev,"Expected title of ambiguous gender:")
         r2=posf(wl,i+1,names.malefirstnamerev,"Expected male first name:")
         r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
         return (names.maletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.malefirstnamenum) + r1 + names.ambtitlenum * (r2 + names.malefirstnamenum * r3),i+3)
      else:
         return None
   elif names.malefirstnamerev.has_key(wl[i]):
      r1=posf(wl,i,names.malefirstnamerev,"Expected male first name:")
      r2=posf(wl,i+1,names.famnamerev,"Expected family name:")
      return (names.maletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.malefirstnamenum) + names.ambtitlenum * names.malefirstnamenum * names.famnamenum + r1 + names.malefirstnamenum * r2,i+2)
   else:
      return None

def parse_pnpf(wl,i):
   if names.femaletitlerev.has_key(wl[i]):
      if i+2 < len(wl) and names.famnamerev.has_key(wl[i+2]):
         if names.ambfirstnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.femaletitlerev,"Expected female title:")
            r2=posf(wl,i+1,names.ambfirstnamerev,"Expected first name of ambiguous gender:")
            r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
            return (names.femaletitlenum * names.famnamenum + r1 + names.femaletitlenum * (r2 + names.ambfirstnamenum * r3),i+3)
         elif names.femalefirstnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.femaletitlerev,"Expected female title:")
            r2=posf(wl,i+1,names.femalefirstnamerev,"Expected female first name:")
            r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
            return (names.femaletitlenum * (names.famnamenum + names.ambfirstnamenum * names.famnamenum) + r1 + names.femaletitlenum * (r2 + names.femalefirstnamenum * r3),i+3)
         else:
            return None
      else:
         if i+1 < len(wl) and names.famnamerev.has_key(wl[i+1]):
            r1=posf(wl,i,names.femaletitlerev,"Expected female title:")
            r2=posf(wl,i+1,names.famnamerev,"Expected family name:")
            return (r1 + names.femaletitlenum * r2,i+2)
         else:
            return None
   elif names.ambtitlerev.has_key(wl[i]):
      if i+1 < len(wl) and names.femalefirstnamerev.has_key(wl[i+1]):
         r1=posf(wl,i,names.ambtitlerev,"Expected title of ambiguous gender:")
         r2=posf(wl,i+1,names.femalefirstnamerev,"Expected female first name:")
         r3=posf(wl,i+2,names.famnamerev,"Expected family name:")
         return (names.femaletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.femalefirstnamenum) + r1 + names.ambtitlenum * (r2 + names.femalefirstnamenum * r3),i+3)
      else:
         return None
   elif names.femalefirstnamerev.has_key(wl[i]):
      r1=posf(wl,i,names.femalefirstnamerev,"Expected female first name:")
      r2=posf(wl,i+1,names.famnamerev,"Expected family name:")
      return (names.femaletitlenum * names.famnamenum * (1 + names.ambfirstnamenum + names.femalefirstnamenum) + names.ambtitlenum * names.femalefirstnamenum * names.famnamenum + r1 + names.femalefirstnamenum * r2,i+2)
   else:
      return None

def parse_npk(k,wl,i):
   if k>0:
      r=posf(wl,i,adjectives.drev,"Expected adjective:")
      (q,ir)=parse_npk(k-1,wl,i+1)
      return (r+q*adjectives.num,ir)
   else:
      r=posf(wl,i,nouns.drev,"Expected noun:")
      return (r,i+1)

def parse_np(k,wl,i):
   if wl[i] == 'the':
      (z,ir)=parse_npk(k,wl,i+1)
      return (num_pnpa()+num_pnpm()+num_pnpf()+z,ir)
   else:
      zir = parse_pnpa(wl,i)
      if zir == None:
         zir = parse_pnpm(wl,i)
         if zir == None:
            zir = parse_pnpf(wl,i)
            if zir == None:
               raise ValueError(appendwords("Expected proper noun or noun phrase with "+k+" adjectives:",wl,i))
            else:
               (z,ir) = zir
               return (z+num_pnpa()+num_pnpm(),ir)
         else:
            (z,ir) = zir
            return (z+num_pnpa(),ir)
            return zir
      else:
         return zir

def parse_pp(k,wl,i):
   r=posf(wl,i,preps.drev,"Expected preposition:")
   (q,ir)=parse_np(k,wl,i+1)
   return (r + preps.num * q,ir)

def parse_vp(k,wl,i):
   if k>0:
      r=posf(wl,i,adverbs.drev,"Expected adverb:")
      (q,ir)=parse_vp(k-1,wl,i+1)
      return (r+q*adverbs.num,ir)
   elif (presverbs.drev.has_key(wl[i])):
      r=posf(wl,i,presverbs.drev,"Expected verb:")
      return (r,i+1)
   elif (pastverbs.drev.has_key(wl[i])):
      r=posf(wl,i,pastverbs.drev,"Expected verb:")
      return (presverbs.num + r,i+1)
   else:
      raise ValueError(appendwords("Expected verb:",wl,i))

def parse_sentence137bit(wl,i):
   (n1,i2) = parse_np(2,wl,i)
   (n2,i3) = parse_pp(1,wl,i2)
   (n3,i4) = parse_vp(1,wl,i3)
   (n4,i5) = parse_np(2,wl,i4)
   (n5,i6) = parse_pp(1,wl,i5)
   return (n1 + (num_np(2) * (n2 + (num_pp(1) * (n3 + (num_vp(1) * (n4 + (num_np(2) * n5))))))),i6)

def parse_sentence89bit(wl,i):
   (n1,i2) = parse_np(1,wl,i)
   (n2,i3) = parse_vp(1,wl,i2)
   (n3,i4) = parse_np(0,wl,i3)
   (n4,i5) = parse_pp(1,wl,i4)
   return (n1 + num_np(1) * (n2 + (num_vp(1) * (n3 + (num_np(0) * n4)))),i5)

def tonum137(wl):
   (n,i) = parse_sentence137bit(wl,0)
   if i < len(wl):
       raise ValueError("Extra words starting at ".wl[i])
   else:
       return n

def tonum89(wl):
   (n,i) = parse_sentence89bit(wl,0)
   if i < len(wl):
       raise ValueError("Extra words starting at ".wl[i])
   else:
       return n

def printphrase(wl):
   s=""
   for i in range(len(wl)):
      if i>0:
         s+=" "
      s+=wl[i]
   print s

def possiblecorrections(wl,checkfun):
   for i in range(len(wl)):
      w = wl[i]
      for ul in [names.ambtitlerev,names.maletitlerev,names.femaletitlerev,names.ambfirstnamerev,names.malefirstnamerev,names.femalefirstnamerev,names.famnamerev,nouns.drev,adverbs.drev,adjectives.drev,preps.drev,presverbs.drev,pastverbs.drev]:
         if ul.has_key(w):
            for u in ul:
               if u != w:
                  wl[i]=u
                  try:
                     if checkfun(wl):
                        printphrase(wl)
                  except:
                     pass
            wl[i]=w
      if presverbs.drev.has_key(w):
         for u in pastverbs.drev:
            if u != w:
               wl[i]=u
               try:
                  if checkfun(wl):
                     printphrase(wl)
               except:
                  pass
         wl[i]=w
      if pastverbs.drev.has_key(w):
         for u in presverbs.drev:
            if u != w:
               wl[i]=u
               try:
                  if checkfun(wl):
                     printphrase(wl)
               except:
                  pass
         wl[i]=w

