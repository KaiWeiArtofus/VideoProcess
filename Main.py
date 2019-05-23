import boto3
import webvtt
from webvtt import WebVTT, Caption

translate = boto3.client(service_name='translate', region_name='eu-west-1', use_ssl=True)

"""result = translate.translate_text(Text="Hallo, Welt",
            SourceLanguageCode="de", TargetLanguageCode="es")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))"""

name = "1d7c2bdeb0c3619ec25020bd846785e0";

spanishFileName = name + '_es.vtt'

spanish = WebVTT()

fileName = name + '.vtt'

for caption in webvtt.read(fileName):
    print(caption.start)
    print(caption.end)
    print(caption.text)
    trans = translate.translate_text(Text=caption.text,
            SourceLanguageCode="en", TargetLanguageCode="es")

    newCaption = Caption(caption.start, caption.end, trans.get('TranslatedText'))
    newCaption.identifier = caption.identifier
    spanish.captions.append(newCaption)

spanish.save(spanishFileName)
