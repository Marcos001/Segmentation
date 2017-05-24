# Segmentation
Segmentação Com Limiar e cluster

O algoritmo: Como funciona a binarização de Otsu

σ2w(t)=q1(t)σ21(t)+q2(t)σ22(t)

onde :

q1(t)=∑ti=1P(i)&q1(t)=∑Ii=t+1P(i)

& :

μ1(t)=∑ti=1iP(i)q1(t)&μ2(t)=∑Ii=t+1iP(i)q2(t)

& :

σ21(t)=∑ti=1[i−μ1(t)]2P(i)q1(t)&σ22(t)=∑Ii=t+1[i−μ1(t)]2P(i)q2(t)

conteudo implementado com base em: 
http://www.meccanismocomplesso.org/opencv-python-otsu-binarization-thresholding/ e também 
no site do OpenCV http://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html.
