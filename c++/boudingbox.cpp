#include <opencv2/opencv.hpp>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <stdio.h>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <cmath>
#include <math.h>
#include <opencv2/core/core.hpp>
#include <vector>       // std::vector
#include <opencv\ml.h>
#include <opencv\cxcore.h>


 //contour
		vector<vector<Point>> contours3;
		vector<Vec4i> hierarchy3;
		Mat grayScale3, edges3;
		/* Aqui o primeiro parametro é a imagem rgb, e o segundo é a imagem de saida em tons de cinza*/
		cv::cvtColor(edges3, grayScale3, CV_RGB2GRAY); // convert imagem de rgb para escala de cinza
	/* Aqui o primeiro parametro é a imagem de entrada, e segundo é a imagem de saida com os contornos*/
		cv::Canny(edges, edges3, 100, 200, 3); // transforma imagem em apenas contornos dela
		findContours(edges, contours3, hierarchy3, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0)); // armazena os contornos em uma matriz (sendo cada mosição, um vetor com os pontos de contornos).


		/* Pecorre todos os contornos, faz um retagulo desses contornos e colocar em um vetor*/
		vector<Rect> boundRect3( contours3.size() );

		for( size_t i = 0; i < contours3.size(); i++ )
		{
			if( (contours3[i].size()!=0)){

				boundRect3[i] = boundingRect( contours3[i] );
			}
		}
		/* Desenha os retangulos daqueles contornos e desenha em uma imagem */
		Mat drawing3 = Mat::zeros( edges.size(), CV_8UC3 );
		Scalar color(0,255,0);
		  for( size_t i = 0; i< contours3.size(); i++ )
		  {
                /* Aqui o primeiro parametro é a imagem de saida e o segundo é o vetor de contornos*/
				rectangle( drawing3, boundRect3[i].tl(), boundRect3[i].br(), color, 2, 8, 0 );

		  }

		  namedWindow( "Bounding Rect", WINDOW_AUTOSIZE );
		  imshow( "Bounding Rect", drawing3 );
