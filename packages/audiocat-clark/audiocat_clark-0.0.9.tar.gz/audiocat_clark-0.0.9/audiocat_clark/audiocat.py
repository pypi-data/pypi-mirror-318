import sys
import subprocess
from signal import signal, SIGINT, SIGTERM
import os



# python wrapper for audiocat shell script
# in order to use PyPi
##########################################
def main():
    # with the following line, no message or stack trace will be printed when you Ctrl+C this program
    signal(SIGINT, lambda _, __: exit())
    # parse arguments
    #################                    
    if len(sys.argv) > 1:
        try:
            # call audiocat shell script
            ############################
            command = "".join(["./audiocat '", sys.argv[1], "'"])        
            p1 = subprocess.Popen(command, shell=True, stdout=None, text=True)
            '''p1 = subprocess.Popen(command,
                            shell=True,
                            text=True,
                            stdin =subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE # ,
                            # universal_newlines=True,
                            # bufsize=0
                            )'''
            out, err = p1.communicate()
            if p1.returncode == 0:
                p1.terminate()
                p1.kill()
        except:
            # send the SIGTERM signal to all the process groups to terminate processes launched from here
            os.killpg(os.getpgid(p1.pid), SIGTERM)
    else:
        print("audiocat: *** you must specify an option, run audiocat -h for more information ***")
    
if __name__ == '__main__':
    main()

