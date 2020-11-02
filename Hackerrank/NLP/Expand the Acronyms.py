from sys import stdin, maxint
import re


candidate_regex = r'\b(?:[Tt]he )?((?:[A-Z][\w\'\-]*)(?:(?:, | (?:of |at |and |to |for |with |under |on |from )?(?:the )?)(?:[A-Z][\w\'\-]*))+(?: number)?)\b(?: \([\w\'\-\s]*?([A-Z]+)\))?'
acronym_regex = r'[A-Z]'
#print candidate_regex


#taken fron https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def expand_acronym_levenshtein(input_acronym, candidates, acronyms_list):
    best_candidate_acronym = acronyms_list[0][0]
    best_candidate_expanded = acronyms_list[0][1]
    best_candidate_distance = levenshtein(input_acronym, best_candidate_acronym)
    
    for curr_candidate_acronym, curr_candidate_expanded in acronyms_list[1:]:
        curr_candidate_distance = levenshtein(input_acronym, curr_candidate_acronym)
        if curr_candidate_distance < best_candidate_distance:
            best_candidate_acronym = curr_candidate_acronym
            best_candidate_expanded = curr_candidate_expanded
            best_candidate_distance = curr_candidate_distance
    
    return best_candidate_expanded


def expand_acronym(input_acronym, candidates, acronyms_dict):
    #print acronym
    #print candidates
    #print acronyms_dict
    if input_acronym in acronyms_dict:
        return acronyms_dict[input_acronym]
    else:
        return None
    

def extract_candidate(text, acronyms_dict):
    extracted_candidates = []
    for match in re.finditer(candidate_regex, text):
        expanded = match.group(1)
        acronym = match.group(2)
        #print match.groups()
        if not acronym:
            acronym = ''.join(re.findall(acronym_regex, expanded))
        #print (acronym, expanded)
        extracted_candidates.append((acronym, expanded))
        acronyms_dict[acronym] = expanded
    return extracted_candidates


def main():
    tests_number = int(stdin.next())
    input_acronyms = []
    acronyms_list = []
    acronyms_dict = dict()
    
    for x in range(tests_number):
        acronyms_list.extend(extract_candidate(stdin.next().strip(), acronyms_dict))
    
    for x in range(tests_number):
        input_acronyms.append(stdin.next().strip())
     
    #print acronyms_dict
    for input_acronym in input_acronyms:
        #print '*'*25 + ' ' + input_acronym
        expanded = expand_acronym(input_acronym, acronyms_list, acronyms_dict)
        if not expanded:
            expanded = expand_acronym_levenshtein(input_acronym, acronyms_list, acronyms_list)
        print expanded

        
main()