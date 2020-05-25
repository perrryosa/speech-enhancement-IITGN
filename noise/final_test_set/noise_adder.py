import audioread
import librosa
import numpy as np
from scipy.io import wavfile
import os
import glob
import random
import scipy
A=glob.glob('/home/perrryosa/cv_corpus_v1/cv-valid-train/*.mp3')

# noise1,sr=librosa.load('pink_11.wav',sr=16000)
# noise2,sr=librosa.load('pink_noise16k.wav',sr=16000)
# noise3,sr=librosa.load('wind1.wav',sr=16000)
# noise4,sr=librosa.load('wind_high_35.wav',sr=16000)
# noise5,sr=librosa.load('wind_low.wav',sr=16e3)
# noise6,sr=librosa.load('wind_variable_25_15.wav',sr=16e3)
noise7, _ = librosa.load('noise_test7.wav', sr = 16000)
noise8 , _ = librosa.load('noise_test8.wav', sr = 16000)
noise24, _ = librosa.load('noise_test24.wav', sr = 16000)
noise50, _ = librosa.load('noise_test50.wav', sr = 16000)
clean7, _ = librosa.load('clean_test7.wav', sr = 16000)
clean8, _ = librosa.load('clean_test8.wav', sr = 16000)
clean24, _ = librosa.load('clean_test24.wav', sr = 16000)
clean50, _ = librosa.load('clean_test50.wav', sr = 16000)
# print(len(noisy))
# noise1,sr=librosa.load('mic1_2cm.wav',sr=16e3)
# noise2,sr=librosa.load('mic2_2cm.wav',sr=16e3)
# noise3,sr=librosa.load('mic1_10cm.wav',sr=16e3)
# noise4,sr=librosa.load('mic2_10cm.wav',sr=16e3)
# noise5,sr=librosa.load('mic1_2cm_constant.wav',sr=16e3)
# noise6,sr=librosa.load('mic2_2cm_constant.wav',sr=16e3)
# cock,sr=librosa.load('cockpit1.wav',sr=16e3)
noise=[noise7, noise8, noise24, noise50]
clean=[clean7, clean8, clean24, clean50]
#print(noise1,noise2)
# A=A[13000:13100]


for i in range(len(noise)):
    SNR = [-5, 0, 5, 10, 15]
    label = ['7', '8', '24', '50']
    noise_ = noise[i]
    clean_ = clean[i]
    n_p = np.sum(noise_**2)
    s_p = np.sum(clean_**2)   
    for j in range(len(SNR)):

        noise_ = noise_ * (np.sqrt((s_p * 10**SNR[j]) / n_p))

        noisy = noise_ + clean_ 

        scipy.io.wavfile.write('/home/perrryosa/Speech-Denoising-With-RNN/final_test_set/' + str(SNR[j]) + 'db'+ '/noisy_test'+label[i]+'_'+str(SNR[j])+'db'+'.wav',
        16000, noisy)
    # print(np.log10(s_p/ np.sum(noise_**2)))


# count=0
# for files in A:
#     dummy,sr=librosa.load(files,sr=16000)
#     #print(type(dummy))
#     ind=np.random.randint(1,1000000)
#     #print(ind)
#     # noisy1=noise[random.randint(0,3)]
#     # noisy2 =noise[random.randint(0,3)]
#     noisy = noise[random.randint(0,3)]
#     len_=len(dummy)
#     # if len(noisy)<ind+len_:
#         # noisy=np.pad(noisy,(0,ind+len_ - len(noisy)),'constant')
#     # if len(cock)<ind+len_:
#         # cock=np.pad(cock,(0,ind+len_ - len(cock)),'constant')
#     # noisy1=noisy1[ind:ind+len_]
#     # noisy2=noisy2[ind:ind+len_]
#     # noisy = noisy1+noisy2
#     # noisy = noisy[ind:ind+len_]
#     n_p = np.sum(noisy**2)
#     s_p = np.sum(dummy**2)
#     noisy = noisy * (np.sqrt(s_p/n_p))
#     # print(len(noisy))
#     # noisy=noisy+cock[ind+ind+len_]
#     #print(type(noisy))
#     noisyAudio=noisy+dummy
#     # print(10*(np.log10(s_p/np.sum(noisy**2))))
#     #print(type(noisyAudio))
#     #print(noisyAudio)
#     scipy.io.wavfile.write('/home/perrryosa/Speech-Denoising-With-RNN/dataset_generate/wind_dataset_IITGN/test_wind/noisy/noisy_test'+str(count)+'.wav',16000,noisyAudio)
#     scipy.io.wavfile.write('/home/perrryosa/Speech-Denoising-With-RNN/dataset_generate/wind_dataset_IITGN/test_wind/clean/clean_test'+str(count)+'.wav',16000,dummy)
#     # scipy.io.wavfile.write('/home/perrryosa/Speech-Denoising-With-RNN/dataset_generate/wind_dataset_IITGN/pink_wind_dataset/test_pink_wind/noise/noise_test'+str(count)+'.wav',16000,dummy)
#     count=count+1

