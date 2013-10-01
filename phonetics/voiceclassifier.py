#!/usr/bin/env python

import os
import numpy as np

from sklearn import svm
from scikits.talkbox.features import mfcc

R=44100

def get_wav_freqs(filename, r=R):
    fd = open(filename)
    fd.read(44) # discard wav header
    data = np.fromfile(fd, dtype=np.int16)
    ceps, mspec, freqs = mfcc(data, fs=r)
    return ceps, mspec, freqs

def get_midfile_cepstrum(afile, r=R):
    ceps, mspec, freqs = get_wav_freqs(afile, r)
    return ceps[len(ceps)/2]

def get_data_from_dir(adir):
    data = []
    for f in os.listdir(adir):
        mid_cep = get_midfile_cepstrum((os.path.join(adir, f)))
        data.append(mid_cep)
    return data

def get_data(voicedir, unvoicedir):
    voiced = get_data_from_dir(voicedir)
    vlabel = [1] * len(voiced)
    unvoiced = get_data_from_dir(unvoicedir)
    ulabel = [-1] * len(unvoiced)
    
    voiced.extend(unvoiced)
    vlabel.extend(ulabel)
    return (voiced, vlabel)

 
def make_model(x, y):
    clf = svm.SVC()
    return clf.fit(x, y)

def predict_sample(model, soundfile):
    cep = get_midfile_cepstrum(soundfile)
    print model.predict(cep)

if __name__ == '__main__':
    x, y = get_data('/home/me/speech/recordings/my_voicing/voiced', '/home/me/speech/recordings/my_voicing/unvoiced')
    model = make_model(x, y)

    while 1:
        predict_sample(model, raw_input())
