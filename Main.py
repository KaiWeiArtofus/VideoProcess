from AWSTranslate import Translate

def main():
    name = '1d7c2bdeb0c3619ec25020bd846785e0'
    translateJob(name, "en", "es")
    translateJob(name, "en", "de")
    translateJob(name, "en", "zh")

def translateJob(name, sourceLanguage, targetLanguage):
    translateJob = Translate(name, sourceLanguage, targetLanguage)
    print("Starting job to translate name from " + sourceLanguage + " to " + targetLanguage + ". Please wait.")
    if translateJob.translate() == 1:
        print("Successfully translated name from " + sourceLanguage + " to " + targetLanguage)
    else:
        print("Failed translating name from " + sourceLanguage + " to " + targetLanguage)

main()