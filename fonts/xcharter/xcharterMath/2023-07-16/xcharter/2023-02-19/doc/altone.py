#!/usr/bin/env python

import os, sys

# Run this in the root directory containing afm files and a texmf branch
# Before running, all encoding files a_* should be renamed to xch_*
# and the corresponding changes applied to xcharter.map
t2aligs='''% LIGKERN hyphen hyphen =: endash ; endash hyphen =: emdash ;
% LIGKERN quoteleft quoteleft =: quotedblleft ;
% LIGKERN quoteright quoteright =: quotedblright ;
% LIGKERN comma comma =: quotedblbase ; less less =: guillemotleft ;
% LIGKERN greater greater =: guillemotright ;
% LIGKERN f f =: ff ; f i =: fi ; f l =: fl ; ff i =: ffi ; ff l =: ffl ;
'''
encfiles=set()
enclst=[]
enclstt1=[]
enclstts1=[]
enclstly1=[]
enclstot1=[]
encfilest1=set()
encfilests1=set()
encfilesly1=set()
encfilesot1=set()
newlines=[]
afmcmds=[]
vflst=[]
tmfv = sys.argv[1]
with open(tmfv+"/fonts/map/dvips/xcharter/XCharter.map",'r') as f:
	for line in f:
		if "-sc-" in line:
			tmp = line.split()
			enc=tmp[4][2:] # omit <[
			if (enc[-4:]==".enc") and (enc[:4]=="xch_"):
				if "-ly1-" in line:
					enclstly1.append(enc)
				elif "-ot1-" in line:
					enclstot1.append(enc)
				elif "-t1-" in line:
					enclstt1.append(enc)
				elif "-ts1-" in line:
					enclstts1.append(enc)				
				else:
					continue
				h=tmp[5][1:-4] # psfile, without .pfb or <
				a=tmp[0][:-6] # name of vf
				vflst.append(a)
				s="/Library/TeX/texbin/afm2tfm "+h+" -T "+tmfv+"/fonts/enc/dvips/xcharter/"+enc+" -v "+a+" "+tmp[0]
				afmcmds.append(s)
					
encfilest1=set(enclstt1)
encfilests1=set(enclstts1)
encfilesly1=set(enclstly1)
encfilesot1=set(enclstot1)
for f in sorted(encfilest1):
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'r') as g:
		tmp = g.read()
		k=tmp.find('/thorn')+6
		s=tmp[k:]
		if '/.notdef' in s:
			s=s.replace('/.notdef','/SSsmall')
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'w') as g:
		g.write(tmp[:k]+s)
for f in sorted(encfilesly1):
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'r') as g:
		tmp = g.read()
		k=tmp.find('/cedilla')+8
		s=tmp[k:]
		j=s.find('/')
		if s[j:j+8]=='/.notdef':
			s=s[:j]+'/SSsmall'+s[j+8:]
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'w') as g:
		g.write(tmp[:k]+s)
# We've modified the encoding files
# Now regenerate the --base and vpl

with open(tmfv+"/fonts/map/dvips/xcharter/XCharter.map",'r') as f:
	for line in f:
		if ("osf-" in line) or ("-ts1" in line):
			tmp = line.split()
			enc=tmp[4][2:]
			if (enc[-4:]==".enc") and (enc[:4]=="xch_"):
				enc=enc[:3]+"1"+enc[3:]
				enclst.append(enc)
				tmp[0]="XCharter1"+tmp[0][8:]
				tmp[2]=tmp[2][:8]+"1"+tmp[2][8:] # encoding name
				tmp[4]="<["+enc # encoding file, prefixed by <[
				newlines.append(' '.join(tmp))
				h=tmp[5][1:-4] # psfile, without .pfb or <
				a=tmp[0]
				if a[-6:]=="--base":
					a=tmp[0][:-6] # name of vf
				vflst.append(a)
				s="afm2tfm "+h+" -T "+tmfv+"/fonts/enc/dvips/xcharter/"+enc+" -v "+a+" "+tmp[0]
				afmcmds.append(s)
				
#print(newlines)
encfiles=set(enclst)
#print sorted(encfiles)
#sys.exit()
for f in sorted(encfiles):
	f0=f[:3]+f[4:] # remove "1"
	os.system("/bin/cp -fp "+tmfv+"/fonts/enc/dvips/xcharter/"+f0+" "+tmfv+"/fonts/enc/dvips/xcharter/"+f)
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'r') as g:
		tmp = g.read()
		tmp=tmp.replace("AutoEnc","AutoEnc1")
		tmp=tmp.replace("one.oldstyle","one.Alt.oldstyle")
		tmp=tmp.replace("/Thorn /.notdef","/Thorn /uni1E9E.ss01")
		tmp=tmp.replace("/cedilla /.notdef","/cedilla /uni1E9E.ss01")
	with open(tmfv+"/fonts/enc/dvips/xcharter/"+f,'w') as g:
		g.write(t2aligs)
		g.write(tmp)
print('++++++++++++++++++++++++++++++++')
# Write the afmcmds and update mapfile
for j in range(len(vflst)):
	a=vflst[j]
	s=afmcmds[j]
	print(s)
	if os.system(s)==0:
		if os.system("vptovf "+a)==0:
			os.system("/bin/mv -f "+a+".tfm "+tmfv+"/fonts/tfm/public/xcharter")
			os.system("/bin/mv -f "+a+"--base.tfm "+tmfv+"/fonts/tfm/public/xcharter")
			os.system("/bin/mv -f "+a+".vf "+tmfv+"/fonts/vf/public/xcharter")
			
# Get rid of 12 spurious vf files
#os.system("cd "+tmfv+"/fonts/vf/public/xcharter;/bin/rm -f XCharter1-*osf*.vf")		

with open(tmfv+"/fonts/map/dvips/xcharter/XCharter.map",'a+') as f:
	for s in newlines:
		f.write(s+'\n')