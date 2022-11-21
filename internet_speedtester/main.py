import speedtest

test = speedtest.Speedtest

down_speed = test.download()
up_speed = test.upload()

print("Download speed: ", down_speed)
print("Upload speed: ", up_speed)

#The codes keep returning to me that the module
# 'speedtest' has no attribute of
# speedtest() that appears on no 3