import pandas as pd

import numpy as np

np.random.randn(1,20)

from ydata_profiling import ProfileReport
df = pd.read_csv(r"/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv")

profile = ProfileReport(df)

#profile.to_html()


profile.to_file(r"/Users/harish/PycharmProjects/april_automation_batch/FIles/out.html")
