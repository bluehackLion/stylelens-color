from stylelens_color.color_extract import ExtractColor

#file = '/Users/lion/Desktop/purple_test.jpg'
file = '/Users/lion/Downloads/hans4.jpg'

extractor = ExtractColor(use_gpu=False)

color = extractor.extract_color(file=file)

print(color)




