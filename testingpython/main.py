import wget

#file_url = 'https://tinypng.com/images/social/website.jpg'
#file_name = wget.download(file_url)

import subprocess


def runcmd(cmd, verbose=False, *args, **kwargs):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

runcmd("wget https://www.scrapingbee.com/images/logo-small.png", verbose = True)
