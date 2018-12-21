#!/usr/bin/env python3

"""Send the contents of a directory as a MIME message."""

import os
import smtplib
# For guessing MIME type based on file name extension
import mimetypes

from argparse import ArgumentParser

from email.message import EmailMessage
from email.policy import SMTP


def main():
    parser = ArgumentParser(description="""\
Send the contents of a directory as a MIME message.
Unless the -o option is given, the email is sent by forwarding to your local
SMTP server, which then does the normal delivery process.  Your local machine
must be running an SMTP server.
""")
    parser.add_argument('-d', '--directory',
                        help="""Mail the contents of the specified directory,
                        otherwise use the current directory.  Only the regular
                        files in the directory are sent, and we don't recurse to
                        subdirectories.""")
    parser.add_argument('-o', '--output',
                        metavar='FILE',
                        help="""Print the composed message to FILE instead of
                        sending the message to the SMTP server.""")
    parser.add_argument('-s', '--sender', required=True,
                        help='The value of the From: header (required)')
    parser.add_argument('-r', '--recipient', required=True,
                        action='append', metavar='RECIPIENT',
                        default=[], dest='recipients',
                        help='A To: header value (at least one required)')
    args = parser.parse_args()
    directory = args.directory
    if not directory:
        directory = '.'
    # Create the message
    msg = EmailMessage()
    msg['Subject'] = 'Contents of directory %s' % os.path.abspath(directory)
    msg['To'] = ', '.join(args.recipients)
    msg['From'] = args.sender
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
        # Guess the content type based on the file's extension.  Encoding
        # will be ignored, although we should check for simple things like
        # gzip'd or compressed files.
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(path, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=filename)
    # Now send or store the message
    if args.output:
        with open(args.output, 'wb') as fp:
            fp.write(msg.as_bytes(policy=SMTP))
    else:
        with smtplib.SMTP('imap.exmail.qq.com', 993) as s:
            s.send_message(msg)


def send_simple_text_message():
    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.message import EmailMessage

    # Open the plain text file whose name is in textfile for reading.
    textfile = "cal.py"
    with open(textfile) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = "shuai.pan@corp.to8to.com" ## 这个需要登录的账号一致，否则审核通不过
    msg['To'] = "1084288424@qq.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.exmail.qq.com', 25)  # s = smtplib.SMTP('localhost') 这个ip和端口的设置bug还是有的
    s.login("shuai.pan@corp.to8to.com", "3FiwCciFeHmC7mkP")
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    # main()
    send_simple_text_message()
