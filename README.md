"# propertyFinderAnalyzer" 



# Dependencies:
 * need access to the API - ONLY 300 calls a month for free package
 * needed to download punkt for the tokenization
 * download the spacy english model 
   * `python -m spacy download en_core_web_sm` (maybe covered in requirements.txt)
   * `python -m spacy download en_core_web_lg` 
   * `python -m spacy download xx_ent_wiki_sm`
   * also installed:
     * Entity models downloads- could be deleted:
       * `nltk.downloader.download('maxent_ne_chunker')
           nltk.downloader.download('words')
           nltk.downloader.download('treebank')
           nltk.downloader.download('maxent_treebank_pos_tagger')
           nltk.downloader.download('punkt')
           nltk.download('averaged_perceptron_tagger')`