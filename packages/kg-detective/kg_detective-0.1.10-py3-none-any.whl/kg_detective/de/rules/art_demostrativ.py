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
        "RIGHT_ID": "noun",
        "RIGHT_ATTRS": {"POS": "NOUN"}
      },
      {
        "LEFT_ID": "noun",
        "REL_OP": ">",
        "RIGHT_ID": "det",
        "RIGHT_ATTRS": {"DEP": "nk", "MORPH": {"IS_SUPERSET": ["PronType=Dem"]}, "TAG": "PDAT"}
      },
    ],
    [
      {
        "RIGHT_ID": "noun",
        "RIGHT_ATTRS": {"POS": "NOUN"}
      },
      {
        "LEFT_ID": "noun",
        "REL_OP": ">",
        "RIGHT_ID": "det",
        "RIGHT_ATTRS": {"DEP": "nk", "MORPH": {"IS_SUPERSET": ["PronType=Ind"]}, "TAG": "PIAT"}
      },
    ],
  ]
  dep_matcher.add("art_demostrativ", dep_patterns)
  matches = dep_matcher(doc)

  for _, (noun, art_demostrativ) in matches:
    span_ids = [noun, art_demostrativ]
   
    sorted_span_ids = sorted(span_ids)
    span_text = " ".join([doc[e].text for e in sorted_span_ids])
    result.append({"text": span_text})


  return result
   
