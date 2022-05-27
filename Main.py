# Author Mr MJ

# Github : https://github.com/MR-MJ-07

 #!/usr/bin/python2

# -*- coding: utf-8

import os,sys,time

def psb(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.02)

def po(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.003)        

def main():

    time.sleep(1)

    os.system ('clear')

    print """
 \033[1;97m##     ## ########      ##     ##       ## 
 \033[1;97m###   ### ##     ##     ###   ###       ## 
 \033[1;97m#### #### ##     ##     #### ####       ## 
 \033[1;97m## ### ## ########      ## ### ##       ## 
 \033[1;97m##     ## ##   ##       ##     ## ##    ## 
 \033[1;97m##     ## ##    ##  ### ##     ## ##    ## 
 \033[1;97m##     ## ##     ## ### ##     ##  ######  
 \033[1;97m___________________________________________
 \033[1;91m[ ] FUCK YOUR OK IDZ
\033[1;92m [ ] ABLAMI NOT ALLOW BRO
\033[1;91m [ ] WE ARE NOT SAME BRO
\033[1;92m [ ] MR.MJ MIND IT'
 \033[1;97m___________________________________________
"""
    psb ('\n\x1b[1;91m\n [1] FUCK K4US4R  \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;92m [2] FUCK RIYAD-RR \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;93m [3] FUCK SHANTO \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;94m [4] FUCK RANJHA \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;95m [5] FUCK MAHIN \033[96;5m[BYPASS]')
    psb ('\n\x1b[1;96m [6] Coming Soon ')
    psb ('\n\x1b[1;93m [0] Exit ')
    gans = raw_input ('\n\n[91m Choice : [93m ')

    if gans in ['1']:
        time.sleep(1)
        os.system('python Fuck-K4US4R.py')
        exit()
    if gans in ['2']:
        time.sleep(1)
        os.system('python Fuck-RR.py')
        exit()
    if gans in ['3']:
        time.sleep(1)
        os.system('python Fuck-SHANTO.py')
        exit()
    if gans in ['4']:
        time.sleep(1)       
        os.system('python Fuck-RANJHA.py')
        exit()
    if gans in ['5']:
        time.sleep(1)
        os.system('python Fuck-MAHIN.py')
        exit()
    if gans in ['6']:
        time.sleep(1)
        os.system ('python coming.py')
        exit()
    if gans in ['0']:
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        psb('\t\t\n              WRONG NUMBER')
        time.sleep(3)
        main()

main()



