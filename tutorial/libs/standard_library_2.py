def Output_Formatting():
    import reprlib
    print(reprlib.repr(set('supercalifragilisticexpialidocious')))

    import pprint
    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
    pprint.pprint(t, width=30)

    import textwrap
    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print(textwrap.fill(doc, width=40))

    import locale
    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    conv = locale.localeconv()  # get a mapping of conventions
    x = 1234567.8
    # locale.format("%d", x, grouping=True) #DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead. locale.format("%d", x, grouping=True)
    locale.format_string("%s%.*f", (conv['currency_symbol'],
                                    conv['frac_digits'], x), grouping=True)


def Templating():
    from string import Template
    t = Template('${village}folk send $$10 to $cause.')
    s = t.substitute(village='Nottingham', cause='the ditch fund')
    print(s)

    t = Template('Return the $item to $owner.')
    d = dict(item='unladen swallow')
    # substitute = t.substitute(d) #error
    # print(substitute)
    safe_substitute = t.safe_substitute(d)
    print(safe_substitute)

    import time, os.path
    photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

    class BatchRename(Template):
        delimiter = '%'
        fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(photofiles):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))


def Working_with_Binary_Data_Record():
    import struct

    with open('myfile.zip', 'rb') as f:
        data = f.read()

    start = 0
    for i in range(3):  # show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start + 16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start + filenamesize]
        start += filenamesize
        extra = data[start:start + extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)

        start += extra_size + comp_size  # skip to the next header


def Multi_threading():
    import threading, zipfile

    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)

    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')

    background.join()  # Wait for the background task to finish
    print('Main program waited until background was done.')

def Logging():
    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')


def Tools_for_Working_with_Lists():
    from array import array
    a = array('H', [4000, 10, 700, 22222])
    print(sum(a))
    print(a[1:3])

    from collections import deque
    d = deque(["task1", "task2", "task3"])
    d.append("task4")
    print("Handling", d.popleft())

    import bisect
    scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    bisect.insort(scores, (300, 'ruby'))
    print(scores)

    from heapq import heapify, heappop, heappush
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapify(data)  # rearrange the list into heap order
    heappush(data, -5)  # add a new entry
    a = [heappop(data) for i in range(3)]  # fetch the three smallest entries
    print(a)


if __name__ == "__main__":
    # Output_Formatting()
    # Templating()
    # Working_with_Binary_Data_Record()
    # Multi_threading()
    # Logging()
    Tools_for_Working_with_Lists()
