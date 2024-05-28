import pandas as pd

df = pd.read_csv("/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv")
print("Info:file has been read successfully")
print("shape", df.shape)
if df.shape[0]>10000000:
    print("warning: I can only handle 1M but provided 10 M")
    logger.warning()
else:
    # print("Warning: file has less records")