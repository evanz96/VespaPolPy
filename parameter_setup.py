# ---- Parameter setup ----
filedir = "H:\My Drive\Research\VespaPolPy"

isSyn = False
is3c = False # for synthetic this will be overriden
comp = "Z" # only applies to real data

modname = "201111221848"
runname = "run11_Z"
totalSteps = int(5e5)

burnInSteps = int(4e5)
nSaveModels = 100
actionsPerStep = 2

maxN = 1

ampRange = (-1., 1.) # only applies to real data
slwRange = (0., 8.) # only applies to real data
minSpace = 1.0

isbp = True
freqs = (0.02, 1.0)

locDiff = False
distRange = (-5., -5.)
bazRange = (-5., -5.)

fitNoise = False