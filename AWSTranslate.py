import boto3
import webvtt
from webvtt import WebVTT, Caption

class Translate(object):

    AWSTranslate = boto3.client(service_name='translate', region_name='eu-west-1', use_ssl=True)

    def __init__(self, fileNameWOType = '', sourceLanguage = "EN", targetLanguage = "CH"):
        self.fileNameWOType = fileNameWOType
        self.sourceLanguage = sourceLanguage
        self.targetLanguage = targetLanguage

    def translate(self):
        newVTT = WebVTT()
        fileName = self.fileNameWOType + '.vtt'
        for caption in webvtt.read(fileName):
#            print(caption.start)
#            print(caption.end)
#            print(caption.text)
            translation = Translate.AWSTranslate.translate_text(Text=caption.text, SourceLanguageCode=self.sourceLanguage, TargetLanguageCode=self.targetLanguage)

            newCaption = Caption(caption.start, caption.end, translation.get('TranslatedText'))
            newCaption.identifier = caption.identifier
            newVTT.captions.append(newCaption)

        translatedFileName = self.fileNameWOType + '_' + self.targetLanguage + '.vtt'
        newVTT.save(translatedFileName)
        return 1
