#!/usr/bin/python
import sys
import getopt
import math

def build_LM(in_file):
    """
    build language models for each label
    each line in in_file contains a label and an URL separated by a tab(\t)
    """
    print('building language models...')
    # Default initialisation of LM
    LM = {"malaysian": {}, "indonesian": {}, "tamil": {}}
    LM_total = {"malaysian": 0, "indonesian": 0, "tamil": 0}

    fd = open(in_file)
    for line in fd:
        cat = line.split()[0]
        data = line.split(" ", 1)[1].strip()
        grams = []
        # Get all the ngrams
        for i in range(len(data) - 3):
            grams.append(tuple(data[i:i+4]))
        # Building the language model
        for gram in grams:
            for LM_cat in LM:
                if gram not in LM[LM_cat]:
                    # Add one smoothing
                    LM[LM_cat][gram] = 1
                    LM_total[LM_cat] += 1
            LM[cat][gram] += 1
            LM_total[cat] += 1
    fd.close()
    return (LM, LM_total)
    
def test_LM(in_file, out_file, LM):
    """
    test the language models on new URLs
    each line of in_file contains an URL
    you should print the most probable label for each URL into out_file
    """
    print("testing language models...")
    fd_in = open(in_file)
    fd_out = open(out_file, "w")
    model = LM[0]
    LM_total = LM[1]
    for line in fd_in:
        grams = []
        result = {}
        not_in_model = 0
        total = 0
        data = line.strip()

        # Getting all the ngrams from the text
        for i in range(len(data) - 3):
            total += 1
            if tuple(data[i:i+4]) in model["malaysian"]:
                grams.append(tuple(data[i:i+4]))
            else:
                not_in_model += 1

        # Calculate probability
        for cat in model:
            current_cat_result = 0
            for gram in grams:
                current_cat_result += math.log10(model[cat][gram] / float(LM_total[cat]))
            result[cat] = current_cat_result
        language_detected = ""

        # Choosing the appropriate language
        if result["malaysian"] > result["tamil"] and result["malaysian"] > result["indonesian"]:
            language_detected = "malaysian"
        elif result["tamil"] > result["malaysian"] and result["tamil"] > result["indonesian"]:
            language_detected = "tamil"
        else:
            language_detected = "indonesian"
        if not_in_model / float(total) >= 0.80:
            language_detected = "other"
        fd_out.write(language_detected + " " + line)
    fd_out.close()
    fd_in.close()

def usage():
    print("usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file")

input_file_b = input_file_t = output_file = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'b:t:o:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == '-b':
        input_file_b = a
    elif o == '-t':
        input_file_t = a
    elif o == '-o':
        output_file = a
    else:
        assert False, "unhandled option"
if input_file_b == None or input_file_t == None or output_file == None:
    usage()
    sys.exit(2)

LM = build_LM(input_file_b)
test_LM(input_file_t, output_file, LM)
