def Operating_System_Interface():
    import os
    os.getcwd()  # Return the current working directory

    os.chdir('/server/accesslogs')  # Change current working directory
    os.system('mkdir today')  # Run the command mkdir in the system shell

    import os
    dir(os)
    help(os)

    import shutil  # For daily file and directory management tasks
    shutil.copyfile('data.db', 'archive.db')
    shutil.move('/build/executables', 'installdir')


def File_Wildcards():
    import glob
    glob.glob('*.py')


def Command_Line_Arguments():
    import sys
    print(sys.argv)


def Error_Output_Redirection_and_Program_Termination():
    import sys
    sys.stderr.write('Warning, log file not found starting a new one\n')


def String_Pattern_Matching():
    import re
    re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

    'tea for too'.replace('too', 'two')


def Mathematics():
    import math
    print(math.cos(math.pi / 4))
    print(math.log(1024, 2))

    import random
    print(random.choice(['apple', 'pear', 'banana']))
    print(random.sample(range(100), 10))  # sampling without replacement
    print(random.random())  # random float
    print(random.randrange(6))  # random integer chosen from range(6)

    import statistics
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(statistics.mean(data))
    print(statistics.median(data))
    print(statistics.variance(data))


def Internet_Access():
    from urllib.request import urlopen

    with urlopen(
            'http://boss.we.com/cat/r/t?op=history&domain=t8t_scm_mdm.app&date=20181215&ip=All&reportType=week&type=Service&sort=total&startDate=20181215&endDate=20181222&queryname=') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
            if 'EST' in line or 'EDT' in line:  # look for Eastern Time
                print(line)

    import smtplib

    server = smtplib.SMTP('localhost')
    server.sendmail('shuai@example.org', 'shuai.pan@corp.to8to.com',
                    """To: jcaesar@example.org
                    From: soothsayer@example.org
                
                    Beware the Ides of March.
                    """)
    server.quit()


def Dates_and_Times():
    # dates are easily constructed and formatted
    from datetime import date
    now = date.today()
    print(now)

    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

    # dates support calendar arithmetic
    birthday = date(1964, 7, 31)
    age = now - birthday
    print(age.days)


def Data_Compression():
    import zlib
    s = b'witch which has which witches wrist watch'
    len(s)

    t = zlib.compress(s)
    len(t)

    zlib.decompress(t)

    zlib.crc32(s)


def Performance_Measurement():
    from timeit import Timer
    a__timeit = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    print(a__timeit)
    b__timeit = Timer('a,b = b,a', 'a=1; b=2').timeit()
    print(b__timeit)


if __name__ == "__main__":

    # Internet_Access()
    # Dates_and_Times()
    # Data_Compression()
    Performance_Measurement()
