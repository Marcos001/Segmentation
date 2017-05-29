#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkScalarImageKmeansImageFilter.h"


int main()
{
	typedef itk::Image< unsigned char, 2>    ImageType;
	typedef itk::ImageFileReader<ImageType> ReaderType;
	typedef itk::ImageFileWriter<ImageType> WriterType;
	typedef itk::ScalarImageKmeansImageFilter<ImageType> KmeansFilterType;

	ReaderType::Pointer reader = ReaderType::New();
	reader->SetFileName("F:\\glaucoma.jpg");
	reader->Update();
	ImageType::Pointer image = reader->GetOutput();

	KmeansFilterType::Pointer KmeansFilter = KmeansFilterType::New();
	KmeansFilter->SetInput(image);
	KmeansFilter->SetUseNonContiguousLabels(4);
	KmeansFilter->Update();
	ImageType::Pointer saida = KmeansFilter->GetOutput();

	WriterType::Pointer writer = WriterType::New();
	writer->SetFileName("F:\\kmeans.jpg");
	writer->SetInput(saida);
	writer->Update();



	return 0;
}