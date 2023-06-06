from time import time
import pdfplumber
from statistics import mode
import gc
import spacy

import re
from collections import Counter
# save model to path

class NER():
    def __init__(self):
        pass            
    def _load_model(self):
        # Load the pretrained model
        start_time = time()
        model = spacy.load('en_core_web_sm')
        end_time = time()
        model_loading_time = end_time-start_time
        print("loading model...")
        return model
    
    def _unload_model(self,model):
        # Clear references to the model
        del model
        # Perform garbage collection
        gc.collect()

    def ner(self,text,model):
        results = []
        try:
            text = text.replace('\n', " ")
            doc = model(text)
            for ent in doc.ents:
                res = (ent.text, ent.start_char, ent.end_char, ent.label_)
                results.append(res)
            return results
        except:
            print("no entities found")

    def _get_text_only(self,textelements):
        text = ""
    
        for element in textelements:
            try:
                if element["text"]:
                    text = text + " " + element["text"]
                    # text.append(element["text"])
            except:
                pass                                                    
        return text
    
    def _clean_plumber_output(self, text):
        text = text.replace("\n","")
        cid_pattern = "\(cid:(\d+)\)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        spaces = "\b\s+\b"
        pattern = re.compile(rf'{cid_pattern}|\d+|{spaces}')
        pattern.search(text)
        fin_text = text
        for m in re.finditer(pattern, text):
            # print(pattern, 'matched from position', m, m.start(), 'to', m.end())
            span_ = m.span()
            to_remove = text[span_[0]:span_[1]]
            fin_text = fin_text.replace(to_remove,"")
            fin_text = fin_text.replace("\n", "")
            fin_text = fin_text.strip()
        return fin_text
        
    def _pdf_ner(self, pdf_path):
        
        model = self._load_model()
        ner_output = []
        pdf_obj = pdfplumber.open(pdf_path,laparams = {})
        for page_number in range(len(pdf_obj.pages)):
            page = pdf_obj.pages[page_number]
            page_textelements = sorted(page.textlinehorizontals, key = lambda x: x['y0'], reverse=True)
            page_text = self._get_text_only(page_textelements)
            ner_output.append(self.ner(page_text,model))
            # break
        self._unload_model(model)
        pdf_obj.close()
        gc.collect() 

        try:
            if ner_output:
                print("entiites found")
                # return mode(langs)
                return ner_output
            else:
                print("Unable to read text! Pdf is scanned.")
                return []
        except:
            pass


from time import time
if __name__=="__main__":
    start_time = time()
    # sentence = "Red Eléctrica Corporación, S.A., sociedade operadora de transporte de eletricidade do sistema elétrico espanhol, onde a REN Serviços, S.A., sociedade subsidiária da REN, detém uma participação de 1% do capital social."
    # sentence = "After receiving all pages from the pdf, structure the output in a way for the next step so that the page number is preserved. La mise en page de chaque page doit être détectée de manière à diviser le texte de chaque page de manière à ce que chaque morceau de texte n'ait qu'un seul"
    # print(Detection().detect(sentence))
    pdf_path = "/home/vivitsa/Downloads/dracula-bram-stoker.pdf"
    print("pdf_path = ", pdf_path)
    print(NER()._pdf_ner(pdf_path))
    end_time = time()
    print("time taken  = ", end_time-start_time)


