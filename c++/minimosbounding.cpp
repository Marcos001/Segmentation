#include "stdio.h"
#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkMinimumMaximumImageCalculator.h"
#include "itkOtsuMultipleThresholdsImageFilter.h"
#include "itkScalarImageKmeansImageFilter.h"


    typedef itk::Image<unsigned char, 2> ImageType;
    typedef itk::ImageFileReader<ImageType> ReaderType;
    typedef itk::ImageFileWriter<ImageType> WriterType;
    typedef itk::MinimumMaximumImageCalculator <ImageType> ImageCalculatorFilterType;
	typedef itk::OtsuMultipleThresholdsImageFilter <ImageType, ImageType> FilterType;


	using namespace std;
    
int getMinimum(ImageType::Pointer image){

  ImageCalculatorFilterType::Pointer imageCalculatorFilter = ImageCalculatorFilterType::New ();
  imageCalculatorFilter->SetImage(image);
  imageCalculatorFilter->Compute();
  return imageCalculatorFilter->GetMinimum();
} 
  // pegar o maior valor da imagem
int getMaximum(ImageType::Pointer image){

	ImageCalculatorFilterType::Pointer imageCalculatorFilter = ImageCalculatorFilterType::New ();
	imageCalculatorFilter->SetImage(image);
	imageCalculatorFilter->Compute();
	return imageCalculatorFilter->GetMaximum();
}
//  função apra criar imagem
ImageType::Pointer createImage1(ImageType::Pointer image){
	
		ImageType::Pointer newImage = ImageType::New();
		ImageType::IndexType start;
		start.Fill(0);
		ImageType::RegionType region;
		region.SetSize(image->GetLargestPossibleRegion().GetSize());
		region.SetIndex(start);
		newImage->SetRegions(region);
		newImage->SetSpacing(image->GetSpacing());
		newImage->Allocate();
		newImage->FillBuffer(getMinimum(image));
	return newImage;
} 
// Algoritmo de Otsu utilizando 2 clusters(CLASSE)
ImageType::Pointer otsuClustering(ImageType::Pointer image, int numCluster){
	// vai aplicar o filtro do OTSU 
	typedef itk::OtsuMultipleThresholdsImageFilter <ImageType, ImageType> FilterType;
	FilterType::Pointer otsuFilter = FilterType::New();
	otsuFilter->SetInput(image);
	otsuFilter->SetNumberOfHistogramBins(255);
	otsuFilter->SetNumberOfThresholds(numCluster);
	otsuFilter->SetLabelOffset(2);
	otsuFilter->Update();
	return otsuFilter->GetOutput();
}
// Algoritmo kmeans separando a imagem em 2 clusters 
ImageType::Pointer KmenasClutering(ImageType::Pointer image, int numCluster){
	
	typedef itk::ScalarImageKmeansImageFilter<ImageType,ImageType> KMeansFilterType;
	KMeansFilterType::Pointer kmeansImgFilter = KMeansFilterType::New();
 	kmeansImgFilter->SetInput(image);
	kmeansImgFilter->SetUseNonContiguousLabels(true);
	int max, min;
	max = getMaximum(image);
	min = getMinimum(image);

	typedef itk::OtsuMultipleThresholdsImageFilter <ImageType, ImageType> FilterType;
	FilterType::Pointer otsuFilter = FilterType::New();
	otsuFilter->SetInput(image);
	// passa o numero de classes 3 por�m se apenas 2 classes. numclusteer= 2
	otsuFilter->SetNumberOfThresholds(numCluster-1);
	otsuFilter->Update();
	// separa as classes 
	FilterType::ThresholdVectorType thresholds = otsuFilter->GetThresholds();
	
	for (unsigned int i = 0; i < thresholds.size(); i++)
		kmeansImgFilter->AddClassWithInitialMean(itk::NumericTraits<FilterType::InputPixelType>::PrintType(thresholds[i]));
	// atualiza a nova imagem segmentada 
	kmeansImgFilter->Update();
  // returna a imagem segmentada com kmeans 
  return kmeansImgFilter->GetOutput();
}

ImageType::Pointer getRegions(ImageType::Pointer image, int clusterizador){

	vector<ImageType::Pointer> regionIsolada;
	//criar a imagem retornando a image criada 
	ImageType::Pointer imageOtsu = createImage1(image);
	//escolhe qual algoritmo vai utilizar primeiro dependo do valor que vinher no clusterizador
	if (clusterizador == 1)
		// segmenta utilizando o de OTSU
		imageOtsu = otsuClustering(image,2);
	if (clusterizador == 2)
		// segmenta utilizando o kmeans 
		imageOtsu = KmenasClutering(image,3);
	// regi�o de interesse da imagem 
	ImageType::Pointer imgRegion;
	ImageType::SizeType size;
	size = imageOtsu->GetLargestPossibleRegion().GetSize();

	// menor e maior escala da imagem 
	int min, max;
	min = getMinimum(imageOtsu);
	max = getMaximum(imageOtsu);
	//
	int sizeHistograma = max+1;

	int *histograma = new int[sizeHistograma];
	for(int i = 0; i < sizeHistograma; i++)
		histograma[i] = 0;
	// menor valor da imagem 
	int background = getMinimum(imageOtsu);

	if (min < 0 )
		min *= -1;

	for(int y = 0; y < size[1]; y++){
		for(int x = 0; x < size[0]; x++){
			ImageType::IndexType position;
			position[0] = x;
			position[1] = y;
			int value = (int)imageOtsu->GetPixel(position);
			//todos os voxels come�am de 0
			if (value != background){
				//if ((value + min) < 0 || value > sizeHistograma)
					//cout << "DEU MERDA: " << value << endl;
				histograma[ value ]++;
			}
		}
	}
	int cont, menor = size[0]*size[1], p, pos = 0;

	for (int h = 0; h<sizeHistograma;h++){
		cont=0;
		// se histograma maior ele cria uma imagem  da regiao segmentada  
		if (histograma[h] > 0){
			//cout<<histograma[h]<<endl;
			ImageType::Pointer imageAux = createImage1(imageOtsu);
			for(int y = 0; y < size[1]; y++){
				for(int x = 0; x < size[0]; x++){
					ImageType::IndexType position;
					position[0] = x;
					position[1] = y;
					int value = imageOtsu->GetPixel(position);
					if (value == h){
						imageAux->SetPixel(position,image->GetPixel(position));
						cont++;
					}
					}
				
			}
	     	if (cont < menor) {
				menor = cont; 
				p = pos;
			}
			pos++;
			regionIsolada.push_back(imageAux);
			imageAux = 0;
		}
	}
	// retorna a regi�o isolada 
	return regionIsolada.at(p);
}
// cria uma imagem 
ImageType::Pointer createImage(ImageType::Pointer image){
	
	ImageType::Pointer newImage = ImageType::New();
	ImageType::IndexType start;
	start.Fill(0);
	ImageType::RegionType region;
	region.SetSize(image->GetLargestPossibleRegion().GetSize());
	region.SetIndex(start);
	newImage->SetRegions(region);
	newImage->SetSpacing(image->GetSpacing());
	newImage->Allocate();
	newImage->FillBuffer(0);
	return newImage;
}
int* getBoundBox(ImageType::Pointer image){
	int minx = 9999, miny = 9999, maxx = -1, maxy = -1;
	
	ImageType::RegionType region;
	region = image->GetLargestPossibleRegion();
	itk::ImageRegionIterator<ImageType> imageIterator(image,region);
	int background = getMinimum(image);
	while(!imageIterator.IsAtEnd())
	{
		short val = imageIterator.Get();
		if (val != background){
			ImageType::IndexType index;
			index = imageIterator.GetIndex();
			//eixo X
			if (index[0] < minx)
				minx = index[0];
			if (index[0] > maxx)
				maxx = index[0];
			//eixo Y
			if (index[1] < miny)
				miny = index[1];
			if (index[1] > maxy)
				maxy = index[1];
			
		}
		++imageIterator;
	}

	   itk::ImageRegionIterator<ImageType> mageIterator(image,image->GetLargestPossibleRegion());
 
 // criar mascara
	   minx;
	   maxx;
	   miny;
	   maxy;

	   int *bb = new int[4];

	   bb[0] = minx; bb[1] = maxx; bb[2] = miny; bb[3] = maxy;
	  
	   return bb;

}

void createIMagemMask(ImageType::Pointer original, ImageType::Pointer mask){
	// tipo da imagem
	ImageType::SizeType size;
	// recebe a possi��o da imagem 
	size = original->GetLargestPossibleRegion().GetSize();

	int x, y; 
	// faz o processo para gera a mascara 
	for (y =0; y<size[1]; y++){
		for (x =0; x<size[1]; x++){
			ImageType::IndexType p;

			p[0] = x;
			p[1] = y;
			int pixel = mask->GetPixel(p);
			if (pixel == 0)
				mask->SetPixel(p,original->GetPixel(p));
		}
	}
	WriterType::Pointer writer = WriterType::New();
	writer->SetFileName("F:\\saidabase.bmp");
	writer->SetInput(mask);
	writer->Update();
}

double getDistance(ImageType::IndexType p1, ImageType::IndexType p2)
{	// calcular distancia 
   double diffX = p2[0] - p1[0];
   double diffY = p2[1] - p1[1];
  return sqrt((pow(diffX, 2) + pow(diffY, 2) ));
}

void getRegionCircular(ImageType::Pointer image, int *bb, int voi){
	stringstream path5;
	//calcular o raio e o centro da imagem
	float raio;
	ImageType::IndexType centro;
	// para identificar o raio tem que saber qual o menor distancia no caso
	// MaiorX - MenorY  Maior Y - Menor X
	if ((bb[1] - bb[0]) > (bb[3] - bb[2]))
		raio = (bb[1] - bb[0])/2;
	else
		raio = (bb[3] - bb[2])/2;
	// cento a a subtra��o do maior X ou Y com o Menor X ou Y dividido por 2, mais o Menor X ou Y 
	centro[0] = (bb[1] - bb[0]) / 2 + bb[0];
	centro[1] = (bb[3] - bb[2]) / 2 + bb[2];

	ImageType::SizeType size = image->GetLargestPossibleRegion().GetSize();
	// criar a imagem 
	ImageType::Pointer newImage = createImage(image);
	// Essa fun��o atribui tudo que estive dentro do raio 
	for(int y = 0; y < size[1]; y++){
		for(int x = 0; x < size[0]; x++){
			ImageType::IndexType position;
			position[0] = x;
			position[1] = y;
			double dist = (double)getDistance(centro, position);
			// Se a distancia menor que o raio esse faz parte da imagem se n�o n�o atribui a imagem
			if (dist <= raio){
				newImage->SetPixel(position,image->GetPixel(position));
			}
			}
		}
	// escrever a imagem 
	    path5.str("");
		path5<<"F:\\RIM-ONE\\Artigo WIM 2\\Segmenta��o\\KmeansCircular\\Glaucomatosas Circular Kmeans\\"<<voi<<".bmp";
		WriterType::Pointer writer = WriterType::New();
		writer->SetFileName(path5.str());
		writer->SetInput(newImage);
		writer->Update();
		voi=0;
	}

int main(){
	
	//OTSU
	stringstream path;
	stringstream path1;
	stringstream path2;
    stringstream path3;
	// percorrer as 40 imagens glaucomatosas 
	for (int voi = 1; voi<=40;voi++){
		// endere�o da imagem
		path.str("");
		path<<"F:\\RIM-ONE\\Artigo WIM 2\\Com varios niveis de glaucoma\\"<<voi<<".bmp";
		cout<<path.str();
		//ler a imagem 
		ReaderType::Pointer reader = ReaderType::New();//ler a imagem
		reader->SetFileName(path.str());
		reader->Update();
		// da um get para manda a imagem pra escrever
		ImageType::Pointer image = reader->GetOutput();
		//escrever imagem 
		path1.str("");
		path1<<"F:\\RIM-ONE\\Artigo WIM 2\\Segmenta��o\\KmeansCircular\\circular\\"<<voi<<".bmp";
		WriterType::Pointer writer = WriterType::New();
		writer->SetFileName(path1.str());
		// passa a imagem e o valor passa saber qual algoritmo vai usar se e o OTSU ou Kmeans 
		writer->SetInput(getRegions(image,2));
		writer->Update();

	}
	for (int vo = 1; vo<=40;vo++){
		
		// ler primeira imagem
		//caminho da imagem
		path2.str("");
		path2<<"F:\\RIM-ONE\\Artigo WIM 2\\Com varios niveis de glaucoma\\"<<vo<<".bmp";
		cout<<path2.str();
		//ler a imagem
		ReaderType::Pointer reader2 = ReaderType::New();//ler a imagem
		reader2->SetFileName(path2.str());
		reader2->Update();
		ImageType::Pointer original = reader2->GetOutput();
		//ler sedunda imagem
		path.str("");
		path<<"F:\\RIM-ONE\\Artigo WIM 2\\Segmenta��o\\KmeansCircular\\circular\\"<<vo<<".bmp";
		cout<<path.str();
		ReaderType::Pointer reader3 = ReaderType::New();//ler a imagem
		reader3->SetFileName(path.str());
		reader3->Update();
		ImageType::Pointer region = reader3->GetOutput();
		int *bb = getBoundBox(region);
        getRegionCircular(original,bb, vo);
	
	}
	
}
	
