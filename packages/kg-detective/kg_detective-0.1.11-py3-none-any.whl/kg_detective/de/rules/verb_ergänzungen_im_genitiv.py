from spacy.matcher import Matcher, PhraseMatcher, DependencyMatcher
from kg_detective.lib import merge

def search_out(doc, nlp):
  """Search for  

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """
  result = []

  dep_matcher = DependencyMatcher(nlp.vocab)
  dep_patterns = [
    [
      {
        "RIGHT_ID": "verb",
        "RIGHT_ATTRS": {"POS": "VERB"}
      },
      {
        "LEFT_ID": "verb",
        "REL_OP": ">",
        "RIGHT_ID": "gen_obj",
        "RIGHT_ATTRS": {"DEP": "og", "POS": {"IN": ["NOUN", "PRON"]}}
      },
    ],
  ]
  dep_matcher.add("verb_genitiv", dep_patterns)
  matches = dep_matcher(doc)

  for _, (verb, gen_obj) in matches:
    span_ids = [verb]
    verb_token = doc[verb] 
    verb_aux = verb_token.head
    if verb_token.dep_ == "oc" and verb_aux.pos_ == "AUX" and verb_aux.tag_ in ["VAFIN", "VMFIN"]:
      span_ids.append(verb_aux.i)
    gen_obj_tree = [e.i for e in doc[gen_obj].subtree]
    span_ids.extend(gen_obj_tree)
    
    sorted_span_ids = sorted(span_ids)
    span_text = " ".join([doc[e].text for e in sorted_span_ids])
    result.append({"text": span_text})


  return result
   
