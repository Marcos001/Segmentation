#include "stdio.h"
#include "itkImage.h"
#include "itkOtsuMultipleThresholdsImageFilter.h"
#include "itkBinaryContourImageFilter.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkGDCMImageIO.h"
#include "itkMinimumMaximumImageCalculator.h"
#include <iostream>
#include "itkGDCMImageIO.h"
#include "itkMinimumMaximumImageCalculator.h"
#include "itkTranslationTransform.h"
#include "itkResampleImageFilter.h"
#include "itkBinaryThinningImageFilter.h"
#include "itkScalarImageKmeansImageFilter.h"
#include "itkImageRegionIterator.h"
#include "itkTIFFImageIO.h"
#include "itkRGBPixel.h"
#include <itkShapeLabelMapFilter.h>

using namespace std;
using namespace itk;

    typedef itk::Image<unsigned char, 2> ImageType;
    typedef itk::ImageFileReader<ImageType> ReaderType;
    typedef itk::ImageFileWriter<ImageType> WriterType;
    typedef itk::MinimumMaximumImageCalculator <ImageType> ImageCalculatorFilterType;


int getMaximum(ImageType::Pointer image){

	ImageCalculatorFilterType::Pointer imageCalculatorFilter = ImageCalculatorFilterType::New ();
	imageCalculatorFilter->SetImage(image);
	imageCalculatorFilter->Compute();
	return imageCalculatorFilter->GetMaximum();
}

int getMinimum(ImageType::Pointer image){

  ImageCalculatorFilterType::Pointer imageCalculatorFilter = ImageCalculatorFilterType::New ();
  imageCalculatorFilter->SetImage(image);
  imageCalculatorFilter->Compute();
  return imageCalculatorFilter->GetMinimum();
}

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
	newImage->FillBuffer(getMinimum(image));
	return newImage;
}


/*
*/
ImageType::Pointer otsuClustering(ImageType::Pointer image, int numCluster){
	typedef itk::OtsuMultipleThresholdsImageFilter <ImageType, ImageType> FilterType;
	FilterType::Pointer otsuFilter = FilterType::New();
	otsuFilter->SetInput(image);
	otsuFilter->SetNumberOfHistogramBins(255);
	otsuFilter->SetNumberOfThresholds(numCluster);
	otsuFilter->SetLabelOffset(2);
	otsuFilter->Update();
	return otsuFilter->GetOutput();
}


/*
*/
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
	otsuFilter->SetNumberOfThresholds(numCluster-1);
	otsuFilter->Update();

	FilterType::ThresholdVectorType thresholds = otsuFilter->GetThresholds();
	//
	for (unsigned int i = 0; i < thresholds.size(); i++)
		kmeansImgFilter->AddClassWithInitialMean(itk::NumericTraits<FilterType::InputPixelType>::PrintType(thresholds[i]));

	kmeansImgFilter->Update();

  return kmeansImgFilter->GetOutput();
}

/*
*/
ImageType::Pointer getRegions(ImageType::Pointer image, int clusterizador){

	vector<ImageType::Pointer> regionIsolada;

	ImageType::Pointer imageOtsu = createImage(image);

	if (clusterizador == 1)
		imageOtsu = otsuClustering(image,2);
	if (clusterizador == 2)
		imageOtsu = KmenasClutering(image,3);

	ImageType::Pointer imgRegion;
	ImageType::SizeType size;
	size = imageOtsu->GetLargestPossibleRegion().GetSize();


	int min, max;
	min = getMinimum(imageOtsu);
	max = getMaximum(imageOtsu);

	int sizeHistograma = max+1;

	int *histograma = new int[sizeHistograma];
	for(int i = 0; i < sizeHistograma; i++)
		histograma[i] = 0;

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
				histograma[ value ]++;
			}
		}
	}
	int cont, menor = size[0]*size[1], p, pos = 0;

	for (int h = 0; h<sizeHistograma; h++){
		cont=0;
		if (histograma[h] > 0){
			ImageType::Pointer imageAux = createImage(imageOtsu);
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

	return regionIsolada.at(p);
}


int main(){
	typedef  itk::ImageFileWriter< ImageType  > WriterType;
    typedef  itk::TIFFImageIO TIFFIOType;

	stringstream path;
	stringstream path1;

	for (int voi = 1; voi<=118; voi++){
		path.str("");
		path<<"F:\\SBAI\\Canal Blue\\Blue Normal\\"<<voi<<".bmp";
		cout<<path.str();

		ReaderType::Pointer reader = ReaderType::New();//ler a imagem
		reader->SetFileName(path.str());
		//reader->Update();
	    ImageType::Pointer image = reader->GetOutput();

		path1.str("");
		path1<<"F:\\SBAI\\Canal Blue\\k-means\\Blue Normal\\"<<voi<<".bmp";
		cout<<path1.str();
		/*writer->SetFileName(path1.str());
		writer->SetInput(getRegions(image,2));
		writer->Update();
		reader=0;*/
		WriterType::Pointer writer = WriterType::New();
		TIFFIOType::Pointer tiffIO = TIFFIOType::New();
		tiffIO->SetPixelType(itk::ImageIOBase::RGBA);
		writer->SetFileName(path1.str());
		writer->SetInput(getRegions(image,2));
		writer->SetImageIO(tiffIO);
		writer->Update();


	}

}



//ler a imagem em colorido



	// cortar a imagem
  /*typedef itk::Image<itk::RGBPixel<unsigned char>, 2> ImageType;
  typedef itk::ImageFileReader<ImageType>             ReaderType;
  typedef itk::ImageFileWriter<ImageType> WriterType;
  typedef itk::OtsuMultipleThresholdsImageFilter<ImageType, ImageType> FilterType;

  ReaderType::Pointer reader = ReaderType::New();
  reader->SetFileName("F:\\olho_glaucoma.jpg");
  reader->Update();
  ImageType::Pointer image = reader->GetOutput();

  FilterType::Pointer otsuFilter = FilterType::New();
  otsuFilter->SetInput(image);
  otsuFilter->SetNumberOfHistogramBins(255);
  otsuFilter->SetNumberOfThresholds(2);
  otsuFilter->SetLabelOffset(2);
  otsuFilter->Update();

  ImageType::SizeType inSize = reader->GetOutput()->GetLargestPossibleRegion().GetSize();

  typedef itk::RegionOfInterestImageFilter< ImageType, ImageType > FilterType;

  ImageType::IndexType start;
  start[0] = inSize[0]/3;
  start[1] = inSize[1]/3;

  ImageType::SizeType size;
  size[0] = inSize[0]/3;
  size[1] = inSize[1]/3;

  ImageType::RegionType desiredRegion;
  desiredRegion.SetSize(size);
  desiredRegion.SetIndex(start);

  FilterType::Pointer filter = FilterType::New();

  filter->SetRegionOfInterest(desiredRegion);
  filter->SetInput(reader->GetOutput());

  ImageType::Pointer filtrada = filter->GetOutput();

  WriterType::Pointer writer = WriterType::New();
  writer->SetFileName("F:\\Filtrada.png");
  writer->SetInput(filtrada);
  writer->Update();

	//dividir em camadas a imagem

typedef itk::Image< unsigned char, 2>   ImageType;
	typedef itk::ImageFileReader<ImageType> ReaderType;
	typedef itk::ImageFileWriter<ImageType> WriterType;
	typedef itk::OtsuMultipleThresholdsImageFilter<ImageType, ImageType> FilterType;
	;

	//ler imagem
	ReaderType::Pointer reader = ReaderType::New();
	reader->SetFileName("F:\\olho_glaucoma.jpg");
	reader->Update();
	ImageType::Pointer image = reader->GetOutput();


	FilterType::Pointer otsuFilter = FilterType::New();
	otsuFilter->SetInput(image);
	otsuFilter->SetNumberOfHistogramBins(255);
	otsuFilter->SetNumberOfThresholds(2);
	otsuFilter->SetLabelOffset(2);
	otsuFilter->Update();

	ImageType::Pointer filtrada = otsuFilter->GetOutput();

	WriterType::Pointer writer = WriterType::New();
	writer->SetFileName("F:\\Filtrada.png");
	writer->SetInput(filtrada);
	writer->Update();


	*/
