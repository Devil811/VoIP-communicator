import subprocess as sub
import shlex

process = sub.Popen(shlex.split("sudo scp /home/pi/log.txt pi@WEBSERVERIP:/home/pi/www/file"),
                    stdout=sub.PIPE,
                    universal_newlines=True)

while True:
    output = process.stdout.readline()
    print((output.strip()))

    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        for output in process.stdout.readlines():
            print(output.strip())
        break